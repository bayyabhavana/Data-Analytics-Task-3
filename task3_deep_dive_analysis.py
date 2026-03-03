# =====================================================
# TASK 3 – Deep-Dive Analysis (Customer Segmentation)
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt

print("========== TASK 3 STARTED ==========\n")

# Load dataset
df = pd.read_csv("cleaned_sales_data.csv")

# KPI Calculations
total_revenue = df["Purchase_Amount"].sum()
total_customers = df["Customer_ID"].nunique()
avg_order_value = df["Purchase_Amount"].mean()

print("Total Revenue:", total_revenue)
print("Total Customers:", total_customers)
print("Average Order Value:", avg_order_value)

# Revenue by Age Group
age_group_revenue = df.groupby("Age_Group")["Purchase_Amount"].sum()

print("\nRevenue by Age Group:")
print(age_group_revenue)

# Plot segmentation chart
plt.figure()
age_group_revenue.plot(kind="bar")
plt.title("Revenue by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show()

print("\n========== TASK 3 COMPLETED ==========")