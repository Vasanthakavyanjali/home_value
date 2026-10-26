"""Entry point for Module 1: load and inspect the housing dataset."""

from data_processing.data_loader import get_data_overview, load_and_save_housing_data


def main() -> None:
    """Load the California Housing data, save a raw copy, and display an overview."""
    data = load_and_save_housing_data()
    overview = get_data_overview(data)

    print(f"Rows: {overview['rows']}")
    print(f"Columns: {overview['columns']}")
    print(f"Duplicate rows: {overview['duplicate_rows']}")
    print("\nColumn data types:")
    for column, dtype in overview["data_types"].items():
        print(f"- {column}: {dtype}")

    print("\nMissing values:")
    for column, count in overview["missing_values"].items():
        print(f"- {column}: {count}")

    print("\nFirst five rows:")
    print(data.head().to_string(index=False))
    print("\nNumeric summary:")
    print(data.describe().round(3).to_string())


if __name__ == "__main__":
    main()
