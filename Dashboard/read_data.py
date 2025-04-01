import pandas as pd
from pathlib import Path

def read_data():
    # Corrected path handling
    data_path = Path("betyg_o_prov_riksnivå.xlsx")  # Path to the file

    # Read Excel with sheet name and skip rows
    df = pd.read_excel(data_path, sheet_name='Tabell 1B', skiprows=7)  
    return df

if __name__ == "__main__":
    df = read_data()
    print(df.columns)
