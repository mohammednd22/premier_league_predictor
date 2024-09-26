# Premier League Winner Prediction

This project develops a machine learning model to predict the winner of the Premier League using historical match data. The model utilizes data from the past 10 seasons, incorporating various features such as match statistics, team performance, and betting odds.

## Features

- **Data Preprocessing:** Loads and cleans data from multiple CSV files for each season.
- **Feature Engineering:** Creates new features like goal difference and encodes categorical variables.
- **Model Training:** Uses a pipeline to preprocess data and train a predictive model.
- **Output:** Provides predictions based on the trained model.

## Dataset

The dataset includes CSV files for each season from 2014 to 2024, located in the `data/` directory. Key columns include:

- `Div`: Division
- `Date`: Match date
- `HomeTeam`: Name of the home team
- `AwayTeam`: Name of the away team
- `FTHG`: Full Time Home Goals
- `FTAG`: Full Time Away Goals
- `FTR`: Full Time Result (H, D, A)
