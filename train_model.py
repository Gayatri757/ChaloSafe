import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
df = pd.read_csv("crime_data.csv")  # Make sure you have crime_data.csv

# Check data
print(df.head())

# Select features and target
# Example: If dataset has 'crime_type', 'time_of_day', 'location', and 'severity'
X = df[['latitude', 'longitude', 'crime_per_area']]  # Use available features
# Define crime risk levels based on crime_per_area
def classify_risk(value):
    if value < 180:
        return 0  # Low risk
    elif value < 210:
        return 1  # Medium risk
    else:
        return 2  # High risk

# Create crime_risk column dynamically
df['crime_risk'] = df['crime_per_area'].apply(classify_risk)

# Now y will work correctly
y = df['crime_risk']

# Convert categorical data if necessary
X = pd.get_dummies(X)  # One-hot encoding if categorical

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save trained model
joblib.dump(model, "crime_model.pkl")
print("Model saved as crime_model.pkl")
