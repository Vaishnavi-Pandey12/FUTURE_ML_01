import datacleaning
import matplotlib.pyplot as plt

df = datacleaning.df

#1. Monthly Sales Analysis
plt.plot(df["InvoiceDate"], df["Sales"])
plt.title("Top Selling Products")
plt.xlabel("Sales")
plt.ylabel("Product Name")
plt.show()

#2. Top Selling Products
sales = df.groupby("Description")["Sales"].sum().sort_values(ascending=False).head(10)
sales.plot(kind="bar")
plt.title("Top Selling Products")
plt.xlabel("Sales")
plt.ylabel("Product Name")
plt.show()

#3. Sales by Country
country_sales = df.groupby("Country")["Sales"].sum().sort_values(ascending=False).head(10)
country_sales.plot(kind="bar")
plt.title("Sales by Country")
plt.xlabel("Sales")
plt.ylabel("Country")
plt.show()

#4. Sales by Day of the Week
day_sales = df.groupby("DayOfWeek")["Sales"].sum().reindex(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
day_sales.plot(kind="bar")
plt.title("Sales by Day of the Week")
plt.xlabel("Sales")
plt.ylabel("Day of the Week")
plt.show()
