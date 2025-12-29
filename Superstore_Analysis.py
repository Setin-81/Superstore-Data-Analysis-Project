# -------------------------------
# Author: Razieh Yazdanian
# Project: Superstore Sales Data Analysis
# -------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Load Dataset
# -------------------------------
url = "https://gist.githubusercontent.com/nnbphuong/38db511db14542f3ba9ef16e69d3814c/raw/Superstore.csv"
df = pd.read_csv(url)

# Strip column names
df.columns = df.columns.str.strip()

# Preview
print(df.head())
print(df.info())

# -------------------------------
# Inspect Missing & Duplicates
# -------------------------------
print("Missing values:\n", df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# -------------------------------
# Data Cleaning
# -------------------------------
df = df.drop_duplicates()
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# -------------------------------
# Feature Engineering
# -------------------------------
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month

# -------------------------------
# Basic EDA
# -------------------------------
print("Total Sales:", df['Sales'].sum())
print("Total Profit:", df['Profit'].sum())
print("Average Discount:", df['Discount'].mean())

# -------------------------------
# Visualization
# -------------------------------
sns.set(style="whitegrid")

# 1) Sales Trend Over Years
plt.figure(figsize=(10,5))
sales_year = df.groupby('Year')['Sales'].sum()
sns.lineplot(x=sales_year.index, y=sales_year.values, marker='o')
plt.title("Sales Trend Over Years")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.show()

# 2) Sales by Region
plt.figure(figsize=(8,5))
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
sns.barplot(x=region_sales.index, y=region_sales.values, palette='viridis')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.show()

# 3) Profit vs Discount
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='Discount', y='Profit', size='Sales', hue='Category', alpha=0.7)
plt.title("Profit vs Discount (Bubble Size = Sales)")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.show()

# 4) Category & Sub-Category Sales
category_sales = df.groupby(['Category','Sub-Category'])['Sales'].sum().unstack()
category_sales.plot(kind='bar', stacked=True, figsize=(10,6), colormap='viridis', title="Sales by Category and Sub-Category")
plt.ylabel("Sales")
plt.show()

# -------------------------------
# Save Cleaned Dataset
# -------------------------------
df.to_csv("Superstore_Cleaned.csv", index=False)
print("Cleaned dataset saved as Superstore_Cleaned.csv")
