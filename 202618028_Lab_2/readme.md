# DS605: Fundamentals of Machine Learning

## Lab Assignment - 2: Vectorized Programming with NumPy and Data Wrangling with Pandas

### Student Details

**Name:** Manush Doshi  
**Student ID:** 202618028  

### Dataset

**Dataset:** Titanic Dataset (`train.csv`)  
**Source:** Kaggle Titanic Dataset  

### Objective
Practice vectorized NumPy operations and basic data wrangling with Pandas using the Titanic dataset.

### Project Details
This assignment focuses on using **NumPy** for vectorized programming and **Pandas** for data wrangling and analysis.

The first part covers NumPy operations such as array creation, statistical calculations, indexing, slicing, reshaping, vectorized arithmetic, matrix operations, normal distribution, and histogram visualization.

The second part uses the Titanic dataset to perform data loading and inspection, filtering, querying, grouping and aggregation, missing-value handling, outlier detection, feature creation, pivot tables, correlation analysis, and visualizations.

The main objective is to understand how NumPy and Pandas can be used efficiently for data manipulation and basic exploratory data analysis.

### Tasks Covered

* NumPy arrays, statistics, and indexing
* Vectorized arithmetic and linear algebra
* Normal distribution and histogram
* Titanic dataset loading and inspection
* Boolean filtering and querying
* `groupby()` and aggregation
* Missing-value analysis and imputation
* Fare outlier detection using IQR
* Feature engineering with `FamilySize` and `IsAlone`
* Pivot table analysis
* Correlation heatmap and visualizations

### Key Observations

1) Female passengers had a much better chance of surviving compared with male passengers.
2) Passengers travelling in 1st class generally had higher survival rates than those in 2nd and 3rd class.
3) Fare was strongly influenced by passenger class, with higher-class passengers usually paying more.
4) Age and Fare did not appear to have a very strong direct relationship in the analysis.
5) The Age, Cabin, and Embarked columns contained missing values, with Cabin having the largest number of missing entries.
6) A few very high Fare values stood out as outliers when using the IQR method.
7) Looking at FamilySize and IsAlone gave some additional insight into how travelling with family may relate to survival.


### Conclusion

This assignment helped me understand how NumPy can be used for fast numerical calculations and how Pandas makes it easier to clean, organize, and analyze real-world data. Working with the Titanic dataset also showed that simple grouping, filtering, and visualizations can reveal useful patterns, especially when comparing survival across gender and passenger class. Overall, the analysis gave me practical experience with basic data wrangling and exploratory data analysis using Python.
