import numpy as np
import nltk
#nltk.download('punkt')
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()


'''
this file handle data input
'''


def tokenize(sentence):
	'''
	input: is sentence
	return: list of words in sentence
	'''
	return nltk.word_tokenize(sentence)

def stem(word):
	'''
	input: word
	return the mean root of word
	'''
	return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentence, all_words):
	'''
	example: 
	tokenized_sentence = ['hello', 'what', 'up']
	all_words = ['hi', 'hello', 'goodbye', 'bye', 'i', 'thank', 'cool']
	return    = [  0  ,   1   ,    0     ,   0   ,  0  ,  0  ,    0 ]
	'''

	tokenized_sentence = [stem(w) for w in tokenized_sentence]

	bag = np.zeros(len(all_words), dtype=np.float32)
	for index, word in enumerate(all_words):
		if word in tokenized_sentence:
			bag[index] = 1.0

	return bag
