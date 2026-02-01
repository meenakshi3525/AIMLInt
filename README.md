# AI & ML Internship - Task 2: Data Cleaning & Missing Value Handling

## Dataset Used
- Dataset name: House Prices Dataset (Housing.csv)
- Rows: 545
- Columns: 13

## Objective
To clean the dataset and handle missing values using Python (Pandas, NumPy).

## Tools Used
- Python 3.11
- Pandas
- NumPy
- Matplotlib
- VS Code

## Steps Performed

### 1. Loaded the Dataset
- Loaded the dataset using `pandas.read_csv()`
- Displayed the first 5 rows to understand structure

### 2. Checked Missing Values
- Used:
  - `df.isna().sum()` to count missing values
  - computed missing percentage for each column

### 3. Visualized Missing Values
- Created a bar chart showing missing value percentage for top missing columns using Matplotlib

### 4. Dropped Columns with High Missing Values
- Dropped columns having more than **60% missing values**
- (In this dataset, no columns crossed the threshold)

### 5. Imputation
- Numerical columns: filled missing values using **median**
- Categorical columns: filled missing values using **mode**
- (This dataset had no missing values, so no imputation was required)

### 6. Validation
- Rechecked missing values after cleaning
- Compared dataset shape before vs after cleaning

### 7. Saved Cleaned Dataset
- Saved the cleaned dataset as:
  - `cleaned_dataset.csv`

## Output Files
- `taskcleaning.py` (cleaning script)
- `cleaned_dataset.csv` (cleaned dataset)
- `README.md` (this file)

## How to Run
```bash
python taskcleaning.py
