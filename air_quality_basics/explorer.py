from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


def load_rows(path: Path, limit: int | None = 2000) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for idx, row in enumerate(reader):
            rows.append(row)
            if limit is not None and idx + 1 >= limit:
                break
    return rows


def mean_emission_by_week(rows: list[dict[str, str]]) -> dict[int, float]:
    grouped: dict[int, list[float]] = defaultdict(list)
    for row in rows:
        week = int(row["week_no"])
        grouped[week].append(float(row["emission"]))
    return {week: sum(values) / len(values) for week, values in grouped.items()}


def top_weeks_by_emission(rows: list[dict[str, str]], top_k: int = 5) -> list[tuple[int, float]]:
    means = mean_emission_by_week(rows)
    ranked = sorted(means.items(), key=lambda item: item[1], reverse=True)
    return ranked[:top_k]


def filter_rows_by_year(rows: list[dict[str, str]], year: int) -> list[dict[str, str]]:
    return [row for row in rows if int(row["year"]) == year]


def yearly_mean_emission(rows: list[dict[str, str]]) -> dict[int, float]:
    grouped: dict[int, list[float]] = defaultdict(list)
    for row in rows:
        grouped[int(row["year"])].append(float(row["emission"]))
    return {year: sum(values) / len(values) for year, values in grouped.items()}
