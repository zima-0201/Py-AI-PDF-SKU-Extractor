import csv
from sku_data import page_categories, sku_pages_2

# Dictionary to store unique SKU and Category combinations to prevent duplicates
unique_sku_categories = {}

# Iterate over each SKU and its pages
for sku, pages in sku_pages_2.items():
    for page in pages:
        page_str = str(page)
        if page_str in page_categories:
            category = page_categories[page_str]
            # Create a unique key for SKU and category
            key = (sku, category)
            # Only add to the output if this specific SKU-category combination hasn't been added yet
            if key not in unique_sku_categories:
                unique_sku_categories[key] = page

# Convert the dictionary to a list for writing to CSV
output_list = [[str(sku), category, page] for (sku, category), page in unique_sku_categories.items()]

# Write the output list to a CSV file
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(['SKU', 'Category', 'Page Number'])
    # Write the data
    writer.writerows(output_list)