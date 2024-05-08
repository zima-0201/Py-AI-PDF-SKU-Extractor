# AI-Powered PDF Data Extraction for E-commerce Category Navigation

## Overview

The script facilitates the automated extraction of SKU numbers and their corresponding categories from PDF files, utilizing AI to interpret complex page layouts and text arrangements. This automation is aimed at refining the structure and user navigation experience on an e-commerce platform.

## Video Preview

[![Video Preview](https://github.com/zima-0201/Project-Images/blob/main/video%20preview/Py-AI-PDF-SKU-Extractor.jpeg)](https://brand-car.s3.eu-north-1.amazonaws.com/Four+Seasons/Py-AI-PDF-SKU-Extractor.mp4)

## Features

- **PDF Reading:** Utilizes PyMuPDF (fitz) to access and read PDF files.
- **Table Extraction:** Employs Tabula to extract tables efficiently from the PDF documents, which is crucial for identifying SKU listings and corresponding data.
- **AI Integration:** Uses OpenAI's powerful language models to accurately determine the context and categorization of SKU numbers based on the surrounding text.
- **GUI Interface:** Incorporates tkinter for a user-friendly graphical interface that allows users to select PDF files easily and initiate the extraction process.
- **Data Handling:** Leverages pandas for organizing the extracted data into structured formats, making further processing and integration straightforward.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.x
- Libraries: PyMuPDF, Tabula, tkinter, pandas, python-dotenv
- An active OpenAI API key set in your environment variables (for AI features)

## Installation

1. Clone the repository or download the source code:
   ```bash
   git clone https://your-repository-link
   cd your-project-directory
   ```

2. Install the required Python libraries:
   ```bash
   pip install pymupdf tabula-py tkinter pandas python-dotenv
   ```

3. Set up your OpenAI API key:
   - Create a `.env` file in the project root.
   - Add `OPENAI_API_KEY=your_api_key_here` to the file.

## Usage

1. Run the script using the command:
   ```bash
   python pdf_data_extractor.py
   ```

2. Use the GUI to select a PDF file by clicking on the "Browse PDF" button.

3. Initiate the extraction process by clicking on the "Extract Data" button. The script will process each page of the PDF, use AI to interpret text and tables, and output the SKU numbers along with their corresponding categories.

4. The results will be saved in a CSV file named `extracted_skus_with_categories.csv`, containing columns for SKU numbers, categories, page numbers, and file paths.

## Data Processing Details

The script performs the following steps:
- Opens the selected PDF and reads it page by page.
- Extracts text and tables from each page.
- Uses AI models to interpret the text and extract SKU numbers and their respective categories based on the context provided by headers and surrounding text.
- Compiles the extracted data into a pandas DataFrame.
- Exports the data to a CSV file for easy integration into database systems or further analysis.
