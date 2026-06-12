import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
df = pd.read_csv("apple_quality.csv")

# Remove ID column if present
if "A_id" in df.columns:
    df.drop("A_id", axis=1, inplace=True)

# Convert target labels
df["Quality"] = df["Quality"].map({
    "good": 1,
    "bad": 0
})

# Convert all columns to numeric
for col in df.columns:
    if col != "Quality":
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove rows with missing values
df.dropna(inplace=True)

# Features and target
X = df.drop("Quality", axis=1)
y = df["Quality"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

print("\nAccuracy:")
print(accuracy_score(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Save model
joblib.dump(model, "apple_quality_model.pkl")

print("\nModel saved as apple_quality_model.pkl")