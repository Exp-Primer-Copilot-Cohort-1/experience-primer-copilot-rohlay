import csv
import pandas as pd

filename = 'path/to/your/file.csv'

with open(filename, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        # Process each row of the CSV file
        print(row)


        # Load CSV into DataFrame
        df = pd.read_csv(filename)

        # Split DataFrame into separate DataFrames for rows and columns
        rows_df = df.copy()
        columns_df = df.transpose()

        # Print the DataFrames
        print("Rows DataFrame:")
        print(rows_df)

        print("Columns DataFrame:")
        print(columns_df)