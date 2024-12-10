from os.path import isfile, join

from .utilities import run_sfalls_assignment
from qaequilibrae.modules.common_tools.report_dialog import ReportDialog


def test_report_dialog(ae_with_project, mocker, qtbot):
    proj = run_sfalls_assignment(ae_with_project)

    file_path = join(ae_with_project.project.project_base_path, "report_output.txt")
    report = ["This is an example"]

    mocker.patch(
        "qaequilibrae.modules.common_tools.report_dialog.ReportDialog.browse_outfile",
        return_value=file_path,
    )
    dialog = ReportDialog(proj.iface, report)
    dialog.path = file_path

    dialog.save_log()

    assert isfile(dialog.path)

    with open(dialog.path, "r", encoding="utf-8") as file:
        for line in file.readlines():
            assert line == report[0]
