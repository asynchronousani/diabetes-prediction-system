# -*- coding: utf-8 -*-

import pickle
import streamlit as st

# loading the saved models
diabetes_model = pickle.load(open('C:/Users/Anirudh128/Desktop/Projects/Machine Learning Projects/Diabetes Prediction System/diabetes_model.sav', 'rb'))

# Diabetes Prediction Page   
# page title
st.title('Diabetes Prediction using ML')
    
    
# getting the input data from the user
col1, col2, col3 = st.columns(3)
    
with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
with col2:
        Glucose = st.text_input('Glucose Level')
    
with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    
with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    
with col2:
        Insulin = st.text_input('Insulin Level')
    
with col3:
        BMI = st.text_input('BMI Value')
    
with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    
with col2:
        Age = st.text_input('Age of the Person')
    
    
# code for Prediction
diab_diagnosis = ''
    
# creating a button for Prediction
    
if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
st.success(diab_diagnosis)