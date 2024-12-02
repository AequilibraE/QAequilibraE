import pytest
import numpy as np
import pandas as pd
from aequilibrae.distribution import Ipf
from aequilibrae.paths import TrafficAssignment, TrafficClass

from .utilities import run_sfalls_assignment
from qaequilibrae.modules.gis.compare_scenarios_dialog import CompareScenariosDialog


def test_compare_scenarios(ae_with_project, qtbot):
    proj = run_sfalls_assignment(ae_with_project)
    proj = future_assignment(proj)

    dialog = CompareScenariosDialog(proj)
    print(dialog.results)
    dialog.cob_alternative_scenario.setCurrentText("future_assignment")

    dialog.execute_comparison()

    path = qtbot.screenshot(dialog)
    print(path)


def future_assignment(aeq_from_qgis):

    project = aeq_from_qgis.project
    project.network.build_graphs()

    graph = project.network.graphs["c"]
    graph.set_graph("free_flow_time")
    graph.set_skimming(["free_flow_time", "distance"])
    graph.set_blocked_centroid_flows(False)

    demand = project.matrices.get_matrix("demand.aem")
    demand.computational_view(["matrix"])

    # Calibrate gravity model
    proj_matrices = project.matrices
    imped = proj_matrices.get_matrix("assignment_car")
    imped_core = "free_flow_time_final"
    imped.computational_view([imped_core])

    np.fill_diagonal(imped.matrix_view, 0)
    intrazonals = np.amin(imped.matrix_view, where=imped.matrix_view > 0, initial=imped.matrix_view.max(), axis=1)
    intrazonals *= 0.75
    np.fill_diagonal(imped.matrix_view, intrazonals)
    
    imped.save(names=["final_time_with_intrazonals"])

    # Adjust future demand with IPF
    origins = np.sum(demand.matrix_view, axis=1)
    destinations = np.sum(demand.matrix_view, axis=0)
    orig = origins * (1 + np.random.rand(origins.shape[0]) / 10)
    dest = destinations * (1 + np.random.rand(origins.shape[0]) / 10)
    dest *= orig.sum() / dest.sum()

    vectors = pd.DataFrame({"origins":orig, "destinations":dest}, index=demand.index[:])

    args = {
    "matrix": demand,
    "vectors": vectors,
    "column_field": "destinations",
    "row_field": "origins",
    "nan_as_zero": True,
    }

    ipf = Ipf(**args)
    ipf.fit()
    
    ipf.save_to_project(name="demand_ipfd", file_name="demand_ipfd.aem")
    ipf.save_to_project(name="demand_ipfd_omx", file_name="demand_ipfd.omx")

    imped = proj_matrices.get_matrix("assignment_car")
    imped.computational_view(["final_time_with_intrazonals"])

    # Future traffic assignment
    demand = proj_matrices.get_matrix("demand_ipfd")
    demand.computational_view("matrix")

    assigclass = TrafficClass("car", graph, demand)

    assig = TrafficAssignment()

    assig.set_classes([assigclass])
    assig.set_vdf("BPR")
    assig.set_vdf_parameters({"alpha": "b", "beta": "power"})
    assig.set_capacity_field("capacity")
    assig.set_time_field("free_flow_time")
    assig.set_algorithm("bfw")
    assig.max_iter = 5
    assig.rgap_target = 0.01
    assig.execute()

    assig.save_results("future_assignment")
    assig.save_skims("future_assignment", which_ones="all", format="omx")

    return aeq_from_qgis