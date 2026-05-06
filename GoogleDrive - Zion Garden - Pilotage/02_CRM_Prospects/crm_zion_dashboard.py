from __future__ import annotations

import argparse
import csv
from pathlib import Path


def load_prospects_csv(csv_path: Path) -> list[dict[str, str]]:
    """Load prospects data from a CSV file (UTF-8)."""
    if not csv_path.exists():
        raise FileNotFoundError(f"File not found: {csv_path}")
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def compute_kpis(rows: list[dict[str, str]]) -> dict[str, int]:
    """Compute simple CRM KPIs from common pipeline columns."""
    stage_col = "sales_stage"
    stage_fallback_col = "statut"
    mail_col = "email"
    phone_col = "phone"

    def field(row: dict[str, str], key: str) -> str:
        return (row.get(key, "") or "").strip()

    def normalize_stage(value: str) -> str:
        s = value.lower().strip()
        if s in {"nouveau", "new", "suspect"}:
            return "suspect"
        if s in {"prospect"}:
            return "prospect"
        if s in {"negociation", "négociation"}:
            return "negociation"
        if s in {"conclusion", "client", "signed"}:
            return "conclusion"
        return s

    stages = []
    for r in rows:
        raw_stage = field(r, stage_col) or field(r, stage_fallback_col)
        stages.append(normalize_stage(raw_stage))

    return {
        "total_prospects": len(rows),
        "with_email": sum(1 for r in rows if field(r, mail_col) != ""),
        "with_phone": sum(1 for r in rows if field(r, phone_col) != ""),
        "suspects": sum(1 for s in stages if s == "suspect"),
        "prospects": sum(1 for s in stages if s == "prospect"),
        "negociation": sum(1 for s in stages if s == "negociation"),
        "clients_signed": sum(1 for s in stages if s == "conclusion"),
    }


def write_markdown_report(kpis: dict[str, int], output_path: Path) -> None:
    lines = [
        "# Dashboard CRM Zion Garden",
        "",
        f"- Total prospects: **{kpis['total_prospects']}**",
        f"- Avec email: **{kpis['with_email']}**",
        f"- Avec téléphone: **{kpis['with_phone']}**",
        f"- Suspects: **{kpis['suspects']}**",
        f"- Prospects: **{kpis['prospects']}**",
        f"- En négociation: **{kpis['negociation']}**",
        f"- Clients signés: **{kpis['clients_signed']}**",
        "",
        "## Prochaine action recommandée",
        "- Compléter email + téléphone des priorités A, puis lancer relances J+2 / J+7 / J+14.",
    ]
    output_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Zion Garden CRM KPI dashboard (CLI, CSV only)."
    )
    parser.add_argument(
        "--file",
        type=Path,
        default=Path("crm_prospects.csv"),
        help="Path to the CRM CSV file.",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("Dashboard CRM - Auto.md"),
        help="Path to Markdown report output file.",
    )
    args = parser.parse_args()

    rows = load_prospects_csv(args.file)
    kpis = compute_kpis(rows)
    write_markdown_report(kpis, args.report)

    print("=== Zion Garden CRM Dashboard ===")
    for key, value in kpis.items():
        print(f"{key}: {value}")
    print(f"report_file: {args.report}")


if __name__ == "__main__":
    main()
