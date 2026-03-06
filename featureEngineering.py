import datacleaning
#import DatasetAnalysis

df = datacleaning.df

df["Sales"] = df["Quantity"] * df["UnitPrice"]

df["Month"] = df["InvoiceDate"].dt.month
df["Year"] = df["InvoiceDate"].dt.year
df["DayOfWeek"] = df["InvoiceDate"].dt.day_name()
df["Quarter"] = df["InvoiceDate"].dt.quarter

monthly_sales = df.groupby(["Year","Month"])["Sales"].sum().reset_index()
monthly_avg_sales = monthly_sales.groupby("Month")["Sales"].mean().reset_index()


df["Holiday"] = df["Month"].apply(lambda x: 1 if x == 12 else 0)

def get_season(month):
    if month in [12,1,2]:
        return "Winter"
    elif month in [3,4,5]:
        return "Spring"
    elif month in [6,7,8]:
        return "Summer"
    else:
        return "Autumn"

df["Season"] = df["Month"].apply(get_season)

print(df.head())