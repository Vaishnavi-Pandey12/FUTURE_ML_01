import pandas as pd
import matplotlib.pyplot as plt
#import dataConversionToTimeSeries
import ml_model
from statsmodels.tsa.arima.model import ARIMA

future_forecast = ml_model.future_forecast

future_df = future_forecast.reset_index()
future_df.columns = ["Date","Sales"]

monthly_sales = ml_model.monthly_sales
historical_df = monthly_sales.reset_index()

historical_df["Type"] = "Actual"
future_df["Type"] = "Forecast"

final_df = pd.concat([historical_df, future_df])

final_df.to_csv("sales_forecast_dataset.csv", index=False)