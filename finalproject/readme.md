This project is a web-based dashboard built with Django that uses a machine learning model (XGBoost Regressor) to predict FIFA players’ overall ratings. It visualizes player statistics, allows exploration by position, and evaluates model performance using real data.

---

## 📊 Dataset Overview

- **Source**: [FIFA 21 dataset from Kaggle](https://www.kaggle.com/stefanoleone992/fifa-21-complete-player-dataset)  
- **Records**: Approximately 18,000 player entries  
- **Target Variable**: `overall` (the overall rating of a player)

### 🔍 Features Used

The following features were selected as they contributed significantly to model performance:

- **Age**: Player's age in years  
- **Height**: Player’s height (in cm)  
- **Weight**: Player’s weight (in kg)  
- **Pace**: Combined sprint speed and acceleration  
- **Shooting**: Finishing, long shots, and shot power  
- **Passing**: Short and long passing accuracy  
- **Dribbling**: Ball control and agility  
- **Defending**: Defensive awareness, standing tackle  
- **Physic**: Strength, aggression, and stamina  
- **Preferred Foot**: Categorical feature, encoded (Right = 1, Left = 0)  
- **Work Rate**: Player’s attacking/defensive work rate, encoded using hash  
- **Player Positions**: Primary position, hashed to numeric

> ⚠️ **Note**: A large number of original columns were removed because they were not relevant to our use case or were redundant with the features above. This helped reduce noise and improve training speed.

---

## 🧹 Preprocessing Steps

1. **Handling Missing Values**  
   - Dropped rows with missing values in key numerical or target fields.

2. **Feature Engineering**  
   - `preferred_foot`: Binary encoding  
   - `work_rate`, `player_positions`: Encoded via lightweight hash-based encoding  
   - Scaling was not explicitly required since XGBoost handles it internally.

3. **Splitting Data**  
   - Used an 80/20 split for training and testing.

---

## 🤖 Model Architecture

- **Model Used**: `XGBoost Regressor`  
- **Why XGBoost?**  
  - Performs exceptionally well on structured/tabular data  
  - Handles missing values natively  
  - Offers fast training and good generalization

- **Parameters**: Default `XGBRegressor()` used for the initial version.

---

## 📈 Training Results

| Metric           | Score  |
|------------------|--------|
| Train RMSE       | ~2.34  |
| Test RMSE        | ~2.35  |
| Train R² Score   | 0.89   |
| Test R² Score    | 0.88   |
| Fit Quality      | Good Fit (Low Bias, Low Variance) |

> Note: Scores may vary slightly depending on the random state used during `train_test_split`.

---

## 🔒 Authentication

Authentication was implemented using Django’s built-in system to protect the dashboard:

- `/login/` – for existing users  
- `/logout/` – to securely sign out  
- `/register/` – for new user signup  
- All key dashboard views are protected using Django's `@login_required` decorator.

---

## ⚠️ Challenges Encountered

### Data Encoding
- Hash encoding was used as a lightweight method to handle categorical values such as `work_rate` and `player_positions` quickly and efficiently.

### Model Generalization
- Addressed early signs of overfitting by using an 80/20 train-test split and monitoring performance metrics like RMSE and R² on both datasets.

### Authentication
- Implemented Django’s authentication system securely, managing session handling and redirect logic to ensure users must log in to access the dashboard.

### Dashboard Design
- Balanced simplicity with clarity: minimal layout, selected visualizations, and responsive design using Bootstrap for a professional and user-friendly UI.
"""

---

## 🔧 Integration Steps

1. **Model Training & Saving**

The model was trained using `XGBRegressor` and saved with `joblib`:

```python
from xgboost import XGBRegressor
from joblib import dump

model = XGBRegressor()
model.fit(X_train, y_train)
dump(model, 'xgboost_fifa_model.pkl')
