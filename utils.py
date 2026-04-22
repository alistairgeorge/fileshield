import os

def log_results(results, log_file="logs/verification.log"):
    """Save verification results to a log file (UTF-8 safe)."""
    os.makedirs("logs", exist_ok=True)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write("Verification Run:\n")
        for file, status in results.items():
            f.write(f"{file}: {status}\n")
        f.write("\n")
