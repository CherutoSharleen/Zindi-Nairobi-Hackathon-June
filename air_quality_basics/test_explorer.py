import unittest
from pathlib import Path

from explorer import (
    filter_rows_by_year,
    load_rows,
    mean_emission_by_week,
    row_count_by_year,
    top_weeks_by_emission,
    weekly_mean_for_year,
    yearly_mean_emission,
)


class AirQualityExplorerTests(unittest.TestCase):
    def test_load_rows_has_expected_fields(self) -> None:
        base = Path(__file__).resolve().parents[1]
        rows = load_rows(base / "Train.csv", limit=20)
        self.assertGreater(len(rows), 0)
        self.assertIn("week_no", rows[0])
        self.assertIn("emission", rows[0])

    def test_mean_emission_by_week_non_empty(self) -> None:
        base = Path(__file__).resolve().parents[1]
        rows = load_rows(base / "Train.csv", limit=100)
        weekly = mean_emission_by_week(rows)
        self.assertGreater(len(weekly), 0)

    def test_top_weeks_ranked(self) -> None:
        base = Path(__file__).resolve().parents[1]
        rows = load_rows(base / "Train.csv", limit=500)
        top = top_weeks_by_emission(rows, top_k=3)
        self.assertEqual(len(top), 3)
        self.assertGreaterEqual(top[0][1], top[1][1])

    def test_filter_rows_by_year(self) -> None:
        base = Path(__file__).resolve().parents[1]
        rows = load_rows(base / "Train.csv", limit=200)
        filtered = filter_rows_by_year(rows, 2019)
        self.assertGreater(len(filtered), 0)
        self.assertTrue(all(int(row["year"]) == 2019 for row in filtered))

    def test_yearly_mean_emission(self) -> None:
        base = Path(__file__).resolve().parents[1]
        rows = load_rows(base / "Train.csv", limit=500)
        yearly = yearly_mean_emission(rows)
        self.assertGreater(len(yearly), 0)
        self.assertIn(2019, yearly)

    def test_weekly_mean_for_year(self) -> None:
        base = Path(__file__).resolve().parents[1]
        rows = load_rows(base / "Train.csv", limit=800)
        weekly = weekly_mean_for_year(rows, 2019)
        self.assertGreater(len(weekly), 0)

    def test_row_count_by_year(self) -> None:
        base = Path(__file__).resolve().parents[1]
        rows = load_rows(base / "Train.csv", limit=100)
        counts = row_count_by_year(rows)
        self.assertIn(2019, counts)


if __name__ == "__main__":
    unittest.main()
