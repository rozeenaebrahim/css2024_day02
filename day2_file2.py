# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:48:24 2024

@author: rebrahim
"""
"""
Loading files in different ways: 1) local, 2) different folder, 3) from url
"""
import pandas as pd

file = pd.read_csv("data_02/country_data_index.csv")

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

"""
Absolute Path: C:/Users/rebrahim/css2024_day2/data_02/iris.csv

Relative Path: data_02/iris.csv
"""

"""
Add column names to iris data
"""

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

df = pd.read_csv(url, header=None, names=column_names) #header=None: Have to first tell pandas that there is no header and then insert it

df1=pd.read_csv("data_02/Geospatial Data.txt",sep=";") #text file

df2 = pd.read_excel("data_02/residentdoctors.xlsx") #excel file

df3 = pd.read_json("data_02/student_data.json") #json file

url2= "https://raw.githubusercontent.com/Asabele240701/css4_day02/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"
#for github urls make sure you post the raw link

df4=pd.read_csv(url2)

df5 = pd.read_csv("data_02/Accelerometer_data.csv", names = ["date_time", "x", "y", "z"])

"""
Transform: cleaning files and so on

1) Getting rid of default index column
"""

df6 = pd.read_csv("data_02/country_data_index.csv",index_col=0)

#skip rows - skip first 5 rows

#df = pd.read_csv("data_01/insurance_data.csv")
#df = pd.read_csv("data_02/insurance_data.csv",skiprows=5)

df7 =pd.read_excel("data_02/residentdoctors.xlsx")
df7["LOWER_AGE"]=df7["AGEDIST"].str.extract('(\d+)-') #adds column lower age to the end with data from AGEDIST column, extract('(\d+)-'): extracts the first decimal number before the - 
df7["UPPER_AGE"]=df7["AGEDIST"].str.extract('-(\d+)')

df7["LOWER_AGE"]=df7["LOWER_AGE"].astype(int) #converts from str to int
df7["UPPER_AGE"]=df7["UPPER_AGE"].astype(int)
"""
Working with dates

30-01-2024 - UK/SA standard
01-30-2024 - US standard
"""

df8 = pd.read_csv("data_02/time_series_data.csv",index_col=0)
# Convert the 'Date' column to datetime
df8['Date'] = pd.to_datetime(df['Date'])

df8['Year']=df8['Date'].dt.year #create year column and extract year dt value from Date column
df8['Month']=df8['Date'].dt.month
df8['Day']=df8['Date'].dt.day

df9 = pd.read_csv("data_02/patient_data_dates.csv",index_col=0)
df9=df9.drop(index=26, inplace=True) #drop row that had incorrect row

df9['Date'] = pd.to_datetime(df9["Date"])
#df = pd.read_csv("data_02/patient_data_dates.csv", index_col=0, skiprows=[27])

#what to do with Nan values - replace with average value of that column to prevent data from being skewed too much

avg_cal=df9["Calories"].mean()

df9["Calories"].fillna(avg_cal, inplace=True)

#df9.loc[7,"Duration"]=45 #replace the incorrect value
df9['Duration']=df9['Duration'].replace([450],50)

#df.drop_duplicates(inplace = True) #to drop any duplicates

col_names=df.columns #print column names

col_names=df.columns.tolist()

df["sepal_length_sq"]=df["sepal_length"]**2 #add extra column with sepal lenght values squared
#df["sepal_length_sq"]=df["sepal_length"].apply(lambda x: x**2) #better to use this for more complicated operations

grouped=df.groupby("class") #class is a specific column

mean_square_values = grouped['sepal_length_sq'].mean() #finding mean value sepal lenght squared valye of the grouped data
print(mean_square_values)

df10=pd.read_csv("data_02/person_split1.csv")
df11=pd.read_csv("data_02/person_split2.csv")

#combine two df together

df12=pd.concat([df10,df11],ignore_index=True)

df13=pd.read_csv("data_02/person_education.csv")
df14=pd.read_csv("data_02/person_work.csv")

#inner join

df_merge_inner=pd.merge(df13,df14,on="id") #merged the data based on the "id" column, common column (relationship) between the two datasets
#df_merge_outer = pd.merge(df13, df14, on='id', how='outer') #outer join returns all the rows from both dataframes  matches up rows where possible, with NaNs elsewhere. Like taking the union of the two datasets

df["class"] = df["class"].str.replace("Iris-", "") #remove the word Iris in the class column

df=df[df['sepal_length']>5] #filter these data to give rows in which sepel lenght > 5

df=df[df["class"]=="virginica"] #extracting only the virginica data from class column

# Calculate the average iris_virginica_sep_length
avg_iris_virginica_sep_length = df['sepal_length'].mean()

"""
Loading data
"""

df.to_csv("pulsar.csv") #once cleaned, load data into a csv 