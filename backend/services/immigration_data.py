import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_PATH = BASE_DIR / "data" / "immigration_rules.json"

with open(DATA_PATH, encoding="utf-8") as f:
    IMMIGRATION_DATA = json.load(f)

def get_country_rules(country: str):
    return IMMIGRATION_DATA.get(country)
