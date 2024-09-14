import pandas as pd

#Series using lists

a = pd.Series([1,2,3,4],index=[5,6,7,8],name="Number")

print(a[6])

b = ["bose","deku"]

series = pd.Series(b,index=[3,4],name="Students")

print(series)

#same value in different indexes...

diff = pd.Series(3,index=[1,5,8])

print(diff)


#Series using dictionaries.

dictionaries = {"a":"bose","b":"deku"}

res = pd.Series(dictionaries)

print(res[0:])

#creating series with multiple cloumn and rows


mul = pd.Series([[1,2,3,4,5],[6,7,8,9,0]],name="array")

mul1=pd.Series({"p":[1,2,3,4,5],"q":[6,7,8,9,0]})

print("mul --> " ,mul1)

print("*******************************************")

print(mul1["p"])

