def html_plaintext(addr):
	import requests
	from bs4 import BeautifulSoup

	page = requests.get(addr)
	return BeautifulSoup(page.text).get_text()



def common_words(text):
	from nltk.tokenize import word_tokenize
	from nltk.corpus import stopwords, wordnet
	from collections import Counter

	words = []
	for word in word_tokenize(text):
		if word.isalpha():
			words.append(word.lower())
	english_stops = set(stopwords.words('english'))
	words = [word for word in words if word not in english_stops]
	nouns, verbs, adverbs, adject = [], [], [], []
	try:
		syn = wordnet.synsets(word)[0]
		c = syn.pos
		if c == 'n': nouns.append(word)
		elif c == 'v': verbs.append(word)
		elif c == 'a': adject.append(word)
		elif c == 'r': adverbs.append(word)
	except IndexError:
		print word

	wordlist = {}
	wordlist['nouns'] = Counter(nouns)
	wordlist['adjectives'] = Counter(adject)
	wordlist['adverbs'] = Counter(adverbs)
	wordlist['verbs'] = Counter(verbs)

	return wordlist
