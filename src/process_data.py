import pandas as pd

def process_excel(file_path):
    try:
        print(f"Attempting to load file: {file_path}")  # Debugging message
        df = pd.read_excel(file_path)
        print("File successfully loaded!")
        print(df.head())  # Display the first few rows of the file
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Adjusted file path for relative location
    file_path = "../input/2023 CVD Cylinder Log Sheet.xlsx"
    process_excel(file_path)
