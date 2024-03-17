# Import modules and Data
import nltk
#nltk.download('*') # Downloads all packages from nltk
from nltk.corpus import movie_reviews, stopwords
from nltk.tokenize import word_tokenize, sent_tokenize, RegexpTokenizer
from nltk.stem import PorterStemmer, LancasterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

movie_reviews.words()

# Tokenisation
data = "I pledge to be a data scientist one day"
tokenized_text=word_tokenize(data)
print("\n Tokenisation Examples: \n", data)
print(tokenized_text)
#print(type(tokenized_text)) # tokenized_text is a list
#input() # Not necessary input prompt for VS code at this point

# ///////////////////////////////////////
para_1="""Cake is a form of sweet food made from flour, sugar, and other ingredients, that is usually baked.
In their oldest forms, cakes were modifications of bread, but cakes now cover a wide range of preparations that can be simple or elaborate, and that share features with other desserts such as pastries, meringues, custards, and pies.
The most commonly used cake ingredients include flour, sugar, eggs, butter or oil or margarine, a liquid, and leavening agents, such as baking soda or baking powder. 
Common additional ingredients and flavourings include dried, candied, or fresh fruit, nuts, cocoa, and extracts such as vanilla, with numerous substitutions for the primary ingredients.
Cakes can also be filled with fruit preserves, nuts or dessert sauces (like pastry cream), iced with buttercream or other icings, and decorated with marzipan, piped borders, or candied fruit."""
tokenized_para=sent_tokenize(para_1)
print("\n Sentences Tokenised: \n", tokenized_para)
#print(type(tokenized_para))

# ///////////////////////////////////////
tokenizer = RegexpTokenizer(r'\w+')
result_a = tokenizer.tokenize("Wow! I am. excited ;to: learn# data science")
print("\n Punctuation removal Example before:     Wow! I am. excited ;to: learn# data science\n Punctuation removal Example after: " ,result_a)

# //////////////////////////////////////
to_be_removed = set(stopwords.words('english'))
para_2="""Cake is a form of sweet food made from flour, sugar, and other ingredients, that is usually baked.
In their oldest forms, cakes were modifications of bread, but cakes now cover a wide range of preparations 
that can be simple or elaborate, and that share features with other desserts such as pastries, meringues, custards, 
and pies."""
tokenized_para_2=word_tokenize(para_2)
print("\n Stopword removal Before: \n", tokenized_para_2)
modified_token_list=[word for word in tokenized_para_2 if not word in to_be_removed]
print("\n Stopword removal after: \n", modified_token_list)

# //////////////////////////////////////
# Punctuation removal from list
modified_token_list_b = modified_token_list[:]  # Duplicate List
for token in modified_token_list_b:             # go element by element
    if not tokenizer.tokenize(token):           # if string element is punctuation
        modified_token_list_b.remove(token)     # remove element
print("\n Punctuation removal 2: \n", modified_token_list_b)

# Verbalisation of above ^ Punctuation removal block
# The token is a string element.
# The tokenizer is a regular expression used to filter out punctuation
# Tokenize-ing the token will return an empty string element if it is punctuation
# otherwise it will return an unchanged token.

# /////// Stemming //////////////////
# ///////////////////////////////////
# /////// Porter Stemmer ////////////
#stemmer_p = PorterStemmer()
#tk_content_a=modified_token_list_b
#stemmed_words_a = [stemmer_p.stem(i) for i in tk_content_a] 
#print("\n Porter Stemmer; \n", stemmed_words_a)

# /////// Lancaster Stemmer /////////
#stemmer_l = LancasterStemmer()
#tk_content_b=modified_token_list_b
#stemmed_words_b = [stemmer_l.stem(i) for i in tk_content_b]
#print("\n Lancaster Stemmer; \n", stemmed_words_b)

# /////// Lemmatization /////////////
lemmatizer = WordNetLemmatizer()
tk_content_c = modified_token_list_b
lemmatized_words = [lemmatizer.lemmatize(i) for i in tk_content_c] 
print("\n Lemmatized words example: \n", lemmatized_words)

# /////// POS Tagging ///////////////
content_a = """Cake is a form of sweet food made from flour, sugar, and other ingredients, that is usually baked.
In their oldest forms, cakes were modifications of bread, but cakes now cover a wide range of preparations 
that can be simple or elaborate, and that share features with other desserts such as pastries, meringues, custards, 
and pies."""
words_a= [word_tokenize(i) for i in sent_tokenize(content_a)]
pos_tag_a= [nltk.pos_tag(i,tagset="universal") for i in words_a]
print("\n\n", pos_tag_a)

# /////// Chunking //////////////////
content_b = "Cake is a form of sweet food made from flour, sugar, and other ingredients, that is usually baked."
tokenized_text_a = nltk.word_tokenize(content_b)
tagged_token_a = nltk.pos_tag(tokenized_text_a)
grammer_a = "NP: {<DT>?<JJ>*<NN>}"
phrases_a = nltk.RegexpParser(grammer_a)
result_b = phrases_a.parse(tagged_token_a)
#print("\n\n", result_b, "\n")
#result_b.draw()

# /////// Bag of Words //////////////
content_c = """Cake is a form of sweet food made from flour, sugar, and other ingredients, that is usually baked.
In their oldest forms, cakes were modifications of bread, but cakes now cover a wide range of preparations that can be simple or elaborate, and that share features with other desserts such as pastries, meringues, custards, and pies."""

count_vectorizer_a = CountVectorizer()
bag_of_words = count_vectorizer_a.fit_transform(content_c.splitlines())

#pd.DataFrame(bag_of_words.toarray(), columns = count_vectorizer_a.get_feature_names()) # Why aren't you working?