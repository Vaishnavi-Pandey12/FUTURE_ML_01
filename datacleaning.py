#Importing necessary libraries

import pandas as pd
import numpy as np

#Loading the dataset
df = pd.read_excel("OnlineRetail.xlsx", sheet_name="Online Retail")

#checking the structure of the dataset

#print(df.head())
#print(df.info())
#print(df.describe())

#Data Cleaning
df = df.drop_duplicates()

print(df.isnull().sum())

print(df["InvoiceDate"].dtype)

df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]
df["Sales"] = df["Quantity"] * df["UnitPrice"]

df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["Day"] = df["InvoiceDate"].dt.day
df["DayOfWeek"] = df["InvoiceDate"].dt.day_name()

#Grouping the data by month and calculating total sales for each month
monthly_sales = df.groupby(pd.Grouper(key="InvoiceDate", freq="ME"))["Sales"].sum()

monthly_sales = monthly_sales.reset_index()

monthly_sales = monthly_sales.sort_values("InvoiceDate")

#Displaying the monthly sales
print(monthly_sales.head())

