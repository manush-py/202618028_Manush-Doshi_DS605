# DS605: Fundamentals of Machine Learning

## Lab Assignment - 3: Scikit-learn: Data Preprocessing and Model Performance Evaluation

### Student Details

**Name:** Manush Doshi  
**Student ID:** 202618028  

### Dataset
**Dataset:** Hotel Booking Demand (`hotel_bookings.csv`)
**Source:** Kaggle Hotel Booking Demand

The dataset contains hotel booking information for city and resort hotels, with `is_canceled` used as the target variable.


## Objective

The objective of this assignment was to build and compare two Scikit-learn preprocessing pipelines and evaluate Logistic Regression and Decision Tree classification models using the same train-test split.

## Preprocessing Choices

### Data Cleaning

- Missing values were checked using both count and percentage for every column.
- The `company` column was removed because it had very high missingness and was not considered useful enough to keep.
- `reservation_status` and `reservation_status_date` were removed because they can reveal the final booking outcome and may cause data leakage.
- Numerical features were inspected using boxplots and the IQR approach.
- Only clearly invalid/extreme values were removed rather than removing all statistical outliers blindly.

### Train-Test Split

The data was split using:

- `test_size=0.2`
- `stratify=y`
- `random_state=42`

The same split was used for all four experiments.

### Pipeline A

**Numerical features:**
- `KNNImputer(n_neighbors=5)`
- `StandardScaler`

**Categorical features:**
- `SimpleImputer(strategy="most_frequent")`
- `OneHotEncoder(handle_unknown="ignore")`

### Pipeline B

**Numerical features:**
- `KNNImputer(n_neighbors=5)`
- `MinMaxScaler`

**Categorical features:**
- `SimpleImputer(strategy="most_frequent")`
- `OneHotEncoder(handle_unknown="ignore")`

Both pipelines used `ColumnTransformer` and Scikit-learn `Pipeline` so that preprocessing was fitted only on the training data.

## Models Compared

Four model-pipeline combinations were evaluated:

1. Logistic Regression + Pipeline A
2. Logistic Regression + Pipeline B
3. Decision Tree + Pipeline A
4. Decision Tree + Pipeline B

Model settings:

- `LogisticRegression(max_iter=1000)`
- `DecisionTreeClassifier(random_state=42)`

## Final Observations

- The **Decision Tree with Pipeline B (MinMaxScaler)** gave the best overall result, with a testing accuracy of **86.10%** and an F1-score of **0.8128**.
- For **Logistic Regression**, StandardScaler performed slightly better than MinMaxScaler. The F1-score was **0.7298** with StandardScaler and **0.7181** with MinMaxScaler.
- Scaling did **not make a major difference for the Decision Tree**. Both scaling methods produced almost identical results, with F1-scores of **0.8126** and **0.8128**.
- The Decision Tree identified more canceled bookings correctly than Logistic Regression. The best Decision Tree correctly classified **7,204 canceled bookings**, compared with **5,899** for the best Logistic Regression.
- The Decision Tree showed a much larger train-test accuracy gap (**99.62% training vs 86.10% testing**), suggesting noticeable overfitting. Logistic Regression had much smaller gaps and therefore generalized better to unseen data.

## Conclusion

Overall, the **Decision Tree + Pipeline B** combination produced the strongest classification performance on the test set. However, its high training accuracy compared with testing accuracy indicates that the model is overfitting. Logistic Regression performed less strongly but showed a much smaller train-test gap, making it more stable in terms of generalization. The comparison also showed that the choice between StandardScaler and MinMaxScaler matters more for Logistic Regression than for the Decision Tree.