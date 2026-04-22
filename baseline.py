import os
import json
from hashing import generate_hash

def create_baseline(file_list, baseline_file="baseline.json"):
    """Create baseline hashes for selected files."""
    baseline = {}
    for file in file_list:
        if os.path.exists(file):
            baseline[file] = generate_hash(file)
        else:
            print(f"Warning: {file} not found.")
    with open(baseline_file, "w", encoding="utf-8") as f:
        json.dump(baseline, f, indent=4)
    print("Baseline created successfully.")
