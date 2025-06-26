Student Performance Prediction using Data Preprocessing and SVR

 Overview

This project is a complete **end-to-end machine learning pipeline** designed to predict student marks based on their study habits. It includes robust **data preprocessing**, **dynamic visualizations**, and **model training** using the **Support Vector Regression (SVR)** algorithm. The code is structured using **Object-Oriented Programming (OOP)** principles for reusability and modularity.

It is built with the goal of:
 Exploring real-world educational data
  Understanding relationships between study time and performance
 Building interpretable and accurate prediction models



 Objectives

  Clean and preprocess data using statistical and null-handling techniques
 Generate univariate and bivariate visualizations
 Train a regression model (SVR) to predict student marks
 Evaluate model performance using standard metrics
 Save the model and preprocessing objects for future use



  Key Features

  Modular OOP Design
The project uses separate classes for each step of the pipeline:
 `Loader`: For reading data from CSV files
 `DataHandler`: For dynamic exploration of the dataset
 `DataPreprocessor`: For statistical and null-value processing
 `UnivariateVisualizer`: For basic column-wise plots
 `BivariateVisualizer`: For analyzing relationships between columns
 `Model`: For building, training, and evaluating the machine learning model

  Visual Insights
The project provides both **univariate** and **bivariate** graphs such as:
 Histograms
 Pie Charts
 Line Charts
 Scatter Plots
 Box Plots
  Correlation Heatmaps

These help in understanding the data distributions, spotting outliers, and identifying strong correlations.

 Machine Learning Workflow
 **Split**: Divide data into training and test sets
 **Scale**: Normalize or standardize features
 **Train**: Fit a Support Vector Regressor to the data
 **Evaluate**: Use metrics like MSE and R² Score
 **Save**: Store the trained model and scaler for deployment

---

##  Dataset Info

The dataset used is `Student_Marks.csv`, which contains:
 `number_courses`: Number of courses taken by the student
 `time_study`: Total hours spent studying
 `Marks`: Final marks obtained (target variable)

---

##  Technologies Used

 **Python 3**
 **Pandas** – for data manipulation
 **Seaborn & Matplotlib** – for data visualization
 **Scikit-learn** – for preprocessing and modeling
 **Pickle** – for saving model and scaler

---

 Use Cases

This project is suitable for:
 Academic research or coursework
 Beginner to intermediate ML practice
 Real-world education analytics
 Demonstrating OOP in data science


