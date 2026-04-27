import os
import pandas as pd


REQUIRED_FILES = [
    "starter_code/pickandplace.py",
    "starter_code/world.xml",
    "starter_code/panda.xml",
    "results/results.csv",
    "docs/report.pdf",
]


def test_required_files_exist():
    for file_path in REQUIRED_FILES:
        assert os.path.exists(file_path), f"Missing required file: {file_path}"


def test_results_csv_format():
    csv_path = "results/results.csv"
    df = pd.read_csv(csv_path)

    required_columns = ["trial", "success", "time"]

    for col in required_columns:
        assert col in df.columns, f"Missing column in results.csv: {col}"

    assert len(df) >= 5, "At least 5 trials are required in results.csv"

    assert df["trial"].notna().all(), "trial column contains empty values"

    assert df["success"].isin([0, 1]).all(), (
        "success column must contain only 0 or 1"
    )

    assert pd.api.types.is_numeric_dtype(df["time"]), (
        "time column must be numeric"
    )

    assert (df["time"] > 0).all(), (
        "time values must be positive"
    )


def test_report_file_not_empty():
    report_path = "docs/report.pdf"

    assert os.path.getsize(report_path) > 1000, (
        "docs/report.pdf exists but seems too small or empty"
    )


def test_code_file_not_empty():
    code_path = "starter_code/pickandplace.py"

    assert os.path.getsize(code_path) > 1000, (
        "starter_code/pickandplace.py exists but seems too small or empty"
    )


def test_xml_files_not_empty():
    xml_files = [
        "starter_code/world.xml",
        "starter_code/panda.xml",
    ]

    for xml_file in xml_files:
        assert os.path.getsize(xml_file) > 100, (
            f"{xml_file} exists but seems empty"
        )
