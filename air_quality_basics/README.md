# Air Quality Basics Explorer

This mini project teaches simple exploratory analysis over the local air-quality competition dataset using pure Python.

## Concepts

- CSV parsing with `csv.DictReader`
- Grouping and aggregation by week
- Ranking weeks by mean emission

## Run

```bash
cd air_quality_basics
python cli.py
```

## Test

```bash
cd air_quality_basics
python -m unittest test_explorer.py
```

## Data note

The project reads local dataset files already in this repository (`Train.csv`). No external downloads or APIs are required.
