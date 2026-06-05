Customer Shopping Behavior Analysis

> End-to-end analysis of customer shopping trends — SQL, Python, and Excel focused on purchase behaviour, seasonal patterns, and customer segmentation.

---

## Project Overview
This project analyses customer shopping behaviour using a dataset of 3,900 transactions across 4 product categories. The focus was on understanding **what drives purchase decisions** — category, season, discounts, age, and gender.

The pipeline covers data cleaning and aggregations in PostgreSQL, exploratory data analysis and visualisations in Python/pandas, and a business-ready report in Excel with pivot tables and conditional formatting.

---

## Tech Stack
| Tool | Purpose |
|------|---------|
| PostgreSQL | Data cleaning, aggregations, window functions |
| Python (pandas, matplotlib, seaborn) | EDA, statistical analysis, visualisations |
| Excel | Pivot tables, charts, conditional formatting — business report |

---

## Dataset
- **Source:** Customer Shopping Trends Dataset (Kaggle)
- **Size:** 3,900 rows, 18 columns
- **Key columns:** Age, Gender, Item Purchased, Category, Purchase Amount (USD), Location, Season, Review Rating, Shipping Type, Discount Applied, Previous Purchases, Frequency of Purchases

---

## Project Structure
```
customer-shopping-analysis/
│
├── data/
│   └── shopping_trends.csv           # Original raw dataset
│   
│
├── sql/
│   ├── avg_of_revenue_for_categories.sql
│   ├── avg_receipt_by_seasons.sql
│   ├── avg_receipt_with_and_without_discount.sql
│   ├── avg_review_rating_by_category_and_gender.sql
│   ├── pct_of_total_for_categories.sql
│   ├── rank_of_product_in_the_category_by_avg.sql
│   ├── sales_for_age_groups.sql
│   ├── top10_items_by_total_sales.sql
│   └── top10_states_by_total_revenue.sql
│
├── python_func/
│   └── shopping_trends.py
│
├── python_visual/
│   ├── average_purchase_amount_by_discount_and_season.png
│   ├── average_review_rating_by_shipping_type.png
│   ├── correlation_heatmap.png
│   ├── distribution_of_purchase_amount_by_category.png
│   └── number_of_sales_by_age_group.png
│
├── excel/
│   └── shopping_trends_excel.xlsx
│
└── README.md
```

---

## Data Cleaning (SQL + Python)
- Checked for NULL values across all columns — none found
- Checked for duplicates — none found
- Created `Age_Group` column: 18-25, 26-35, 36-50, 50+

---

## SQL Analysis
9 queries covering key business questions:

| File | Description |
|------|-------------|
| avg_of_revenue_for_categories | Average purchase amount per category |
| top10_items_by_total_sales | Top 10 most purchased items |
| avg_receipt_by_seasons | Average spend per season |
| avg_receipt_with_and_without_discount | Impact of discount on purchase amount |
| top10_states_by_total_revenue | Top 10 states by total revenue |
| rank_of_product_in_the_category_by_avg | Window function: product ranking by avg price within category |
| pct_of_total_for_categories | Window function: % share of each category in total sales |
| avg_review_rating_by_category_and_gender | Average rating by category and gender |
| sales_for_age_groups | Purchase frequency by age group |

---

## Python Analysis
Python was used for statistical analysis and visualisations that go beyond SQL:

**Statistical Analysis:**
- Correlation between Age, Purchase Amount, Review Rating, Previous Purchases
- Comparison of average spend with vs without discount
- Groupby aggregations by category, season, shipping type

**Visualisations:**
| File | Description |
|------|-------------|
| distribution_of_purchase_amount_by_category | Boxplot — price spread per category |
| correlation_heatmap | Heatmap — correlation between numeric columns |
| average_purchase_amount_by_discount_and_season | Bar chart — discount impact by season |
| average_review_rating_by_shipping_type | Bar chart — rating by shipping type |
| number_of_sales_by_age_group | Bar chart — sales volume by age group |

---

## Excel Business Report
Excel file contains a business-ready report for non-technical stakeholders:

- **Pivot Table 1** — Total revenue by category and season
- **Pivot Table 2** — Average spend by gender and age group
- **Chart** — Top items by number of sales
- **Conditional Formatting** — Review Rating highlighted by performance (green = high, red = low)
- **Summary Sheet** — Key metrics: total revenue, average order value, top category, top season

---

## Key Findings

### 🛒 Purchase Amount
Average purchase amount is consistent across categories (~$57–62), suggesting price is not a strong differentiator between categories.

### 🏷️ Discount Impact
Discounts have minimal impact on average purchase amount — customers spend similarly with and without discounts, suggesting discounts don't drive higher spending.

### 📅 Seasonality
Purchase volume is relatively stable across seasons with slight peaks in Spring and Winter — no strong seasonal pattern unlike typical retail.

### 👥 Customer Segments
- **Adults (36–50)** are the most active buyers
- Gender split is nearly equal with minimal difference in average spend
- Customers with more previous purchases do not consistently spend more — loyalty doesn't strongly predict order value

### 🚚 Shipping & Ratings
Review ratings vary slightly by shipping type — understanding which shipping methods correlate with higher satisfaction is actionable for operations teams.

---
