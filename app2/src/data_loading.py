# Generate a python function to read the csv data & gives dataframe
import pandas as pd
def load_data(file_path):
    """
    Load data from a CSV file and return a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: A DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")
        return None