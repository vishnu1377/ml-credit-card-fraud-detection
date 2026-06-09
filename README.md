# ml-credit-card-fraud-detection
A machine learning project that detects fraudulent credit card transactions using Logistic Regression. Built with Python, Scikit-learn, and Streamlit, featuring data analysis, model evaluation, and an interactive web application for real-time fraud prediction.
# Credit Card Fraud Detection using Logistic Regression

## Project Overview

This project focuses on building a machine learning model to identify fraudulent credit card transactions using **Logistic Regression**, one of the most widely used classification algorithms. Credit card fraud has become a significant challenge in the financial sector, making fraud detection systems essential for minimizing financial losses and protecting customers.

The objective of this project is to classify transactions as either **fraudulent** or **non-fraudulent** based on transaction-related features. The project demonstrates the complete machine learning workflow, from data preprocessing and exploratory data analysis to model training, evaluation, and deployment through an interactive web application.

## Features

* Data loading and preprocessing using **Pandas** and **NumPy**
* Exploratory Data Analysis (EDA) to understand the dataset
* Visualization of fraud and non-fraud transaction distributions using **Seaborn** and **Matplotlib**
* Training a **Logistic Regression** model using **Scikit-learn**
* Splitting the dataset into training and testing sets for performance evaluation
* Evaluation using:

  * Accuracy Score
  * Confusion Matrix
  * Classification Report
* Interactive user interface built with **Streamlit**
* Real-time prediction of transaction status based on user inputs

## Technologies Used

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Scikit-learn**
* **Streamlit**

## Machine Learning Workflow

1. **Data Collection:** Load the credit card transaction dataset.
2. **Data Exploration:** Examine the structure of the dataset and identify missing values.
3. **Visualization:** Analyze the distribution of fraudulent and non-fraudulent transactions.
4. **Feature Selection:** Select relevant features for model training.
5. **Train-Test Split:** Divide the dataset into training and testing subsets.
6. **Model Development:** Train a Logistic Regression model on the selected features.
7. **Performance Evaluation:** Assess the model using various classification metrics.
8. **Deployment:** Develop a Streamlit application to allow users to interact with the model and obtain predictions.

## Application Functionality

The Streamlit application enables users to enter transaction details, such as transaction time, amount, and distance from home, and instantly receive a prediction indicating whether the transaction is likely to be fraudulent or legitimate.

This project highlights how machine learning techniques can be applied to solve real-world financial security problems while providing practical experience in building and deploying predictive models.

## Learning Outcomes

Through this project, I gained hands-on experience in:

* Data preprocessing and analysis
* Binary classification using Logistic Regression
* Evaluating machine learning models
* Developing interactive web applications with Streamlit
* Understanding the practical applications of fraud detection systems

## Future Enhancements

* Incorporate additional transaction features to improve prediction accuracy.
* Experiment with advanced classification algorithms such as Random Forest, XGBoost, and Neural Networks.
* Implement feature scaling and hyperparameter tuning.
* Deploy the application to cloud platforms for public accessibility.
* Add model persistence using Pickle for efficient deployment.

## Conclusion

This project serves as an excellent introduction to machine learning-based fraud detection systems. By combining data analysis, predictive modeling, and web application development, it demonstrates how technology can be leveraged to enhance security and support decision-making in the financial domain.
