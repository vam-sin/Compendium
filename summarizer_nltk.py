# Libraries
from nltk import tokenize
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
nltk.download('stopwords')

# File Input
f = open("input.txt", "r")
input_text = f.read()

# print(input_text)

# Sentence Tokenize
sentences = tokenize.sent_tokenize(input_text)
# print(sentences)

# Processing the text
stop_words = set(stopwords.words('english'))
words = []
tokenizer = RegexpTokenizer(r'\w+')
for sentence in sentences:
    sentence = sentence.lower()
    word_tokens = tokenizer.tokenize(sentence)
    for w in word_tokens:
        if w not in stop_words:
            words.append(w)

print(words)

# Frequency and Weighted Frequency
unique_words = []
freq = []
weighted_freq = []

for str in words:
    if str not in unique_words:
        unique_words.append(str)

# print(unique_words)

for str in unique_words:
    freq.append(words.count(str))

# print(freq)

for val in freq:
    weighted_freq.append(val/max(freq))

# print(weighted_freq)

# Sentence Sum
sentence_sum = []

for sentence in sentences:
    score = 0
    sentence = sentence.lower()
    word_tokens = tokenizer.tokenize(sentence)
    for w in word_tokens:
        if w in unique_words:
            score = score + weighted_freq[unique_words.index(w)]
    sentence_sum.append(score)

# print(sentence_sum)

# Final Summary
print(sentences[sentence_sum.index(max(sentence_sum))])
