import tkinter as tk
from tkinter import filedialog, messagebox
from baseline import create_baseline
from verify import verify_files

def select_files():
    files = filedialog.askopenfilenames(title="Select files to monitor")
    if files:
        create_baseline(files)
        messagebox.showinfo("FileShield", "Baseline created successfully!")

def run_verification():
    results = verify_files()
    if results:
        output_text.delete("1.0", tk.END)
        for file, status in results.items():
            if status == "Unchanged":
                color = "green"
            elif status == "Modified":
                color = "orange"
            else:  # Missing
                color = "red"
            output_text.insert(tk.END, f"{file}: {status}\n", color)

# Create main window
root = tk.Tk()
root.title("FileShield – File Integrity Checker")
root.geometry("600x400")

# Buttons
tk.Button(root, text="Create Baseline", command=select_files, width=20).pack(pady=10)
tk.Button(root, text="Verify Files", command=run_verification, width=20).pack(pady=10)

# Output area
output_text = tk.Text(root, height=15, width=70)
output_text.pack(pady=10)

# Define text tags for colors
output_text.tag_config("green", foreground="green")
output_text.tag_config("orange", foreground="orange")
output_text.tag_config("red", foreground="red")

root.mainloop()
