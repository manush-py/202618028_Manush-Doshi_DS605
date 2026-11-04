# DS605: Fundamentals of Machine Learning

**Student Name:** Manush Doshi  
**Student ID:** 202618028  

This repository serves as the central collection of coursework for DS605: Fundamentals of Machine Learning. It comprises eight comprehensive laboratory assignments that demonstrate the progressive application of data science pipelines, classical machine learning algorithms, and model deployment techniques.

## Tools and Technologies

Across the duration of this coursework, the following technologies and libraries were utilized:

* **Languages:** Python
* **Data Manipulation and Mathematics:** NumPy, Pandas
* **Machine Learning:** Scikit-learn
* **Computer Vision and Image Processing:** OpenCV
* **Data Collection:** Scrapy
* **Data Visualization:** Matplotlib, Seaborn
* **Deployment:** Streamlit

## Course Directory

### [Lab Assignment 1: Data Scraping and Preprocessing using Python and Scrapy](./202618028_Lab_1)

* **Dataset:** "Books to Scrape" Sandbox
* **Overview:** This assignment establishes a complete data pipeline originating from web scraping. Data was collected via a custom Scrapy spider, systematically cleaned, and visually analyzed using Matplotlib and Seaborn to extract empirical insights.

### [Lab Assignment 2: Vectorized Programming with NumPy and Data Wrangling with Pandas](./202618028_Lab_2)

* **Dataset:** Kaggle Titanic Dataset
* **Overview:** An extensive examination of vectorized NumPy operations and data wrangling methodologies using Pandas. The project executes essential exploratory data analysis techniques, including missing value imputation, outlier detection, feature engineering, and correlation analysis.

### [Lab Assignment 3: Scikit-learn: Data Preprocessing and Model Performance Evaluation](./202618028_Lab_3)

* **Dataset:** Kaggle Hotel Booking Demand
* **Overview:** This assignment implements formal preprocessing pipelines utilizing Scikit-learn. Various combinations of scalers and imputers were evaluated alongside Logistic Regression and Decision Tree classifiers to assess accuracy, model overfitting, and test-set generalization metrics.

### [Lab Assignment 4: End-to-End Machine Learning Project: Airbnb Price Prediction](./202618028_Lab_4)

* **Dataset:** Kaggle New York City Airbnb Open Data
* **Overview:** Constructed an end-to-end regression workflow to predict Airbnb nightly prices employing a hyperparameter-tuned Gradient Boosting model. The final serialized model was successfully deployed as an interactive web application utilizing Streamlit.

### [Lab Assignment 5: Machine Learning with Scikit-learn and From Scratch](./202618028_Lab_5)

* **Dataset:** UCI Productivity Prediction of Garment Employees
* **Overview:** Investigated the internal mechanics of predictive algorithms by implementing closed-form Linear Regression and Gradient Descent Logistic Regression entirely from scratch using NumPy. These manual implementations were subsequently optimized with L2 regularization and early stopping, then benchmarked against Scikit-learn's optimized solvers.

### [Lab Assignment 6: Feature Extraction and ML with Image and Text Data](./202618028_Lab_6)

* **Datasets:** Mendeley Asphalt Crack Dataset & Kaggle Email Spam Classification
* **Overview:** Focused on extracting numerical features from unstructured text and image data independent of Deep Learning frameworks. Features were engineered via OpenCV Canny edge detection for images and customized n-gram vectorizers for text, followed by classification utilizing Support Vector Machines and Naive Bayes algorithms.

### [Lab Assignment 7: Image Representation, PCA, Eigenfaces and Face Recognition](./202618028_Lab_7)

* **Dataset:** AT&T Database of Faces (ORL)
* **Overview:** Implemented Principal Component Analysis (PCA) strictly from scratch utilizing fundamental linear algebra properties to extract "Eigenfaces" and compress high-dimensional image data. A custom 1-Nearest Neighbor matching algorithm was developed to evaluate face recognition efficacy within this reduced principal component space.

### [Lab Assignment 8: Decision Trees and Support Vector Machines](./202618028_Lab_8)

* **Dataset:** UCI Banknote Authentication
* **Overview:** Deconstructed and implemented Decision Tree and Linear Support Vector Machine classifiers from scratch using core NumPy operations. The assignment visually mapped 2D decision boundaries, analyzed the impact of hyperparameter tuning, and demonstrated the mathematical necessity of the "Kernel Trick" for classifying non-linear data distributions.