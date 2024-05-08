import fitz  # PyMuPDF

def extract_categories(pdf_path):
    # Open the PDF
    doc = fitz.open(pdf_path)
    categories = []

    for i, page in enumerate(doc):
        # Define the rectangle area at the top of the page where the category is likely to be.
        # You may need to adjust these coordinates.
        rect = fitz.Rect(0, 0, page.rect.width, page.rect.height)
        
        # Extract text from the defined area
        text = page.get_textbox(rect)
        print(text)
        # Assuming the category is the first line of text extracted from this area
        category = text.split('\n')[0].strip()
        categories.append(category)

    doc.close()
    return categories

# Example usage:
pdf_path = 'path.pdf'
categories = extract_categories(pdf_path)

# Now `categories` holds all the extracted category names.
