# DS605: Fundamentals of Machine Learning

## Lab Assignment - 8: Decision Trees and Support Vector Machines

### Student Details

**Name:** Manush Doshi  
**Student ID:** 202618028  

### Dataset
**Dataset:** UCI Banknote Authentication  
**Source:** Local Archive (`data_banknote_authentication.txt`)

The dataset contains 1,372 samples with 4 continuous features (`variance`, `skewness`, `kurtosis`, `entropy`) used to classify banknotes into 2 distinct classes (authentic or forged).

## Objective

The objective of this assignment was to implement Decision Tree and Linear Support Vector Machine (SVM) classifiers completely from scratch using fundamental NumPy operations. The assignment explores 2D decision boundary visualizations, hyperparameter tuning, and the "Kernel Trick" on non-linear data, culminating in a full 4-feature performance comparison against highly optimized Scikit-learn baseline models.

## Preprocessing & Representation Choices

### Feature Selection & Label Mapping
- **2D Visualizations (Parts A & B):** Only the first two features (`variance` and `skewness`) were used to allow for clear 2D scatter plots and decision boundary contour mapping.
- **Full Evaluation (Part D):** All 4 features were utilized to test the models' true predictive capabilities.
- **SVM Label Mapping:** For the manual SVM, binary class labels (0 and 1) were explicitly mapped to -1 and +1 to properly compute the hinge loss.

### Data Scaling
- **Decision Trees:** Raw features were passed directly, as tree-based models rely on relative threshold splits and are scale-invariant.
- **SVMs:** A manual `StandardScalerScratch` class was implemented to standardize features (mean = 0, variance = 1). Scaling was strictly applied to SVM inputs to ensure unbiased distance and margin calculations.

### Train-Test Split
The data was partitioned using a 70-30 split (`test_size=0.3`) with `random_state=42` to ensure a consistent evaluation baseline across all manual and Scikit-learn models.

## Implementation Details

### Part A: Decision Tree (From Scratch)
- **Recursive Splitting:** Implemented a `Node` class and a recursive tree-growing algorithm based on Information Gain.
- **Impurity Metrics:** The code supports dynamic switching between **Gini Impurity** and **Entropy** to evaluate the best feature-threshold splits.
- **Rules Extraction:** A custom tree-traversal function prints the learned `if-else` split rules in a readable, nested format.

### Part B: Linear SVM (From Scratch)
- **Subgradient Descent:** The Linear SVM was built using a soft-margin hinge-loss objective, optimized via subgradient descent. 
- **Margin Violators:** The custom plotting function actively highlights margin-violating samples where $y \cdot (w \cdot x - b) < 1$.
- **Hyperparameter Exploration:** A systematic loop tested various configurations of Regularization ($C$), Learning Rate, and Iterations. 

### Part C: Kernel SVM and Nonlinear Boundaries
- **Synthetic Data:** A complex, non-linear dataset was generated using `make_moons` (noise=0.15).
- **The Kernel Trick:** Sklearn SVMs with Linear, Polynomial (degree=3), and RBF kernels were trained. Visualizations demonstrated how linear hyperplanes fail on curved data, whereas Polynomial and RBF kernels map the data into higher dimensions to achieve perfect separability.

## Models Compared (Part D)

Using the full 4-feature dataset, the following models were trained and benchmarked for Accuracy, Precision, Recall, F1-Score, and Execution Time:

1. Manual Decision Tree (Depth=5)
2. Scikit-Learn DecisionTreeClassifier (Depth=5)
3. Manual Linear SVM 
4. Scikit-Learn Linear SVC
5. Scikit-Learn RBF SVC

## Final Observations and Performance Analysis

- **Hyperparameter Trade-offs (SVM):** Exploring the $C$ parameter in the manual SVM proved that a low $C$ (e.g., 0.01) creates a wider margin but heavily underfits the data (causing numerous violations). A high $C$ (e.g., 100) creates a strict boundary, achieving higher accuracy but risking overfitting to outliers.
- **Execution Time & Optimization:** The manual implementations (using Python `for` loops) were noticeably slower during training compared to Scikit-learn. Sklearn utilizes optimized C/Cython backends (like `libsvm`), making it significantly more efficient for large-scale subgradient descent.
- **Interpretability vs. Complexity:** The manual Decision Tree provided excellent transparency—the printed split rules make it easy to explain exactly *why* a classification was made. Conversely, the SVMs (particularly RBF) acted as black-box models, trading interpretability for boundary flexibility.
- **Best Overall Model:** On the complete 4-feature dataset, the **Scikit-Learn RBF SVM** captured the complex underlying data patterns best, yielding the highest overall performance metrics across the board.

## Conclusion

This assignment successfully deconstructed two fundamental machine learning algorithms. Building them from scratch highlighted the core mathematical differences between the algorithms: Decision Trees perform axis-parallel, scale-invariant splits based on entropy, while SVMs rely heavily on scaled distance metrics and vector geometry to maximize a separating margin. Furthermore, exploring non-linear kernels emphasized the necessity of the "Kernel Trick" when dealing with real-world, overlapping datasets.