from ..common_tools import ParameterDialog


def run_change_parameters(qgis_project):
    if qgis_project.project is None:
        qgis_project.show_message_no_project()
        return
    dlg2 = ParameterDialog(qgis_project)
    dlg2.show()
    dlg2.exec_()
