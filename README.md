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