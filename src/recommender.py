def generate_recommendations(current_month_df, avg_category_spending, avg_monthly_expense, predicted_expense):
    """Generates alerts and recommendations based on current spending vs. average."""
    alerts = []
    recommendations = []

    # Get Current Month's Spending
    current_month_total = current_month_df['Amount'].abs().sum()
    monthly_deviation_pct = (current_month_total - avg_monthly_expense) / avg_monthly_expense

    # R1: Monthly Budget Alert (10% Over Average)
    if monthly_deviation_pct > 0.10:
        alerts.append(
            f"🚨 **Monthly Alert:** You are trending **{monthly_deviation_pct * 100:.1f}%** over your average monthly expense. "
            f"Projected total: ${predicted_expense:,.2f}."
        )

    # R2: Category Overspending Alert (20% Over Category Average)
    for category, avg_spend in avg_category_spending.items():
        current_category_spend = current_month_df[current_month_df['Category'] == category]['Amount'].abs().sum()
        category_deviation_pct = (current_category_spend - avg_spend) / avg_spend
        if category_deviation_pct > 0.20 and current_category_spend > 50: 
            alerts.append(
                f"⚠️ **{category} Warning:** Spent ${current_category_spend:,.2f}, which is **{category_deviation_pct * 100:.0f}%** more than your typical ${avg_spend:,.2f}."
            )

    # R3: Saving Tip (Focus on Top 1 Non-Essential Category)
    non_essential = ['Entertainment', 'Food & Drink', 'Shopping', 'Travel']
    saving_focus = avg_category_spending[avg_category_spending.index.isin(non_essential)].head(1)
    
    if not saving_focus.empty:
        top_saving_cat = saving_focus.index[0]
        top_saving_amt = saving_focus.values[0]
        
        # Suggest a 15% reduction
        recommendations.append(
            f"💡 **Saving Tip:** By aiming for a 15% reduction in **{top_saving_cat}**, you can save an estimated **${top_saving_amt * 0.15:,.2f}** this month!"
        )

    return alerts, recommendations
