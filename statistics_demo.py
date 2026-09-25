"""
statistics_demo.py
Demonstrates descriptive statistics, a normal-distribution probability check,
and a simple hypothesis test (one-sample t-test) using the sample dataset.
"""

import pandas as pd
from scipy import stats

from data_cleaning import load_data, clean_data


def descriptive_summary(df):
    summary = {
        "mean_revenue": df["revenue"].mean(),
        "median_revenue": df["revenue"].median(),
        "std_revenue": df["revenue"].std(),
        "skewness": df["revenue"].skew(),
    }
    return summary


def hypothesis_test(df, hypothesized_mean=1500):
    """
    One-sample t-test: is the average revenue significantly different
    from a hypothesized value (e.g. a target of 1500)?
    """
    t_stat, p_value = stats.ttest_1samp(df["revenue"], hypothesized_mean)
    significant = p_value < 0.05
    return t_stat, p_value, significant


if __name__ == "__main__":
    df = clean_data(load_data())

    print("Descriptive statistics:")
    for k, v in descriptive_summary(df).items():
        print(f"  {k}: {v:.2f}")

    t_stat, p_value, significant = hypothesis_test(df)
    print(f"\nHypothesis test vs. target mean of 1500:")
    print(f"  t-statistic = {t_stat:.3f}, p-value = {p_value:.3f}")
    print(f"  Statistically significant at 0.05? {significant}")

    correlation = df["age"].corr(df["revenue"])
    print(f"\nCorrelation between age and revenue: {correlation:.3f}")
