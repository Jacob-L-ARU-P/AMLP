# Tokenisor04

import nltk
import string

from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download("stopwords")

from nltk.corpus import stopwords

example_string = """To be, or not to be: that is the question: Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous fortune, Or to take arms against a sea of
troubles And, by opposing, end them. To die: to sleep; No more; and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to, 'tis a
consummation Devoutly to be wish'd. To die, to sleep; To sleep: perchance to dream: ay, there's the rub; For in that sleep of death what dreams may come When we have shuffled
off this mortal coil, Must give us pause: there's the respect That makes calamity of so long life."""

words_in_quote = word_tokenize(example_string)
#print(words_in_quote)

stop_words = set(stopwords.words("english"))

filtered_list = []

for word in words_in_quote:
    if word.casefold() not in stop_words:
        filtered_list.append(word)
#print(filtered_list)

filtered_list_b = filtered_list

# DOES NOT WORK SHOULD OF USED REGULAR EXPRESSION METHOD AS MENTIONED HERE: https://stackoverflow.com/questions/15547409/how-to-get-rid-of-punctuation-using-nltk-tokenizer
for word in filtered_list_b:
    word = word.translate(string.punctuation)

print(filtered_list_b)