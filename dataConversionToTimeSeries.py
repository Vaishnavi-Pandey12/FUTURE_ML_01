import datacleaning

df = datacleaning.df

df = df.set_index("InvoiceDate")
monthly_sales = df["Sales"].resample("ME").sum()
monthly_sales = monthly_sales.reset_index()
monthly_sales.rename(columns={"InvoiceDate":"Date"}, inplace=True)

monthly_sales = monthly_sales.sort_values("Date")

print(monthly_sales.head())
print(monthly_sales.shape)