import os
from pathlib import Path
import pytest

from qaequilibrae.i18n.create_pro_file import create_file


@pytest.mark.skip("Windows release test")
def test_file_creation():
    create_file()
    output_path = Path("qaequilibrae/i18n/qaequilibrae.pro")

    assert output_path.exists()
    assert os.stat(output_path).st_size > 0

    os.remove(output_path)
