DS605: Fundamentals of Machine Learning

## Lab Assignment - 6: Feature Extraction and Machine Learning with Image and Text Data

### Student Details

**Name:** Manush Doshi

**Student ID:** 202618028

### Datasets

1. **Image Dataset:** Asphalt Crack Dataset

   * **Source:** Mendeley Data

   * **Description:** A collection of 400 images containing 'Cracks' and 'NonCracks' to evaluate image processing and feature extraction for infrastructure defect detection.

2. **Text Dataset:** Email Spam Classification Dataset

   * **Source:** Kaggle

   * **Description:** A dataset of 5,172 emails labeled as spam or non-spam, containing pre-vectorized word counts that were reconstructed for raw text processing.

## Objective

The objective of this assignment was to manually convert raw image and text data into numerical feature representations without using Deep Learning/CNNs. It involved engineering features using NumPy and OpenCV for images, and Scikit-learn vectorizers for text. The assignment required evaluating traditional machine-learning models on these representations and making a justified improvement to optimize the trade-off between dimensionality, computation time, and accuracy.

## Preprocessing & Representation Choices

### Part A: Image Feature Extraction

* **Preprocessing:** Images were read using OpenCV, resized to a standard 128x128 dimension, and converted to grayscale.

* **Feature Engineering:** Five core numerical features were extracted per image using NumPy and OpenCV:

  1. Mean Brightness

  2. Contrast (Standard Deviation)

  3. Dark-Pixel Ratio (Threshold < 50)

  4. Bright-Pixel Ratio (Threshold > 200)

  5. Edge Density (Computed via OpenCV Canny edge detection with 100/200 thresholds).

* **Scaling:** Features were standardized using `StandardScaler` to ensure distance-based classifiers (like SVM) operated correctly.

### Part B: Text Vectorization

* **Text Reconstruction:** Raw text strings were reconstructed from the dataset's existing word-count columns using a highly optimized NumPy repetition strategy.

* **Vectorization Comparison:**

  * *Representation A:* Unigrams (single words) via `CountVectorizer`. (Generated 2,738 features).

  * *Representation B:* Unigrams + Bigrams via `CountVectorizer`. (Generated 54,983 features).

## Implementation Details

### Train-Test Split

Both image and text datasets were split using a standard `test_size=0.2`, utilizing `stratify=y` to maintain the original class distributions across the training and testing sets, and `random_state=42` for reproducibility.

### Models Compared

* **Image Classification (Part A):**

  * Random Forest Classifier (100 estimators)

  * Support Vector Machine (RBF Kernel)

* **Text Classification (Part B & C):**

  * Multinomial Naive Bayes (`MultinomialNB`)

## Observations and Results

### Image Classification Performance

* The **Support Vector Machine (RBF)** outperformed the Random Forest, achieving **96.25% Accuracy** and an F1-Score of **0.9630**.

* **Random Forest** achieved **95.00% Accuracy**. Based on the Random Forest's feature importances, *Bright_Pixel_Ratio* (0.2856) and *Mean_Brightness* (0.2507) were the most influential features, followed closely by *Dark_Pixel_Ratio* (0.2153) and *Edge_Density* (0.1539).

### Text Classification Performance

* Using **Unigrams** yielded an accuracy of **93.82%** with a highly efficient 2,738 features.

* Expanding to **Unigrams + Bigrams** increased accuracy slightly to **94.98%**, but drastically inflated the feature space to 54,983 features.

### Representation Improvement (Part C)

To address the massive dimensionality explosion caused by bigrams, a **Pruned Unigrams + Bigrams** approach was tested.

* **Strategy:** Implemented `min_df=3` (removing highly obscure words) and `max_features=3000` to limit the vocabulary strictly to the most impactful terms.

* **Result:** The feature space was successfully compressed from 54,983 down to a strict **3,000 features**.

* **Trade-off:** This 94.5% reduction in dimensionality only resulted in a minor drop in accuracy (from 94.98% to 93.33%). This represents a highly efficient trade-off, creating a vastly lighter and faster model with highly competitive predictive power.

## Conclusion

This assignment successfully demonstrated the foundations of classical machine learning pipelines. For image data, custom statistical and edge-based features proved robust enough to achieve >96% accuracy using SVMs, without needing complex neural networks. For NLP tasks, the text experiments highlighted the curse of dimensionality; while adding n-grams slightly improves context and accuracy, aggressive vocabulary pruning is a practical and necessary step to maintain computational efficiency while sacrificing minimal performance.