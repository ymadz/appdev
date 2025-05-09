# ⚽ FIFA Player Dashboard with Machine Learning

This project is a web-based dashboard built with Django that uses a machine learning model (XGBoost Regressor) to predict FIFA players’ overall ratings. It visualizes player statistics, allows exploration by position, and evaluates model performance using real data.

---

## 📊 Dataset Overview

- **Source**: [FIFA 21 dataset from Kaggle](https://www.kaggle.com/stefanoleone992/fifa-21-complete-player-dataset)
- **Records**: ~18,000 player entries
- **Features Used**:
  - Age, Height, Weight
  - In-game stats: Pace, Shooting, Passing, Dribbling, Defending, Physic
  - Categorical: Preferred Foot, Work Rate, Player Positions
- **Target**: `overall` (overall rating)

---

## 🧹 Preprocessing Steps

1. **Handling Missing Values**:
   - Rows missing key numeric or target fields were dropped.

2. **Feature Engineering**:
   - `preferred_foot`: Encoded as binary (Right = 1, Left = 0)
   - `work_rate` and `player_positions`: Encoded using simple hashing
   - All features scaled naturally (XGBoost handles scaling internally)

3. **Splitting Data**:
   - `train_test_split` (80/20 ratio)

---

## 🤖 Model Architecture

- **Model Used**: `XGBoost Regressor`
- **Reason**: Efficient with tabular data, handles missing values, good out-of-the-box performance
- **Parameters**: Default `XGBRegressor()` settings for initial development

---

## 📈 Training Results

| Metric         | Score |
|----------------|-------|
| Train RMSE     | ~2.34 |
| Test RMSE      | ~2.35 |
| Train R² Score | 0.89  |
| Test R² Score  | 0.88  |
| Bias-Variance Status | Good Fit (Low Bias, Low Variance) |

> Note: These values are dynamically calculated and may vary slightly depending on the random train-test split.

---

## 🔒 Authentication

Authentication was added using Django’s built-in authentication system:

- Users must log in to access the dashboard
- `/login/`, `/logout/`, and `/register/` routes were created
- `@login_required` decorator used to protect dashboard views

---

## 🔧 Integration Steps

1. **Model Training**:  
   Train `XGBRegressor` on selected features and save using `joblib`:

   ```python
   from xgboost import XGBRegressor
   from joblib import dump

   model = XGBRegressor()
   model.fit(X_train, y_train)
   dump(model, 'xgboost_fifa_model.pkl')