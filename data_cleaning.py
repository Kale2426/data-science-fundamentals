"""
data_cleaning.py
Loads the sample sales dataset and demonstrates common data-cleaning steps:
handling missing values, detecting outliers, and encoding categorical data.
"""

import os
import pandas as pd

_HERE = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(_HERE, "..", "data", "sales_data.csv")


def load_data(path=DATA_PATH):
    return pd.read_csv(path)


def clean_data(df):
    df = df.copy()

    # Handle missing numeric values via median imputation
    df["revenue"] = df["revenue"].fillna(df["revenue"].median())
    df["age"] = df["age"].fillna(df["age"].median())

    # Remove exact duplicate rows, if any
    df = df.drop_duplicates()

    # Simple outlier flag using the IQR method on revenue
    q1, q3 = df["revenue"].quantile([0.25, 0.75])
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    df["revenue_outlier"] = ~df["revenue"].between(lower, upper)

    # One-hot encode the categorical column
    df = pd.get_dummies(df, columns=["category"], prefix="cat")

    return df


if __name__ == "__main__":
    raw = load_data()
    print("Raw data:\n", raw, "\n")

    cleaned = clean_data(raw)
    print("Cleaned data:\n", cleaned)

    monthly_totals = raw.groupby("month")["revenue"].sum(min_count=1)
    print("\nMonthly revenue totals:\n", monthly_totals)
