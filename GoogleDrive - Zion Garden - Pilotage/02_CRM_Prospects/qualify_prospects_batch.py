from __future__ import annotations

import argparse
import csv
from pathlib import Path


SEGMENT_MESSAGE = {
    "Administration": "Bonjour, je vous contacte pour proposer un atelier jardin a impact social adapte a vos publics.",
    "Institution sociale": "Bonjour, je vous contacte pour proposer des jardins-activites adaptes a vos beneficiaires.",
    "Sante": "Bonjour, je vous contacte pour proposer un programme de jardin therapeutique et plantes medicinales.",
    "Education": "Bonjour, je vous contacte pour proposer un cycle de potager pedagogique cle en main pour votre ecole.",
    "Formation": "Bonjour, je vous contacte pour explorer un partenariat atelier ecologie et maraichage.",
    "Education superieure": "Bonjour, je vous contacte pour une action campus durable et atelier pratique.",
    "Media": "Bonjour, je vous contacte pour un sujet local autour de la permaculture de terrain en Wallonie.",
    "Influenceur": "Bonjour, je vous contacte pour une collaboration contenu autour du potager et de la permaculture.",
    "Communaute": "Bonjour, je vous contacte pour un partenariat de visibilite sur des actions locales.",
}


def score_letter(priority: str) -> str:
    p = (priority or "").strip().upper()
    if p == "A":
        return "A"
    if p == "B":
        return "B"
    return "C"


def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def save_rows(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Qualify Zion Garden prospects by batch.")
    parser.add_argument("--input", type=Path, required=True, help="Input CSV")
    parser.add_argument("--output", type=Path, required=True, help="Output CSV enriched")
    parser.add_argument("--batch-output", type=Path, required=True, help="Output CSV current batch")
    parser.add_argument("--batch-size", type=int, default=20, help="Batch size")
    args = parser.parse_args()

    rows = load_rows(args.input)
    extra_fields = ["qualification_abc", "message_type", "canal_prioritaire", "statut_relance", "ordre_lot"]

    fieldnames = list(rows[0].keys()) if rows else []
    for f in extra_fields:
        if f not in fieldnames:
            fieldnames.append(f)

    # Sort: A first, then B, then C
    rows_sorted = sorted(rows, key=lambda r: {"A": 0, "B": 1}.get((r.get("priority") or "").upper(), 2))

    for idx, r in enumerate(rows_sorted, start=1):
        segment = (r.get("segment") or "").strip()
        qual = score_letter(r.get("priority", ""))
        r["qualification_abc"] = qual
        r["message_type"] = SEGMENT_MESSAGE.get(segment, "Bonjour, je vous contacte pour presenter une offre adaptee a votre structure.")
        r["canal_prioritaire"] = "email" if qual in {"A", "B"} else "linkedin"
        r["statut_relance"] = r.get("statut_relance", "") or "a_contacter"
        r["ordre_lot"] = str(idx)

    save_rows(args.output, rows_sorted, fieldnames)

    batch = rows_sorted[: args.batch_size]
    save_rows(args.batch_output, batch, fieldnames)

    print(f"total: {len(rows_sorted)}")
    print(f"batch_size: {len(batch)}")
    print(f"output: {args.output}")
    print(f"batch_output: {args.batch_output}")


if __name__ == "__main__":
    main()
