# main.py
import pandas as pd
from preprocessing import load_and_preprocess_data
from feature_engineering import engineer_features
from model import train_model

def main():
    # Load and preprocess data
    data = load_and_preprocess_data('data')
    
    # Feature engineering
    data = engineer_features(data)

    # Train the model
    model, accuracy, report = train_model(data)

    # Save the model if desired (using joblib or pickle)
    # from joblib import dump
    # dump(model, 'premier_league_model.joblib')

if __name__ == "__main__":
    main()
