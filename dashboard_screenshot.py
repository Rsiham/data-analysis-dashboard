import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [1200, 1500, 1800, 1700, 2100],
    "Customers": [80, 95, 110, 105, 130]
}

df = pd.DataFrame(data)

total_sales = df["Sales"].sum()
average_sales = df["Sales"].mean()
average_customers = df["Customers"].mean()

plt.figure(figsize=(10, 6))

plt.text(0.05, 0.9, "Data Analysis Dashboard", fontsize=22, weight="bold")
plt.text(0.05, 0.75, f"Total Sales: {total_sales}", fontsize=14)
plt.text(0.05, 0.65, f"Average Sales: {average_sales:.0f}", fontsize=14)
plt.text(0.05, 0.55, f"Average Customers: {average_customers:.0f}", fontsize=14)

plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("dashboard_mockup.png")
plt.show()
