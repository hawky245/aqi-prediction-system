# AQI Prediction System

## Overview

AQI Prediction System is a machine learning application that predicts future Air Quality Index (AQI) values using historical air quality data and Linear Regression.

The application provides AQI forecasting, visualization of future trends, and classification of predicted air quality levels.

## Features

- Future AQI prediction
- Interactive Streamlit interface
- AQI trend visualization
- Air quality classification
- Machine learning based forecasting

## Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib
- Scikit-Learn

## Machine Learning Model

The project uses Linear Regression trained on:

- Day
- Month
- Year

to predict AQI values for future dates.

## AQI Categories

| AQI Range | Category |
|------------|-----------|
| 0-50 | Good |
| 51-100 | Moderate |
| 101-200 | Poor |
| Above 200 | Severe |

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Future Improvements

- Random Forest Regression
- XGBoost
- LSTM Forecasting
- Weather Parameter Integration
- Multi-city Predictions

## Author

Abhay Surya R

## License

MIT License
