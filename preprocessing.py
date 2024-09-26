import pandas as pd
import os

def load_and_preprocess_data(data_folder):
    dataframes = []
    
    for filename in os.listdir(data_folder):
        if filename.endswith('.csv'):
            file_path = os.path.join(data_folder, filename)
            df = pd.read_csv(file_path)
            
            # Select relevant columns for the model
            df = df[['Div', 'Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR', 'HS', 'AS', 'HF', 'AF']]
            dataframes.append(df)
    
    # Concatenate all DataFrames
    full_data = pd.concat(dataframes, ignore_index=True)
    
    # Convert date to datetime format
    full_data['Date'] = pd.to_datetime(full_data['Date'])
    
    return full_data

if __name__ == "__main__":
    data = load_and_preprocess_data('data')
    print(data.head())
