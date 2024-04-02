import pandas as pd

def update_local_data(input_csv, output_csv):
    # Read input CSV file into a pandas DataFrame
    df = pd.read_csv(input_csv)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Write DataFrame to output CSV file
    df.to_csv(output_csv, index=False)