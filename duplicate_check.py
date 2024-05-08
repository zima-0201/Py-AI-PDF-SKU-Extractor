import pandas as pd

# Define the path to your CSV file
file_path = 'source.csv'

try:
    # Attempt to read the CSV file with UTF-8 encoding
    df = pd.read_csv(file_path)
except UnicodeDecodeError:
    # If a UnicodeDecodeError occurs, try reading with 'latin1' encoding
    df = pd.read_csv(file_path, encoding='latin1')

# Drop duplicates based on SKU Number and Page Number
df_filtered = df.drop_duplicates(subset=['SKU Number', 'Page Number'])

# Save the filtered data to a new CSV file
df_filtered.to_csv('filtered_file.csv', index=False)

print("Filtered file saved as 'filtered_file.csv'.")
