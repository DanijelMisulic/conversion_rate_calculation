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
m, n = pace_data.shape
#check if columns have names
pace_data.columns
#types of column data
pace_data.dtypes

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
len(pace_data["date"].unique())
len(pace_data["customer_id"].unique())

#add origin column before merging data
pace_data['origin'] = "pace"

#calculate number of full licences
number_of_full_licences = pace_data[pace_data['licence_type'] == "FULL"].shape

#calculate percentage of full licences
print ("Percentage of full licences", number_of_full_licences[0]/m * 100, "%")
#users that pop up twice should be ones who switched from trial to full
#thats not the case every time - there are users who got trial version more times
more_than_one_time_users = len(pace_data[pace_data['customer_id'].duplicated()]['customer_id'].unique())

#instead calulate number of users that have duplicate entries in columns customer_id and licence_type
data = pace_data[["customer_id","licence_type"]]
duplicated_licences = data[data.duplicated() == True]
duplicates_with_same_licence_type = len(duplicated_licences['customer_id'].unique())

print ("Number of users that switched from trial to full licence is", more_than_one_time_users-duplicates_with_same_licence_type)

pace_data[pace_data['customer_id'].duplicated()]