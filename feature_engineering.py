# feature_engineering.py
import pandas as pd

def engineer_features(data):
    # Encode FTR (Full Time Result) into a numerical format
    data['FTR'] = data['FTR'].map({'H': 1, 'D': 0, 'A': -1})  # Home Win, Draw, Away Win

    # Create features for home and away performance
    home_stats = data.groupby('HomeTeam').agg({
        'FTHG': 'mean',  # average goals scored at home
        'FTAG': 'mean',  # average goals conceded at home
        'FTR': 'mean'     # average result (1 for win, 0 for draw, -1 for loss)
    }).rename(columns={'FTHG': 'HomeGoalsScored', 'FTAG': 'HomeGoalsConceded', 'FTR': 'HomeWinRate'})

    away_stats = data.groupby('AwayTeam').agg({
        'FTHG': 'mean',  # average goals scored away
        'FTAG': 'mean',  # average goals conceded away
        'FTR': 'mean'     # average result
    }).rename(columns={'FTHG': 'AwayGoalsScored', 'FTAG': 'AwayGoalsConceded', 'FTR': 'AwayWinRate'})

    # Merge the home and away stats back into the original dataframe
    data = data.merge(home_stats, left_on='HomeTeam', right_index=True, how='left')
    data = data.merge(away_stats, left_on='AwayTeam', right_index=True, how='left')
    
    return data

if __name__ == "__main__":
    # Sample DataFrame for testing purposes
    sample_data = pd.DataFrame({
        'Div': ['E0', 'E0', 'E0'],
        'Date': ['2014-08-16', '2014-08-16', '2014-08-17'],
        'HomeTeam': ['A', 'B', 'C'],
        'AwayTeam': ['B', 'C', 'A'],
        'FTHG': [1, 2, 3],
        'FTAG': [0, 1, 1],
        'FTR': ['H', 'H', 'A'],
        'HS': [10, 12, 8],
        'AS': [5, 3, 7],
        'HF': [10, 15, 8],
        'AF': [2, 5, 7],
    })
    features = engineer_features(sample_data)
    print(features.head())
