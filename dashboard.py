import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [1200, 1500, 1800, 1700, 2100]
}

df = pd.DataFrame(data)

plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
