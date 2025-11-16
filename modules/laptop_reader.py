import json
import os

def load_laptops(base_dir=None):
    if base_dir is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    laptops_path = os.path.join(base_dir, "data", "laptops.json")
    with open(laptops_path, "r", encoding="utf-8") as f:
        return json.load(f)

def find_laptop(name, laptops):
    name = name.lower()
    return next((l for l in laptops if l["name"].lower() == name), None)
