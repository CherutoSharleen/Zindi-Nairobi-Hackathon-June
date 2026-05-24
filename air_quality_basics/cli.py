from __future__ import annotations

from pathlib import Path

from explorer import load_rows, top_weeks_by_emission


def main() -> None:
    base = Path(__file__).resolve().parents[1]
    rows = load_rows(base / "Train.csv", limit=4000)
    ranked = top_weeks_by_emission(rows, top_k=5)
    print("Top 5 weeks by mean emission (sampled rows):")
    for week, value in ranked:
        print(f"- week {week}: {value:.4f}")


if __name__ == "__main__":
    main()
