import os
import pandas as pd

def test_required_files_exist():
    required_files = [
        "starter_code/pickandplace.py",
        "starter_code/world.xml",
        "starter_code/panda.xml",
        "results/results.csv",
        "docs/report.pdf",
    ]

    for file_path in required_files:
        assert os.path.exists(file_path), f"Missing required file: {file_path}"

def test_results_csv_format():
    csv_path = "results/results.csv"
    assert os.path.exists(csv_path), "Missing results/results.csv"

    df = pd.read_csv(csv_path)

    required_columns = ["trial", "success", "time"]
    for col in required_columns:
        assert col in df.columns, f"Missing column in CSV: {col}"

    assert len(df) >= 5, "At least 5 trials are required"

    assert df["success"].isin([0, 1]).all(), "success must be 0 or 1"
    assert (df["time"] > 0).all(), "time must be positive"
