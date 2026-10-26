
@echo off
setlocal

set "PROJECT=house_price_prediction"

if not exist "%PROJECT%" mkdir "%PROJECT%"
cd "%PROJECT%"

mkdir data\raw 2>nul
mkdir data\processed 2>nul
mkdir notebooks 2>nul
mkdir data_processing 2>nul
mkdir machine_learning 2>nul
mkdir models 2>nul
mkdir outputs\figures 2>nul
mkdir outputs\metrics 2>nul

type nul > data_processing\__init__.py
type nul > data_processing\data_loader.py
type nul > data_processing\data_cleaning.py
type nul > data_processing\feature_engineering.py

type nul > machine_learning\__init__.py
type nul > machine_learning\train_model.py
type nul > machine_learning\evaluate_model.py
type nul > machine_learning\predict.py

type nul > main.py
type nul > requirements.txt
type nul > README.md
type nul > .gitignore

if not exist notebooks\house_price_prediction.ipynb (
    echo Creating notebook...
    python -c "import nbformat; nbformat.write(nbformat.v4.new_notebook(), 'notebooks/house_price_prediction.ipynb')" 2>nul
)

echo.
echo Project structure created.
echo.
tree /F
echo.
pause
