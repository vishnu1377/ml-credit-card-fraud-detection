import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt
import warnings 
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle
import streamlit as st

st.title('Credit Card Fraud Detection using Logistic Regression')

data = pd.read_csv('credit_card_fraud_dataset.csv')
st.subheader('Dataset Overview')
st.write(data.head())

st.write("Dataset Information:")
st.write(data.info())
st.write(data.describe())
st.write(data.isnull().sum())

sns.countplot(x = 'is_fraud', data = data)

plt.title('Distribution of is_fraud Class')
plt.xlabel('is_fraud')
plt.ylabel('Count')
st.pyplot(plt.gcf())

X = data[['time', 'amount', 'distance_from_home_km']]
y = data['is_fraud']

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
model = LogisticRegression()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)

st.write("confusion_matrix:")
st.write(confusion_matrix(y_test, y_pred))

st.write("classification_report:")
st.write(classification_report(y_test, y_pred))

st.write("accuracy_score:")
st.write(accuracy_score(y_test, y_pred))

comparison = pd.DataFrame({
    'Actual Class' : y_test,
    'Predicted Class' : y_pred
})
st.write(comparison.head(10))

st.write("Enter the details of the transaction to check for fraud:")
time = st.number_input("Enter time")
amount = st.number_input("Enter amount")
distance_from_home_km = st.number_input("distance_from_home_km")
input_data = [time, amount, distance_from_home_km]
input_data = np.array(input_data).reshape(1, -1)
prediction = model.predict(input_data)

st.write("Prediction value:", prediction[0])
if prediction[0] == 1:
    st.write("The transaction is predicted to be fraud.")
else:   st.write("The transaction is predicted to be non-fraud.")