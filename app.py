import nltk
nltk.download('punkt')         # download again to ensure it's cached correctly
nltk.download('stopwords')     # download stopwords (already done, but just in case)
nltk.download('omw-1.4')       # optional: fixes some other future issues
nltk.download('wordnet')       # optional for future keyword improvements

# Test if everything is working
from nltk.tokenize import word_tokenize
text = "Hello! How can I help you today?"
print(word_tokenize(text))

exit()
