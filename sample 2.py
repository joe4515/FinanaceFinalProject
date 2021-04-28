import pandas as pd

dataset=pd.read_csv("nyc-rolling-sales.csv.zip")


##find the avergae price of housing in each borough
print(NYC_housing_data[NYC_housing_data["BOROUGH"] == 1] & NYC_housing_data["SALE PRICE"]<1)

print(NYC_housing_data.loc[NYC_housing_data["BOROUGH"] == 5] & ["SALE PRICE"]>)

NYC_borough_1= NYC_housing_data.loc[(NYC_housing_data["BOROUGH"]== '1') & (NYC_housing_data["SALE PRICE"]>1)]
print(NYC_borough_1)

np.array(["BOROUGH","SALE PRICE"])
NYC_borough_1= (["BOROUGH"],["SALE PRICE"])
NYC_borough_1= NYC_housing_data["BOROUGH"] ==1
print(NYC_borough_1)
##no missing values




