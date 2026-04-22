from baseline import create_baseline
from verify import verify_files

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
