import pandas as pd
"""""
#using list in dataframes...

df = pd.DataFrame([["bose","deku"],["madhu","mitha"]])

print(df)

lst = [ {"a":"bose","b":"deku"},{"a":"cat","b":"dog"}]

d_df = pd.DataFrame(lst)

print(d_df)


#using dictionaries + series for data frames ....

stu_details = {
    "Rollno":pd.Series([1,2,3,4,5]),
    "Tamil":pd.Series([45,67,89,76,87])
}

res = pd.DataFrame(stu_details)
print("*************")

print(res)
"""

#reading csv files

csv = pd.read_csv('./churn.csv')

print(type(csv))