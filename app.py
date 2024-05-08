import tabula
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd

def select_pdf():
    global filepath  # Use a global variable to store the file path
    filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not filepath:
        messagebox.showerror("Error", "No file was selected.")
    else:
        messagebox.showinfo("File Selected", f"You have selected {filepath}")

def extract_data():
    """ Extract tables from a selected PDF file that include 'part number' in the headers """
    if not filepath:
        messagebox.showerror("Error", "Please select a PDF file first.")
        return
    try:
        # Extract tables
        dfs = tabula.read_pdf(filepath, pages='all', multiple_tables=True)
        for i, df in enumerate(dfs):
            # Normalize the column names to lowercase for easier comparison
            df.columns = [c.lower() for c in df.columns]
            # Check if 'part number' and 'description' are in the headers
            if 'part number' in df.columns and 'description' in df.columns:
                # Save the data to a CSV file
                df.to_csv(f'extracted_data_{i}.csv', index=False)
        messagebox.showinfo("Success", "Data extracted and saved to CSV files.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract tables from PDF: {e}")

root = tk.Tk()
root.title("PDF Table Extractor")

# Only keep the browse and run buttons
browse_button = tk.Button(root, text="Browse PDF", command=select_pdf)
browse_button.pack(pady=10)

run_button = tk.Button(root, text="Extract Data", command=extract_data)
run_button.pack(pady=10)

root.mainloop()
