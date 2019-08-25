# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:13:46 2019

@author: Danijel
"""

import pandas as pd

#import data and define column names since they are missing
pace_data = pd.read_csv('C:/Users/Danijel/Desktop/PLINI_PACE_0519-1.csv', delimiter=',', names=["date", "company", "item_product_id", "customer_id", "item_name", "licence_type"], index_col=None)

#DATA PREPROCESSING AND CLEANING

#number of rows and columns
pace_data.shape
#check if columns have names
pace_data.columns
#types of column data
print (pace_data.dtypes)

#check for missing values
pace_data[pace_data["date"].isnull() == True].shape
pace_data[pace_data["company"].isnull() == True].shape
pace_data[pace_data["item_product_id"].isnull() == True].shape
pace_data[pace_data["customer_id"].isnull() == True].shape
pace_data[pace_data["item_name"].isnull() == True].shape
pace_data[pace_data["licence_type"].isnull() == True].shape

#check for duplicated rows
pace_data[pace_data.duplicated() == True].shape

#check for unique values for date and user ids
print (len(pace_data["date"].unique()))
print (len(pace_data["customer_id"].unique()))

#add origin column before merging data
pace_data['origin'] = "pace"

#calculate number of full licences
print (pace_data[pace_data['licence_type'] == "FULL"].shape)
