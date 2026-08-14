import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re


# TASK 2: DATA PREPROCESSING
print("Starting Data Preprocessing...")

# 1. Load the raw data
df = pd.read_csv('raw_books.csv')

# 2. Clean up extra spaces and inconsistent text
df['title'] = df['title'].str.strip()
df['category'] = df['category'].str.strip()

# 3. Remove duplicate books by UPC
df.drop_duplicates(subset=['upc'], inplace=True)

# 4. Handle missing descriptions
df['description'] = df['description'].fillna('No description available')

# 5. Convert price to a numeric value (extracting just the numbers/decimals)
df['price'] = df['price'].astype(str).str.extract(r'(\d+\.\d+)').astype(float)

# 6. Map ratings One-Five to integers
rating_mapping = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['rating_num'] = df['rating'].map(rating_mapping)

# 7. Extract available stock count from the availability string
df['stock_count'] = df['availability'].astype(str).str.extract(r'(\d+)').astype(float)
df['stock_count'] = df['stock_count'].fillna(0) # If no number found, assume 0

# 8. Create at least three useful features
# Feature 1: description_word_count
df['description_word_count'] = df['description'].apply(lambda x: len(str(x).split()))

# Feature 2: price_band (categorizing books by price)
df['price_band'] = pd.cut(df['price'], bins=[0, 20, 40, 60, 100], labels=['Budget', 'Moderate', 'Expensive', 'Premium'])

# Feature 3: value_score (rating divided by price - higher is better value)
df['value_score'] = (df['rating_num'] / df['price']).round(3)

# Save the cleaned dataset
df.to_csv('cleaned_books.csv', index=False)
print("Data Preprocessing complete. Cleaned data saved to 'cleaned_books.csv'.")



# TASK 3: VISUALIZATION AND ANALYSIS
print("Generating Visualizations...")
sns.set_theme(style="whitegrid")

# Plot 1: Price Distribution (Histogram)
plt.figure(figsize=(8, 5))
sns.histplot(df['price'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Book Prices')
plt.xlabel('Price (£)')
plt.ylabel('Frequency')
plt.savefig('plot1_price_distribution.png')
plt.close()

# Plot 2: Rating Distribution (Bar Chart)
plt.figure(figsize=(8, 5))
sns.countplot(x='rating_num', data=df, palette='viridis')
plt.title('Distribution of Book Ratings')
plt.xlabel('Rating (1-5 Stars)')
plt.ylabel('Count')
plt.savefig('plot2_rating_distribution.png')
plt.close()

# Plot 3: Average Price by Category (Bar Chart)
# Taking top 10 categories with the most books to keep the chart readable
top_categories = df['category'].value_counts().nlargest(10).index
df_top_cats = df[df['category'].isin(top_categories)]

plt.figure(figsize=(10, 6))
sns.barplot(x='price', y='category', data=df_top_cats, errorbar=None, palette='mako')
plt.title('Average Price by Category (Top 10 Categories)')
plt.xlabel('Average Price (£)')
plt.ylabel('Category')
plt.savefig('plot3_avg_price_by_category.png')
plt.close()

# Plot 4: Relationship Plot (Price vs. Rating)
plt.figure(figsize=(8, 5))
sns.boxplot(x='rating_num', y='price', data=df, palette='coolwarm')
plt.title('Price Distribution Across Ratings')
plt.xlabel('Rating (1-5 Stars)')
plt.ylabel('Price (£)')
plt.savefig('plot4_price_vs_rating.png')
plt.close()

# Plot 5: Word Cloud from combined descriptions
text = " ".join(desc for desc in df['description'] if desc != 'No description available')
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Book Descriptions')
plt.savefig('plot5_wordcloud.png')
plt.close()

print("Visualizations saved as PNG files in your folder!")

# Generate Summary Statistics for Task 4
print("\n--- Summary Statistics for Task 4 Insights ---")
print(df[['price', 'rating_num', 'stock_count', 'description_word_count', 'value_score']].describe())