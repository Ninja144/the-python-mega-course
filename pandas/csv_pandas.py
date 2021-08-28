import os
import pandas

print(os.listdir('./supermarkets'))

df1 = pandas.read_csv('./supermarkets/supermarkets.csv')
print(df1)

df2 = pandas.read_json('./supermarkets/supermarkets.json')
print(df2)