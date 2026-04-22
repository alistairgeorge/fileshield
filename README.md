# FileShield 

FileShield is a **file integrity verification tool** written in Python.  
It allows users to create a baseline of trusted files, verify them against SHA‑256 hashes, and detect changes (modified, missing, or unchanged).  
Results are displayed in a Tkinter GUI with colour‑coded output and logged for audit purposes.

---

## Features
- **Baseline Creation**: Generate a JSON baseline of file hashes.
- **Verification**: Compare current files against the baseline.
- **Colour‑coded GUI**: Green = unchanged, Orange = modified, Red = missing.
- **Logging**: Results appended to `verification.log` for audit trails.
- **Modular Design**: Separate scripts for hashing, baseline management, verification, utilities, and GUI.

---

## Repository Structure
fileshield/
├── baseline.py        # Create baseline JSON
├── verify.py          # Verify files against baseline
├── hashing.py         # SHA-256 hashing functions
├── utils.py           # Logging and encoding utilities
├── main_gui.py        # Tkinter GUI interface
├── main.py            # Entry point
├── baseline.json      # Example baseline file
├── verification.log   # Example log output
└── logs/              # Directory for log files
```

---

## Installation & Usage

### Prerequisites
- Python 3.8+
- Tkinter (for GUI)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/alistairgeorge/fileshield.git
   cd fileshield
   ```
2. Run the GUI:
   ```bash
   python main_gui.py
   ```
3. Use the buttons to **Create Baseline** or **Verify Files**.
4. Check results in the GUI and `verification.log`.

---

## Example Workflow
1. Select a directory and **Create Baseline** → generates `baseline.json`.
2. Later, run **Verify Files** → compares current files with baseline.
3. GUI shows results (green/orange/red).
4. Logs saved in `verification.log`.

---

## License
This project is licensed under the MIT License — free to use, modify, and distribute.
```

