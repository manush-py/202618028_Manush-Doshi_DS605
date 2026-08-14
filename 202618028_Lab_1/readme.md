# DS605 - Fundamentals of Machine Learning

## Lab Assignment 1: Data Scraping and Preprocessing using Python and Scrapy

**Name:** Manush Doshi  
**Student ID:** 202618028

---

## Objective

The goal of this assignment is to build a complete data pipeline by scraping book information from the "Books to Scrape" sandbox website using Scrapy. After collecting the data, the objective is to clean it up, explore it visually, and pull out some interesting data-driven insights.

---

## Tools and Libraries Used

- Python
- Scrapy
- Pandas
- Matplotlib
- Seaborn
- WordCloud

---

## Project Structure

```text
202618028_Lab_1/
├── bookscraper/                 # Scrapy framework folder
│   ├── spiders/
│   │   └── bookspider.py        # The actual spider script
│   └── (other scrapy framework files like settings.py)
├── analyze_books.py             # Script for preprocessing and visualization
├── raw_books.csv                # Uncleaned dataset (100 books)
├── cleaned_books.csv            # Cleaned dataset with new features
├── Task4_Insights.txt           # Detailed breakdown of Task 4 observations
├── plot1_price_distribution.png # Histogram of prices
├── plot2_rating_distribution.png# Bar chart of star ratings
├── plot3_avg_price_by_category.png # Average price per genre
├── plot4_price_vs_rating.png    # Boxplot of price across ratings
├── plot5_wordcloud.png          # Word cloud of book descriptions
└── README.md
```

## Observations
https://github.com/manush-py/202618028_Manush-Doshi_DS605/blob/main/202618028_Lab_1/task_4.txt


## Conclusion
To sum it up, this assignment proved that the full data pipeline—from web scraping to data cleaning and visualization—is working exactly as intended. While the charts and insights are interesting to look at, the data comes from a sandbox site using placeholder text, so we can't draw any real-world publishing conclusions from it (especially with only 100 books and no real reviews). The main goal was to build the technical infrastructure to extract and analyze the data, and this project successfully does just that.