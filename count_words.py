# import re
# def count_words(input):
#     # lst = input.split()
#     lst = re.findall(r'\w+',input)
#     result = dict()
#     for word in lst:
#         result[word.lower()] = result.get(word,0) + 1
#     print(result)
# count_words("Oh what a day what a lovely day!")
from collections import Counter

def count_words(string):
    """Return the number of times each word occurs in the string."""
    words = []
    for word in string.lower().split():
        words.append(word.strip(',;.!?"()'))
        print(Counter(words))
count_words("Oh don't' a day what a lovely day!")