import joblib
import pandas as pd

# Load trained model
model = joblib.load("apple_quality_model.pkl")

# Example apple
sample = pd.DataFrame([{
    "Size": -3.5,
    "Weight": -2.0,
    "Sweetness": 6.0,
    "Crunchiness": 4.5,
    "Juiciness": 5.0,
    "Ripeness": 1.5,
    "Acidity": 2.0
}])

prediction = model.predict(sample)[0]

if prediction == 1:
    print("🍎 GOOD APPLE")
else:
    print("❌ BAD APPLE")
    re