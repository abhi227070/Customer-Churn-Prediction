import pickle
import streamlit as st
import pandas as pd


def load():
    model = pickle.load(open('CustomerPipe.pkl','rb'))
    df = pd.read_excel('customer_churn_large_dataset.xlsx')
    
    return model,df
    
model,df = load()

st.title('Customer Churn Prediction')

st.write('Please Fill the following parameters:')

id = st.text_input('Customer ID')
name = st.text_input("Customer Name")
age = st.number_input("Age")
Gender = st.selectbox('Gender',df['Gender'].unique())
Location = st.selectbox('Location',df['Location'].unique())
sub = st.number_input('Subscription Length Months')
month = st.number_input('Monthly Bill')
total = st.number_input('Total Usage (in GB)')

if st.button('Predict'):

    predict = model.predict([[age,Gender,Location,sub,month,total]])

    if predict == 0:
        st.success('The Customer will retain.')
    else:
        st.success('The Customer will not retain.')