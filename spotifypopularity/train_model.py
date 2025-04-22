import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv("dataset.csv")

# Convert 'explicit' column to int (if it's boolean or string)
df['explicit'] = df['explicit'].astype(int)

# Create the binary label: popular if popularity >= 70
df['is_popular'] = (df['popularity'] >= 70).astype(int)

# Drop non-numeric columns we don't need
non_numeric_cols = ['Unnamed: 0', 'track_id', 'artists', 'album_name', 'track_name', 'track_genre', 'popularity']
df.drop(columns=non_numeric_cols, inplace=True, errors='ignore')

# Drop rows with missing or invalid values
df.dropna(inplace=True)

# Separate features and labels
X = df.drop(columns=['is_popular'])
y = df['is_popular']

# Check all columns are numeric (optional debug step)
# print(X.dtypes)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into training/testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train logistic regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model, scaler, and feature names
with open("model.pkl", "wb") as f:
    pickle.dump((model, scaler, X.columns.tolist()), f)

print("✅ Model trained successfully and saved to model.pkl")
