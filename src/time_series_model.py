from statsmodels.tsa.statespace.sarimax import SARIMAX

def run_sarima_forecast(monthly_series):
    """Fits SARIMA model and returns the next month's prediction."""
    
    # Fixed parameters (p=1, d=1, q=0, S=12) for reliable demo.
    order = (1, 1, 0)
    seasonal_order = (1, 1, 0, 12)
    
    try:
        model = SARIMAX(
            monthly_series,
            order=order,
            seasonal_order=seasonal_order,
            enforce_stationarity=False,
            enforce_invertibility=False
        )
        results = model.fit(disp=False)
        
        forecast_steps = 1
        forecast = results.get_prediction(start=len(monthly_series), end=len(monthly_series) + forecast_steps - 1)
        
        pred_mean = forecast.predicted_mean.iloc[0]
        pred_ci = forecast.conf_int().iloc[0]
        
        return pred_mean, pred_ci
    except Exception as e:
        # Fallback: Use last month's spending + 5% if SARIMA fails.
        print(f"SARIMA failed: {e}. Using simple fallback prediction.")
        fallback_pred = monthly_series.iloc[-1] * 1.05 if not monthly_series.empty else 0
        return fallback_pred, None