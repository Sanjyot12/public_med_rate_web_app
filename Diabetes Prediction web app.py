# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:11:35 2024

@author: khang
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model=pickle.load(open('C:/Deployment ML/trained_model.sav','rb'))

#creating a function for prediction
def diabetes_predictions(input_data):
    
    

    #changing the input_data to numpy array
    input_data_as_numpy_array=np.asarray(input_data)

    #reshape the array as we are predicting for one instance
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)



    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return'The person is not diabetic'
    else:
        return'The person is diabetic'
        

def main():
    
    # giving a title
    st.title('MEDICINE RECOMMENDATION')
    
    #getting the input data from the user 
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Level')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPredigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    
    #code for Prediction 
    diagnosis = ''
    
    #creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_predictions([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPredigreeFunction,Age])
        
    
    st.success(diagnosis)
    
    
    
if __name__ == '__main__':
    main()
         