from pandas import *
from random import choice

df = read_csv("french_words.csv")
words_dict = df.to_dict(orient='records')
word_text = choice(words_dict)
print(word_text["French"])
words_to_learn = {}
words_to_learn_fr = [f"{word_text["French"]}"]
words_to_learn_en = [f"{word_text["English"]}"]

dataf = DataFrame(
    {
        "French": words_to_learn_fr,
        "English": words_to_learn_en
    }
)

print(dataf)