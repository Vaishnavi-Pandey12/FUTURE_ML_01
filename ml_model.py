import pandas as pd
import matplotlib.pyplot as plt
import dataConversionToTimeSeries
from statsmodels.tsa.arima.model import ARIMA
import datacleaning, dataConversionToTimeSeries

df = datacleaning.df
monthly_sales = dataConversionToTimeSeries.monthly_sales

monthly_sales["Date"] = pd.to_datetime(monthly_sales["Date"])
monthly_sales = monthly_sales.set_index("Date")

monthly_sales["Sales"].plot(figsize=(10,5))
plt.title("Monthly Sales Trend")
plt.show()

train = monthly_sales.iloc[:-3]
test = monthly_sales.iloc[-3:]

model = ARIMA(train["Sales"], order=(1,1,1))
model_fit = model.fit()

forecast = model_fit.forecast(steps=len(test))

#Model Evaluation
plt.figure(figsize=(10,5))

plt.plot(train.index, train["Sales"], label="Train")
plt.plot(test.index, test["Sales"], label="Actual")
plt.plot(test.index, forecast, label="Predicted")

plt.legend()
plt.title("Sales Forecast vs Actual")
plt.show()

#Forecast Future Sales
future_forecast = model_fit.forecast(steps=6)
print(future_forecast)

plt.figure(figsize=(10,5))

plt.plot(monthly_sales.index, monthly_sales["Sales"], label="Historical Sales")
plt.plot(future_forecast.index, future_forecast, label="Future Forecast")

plt.legend()
plt.title("Future Sales Forecast")
plt.show()