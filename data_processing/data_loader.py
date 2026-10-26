"""Load and inspect the California Housing dataset."""

from pathlib import Path
from typing import Any

import pandas as pd
from sklearn.datasets import fetch_california_housing


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
DEFAULT_RAW_PATH = RAW_DATA_DIR / "california_housing.csv"


def load_housing_data(as_frame: bool = True) -> pd.DataFrame:
    """Load California Housing data from scikit-learn and return its features and target."""
    housing = fetch_california_housing(as_frame=as_frame)
    data = housing.frame.copy()
    data = data.rename(columns={"MedHouseVal": "median_house_value"})
    return data


def get_data_overview(data: pd.DataFrame) -> dict[str, Any]:
    """Return basic dimensions, column types, missing-value counts, and descriptive statistics."""
    return {
        "rows": int(data.shape[0]),
        "columns": int(data.shape[1]),
        "column_names": data.columns.tolist(),
        "data_types": data.dtypes.astype(str).to_dict(),
        "missing_values": data.isna().sum().astype(int).to_dict(),
        "duplicate_rows": int(data.duplicated().sum()),
        "numeric_summary": data.describe().round(3).to_dict(),
    }


def save_raw_data(data: pd.DataFrame, output_path: Path = DEFAULT_RAW_PATH) -> Path:
    """Save the downloaded dataset as a CSV file and return the saved path."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    data.to_csv(output_path, index=False)
    return output_path


def load_and_save_housing_data(output_path: Path = DEFAULT_RAW_PATH) -> pd.DataFrame:
    """Load the California Housing dataset, save a raw CSV copy, and return the data."""
    data = load_housing_data()
    save_raw_data(data, output_path)
    return data
