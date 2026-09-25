# Data Science Fundamentals Assessment

Supporting code for the "Data Science Fundamentals Assessment" task of the
YuvaIntern Data Analyst Internship. This repo demonstrates the concepts
covered in the written report: Python basics, data cleaning, and
statistical analysis, using a small sample sales dataset.

## Project structure

```
data-science-fundamentals/
├── data/
│   └── sales_data.csv        # sample dataset used by the scripts
├── src/
│   ├── python_basics.py      # core Python collections, control flow, functions
│   ├── data_cleaning.py      # missing values, outliers, encoding, pandas groupby
│   └── statistics_demo.py    # descriptive stats, hypothesis test, correlation
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the scripts

```bash
cd src
python python_basics.py
python data_cleaning.py
python statistics_demo.py
```

## What each script covers

- **python_basics.py** — lists, tuples, dictionaries, sets, f-strings,
  conditionals, and a reusable function (`categorize_age`).
- **data_cleaning.py** — loading a CSV with pandas, imputing missing values,
  removing duplicates, flagging outliers with the IQR method, one-hot
  encoding a categorical column, and grouping data for monthly totals.
- **statistics_demo.py** — descriptive statistics (mean, median, standard
  deviation, skewness), a one-sample t-test for hypothesis testing, and a
  correlation check between two numeric columns.

## Author

Ambika — Data Analyst Intern, YuvaIntern
