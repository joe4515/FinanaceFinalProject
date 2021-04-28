#import numpy as np
#import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
##most expensive area for housing in NYC
import pandas as pd
##print my dataset
dataset=pd.read_csv("nyc-rolling-sales.csv.zip")
print(dataset)
##print colums
print(sorted(dataset))
##subset adress,borough,neighbourhood,residentail units, sale price
NYC_housing_data =dataset[["ADDRESS", "BOROUGH", "NEIGHBORHOOD", "RESIDENTIAL UNITS", "SALE PRICE"]]
print(NYC_housing_data)
import numpy as np
##check each collumn for missing values
print(NYC_housing_data.isna().any())

mask_Borough_1 =NYC_housing_data ["BOROUGH"]==1
mask_Price_1 =NYC_housing_data.int(["SALE PRICE"]>=1)

















