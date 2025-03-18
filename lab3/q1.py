import pandas as pd

# Function to apply X-Y Anonymity
def apply_xy_anonymity(df, k=2):
    # Ensure 'Age' and 'Zip' columns are treated as object (string) type
    df['Age'] = df['Age'].astype(str)
    df['Zip'] = df['Zip'].astype(str)
    
    # Group by the combination of 'Age' and 'Zip' and count the occurrences
    grouped = df.groupby(['Age', 'Zip']).size().reset_index(name='Count')
    
    # Identify combinations that occur less than k times
    underrepresented = grouped[grouped['Count'] > k]
    
    # Iterate through the underrepresented combinations and generalize
    for _, row in underrepresented.iterrows():
        age, zip_code = row['Age'], row['Zip']
        # Generalize the Age and Zip for all matching rows
        df.loc[(df['Age'] == age) & (df['Zip'] == zip_code), 'Age'] = 'Generalized'
        df.loc[(df['Age'] == age) & (df['Zip'] == zip_code), 'Zip'] = 'Generalized'
    
    return df

# Main function to process the CSV files
def process_csv(input_file, output_file, k=2):
    # Read the input CSV file
    df = pd.read_csv(input_file)
    
    # Apply X-Y Anonymity
    anonymized_df = apply_xy_anonymity(df, k)
    
    # Write the anonymized data to a new CSV file
    anonymized_df.to_csv(output_file, index=False)
    print(f"X-Y Anonymity applied successfully. The result is saved in '{output_file}'")

# Example usage:
input_file = 'input_data.csv'  # Path to the input CSV file
output_file = 'output_data_anonymized.csv'  # Path for the output CSV file

# Process the CSV file and apply X-Y Anonymity with k=2
process_csv(input_file, output_file, k=2)





