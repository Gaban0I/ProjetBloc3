
import os
import requests
import zipfile
import pandas as pd

# Configuration
# Build paths relative to the project root, which is one level up from the script's location (src).
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
DOWNLOAD_URL = "https://www.kaggle.com/api/v1/datasets/download/blastchar/telco-customer-churn"
ZIP_PATH = os.path.join(DATA_DIR, "telco-customer-churn.zip")
RAW_CSV_NAME = "WA_Fn-UseC_-Telco-Customer-Churn.csv"
PROCESSED_CSV_PATH = os.path.join(DATA_DIR, "churn_data_processed.csv")

def download_and_unzip_data():
    """
    Downloads and unzips the Telco Customer Churn dataset.
    """
    print("Creating data directory...")
    os.makedirs(DATA_DIR, exist_ok=True)

    print(f"Downloading data from {DOWNLOAD_URL}...")
    response = requests.get(DOWNLOAD_URL, stream=True)
    response.raise_for_status()  # Raise an exception for bad status codes

    with open(ZIP_PATH, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Data downloaded to {ZIP_PATH}")

    print(f"Unzipping {ZIP_PATH}...")
    with zipfile.ZipFile(ZIP_PATH, "r") as zip_ref:
        zip_ref.extractall(DATA_DIR)
    print(f"Data unzipped in {DATA_DIR}")
    
    # Clean up the zip file
    os.remove(ZIP_PATH)
    print(f"Removed zip file: {ZIP_PATH}")


def preprocess_data():
    """
    Loads the raw data, performs initial cleaning, and saves the result.
    """
    raw_csv_path = os.path.join(DATA_DIR, RAW_CSV_NAME)
    if not os.path.exists(raw_csv_path):
        print(f"Error: Raw data file not found at {raw_csv_path}")
        return

    print(f"Loading raw data from {raw_csv_path}...")
    df = pd.read_csv(raw_csv_path)

    print("Starting data preprocessing...")
    
    # The 'TotalCharges' column has spaces for new customers.
    # Convert to numeric, coercing errors to NaN, then fill with 0.
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df['TotalCharges'].fillna(0, inplace=True)
    print("Cleaned 'TotalCharges' column.")

    print(f"Saving processed data to {PROCESSED_CSV_PATH}...")
    df.to_csv(PROCESSED_CSV_PATH, index=False)
    print("Preprocessing complete.")


if __name__ == "__main__":
    # Check if processed data already exists
    if os.path.exists(PROCESSED_CSV_PATH):
        print(f"Processed data already found at {PROCESSED_CSV_PATH}. Skipping script.")
    else:
        download_and_unzip_data()
        preprocess_data()

