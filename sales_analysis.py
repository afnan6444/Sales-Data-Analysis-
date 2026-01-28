
# Sales Data Analysis Project

# Day 1: Setup & Load Data
import pandas as pd

# Load dataset
df = pd.read_csv('sales_data.csv')

# Day 2: Explore Data
print("Dataset Shape:", df.shape)          # Rows, Columns
print("Columns:", df.columns.tolist())     # Column names
print("Data Types:\n", df.dtypes)          # Data types

# Day 3: Clean Data
# Handle missing values
df = df.fillna(0)  # Replace NaN with 0 for numerical columns
# Remove duplicates
df = df.drop_duplicates()

# Day 4: Analyze Sales
# Metric 1: Total Revenue
total_revenue = df['Total_Sales'].sum()

# Metric 2: Best-Selling Product
best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()
best_product_sales = df.groupby('Product')['Total_Sales'].sum().max()

# Metric 3: Average Sales per Transaction
avg_sales = df['Total_Sales'].mean()

# Day 5: Create Report (print insights)
print("\n--- Sales Analysis Report ---")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Best-Selling Product: {best_product} (₹{best_product_sales:,.2f})")
print(f"Average Sales per Transaction: ₹{avg_sales:,.2f}")
