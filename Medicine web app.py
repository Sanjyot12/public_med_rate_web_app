# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 14:13:02 2024

@author: khang
"""

import numpy as np
import pickle 
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('C:/Deployment ML/medicine_model.sav','rb'))


#creating the function for recommending 

def medicine_prediction(input_data):
    
    #Print the top 10 recommendations
    return("Top 10 recommended medicines:")
    for _, row in loaded_model.head(10).iterrows():
        return(f"{row['DRUG NAME']}")



def main():
    
    #giving the title
    st.title('MEDICINE RECOMMENDATION SYSTEM')
    
    option = st.selectbox(
    'Select a Disease',
    ['Diabetes']
    )

    
    


    #code for prediction
    diagnosis=''
    
   



    # creating a button
    if st.button('Get Recommendations'):
        st.write("Top 10 recommended medicines:")
        for _, row in loaded_model.head(10).iterrows():
            st.write(f"{row['DRUG NAME']}")
    
            
            
            
           
    
    
if __name__ == '__main__':
    main()