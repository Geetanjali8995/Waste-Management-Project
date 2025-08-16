from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load trained model
model_path = os.path.join("models", "trained_model.pkl")
model = joblib.load(model_path)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"
        file = request.files["file"]
        if file.filename == "":
            return "No selected file"
        
        # Read uploaded CSV
        df = pd.read_csv(file)

        # 🔹 Preprocessing if needed (remove object cols except numeric)
        df_encoded = pd.get_dummies(df)
        
        # Predict
        preds = model.predict(df_encoded)
        
        # Prepare results dataframe
        df["Predicted Recycling Rate (%)"] = preds
        results_html = df.to_html(classes="table table-striped", index=False)
        
        return render_template("results.html", tables=[results_html])
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
