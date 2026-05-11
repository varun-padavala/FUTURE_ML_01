# 🚀 AI-Powered Sales Forecasting Dashboard

## 📌 Overview
This project builds a sales forecasting system using historical retail data to predict future demand and support business decision-making.

The system uses time-series modeling (Facebook Prophet) and presents results through a Power BI dashboard.

---

## 🎯 Objectives
- Forecast future sales trends
- Identify seasonal patterns
- Support inventory and staffing decisions

---

## 🛠 Tech Stack
- Python (Pandas, Prophet, Matplotlib, NumPy, Scikit-learn)
- Power BI
- Superstore Dataset

---

## ⚙️ Approach

### 1. Data Preparation
- Cleaned dataset
- Converted date column
- Aggregated monthly sales

### 2. Modeling
- Applied Prophet for time-series forecasting
- Captured trend + seasonality

### 3. Forecasting
- Predicted next 12 months
- Generated confidence intervals

### 4. Visualization
- Created forecast plots
- Built Power BI dashboard

---

## 📊 Results

- Model successfully captured sales trend and seasonal patterns
- Forecast shows continued business growth
- Confidence intervals provide uncertainty estimation

---

## 📈 Model Performance

- MAE: 5665.18  
- RMSE: 7260.16  
- MAPE: ~13%

---

## 💡 Business Insights

- Sales show a consistent upward trend over time
- Strong seasonal patterns observed in monthly demand
- Peak months indicate higher customer activity
- Forecast helps optimize inventory and staffing

---

## 📊 Dashboard Features

- Sales Forecast vs Actual
- KPI Cards (Total Sales, Avg Sales)
- Filters (Region, Category)
- Trend Analysis

---

## 🚀 How to Run

```bash
cd code
python prophet_model.py
python evaluation.py