# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

# loading the saved model
loaded_model = pickle.load(open('C:/Deployment ML/medicine_model.sav','rb'))


#Print the top 10 recommendations
print("Top 10 recommended medicines:")
for _, row in loaded_model.head(10).iterrows():
    print(f"{row['DRUG NAME']}")

