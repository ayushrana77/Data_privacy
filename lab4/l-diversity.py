import pandas as pd
from collections import Counter

def l_diversity(input_csv, output_csv, quasi_identifiers, sensitive_attribute, l):
    """
    Applies l-diversity to the input CSV file.
    
    Args:
    - input_csv (str): Path to the input CSV file.
    - output_csv (str): Path to the output anonymized CSV file.
    - quasi_identifiers (list): List of quasi-identifier column names.
    - sensitive_attribute (str): Name of the sensitive attribute column.
    - l (int): The l-diversity parameter.

    Returns:
    - None: Outputs the l-diverse data to a CSV file.
    """
    # Read the input CSV
    df = pd.read_csv(input_csv)

    # Group by quasi-identifiers
    grouped = df.groupby(quasi_identifiers)

    # Create an output DataFrame
    anonymized_data = []

    for _, group in grouped:
        # Count sensitive values
        sensitive_counts = Counter(group[sensitive_attribute])

        # Check if the group satisfies l-diversity
        if len(sensitive_counts) >= l:
            # Add the entire group to the anonymized data
            anonymized_data.append(group)
        else:
            # Suppress or generalize the group if it doesn't meet l-diversity
            suppressed_group = group.copy()
            suppressed_group[sensitive_attribute] = "Suppressed"
            anonymized_data.append(suppressed_group)

    # Concatenate all the groups
    anonymized_df = pd.concat(anonymized_data)

    # Output the anonymized data to a new CSV
    anonymized_df.to_csv(output_csv, index=False)
    print(f"Anonymized data has been saved to {output_csv}")


# Example Usage
input_file = "input_data.csv"  # Replace with your input CSV path
output_file = "anonymized_data.csv"  # Replace with your desired output CSV path
quasi_id_columns = ["Age", "Zipcode"]  # Replace with your quasi-identifiers
sensitive_column = "Disease"  # Replace with your sensitive attribute
l_value = 5  # Replace with your desired l-diversity value

l_diversity(input_file, output_file, quasi_id_columns, sensitive_column, l_value)
