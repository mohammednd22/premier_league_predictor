# model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_model(data):
    # Features and labels
    X = data[['HomeGoalsScored', 'HomeGoalsConceded', 'HomeWinRate',
               'AwayGoalsScored', 'AwayGoalsConceded', 'AwayWinRate']]
    y = data['FTR']  # Target variable

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # Train the model
    model.fit(X_train, y_train)

    # Predictions
    predictions = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions)
    
    return model, accuracy, report

if __name__ == "__main__":
    data = pd.read_csv('data/combined_data.csv')  # This should be your processed data file
    model, accuracy, report = train_model(data)
    print(f'Accuracy: {accuracy}')
    print('Classification Report:')
    print(report)
