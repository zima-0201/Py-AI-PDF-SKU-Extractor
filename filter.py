import csv
from category_index import check_array

# Index array for SKU numbers
index_skus = check_array

# Function to check if SKU number is in index array
def is_valid_sku(sku):
    return sku in index_skus

# Read CSV file and filter rows
def filter_csv(input_file, output_file):
    rows_to_keep = []
    with open(input_file, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sku = row['SKU Number']
            if is_valid_sku(sku):
                rows_to_keep.append(row)

    # Write filtered rows to new CSV file
    with open(output_file, mode='w', newline='') as csvfile:
        fieldnames = ['SKU Number', 'Category', 'Page Number', 'PDF File Path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows_to_keep:
            writer.writerow(row)

# Example usage
input_csv_file = 'extracted_skus_with_categories.csv'
output_csv_file = 'notinvolved.csv'
filter_csv(input_csv_file, output_csv_file)
print("Filtered CSV file created successfully.")
