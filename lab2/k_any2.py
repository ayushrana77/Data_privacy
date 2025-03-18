import pandas as pd
import numpy as np

# Function to perform basic generalization for k-anonymization
def generalize_data(df, quasi_identifiers, k=2):
    """
    Apply generalization (simple bucketing) to the quasi-identifiers to achieve k-anonymity.
    Args:
        df (pd.DataFrame): The input dataset.
        quasi_identifiers (list): List of column names to apply generalization.
        k (int): The minimum number of records for k-anonymity (default is 2).
    Returns:
        pd.DataFrame: The generalized dataset.
    """
    generalized_df = df.copy()

    # Generalization strategy: Bucketing (for simplicity)
    number_col = len(quasi_identifiers)
    number_row = len(df)
    print(number_col,number_row)
    arr = []
    for i in range(number_col):
        if(i%2 == 0):
            arr.append(0)
        else:
            arr.append(number_row-1)
    new_rows = []
    for i in range (number_row*(k-1)):
        new_row = {}
        for j in range (number_col):
            x = generalized_df[quasi_identifiers[j]][arr[j]]
            new_row[quasi_identifiers[j]] = x
            if(j%2 == 0):
                arr[j] += 1
                if arr[j] ==  number_row:
                    arr[j] = 0
            else:
                arr[j] -= 1
                if arr[j] == -1:
                    arr[j] = number_row-1
        # Collect new row for concatenation
        new_rows.append(new_row)
    # Concatenate the new rows to the generalized_df
    new_rows_df = pd.DataFrame(new_rows)
    generalized_df = pd.concat([generalized_df, new_rows_df], ignore_index=True)

    return generalized_df

def import_and_process_data(file_path, drop_columns, quasi_identifiers, k=2):
    """
    Import the data from a CSV file, drop unnecessary columns, and perform k-anonymization.
    Args:
        file_path (str): Path to the CSV file.
        drop_columns (list): List of columns to drop.
        quasi_identifiers (list): Columns to generalize for k-anonymization.
        k (int): The minimum number of records for k-anonymity.
    Returns:
        pd.DataFrame: The k-anonymous dataset.
    """
    # Load data from CSV
    df = pd.read_csv(file_path)
    
    # Drop unnecessary columns
    df = df.drop(columns=drop_columns)
    
    # Perform k-anonymization
    result_df = generalize_data(df, quasi_identifiers, k)
    
    return result_df

def save_to_csv(df, output_file):
    """
    Save the processed DataFrame to a CSV file.
    Args:
        df (pd.DataFrame): The DataFrame to save.
        output_file (str): The path where the CSV file will be saved.
    """
    df.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")

# Example usage
if __name__ == "__main__":
    # Path to your input CSV file
    file_path = 'input_d.csv'
    
    # Columns to drop
    drop_columns = ['Name']  # Example columns to drop
    
    # Quasi-identifiers (columns for k-anonymization)
    quasi_identifiers = ['Age', 'ZipCode','Address']  # Example quasi-identifiers
    
    # Perform k-anonymization
    result_df = import_and_process_data(file_path, drop_columns, quasi_identifiers, k=2)
    
    # Save the result to a new CSV file
    save_to_csv(result_df, 'output_k_ano.csv')
