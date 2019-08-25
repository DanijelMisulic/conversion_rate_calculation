# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:13:46 2019

@author: Danijel
"""

import pandas as pd

pace_data = pd.read_csv('C:/Users/Danijel/Desktop/PLINI_PACE_0519-1.csv', delimiter=',', index_col=None)

#DATA PREPROCESSING AND CLEANING

#number of rows and columns
pace_data.shape
#check if columns have names
pace_data.columns
#types of column data
print (pace_data.dtypes)

#check for missing values
print (pace_data[pace_data["CODEREDEMPTION"].isnull() == True].shape)
#print (pace_data.duplicated())

#pace_data["account_status"].unique()


pace_data['origin'] = "plini"

#print (pace_data)


