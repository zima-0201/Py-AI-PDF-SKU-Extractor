import csv
from category_index import check_array

# Index array for SKU numbers
index_skus = check_array

# Function to create a set of SKU numbers from CSV
def create_sku_set(input_file):
    sku_set = set()
    with open(input_file, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sku = row['SKU Number']
            sku_set.add(sku)
    return sku_set

# Read CSV file and filter rows based on SKU set
def filter_csv(input_file, output_file, sku_set):
    rows_to_keep = []
    with open(input_file, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['SKU Number'] in sku_set:
                rows_to_keep.append(row)

    # Write filtered rows to new CSV file
    with open(output_file, mode='w', newline='') as csvfile:
        fieldnames = ['SKU Number', 'Category', 'Page Number', 'PDF File Path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows_to_keep:
            writer.writerow(row)

# Example usage
input_csv_file = 'filtered_data-2.csv'
output_csv_file = 'filtered_skus.csv'

# Create set of SKU numbers from CSV
sku_set = create_sku_set(input_csv_file)

# Filter only SKUs that are in the index array
filtered_sku_set = set(index_skus).intersection(sku_set)

# Filter the CSV based on the filtered SKU set
filter_csv(input_csv_file, output_csv_file, filtered_sku_set)
print("Filtered CSV file created successfully.")
