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
	numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven',
	'eight', 'nine', 'ten', 'once', 'twice', 'first', 'second']
	words = [word for word in words if word not in english_stops and word not in numbers]
	nouns, verbs, adverbs, adject = [], [], [], []
	for word in words:
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

def summary_sentence(text):
	d = common_words(text)
	noun1, _ = d['nouns'].most_common(1)[0]
	noun2, _ = d['nouns'].most_common(2)[1]
	verb, _ = d['verbs'].most_common(1)[0]
	adj, _ = d['adjectives'].most_common(1)[0]
	adv, _ = d['adverbs'].most_common(1)[0]

	return " ".join([adj, noun1, adv, verb, noun2])
