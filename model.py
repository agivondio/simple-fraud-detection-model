import pandas as pd
from sklearn.ensemble import IsolationForest

# Load dataset
data = pd.read_csv("dataset.csv")

# Features
X = data[["amount", "frequency"]]

# Train model
model = IsolationForest(contamination=0.3)
model.fit(X)

# Predict
data["prediction"] = model.predict(X)

# Convert result (-1 fraud, 1 normal)
data["prediction"] = data["prediction"].apply(lambda x: 1 if x == -1 else 0)

print("=== Fraud Detection Result ===")
print(data)

# Test with new transaction
new_data = pd.DataFrame([[6000, 9]], columns=["amount", "frequency"])
prediction = model.predict(new_data)

print("\nNew Transaction:", new_data)
print("Fraud?" , "YES" if prediction[0] == -1 else "NO")

print("\n=== Summary ===")
fraud_count = data["prediction"].sum()
print(f"Detected fraud cases: {fraud_count}")