import pandas as pd
Data = pd.read_excel("Dataset.xlsx")


# Data Info

Data.info()                             # To get information about the dataset
print(Data.columns)                     # To get the column names of the dataset
print(Data.head())  
print(Data.tail())                    # To get the last 5 rows of the dataset
print(Data.describe())                 # To get the statistical summary of the data


# Data Cleaning

print(Data.isnull().sum())                  # To check for missing values in the dataset   
Data["CouponCode"] = Data["CouponCode"].fillna("No Coupon")  # To fill missing values in the 'couponCode' column with 'No Coupon'
print(Data.duplicated().sum())              # To check for duplicate rows in the dataset

# Checking Data Types
print(Data.dtypes)                          # To check the data types of each column in the dataset
Data['Date'] = pd.to_datetime(Data['Date'])      # To convert the 'date' column to datetime format


#remove Spaces from the text columns
text_columns = Data.select_dtypes(include="object").columns

for col in text_columns:
    Data[col] = Data[col].str.strip()

#Check Numeric Columns
Data[Data["Quantity"] < 0]
Data[Data["UnitPrice"] < 0]

#verify total price column
(Data["Quantity"] * Data["UnitPrice"] == Data["TotalPrice"]).all()

#Final Checking
print(Data.isnull().sum())
print(Data.duplicated().sum())
print(Data["OrderID"].duplicated().sum())

#clean Dataset 
Cleaned_Data = Data.to_csv("Cleaned_Dataset.csv", index=False)