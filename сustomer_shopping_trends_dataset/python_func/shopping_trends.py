import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('C:/python_projects/shopping_trends.csv')

# nulls = df.isnull().sum()
# print (nulls)

# df = df.drop_duplicates()
# df.to_csv('C:/python_projects/shopping_trends_clear.csv', index=False)

df['Age_Group'] = df['Age'].apply(lambda x: 
    '18-25' if x <= 25 else
    '26-35' if x <= 35 else
    '36-50' if x <= 50 else
    '50+'
)

count_of_sales_by_age_group = df.groupby('Age_Group').size() #Bar chart - quantity of sales by age group
print(count_of_sales_by_age_group, '\n')
plt.bar(count_of_sales_by_age_group.index, count_of_sales_by_age_group.values)
plt.xlabel('Age Group')
plt.ylabel('Number of Sales')
plt.title('Number of Sales by Age Group')
plt.show()


corr = df[['Age', 'Purchase Amount (USD)', 'Review Rating', 'Previous Purchases']].corr() #Heatmap  - correlation between age, purchase amount, review rating and previous purchases
print(corr, '\n')
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

discount_avg = df.groupby(['Discount Applied', 'Season'])['Purchase Amount (USD)'].mean().reset_index() #Bar chart - average purchase amount by discount and season
print(discount_avg, '\n')
discount_avg['label'] = discount_avg['Discount Applied'] + ' / ' + discount_avg['Season']
plt.figure(figsize=(12, 6))
plt.bar(discount_avg['label'], discount_avg['Purchase Amount (USD)'])
plt.xlabel('Discount / Season')
plt.ylabel('Average Purchase Amount (USD)')
plt.title('Average Purchase Amount by Discount and Season')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

mean_of_receipt_by_category = df.groupby('Category')['Purchase Amount (USD)'].mean() #Boxplot - distribution of purchase amount by category
print(mean_of_receipt_by_category, '\n')
plt.boxplot([df[df['Category'] == category]['Purchase Amount (USD)'] for category in df['Category'].unique()], labels=df['Category'].unique())
plt.xlabel('Category')
plt.ylabel('Purchase Amount (USD)')
plt.title('Distribution of Purchase Amount by Category')
plt.show()

mean_review_rating_by_shipping_method = df.groupby('Shipping Type')['Review Rating'].mean() #Line chart - average review rating by shipping type
print(mean_review_rating_by_shipping_method, '\n')
plt.plot(mean_review_rating_by_shipping_method.index, mean_review_rating_by_shipping_method.values, marker='o')
plt.xlabel('Shipping Type')
plt.ylabel('Average Review Rating')
plt.title('Average Review Rating by Shipping Type')
plt.xticks(rotation=45)
plt.show()



