import json
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os

# ===== Paths =====
base_dir = os.path.dirname(__file__)
metrics_path = os.path.join(base_dir, "metrics.json")
data_path = os.path.join(base_dir, "data", "processed", "waste_management_processed.csv")
pdf_path = os.path.join(base_dir, "report.pdf")

# ===== Load Data =====
with open(metrics_path, "r") as f:
    metrics = json.load(f)

df = pd.read_csv(data_path)

# Dataset details
rows, cols = df.shape
missing_values = df.isnull().sum().sum()

# Best model
best_model = min(metrics, key=metrics.get)
best_rmse = metrics[best_model]

# ===== Create PDF =====
c = canvas.Canvas(pdf_path, pagesize=letter)
width, height = letter

# Title
c.setFont("Helvetica-Bold", 20)
c.drawString(50, height - 50, "Waste Management & Recycling - Model Report")

# Subtitle
c.setFont("Helvetica", 12)
c.drawString(50, height - 80, "Hackathon Project - Model Performance Summary")

# Date & Author
c.setFont("Helvetica-Oblique", 10)
c.drawString(50, height - 100, f"Date Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
c.drawString(50, height - 115, "Author: Geetanajali Chavan")  # Change to your name/team

# Dataset Information
c.setFont("Helvetica-Bold", 14)
c.drawString(50, height - 150, "Dataset Information:")
c.setFont("Helvetica", 12)
c.drawString(60, height - 170, f"Rows: {rows}")
c.drawString(60, height - 190, f"Columns: {cols}")
c.drawString(60, height - 210, f"Missing Values: {missing_values}")

# Model Metrics Section
c.setFont("Helvetica-Bold", 14)
c.drawString(50, height - 240, "Model Evaluation Metrics:")
y_pos = height - 260
c.setFont("Helvetica", 12)
for model_name, rmse in metrics.items():
    c.drawString(60, y_pos, f"{model_name}: RMSE = {rmse:.4f}")
    y_pos -= 20

# Highlight Best Model
c.setFont("Helvetica-Bold", 14)
c.drawString(50, y_pos - 10, "Best Model:")
c.setFont("Helvetica", 12)
c.drawString(60, y_pos - 30, f"{best_model} (RMSE = {best_rmse:.4f})")
y_pos -= 60

# Insights / Recommendations
c.setFont("Helvetica-Bold", 14)
c.drawString(50, y_pos, "Insights & Recommendations:")
c.setFont("Helvetica", 12)
c.drawString(60, y_pos - 20, "- Best model selected based on lowest RMSE.")
c.drawString(60, y_pos - 40, "- Can be deployed for waste volume prediction.")
c.drawString(60, y_pos - 60, "- Consider more feature engineering to improve accuracy.")
c.drawString(60, y_pos - 80, "- Use live IoT data for real-time waste monitoring.")

# Footer
c.setFont("Helvetica-Oblique", 10)
c.drawString(50, 30, "Generated automatically using ReportLab")

# Save PDF
c.save()

print(f"✅ Extended PDF report generated: {pdf_path}")
