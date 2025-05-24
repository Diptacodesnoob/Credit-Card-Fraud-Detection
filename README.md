#  Credit Card Fraud Detection App

This project is a web application built using Streamlit that allows users to detect the probability of credit card fraud based on transaction features. It uses a Random Forest model trained with an undersampled and tuned dataset.

## Features

- Input transaction data including time, amount, and anonymized features (V1 to V28)
- Predict fraud probability using a trained machine learning model
- Provides visual alerts for high, moderate, and low-risk transactions

## Model Info

- **Model**: Random Forest Classifier
- **Training**: Trained on a credit card fraud detection dataset
- **Techniques used**: Undersampling and model tuning
- **Notebook**: `frauddetection-undersampling-model-tuning(app).ipynb`

## 📦 Installation

## 1. Clone this repository:

   git clone https://github.com/Diptacodesnoob/credit-card-fraud-detection-app.git
   cd credit-card-fraud-detection-app
## 2.Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate


## 3.Install dependencies:
pip install -r requirements.txt

## Running the App
Make sure fraud_rf_model.pkl is in the project directory. Then run:

streamlit run app.py

You will be prompted to enter input values for all features. Once submitted, the app will show the probability of the transaction being fraudulent and a corresponding warning level.

## Input Fields
Time: Seconds elapsed between this transaction and the first transaction

Amount: Transaction amount

V1 - V28: PCA-transformed features from the original dataset

## Dependencies
All necessary libraries are listed in requirements.txt, including:

streamlit

pandas

numpy

scikit-learn

imbalanced-learn

matplotlib

seaborn

## Files

Dataset: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

app.py: Streamlit web application script

frauddetection-undersampling-model-tuning(app).ipynb: Notebook for model training and tuning

requirements.txt: List of dependencies

fraud_rf_model.pkl:  Pretrained model file used by the app

## Notes
This app is for educational/demo purposes and should not be used in production without proper validation.

The trained model (fraud_rf_model.pkl) must be placed in the root directory of the project.

## Contact


Developer : Sudipta Das


Email: dipta6349@gmail.com


Github: https://github.com/Diptacodesnoob

## Happy Predicting!




