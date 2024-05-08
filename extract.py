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
        all_skus = []
        all_categories = []
        all_file_paths = []  # List to store the file path for each part number
        all_pages = []  # List to store the file path for each part number
        
        for page_num, page in enumerate(doc, start=1):
            if tabula.read_pdf(filepath, pages=page_num, multiple_tables=True):
                rect = fitz.Rect(0, 0, page.rect.width, 100)
                text = page.get_text()     
                prompt = (f'`{prompt_category}`:\n\nThis JSON data includes a table content of a pdf file and it includes page numbers, and corresponding categories. \nKeywords are page numbers and values are categories.\n These keywords(page numbers) mean page number ranges or individual page numbers.\n If I provide page number, give me only category value as normal text without page number from the above JSON data.\n\nThis is page number: {page_num}') 
                completion = client.chat.completions.create(
                max_tokens=1000,
                model="gpt-4-turbo",
                messages=[        
                    {"role": "user", "content": prompt}
                ]
                )

                full_category = completion.choices[0].message.content.strip('[]')         
                print(full_category)                    
                # Extract full text from the page for debugging or logging, optional
                prompt = (f'`{text}`:\n\nGive me all SKU numbers consisted of 6 letters as an array such as [sku, sku, sku, sku] without any additional descriptions from the above text content. Keep in mind this. You must find all sku numbers. \n\nIf can not see reasonable numbers from the text, you should return empty array([]). \n\nThis is related with my life. So you must not miss even one and give me all sku numbers from each page.')

                completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[        
                    {"role": "user", "content": prompt}
                ]
                )

                print(completion.choices[0].message.content)    
                skus = completion.choices[0].message.content.strip('[]').replace('\n', '').split(',')
                skus = [sku.strip() for sku in skus]
                unique_skus = list(set(skus))  # Remove duplicates by converting to a set and back to a list
                all_skus.extend(unique_skus)
                all_categories.extend([full_category] * len(unique_skus))
                all_file_paths.extend([filepath] * len(unique_skus))
                all_pages.extend([page_num] * len(unique_skus))

        # Create and save the data to a CSV file
        final_df = pd.DataFrame({
            'SKU Number': all_skus,
            'Category': all_categories,
            'Page Number': all_pages,
            'PDF File Path': all_file_paths
        })
        final_df.to_csv('extracted_skus_with_categories.csv', index=False)

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
