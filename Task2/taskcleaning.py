import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FILE = "houseprices.csv"          # change if needed
OUT_FILE = "cleaned_dataset.csv"
drop_thresh = 0.60
num_strategy = "median"

df = pd.read_csv(FILE)

print("Shape:", df.shape)
print(df.head())

# missing values (count + %)
miss_cnt = df.isna().sum()
miss_pct = (miss_cnt / len(df)).sort_values(ascending=False) * 100

miss = pd.DataFrame({
    "missing_count": miss_cnt,
    "missing_pct": miss_pct.round(2),
    "dtype": df.dtypes.astype(str)
}).sort_values("missing_count", ascending=False)

print("\nColumns with missing values:")
missing_only = miss[miss["missing_count"] > 0]
if len(missing_only) == 0:
    print("No missing values found.")
else:
    print(missing_only.to_string())

# plot top missing columns
top = missing_only.head(25)
if len(top) > 0:
    plt.figure(figsize=(10, 5))
    plt.bar(top.index.astype(str), top["missing_pct"].values)
    plt.xticks(rotation=70, ha="right")
    plt.ylabel("Missing (%)")
    plt.title("Top columns with missing values")
    plt.tight_layout()
    plt.show()

# drop columns with too many missing values
cols_to_drop = miss[miss["missing_pct"] > drop_thresh * 100].index.tolist()
df2 = df.drop(columns=cols_to_drop)

print("\nDropped columns:", cols_to_drop)
print("After dropping columns:", df2.shape)

# split numeric / categorical
num_cols = df2.select_dtypes(include=["number"]).columns
cat_cols = [c for c in df2.columns if c not in num_cols]

# impute numeric
if len(num_cols) > 0:
    if num_strategy == "mean":
        df2[num_cols] = df2[num_cols].fillna(df2[num_cols].mean())
    else:
        df2[num_cols] = df2[num_cols].fillna(df2[num_cols].median())

# impute categorical
for c in cat_cols:
    if df2[c].isna().any():
        mode_vals = df2[c].mode(dropna=True)
        df2[c] = df2[c].fillna(mode_vals.iloc[0] if len(mode_vals) else "Unknown")

# validate
remaining = df2.isna().sum().sort_values(ascending=False)
remaining = remaining[remaining > 0]

print("\nAfter cleaning shape:", df2.shape)
if len(remaining) == 0:
    print("Missing values after cleaning: 0")
else:
    print("Missing values still present:")
    print(remaining.to_string())

# before vs after summary
summary = pd.DataFrame({
    "before": [df.shape[0], df.shape[1], int(df.isna().sum().sum()), int((df.isna().sum() > 0).sum())],
    "after":  [df2.shape[0], df2.shape[1], int(df2.isna().sum().sum()), int((df2.isna().sum() > 0).sum())]
}, index=["rows", "cols", "total_missing", "cols_with_missing"])

print("\nBefore vs after:")
print(summary.to_string())

df2.to_csv(OUT_FILE, index=False)
print("\nSaved:", OUT_FILE)
print(df2.head())
