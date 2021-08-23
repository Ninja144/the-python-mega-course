import json

data = json.load(open("data.json", "r"))


def translate(word):
    return data[word]


word = input("Enter word: ")

print(translate(word))
