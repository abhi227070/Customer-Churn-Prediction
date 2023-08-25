# Customer-Churn-Prediction

# Customer Churn Prediction

Customer Churn Prediction is a project focused on predicting customer churn in a given dataset. The project involves various stages, from data preprocessing to model building and deployment of a user-friendly web application using Streamlit.

## Table of Contents

- [Introduction](#introduction)
- [Project Workflow](#project-workflow)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Models and Selection](#models-and-selection)
- [Deployment](#deployment)
- [Contact](#contact)

## Introduction

Customer churn, also known as customer attrition, is a critical business concern. This project aims to predict customer churn based on a dataset's attributes. The project involves data analysis, preprocessing, feature engineering, model building, and deployment of a user interface for interaction.

## Project Workflow

1. **Data Import and Preprocessing:** Begin by importing necessary libraries and loading the dataset. Perform initial data analysis to check the dataset's size, null values, duplicates, and statistical summary.

2. **Feature Engineering:** Standardize the data using the StandardScaler. Split the dataset into training and testing subsets for model evaluation.

3. **Model Building:** Experiment with various machine learning models, including Logistic Regression, Support Vector Classifier (SVC), K-Nearest Neighbors (KNN) Classifier, Decision Tree Classifier, Random Forest Classifier, XG Boost Classifier, and Artificial Neural Network (ANN). Based on performance metrics, select the XG Boost Classifier as the final model.

4. **Deployment:** Create a deployment pipeline using Streamlit. Develop a web application that allows users to interact with the trained model for churn prediction.

## Getting Started

To replicate or contribute to this project, follow these steps:

1. Clone the repository:


2. Install the required dependencies:

3. Run the preprocessing and model building scripts:

4. Launch the Streamlit web app:

## Usage

The primary goal of this project is to predict customer churn using a machine learning model. Users can also contribute to the project by testing different models, improving preprocessing steps, or enhancing the deployment interface.

## Models and Selection

After experimenting with multiple machine learning models, the XG Boost Classifier was selected due to its superior performance in predicting customer churn. The evaluation was based on accuracy, precision, recall, and F1-score.

## Deployment

The web application for customer churn prediction is built using Streamlit. Users can input relevant customer attributes and receive churn predictions instantly.

## Contact

If you have any questions, suggestions, or would like to contribute to this project, please feel free to contact me through my email: abhijeetmaharana77@gmail.com

---

This README outlines the key aspects of the Customer Churn Prediction project. For more detailed information, code implementation, and step-by-step instructions, please refer to the project repository.
