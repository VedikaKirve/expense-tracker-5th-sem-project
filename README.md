# 💰 Personalized Expense Tracker & Financial Insight System

## 5th Semester Data Science Project

This project is an end-to-end data science application designed to analyze an individual's financial transactions over time, identify key spending patterns, predict future expenses, and deliver actionable, personalized saving recommendations.

The application is built with Python, showcasing a modular design (using the `src/` directory) and an interactive dashboard built with Streamlit.

---

### 🛠️ Key Data Science Skills Demonstrated

| Skill Area | Components Used | Project Deliverables |
| :--- | :--- | :--- |
| **Feature Engineering** | Python (`pandas`, `numpy`) | Creation of **`Signed_Amount`**, **`Running_Balance`**, and time-based features (`DayName`, `Month`). |
| **Exploratory Data Analysis (EDA)** | Python (`matplotlib`, `seaborn`) | Visualization of **Category-wise Breakdown** and **Monthly Spending Trends**. |
| **Time Series Forecasting** | Python (`statsmodels.SARIMA`) | Prediction of the user's **Next Month's Total Expense**. |
| **Recommendation System** | Rule-Based Logic | Generation of **Personalized Alerts** (for overspending) and **Saving Tips**. |
| **Deployment** | Python (`Streamlit`) | Interactive web dashboard for real-time visualization and insights. |

---

### Project Goal (The Why)
The singular goal of this project is to create a robust and demonstrable data science portfolio piece that provides quantifiable value to the user:

Goal: To convert passive financial data into active financial guidance, enabling the user to gain complete foresight and control over their budget. The system must deliver accurate predictions (e.g., next month's expense) and actionable, personalized advice (e.g., saving tips and overspending alerts) based on observed behavior.

### 💡 Key Financial Insights
-Budget Focus: Spending is heavily concentrated in a few categories (e.g., Rent, Travel). Budgeting efforts should target these high-impact areas first.
-Volatile Behavior: Spending shows high volatility and seasonality (spikes around holidays), justifying the use of the SARIMA model for reliable forecasting.
-Actionable Value: The system generates proactive alerts for anomalies (e.g., Rent Warning) and provides concrete saving tips (e.g., reducing Travel by 15% saves $\$X$), translating analysis into direct user action.
-Health Warning: High net expense indicates the system is vital for establishing financial discipline and stabilizing overall financial health.

### 🚀 How to Run Locally

1.  **Environment Setup:** Navigate to the project root and create and activate the virtual environment:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```
2.  **Data:** Ensure the Kaggle CSV (`Personal_Finance_Dataset.csv`) is placed inside the **`data/`** folder.
3.  **Launch Application:**
    ```bash
    python -m streamlit run app.py
    ```

---

### Author 
Vedika Kirve

Email: vedikakirve6@gmail.com 

LinkedIn: http://www.linkedin.com/in/vedikakirve06 

GitHub: https://github.com/VedikaKirve

Project Status: Complete and Deployed.
