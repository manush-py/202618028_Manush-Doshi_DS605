# DS605: Fundamentals of Machine Learning

## Lab Assignment - 5: Machine Learning with Scikit-learn and From Scratch

### Student Details

**Name:** Manush Doshi  
**Student ID:** 202618028  

### Dataset
**Dataset:** UCI Productivity Prediction of Garment Employees (`garments_worker_productivity.csv`)  
**Source:** UCI Machine Learning Repository

The dataset contains garment employee production features, using `actual_productivity` as the regression target. A binary variable `MeetsTarget` was created for the classification target, assigning a 1 when actual productivity was greater than or equal to targeted productivity, and 0 otherwise. `actual_productivity` was not used as an input for the classification models.

## Objective

The objective of this assignment was to build regression and classification models using Scikit-learn, recreate the entire workflow manually using only NumPy and Pandas, and compare predictive performance and execution time. Furthermore, the manual implementations were optimized to close the performance and runtime gap with Scikit-learn.

## Preprocessing Choices

### Data Cleaning

- Inconsistent string formatting in the `department` column was removed using string stripping.
- The `date`, `actual_productivity`, and `MeetsTarget` columns were dropped from the feature matrix.

### Train-Test Split

The data was split using:

- `test_size=0.2`
- `random_state=42`

The exact same train-test split was used for both the Scikit-learn implementation and the manual from-scratch implementation to ensure a fair comparison.

### Scikit-learn Pipeline (Part A)

**Numerical features:**
- `SimpleImputer(strategy='median')`
- `StandardScaler()`

**Categorical features:**
- `SimpleImputer(strategy='most_frequent')`
- `OneHotEncoder(handle_unknown='ignore', sparse_output=False)`

Both pipelines were combined into a `ColumnTransformer` to fit only on the training data.

### Manual Implementation (Part B)

- **Missing Values:** Computed medians for numeric columns and modes for categorical columns on the training set, applying them to both train and test sets.
- **Scaling:** Standardized numeric features manually using training set means and standard deviations (with `ddof=0` to match Scikit-learn).
- **Encoding:** Used Pandas `get_dummies` and aligned columns to ensure identical features across train and test sets.
- **Bias Term:** Manually concatenated a column of 1s at index 0 for the model intercept. Scikit-learn utilities were entirely avoided in this section.

## Models Compared

Five model configurations were evaluated:

1. Linear Regression via Scikit-learn
2. Logistic Regression via Scikit-learn (`max_iter=1000`)
3. Manual Linear Regression (Closed-Form Solution via Pseudo-Inverse)
4. Manual Logistic Regression (Gradient Descent, `lr=0.1`, `epochs=1000`)
5. Optimized Manual Models (Ridge Regression and Early-Stopping Logistic Regression)

## Observations and Execution Differences

The manual implementations achieved better predictive scores for both regression and classification metrics on this specific dataset split, but execution speeds varied significantly based on the underlying mathematics and library optimizations.

- **Linear Regression Execution Profile:** The manual implementation calculates the exact analytical solution using the Normal Equation, $\theta=(X^TX)^{-1}X^Ty$. The manual matrix inversion via `np.linalg.pinv` executed faster (~0.002s) than Scikit-learn's object (~0.103s). This occurs because Scikit-learn wraps mathematical operations in extensive input validations, data-type checking, and formatting safety nets, which adds overhead for small datasets. By adding L2 regularization (Ridge) in the optimized step, the manual model better handled multicollinearity in the garment features while maintaining robust R2 scores.
- **Logistic Regression Execution Profile:** Scikit-learn's `LogisticRegression` solver utilizes highly optimized quasi-Newton methods (`lbfgs` by default) operating in backend C/C++ libraries. The initial Part B from-scratch model used an unoptimized Gradient Descent with a fixed learning rate and 1000 hard-coded iterations, resulting in a slower training time (~0.068s) compared to Scikit-learn (~0.020s).
- **The Optimization Strategy (Part C):** To close the runtime and performance gap, the code incorporates three enhancements into the classification algorithm:
  - **L2 Regularization:** A penalty factor was added to limit the weights and prevent overfitting.
  - **Increased Learning Rate:** The base algorithm was bumped to `lr=0.5`, allowing larger steps towards the minimum.
  - **Early Stopping:** Instead of completing unnecessary iterations, training halts automatically when the loss tolerance (1e-5) plateaus. This trims execution time, helping the manual model closely rival Scikit-learn's runtime while retaining competitive accuracy and F1-Scores.

## Final Observations

- The **Manual Linear Regression** yielded a slightly higher R2 score of **0.1736** compared to Scikit-learn's **0.1584**.
- The **Manual Linear Regression** trained much faster at **0.00206 seconds**, whereas the Scikit-learn model took **0.10347 seconds**.
- For classification, the **Manual Logistic Regression** achieved a higher F1-score (**0.8571**) and Accuracy (**0.7625**) than the Scikit-learn equivalent (F1-score: **0.8451**, Accuracy: **0.7542**).
- The **Scikit-learn Logistic Regression** was much faster to train, requiring only **0.02008 seconds** compared to the manual model's **0.06845 seconds**.
- To optimize the manual models in Part C, **L2 regularization** was introduced to improve robustness, and **early stopping** based on loss plateauing was added to the logistic regression to heavily reduce runtime.

## Conclusion

This project demonstrates that while mathematical formulas can be directly coded from scratch to achieve high predictive accuracy, optimized libraries like Scikit-learn are essential for rapid convergence in iterative algorithms. Building explicit optimizations like early stopping and regularization from scratch effectively bridges this gap, providing a deeper understanding of how production-grade machine learning libraries operate under the hood.
