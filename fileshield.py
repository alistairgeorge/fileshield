import hashlib
import os
import json

# -------------------------------
# Generate SHA-256 hash for a file
# -------------------------------
def generate_hash(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

# -------------------------------
# Create baseline (store hashes)
# -------------------------------
def create_baseline(file_list, baseline_file="baseline.json"):
    baseline = {}
    for file in file_list:
        if os.path.exists(file):
            baseline[file] = generate_hash(file)
        else:
            print(f"Warning: {file} not found.")
    with open(baseline_file, "w") as f:
        json.dump(baseline, f, indent=4)
    print("Baseline created successfully.")

# -------------------------------
# Verify files against baseline
# -------------------------------
def verify_files(baseline_file="baseline.json"):
    if not os.path.exists(baseline_file):
        print("No baseline found. Please create one first.")
        return

    with open(baseline_file, "r") as f:
        baseline = json.load(f)

    print("\nVerification Results:")
    for file, stored_hash in baseline.items():
        if not os.path.exists(file):
            print(f"{file}: Missing ❌")
        else:
            current_hash = generate_hash(file)
            if current_hash == stored_hash:
                print(f"{file}: Unchanged ✅")
            else:
                print(f"{file}: Modified ⚠️")

# -------------------------------
# Main program flow
# -------------------------------
def main():
    print("=== FileShield – File Integrity Checker ===")
    print("1. Create baseline")
    print("2. Verify files")
    choice = input("Enter choice (1/2): ")

    if choice == "1":
        files = input("Enter file paths separated by commas: ").split(",")
        create_baseline([f.strip() for f in files])
    elif choice == "2":
        verify_files()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
