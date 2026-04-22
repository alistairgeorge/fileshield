import os
import json
from hashing import generate_hash
from utils import log_results

def verify_files(baseline_file="baseline.json"):
    """Verify files against stored baseline hashes."""
    if not os.path.exists(baseline_file):
        print("No baseline found. Please create one first.")
        return None

    with open(baseline_file, "r", encoding="utf-8") as f:
        baseline = json.load(f)

    results = {}
    for file, stored_hash in baseline.items():
        if not os.path.exists(file):
            results[file] = "Missing"
        else:
            current_hash = generate_hash(file)
            if current_hash == stored_hash:
                results[file] = "Unchanged"
            else:
                results[file] = "Modified"

    # Save results to log
    log_results(results)
    return results
