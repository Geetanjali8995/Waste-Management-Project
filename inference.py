import pandas as pd
import joblib
import sys
import os

# -----------------------------
# Load Model
# -----------------------------
model_path = os.path.join(os.path.dirname(__file__), "../models/trained_model.pkl")
model = joblib.load(model_path)

# -----------------------------
# Load New Data
# -----------------------------
if len(sys.argv) != 2:
    print("Usage: python inference.py <path_to_new_data.csv>")
    sys.exit(1)

new_data_path = sys.argv[1]
new_data = pd.read_csv(new_data_path)

# -----------------------------
# Predict
# -----------------------------
predictions = model.predict(new_data)

# -----------------------------
# Save Predictions
# -----------------------------
output_path = os.path.join(os.path.dirname(__file__), "../predictions/new_predictions.csv")
pd.DataFrame({"Prediction": predictions}).to_csv(output_path, index=False)

print(f"Predictions saved to {output_path}")
