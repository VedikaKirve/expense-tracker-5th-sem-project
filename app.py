import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- 1. Import Modular Logic ---
from src.data_processor import load_and_preprocess_data
from src.time_series_model import run_sarima_forecast
from src.recommender import generate_recommendations


def display_dashboard(df, monthly_df, expense_df, avg_category_spending, avg_monthly_expense):
    st.title("💸 Personalized Expense Tracker & Insight System")
    st.subheader("5th Semester Project")
    st.markdown("---")

# --- 1. Prepare Current Period Metrics ---
    current_date = df['Date'].iloc[-1]
    last_month_end = current_date - pd.offsets.MonthBegin(1)

    current_month_df = expense_df[
    (expense_df['Date'].dt.year == last_month_end.year) & 
    (expense_df['Date'].dt.month == last_month_end.month)
]

# --- 2. Run Models and Recommender ---
    monthly_series = monthly_df.set_index('Date')['Monthly_Expense']
    pred_mean, pred_ci = run_sarima_forecast(monthly_series)

    alerts, recommendations = generate_recommendations(
    current_month_df, 
    avg_category_spending, 
    avg_monthly_expense, 
    pred_mean
)

# --- Display Layout ---

    col1, col2 = st.columns(2)
    with col1:
        st.header("✨ Key Insights & Alerts")
    if alerts:
        for alert in alerts:
            st.markdown(alert)
    else:
        st.success("Your spending is on track! Keep up the good work.")
        
    st.markdown("---")
    if recommendations:
        st.subheader("Actionable Savings Tips")
        for rec in recommendations:
            st.markdown(rec)

    with col2:
        st.header("📈 Next Month's Forecast")
        st.metric(
        label=f"Predicted Total Expense (for {current_date.strftime('%b %Y')})",
        value=f"${pred_mean:,.0f}",
        delta=f"Avg: ${avg_monthly_expense:,.0f}",
        delta_color="off"
    )
    if pred_ci is not None:
         st.markdown(f"**95% CI:** $\\${pred_ci[0]:,.0f}$ to $\\${pred_ci[1]:,.0f}$")
    
    total_income = df[df['Type'] == 'Income']['Signed_Amount'].sum()
    total_expense = np.abs(df[df['Type'] == 'Expense']['Signed_Amount'].sum())
    net_savings = total_income + total_expense
    st.markdown(f"**Historical Net Flow:** $\\${net_savings:,.0f}$ (Income: $\\${total_income:,.0f}$ | Expense: $\\${total_expense:,.0f}$)")


# Row 2: EDA Visualizations
    st.markdown("---")
    st.header("📊 Spending Patterns & Trends")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Category Breakdown")
        fig, ax = plt.subplots(figsize=(6, 6))
        category_spending = expense_df.groupby('Category')['Amount'].sum().sort_values(ascending=False).head(8)
        ax.pie(category_spending.values, labels=category_spending.index, autopct='%1.1f%%', startangle=140)
        ax.axis('equal')
        st.pyplot(fig)

    with col4:
        st.subheader("Monthly Spending Trend")
        fig, ax = plt.subplots(figsize=(8, 4))
        monthly_series.plot(ax=ax, color='darkgreen', label='Historical Expense')
    
    forecast_date = monthly_series.index[-1] + pd.DateOffset(months=1)
    ax.scatter(forecast_date, pred_mean, color='red', marker='X', s=200, label='Predicted Expense')
    ax.plot(pd.to_datetime([monthly_series.index[-1], forecast_date]), [monthly_series.iloc[-1], pred_mean], 'r--')
    
    ax.set_title('Total Monthly Expenses & Forecast')
    ax.set_xlabel('Date')
    ax.set_ylabel('Amount ($)')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)
    st.pyplot(fig)


    # --- Execute App (The Correct Runner) ---
if __name__ == "__main__":
    # 1. Configuration (MUST be the first Streamlit command)
    st.set_page_config(layout="wide", page_title="5th Sem Expense Tracker")

    # 2. Load the data and all processed variables
    df_data = load_and_preprocess_data()
    
    # 3. Check if data loading was successful
    # df_data[0] is df, and we check if it's not None
    if df_data is not None and df_data[0] is not None:
        # 3. Launch the dashboard, unpacking the returned tuple of variables
        display_dashboard(*df_data)
    else:
        # Display an error message if the file was not found (for debugging)
        st.error("Application failed to load: Ensure 'Personal_Finance_Dataset.csv' is in the 'data/' folder.")
