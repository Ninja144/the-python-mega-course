import pandas

data = pandas.read_csv("reviews.csv")

print(data[data['Rating'] > 4].count())
