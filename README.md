# ♻ Waste Management & Recycling - Hackathon Project

## 📌 Overview
This project was created for the **Mini Hackathon: Waste Management & Recycling**.  
Our goal: **Predict waste volume** using machine learning models trained on landfill and recycling center data.  
By analyzing waste patterns, municipalities can **optimize collection schedules**, **reduce overflow**, and **improve recycling efficiency**.

---

## 📊 Dataset Overview
- **Source:** Provided hackathon dataset  
- **Rows:** ~700  
- **Columns:** Multiple numerical and categorical features (e.g., waste type, location, recycling rates)
- **Target Variable:** Waste volume (tons)
- **Cleaning Steps:**
  - Handled missing values
  - Encoded categorical columns (`Waste Type`, `Region`, etc.)
  - Removed non-numeric columns from modeling

---

## 📂 Project Structure

project_root/
│
├── data/
│ ├── raw/ # Raw dataset files
│ ├── processed/ # Cleaned CSVs
│
├── notebooks/
│ ├── eda.ipynb # Exploratory Data Analysis
│ ├── data_preparation.ipynb # Data cleaning & encoding
│ ├── model_training.ipynb # Model training & evaluation
│ ├── visualization.ipynb # Charts and performance visuals
│
├── src/
│ ├── inference.py # Predict from CSV
│
├── predictions/ # Output prediction files
├── models/ # Saved trained models
├── app.py # Flask app
├── templates/index.html # Web UI
├── metrics.json # Model scores
├── report.pdf # Generated summary report
├── README.md # This file
└── requirements.txt # Python dependencies

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Jupyter Notebooks (EDA, training)
jupyter notebook

4️⃣ Run Flask App
python app.py


Visit: http://127.0.0.1:5000

🖼 Example Outputs
EDA Visualization

Flask Prediction Interface

📈 Model Performance

| Model            | RMSE    |
| ---------------- | ------- |
| LinearRegression | 17.3203 |
| RandomForest     | 17.3758 |
| XGBoost          | 19.3053 |
| LightGBM         | 19.3761 |

✅ Best Model: LinearRegression

📑 Reports

report.pdf – Model summary, dataset info, insights.

metrics.json – RMSE scores.