import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from collections import Counter

def getWords(addr):
	page = requests.get(addr)
	words = word_tokenize(BeautifulSoup(page.text).get_text())
	english_stops = set(stopwords.words('english'))
	words = [word.lower() for word in words if word not in english_stops]
	nouns, verbs, adverbs, adject = [], [], [], []
	for word in words:
		if not word.isalpha():
			continue
		try:
			syn = wordnet.synsets(word)[0]
			c = syn.pos
			if c == 'n': nouns.append(word)
			elif c == 'v': verbs.append(word)
			elif c == 'a': adject.append(word)
			elif c == 'r': adverbs.append(word)
		except IndexError:
			# print word
			continue

	wordlist = {}
	wordlist['nouns'] = Counter(nouns)
	wordlist['adjectives'] = Counter(adject)
	wordlist['adverbs'] = Counter(adverbs)
	wordlist['verbs'] = Counter(verbs)

	return wordlist
