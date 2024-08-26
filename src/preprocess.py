import nltk
#nltk.download()
import re
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity

# Define function for preprocessing test for NLP analysis - lemmatization and acronym removal
lemmatizer = WordNetLemmatizer()
def remove_acronyms(text):
    return re.sub(r'\b[A-Z\.]{2,}\b', ' ', text)
def lemmatize_sentence(sentence):
    words = sentence.split()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(lemmatized_words)

# Apply function to clean and process the job title column.
df['job_title'] = df['job_title'].apply(remove_acronyms)
df['job_title'] = df['job_title'].apply(lemmatize_sentence)