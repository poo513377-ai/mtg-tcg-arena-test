#!/usr/bin/env python3
"""
Simple helper to add a custom card to cards.json

Usage:
  python add_custom_card.py

It will ask you for the details and append the card.
"""

import json
import os
import sys

CARDS_FILE = "cards.json"

def make_card(id_, name, type_, cost, colors, type_line, image, power=None, toughness=None):
    card = {
        "id": id_,
        "name": name,
        "type": type_,
        "cost": int(cost) if cost != "" else 0,
        "Colors": [c.strip().upper() for c in colors.split(",") if c.strip()],
        "Card type": type_line,
        "Color identity": [c.strip().upper() for c in colors.split(",") if c.strip()],
        "isHorizontal": False,
        "face": {
            "front": {
                "name": {"name": name},
                "type": type_,
                "cost": int(cost) if cost != "" else 0,
                "isHorizontal": False,
                "image": image
            }
        },
        "_legal": {
            "EDH": True, "MD": True, "VI": True, "ST": True,
            "PA": True, "LG": True, "PI": True
        }
    }
    if power not in (None, ""):
        card["power"] = int(power)
        card["toughness"] = int(toughness)
    return card

def main():
    if not os.path.exists(CARDS_FILE):
        print(f"Error: {CARDS_FILE} not found. Run this in the same folder as cards.json")
        sys.exit(1)

    with open(CARDS_FILE) as f:
        cards = json.load(f)

    print("=== Add a Custom Card ===\n")
    id_ = input("Card ID (unique, e.g. custom-my-card-01): ").strip()
    if not id_:
        print("ID required")
        return
    if id_ in cards:
        print(f"Warning: ID '{id_}' already exists. It will be overwritten.")

    name = input("Card Name: ").strip()
    type_ = input("Type (Creature / Instant / Sorcery / Artifact / Enchantment / Land / Planeswalker): ").strip() or "Creature"
    cost = input("Mana cost number (e.g. 3): ").strip() or "0"
    colors = input("Colors (comma separated, e.g. R or W,U or leave empty for colorless): ").strip()
    type_line = input("Full type line (e.g. Creature — Dragon): ").strip() or type_
    image = input("Image URL (must be publicly accessible): ").strip()
    power = input("Power (leave empty if not a creature): ").strip()
    toughness = input("Toughness (leave empty if not a creature): ").strip()

    if not image:
        print("Image URL is required")
        return

    card = make_card(id_, name, type_, cost, colors, type_line, image, power, toughness)
    cards[id_] = card

    with open(CARDS_FILE, "w") as f:
        json.dump(cards, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Added '{name}' (id: {id_}) to {CARDS_FILE}")
    print(f"Total cards now: {len(cards)}")
    print("\nNext steps:")
    print("1. Re-upload the updated cards.json to your GitHub Pages / host")
    print("2. (Optional) bump the 'version' number in Game_MTG_Custom.json")

if __name__ == "__main__":
    main()
