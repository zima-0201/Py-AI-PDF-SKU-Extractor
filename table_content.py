import fitz  # PyMuPDF for reading PDFs
import tabula  # For extracting tables from PDFs
import tkinter as tk
import pandas as pd
import time
import os
import dotenv
from prompt import prompt_category
from openai import OpenAI
from tkinter import filedialog, messagebox

dotenv.load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)
    
def select_pdf():
    global filepath
    filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if not filepath:
        messagebox.showerror("Error", "No file was selected.")
    else:
        messagebox.showinfo("File Selected", f"You have selected {filepath}")

def extract_data():
    if not filepath:
        messagebox.showerror("Error", "Please select a PDF file first.")
        return
    try:
        doc = fitz.open(filepath)
        text = ''
        all_skus = []
        all_categories = []
        all_file_paths = []  # List to store the file path for each part number
        all_pages = []  # List to store the file path for each part number
        page_nums = [142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152]

        # Define the output file path
        output_file_path = "extracted_text.txt"

        # Write the extracted text to the output file
        with open(output_file_path, "w", encoding="utf-8") as text_file:
            for page_num in page_nums:
                # Assuming 'doc' is the PDF document opened with PyMuPDF
                text += f'{doc[page_num-1].get_text()}\n'
            text_file.write(text)
                
        doc.close()
        messagebox.showinfo("Success", "Data extracted and saved to CSV.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to extract data from PDF: {e}")

root = tk.Tk()
root.title("PDF Data Extractor")

browse_button = tk.Button(root, text="Browse PDF", command=select_pdf)
browse_button.pack(pady=10)

run_button = tk.Button(root, text="Extract Data", command=extract_data)
run_button.pack(pady=10)

root.mainloop()
