import pandas as pd
import numpy as np

# Note: Adjust the filename if your CSV name is different!
FILE_PATH = 'data/Personal_Finance_Dataset.csv' 

def load_and_preprocess_data():
# -----------------------------------------------------
# EVERYTHING BELOW MUST BE INDENTED (TABBED) BY ONE LEVEL
# -----------------------------------------------------
    """Loads, cleans, creates essential features, and aggregates data."""
    try:
        df = pd.read_csv(FILE_PATH)
    except FileNotFoundError:
        print(f"Error: {FILE_PATH} not found. Please ensure the CSV is in the 'data/' folder.")
        # Returning None, None, etc. matches the number of variables expected
        return None, None, None, None, None 

    # 1. Cleaning and Polarity
    df['Date'] = pd.to_datetime(df['Date'])
    df['Type'] = df['Type'].str.strip().str.capitalize()
    
    # Expense as negative, Income as positive.
    df['Signed_Amount'] = np.where(df['Type'] == 'Expense', -df['Amount'].abs(), df['Amount'].abs())
    
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    df = df.sort_values('Date').reset_index(drop=True)

    # 2. Feature Engineering
    df['DayName'] = df['Date'].dt.day_name()
    df['Running_Balance'] = df['Signed_Amount'].cumsum()
    
    # 3. Aggregated Data for TS and Recommender
    expense_df = df[df['Type'] == 'Expense'].copy()
    expense_df['Amount'] = expense_df['Amount'].abs()
    
    # Monthly Aggregation for Time Series 
    monthly_df = expense_df.set_index('Date')['Amount'].resample('M').sum().reset_index()
    monthly_df.columns = ['Date', 'Monthly_Expense']
    
    # Category Averages for Recommender
    category_monthly_avg = expense_df.groupby([expense_df['Date'].dt.to_period('M'), 'Category'])['Amount'].sum().reset_index()
    avg_category_spending = category_monthly_avg.groupby('Category')['Amount'].mean().sort_values(ascending=False)
    
    avg_monthly_expense = monthly_df['Monthly_Expense'].mean()

    # The final line that was causing the error:
    return df, monthly_df, expense_df, avg_category_spending, avg_monthly_expense
