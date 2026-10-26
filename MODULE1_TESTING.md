# Module 1 — Local setup and test

Run these commands from the `homevalue` project root in Windows CMD.

```cmd
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

Expected checks after the first dataset download:
- 20,640 rows and 9 columns, including the `median_house_value` target.
- A data type listing, missing-value counts, duplicate-row count, first five rows, and descriptive statistics.
- A CSV saved at `data\raw\california_housing.csv`.

The first run needs internet access because scikit-learn downloads the dataset. Subsequent runs normally use the local scikit-learn cache.

Notebook test:
```cmd
jupyter notebook
```
Open `notebooks/house_price_prediction.ipynb`, run all cells, and confirm the CSV path is printed.

Do not start Module 2 until these checks pass. If an error appears, copy the complete traceback and send it back.
