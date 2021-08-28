import os
import pandas

print(*os.listdir('./supermarkets'))
print()

# df1 = pandas.read_csv('./supermarkets/supermarkets.csv')
# print(df1)
# print()
#
# df2 = pandas.read_json('./supermarkets/supermarkets.json')
# print(df2)
# print()
#
# df3 = pandas.read_excel('./supermarkets/supermarkets.xlsx', sheet_name=0)
# print(df3)
# print()
#
# df4 = pandas.read_csv('./supermarkets/supermarkets-commas.txt')
# print(df4)
# print()
#
# df5 = pandas.read_csv('./supermarkets/supermarkets-semi-colons.txt', sep=';')
# print(df5)
# print()

df6 = pandas.read_csv('./supermarkets/supermarkets-semi-colons.txt', sep=';', header=None)
print(df6)
print()

df6.columns = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
print(df6)
print()

df6.set_index("one", inplace=True)
print(df6)
print()

df6.loc['2':'3']
print(df6)
