import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pickle

# Load your dataset
df = pd.read_csv("players_15.csv")

# Define features and target
features = ['pace', 'shooting', 'passing', 'dribbling', 'defending', 'physic']
target = 'overall'

X = df[features]
y = df[target]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost model
model = xgb.XGBRegressor()
model.fit(X_train, y_train)

# Evaluate (optional)
preds = model.predict(X_test)
rmse = mean_squared_error(y_test, preds) ** 0.5

print(f"RMSE: {rmse:.2f}")

# Save the model as pickle
# with open("xgboost_fifa_model.pkl", "wb") as f:
#     pickle.dump(model, f)

# print("✅ Model saved as xgboost_fifa_model.pkl")
