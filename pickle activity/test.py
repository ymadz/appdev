import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor
import pickle

# Load the dataset
df = pd.read_csv("players_15.csv")

# Drop rows where the target value is missing
df.dropna(subset=["overall"], inplace=True)

# Define features and target
features = [
    "age", "height_cm", "weight_kg", "potential", "value_eur", "wage_eur",
    "international_reputation", "weak_foot", "skill_moves",
    "pace", "shooting", "passing", "dribbling", "defending", "physic"
]
X = df[features].copy()
y = df["overall"]

# Fill missing values in X
X = X.fillna(X.mean(numeric_only=True))

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Initialize and train XGBoost model
model = XGBRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Calculate RMSE manually
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"XGBoost RMSE: {rmse:.2f}")

# Save model with pickle
# with open("xgb_fifa_model.pkl", "wb") as f:
#     pickle.dump(model, f)

# print("XGBoost model saved as xgb_fifa_model.pkl")
