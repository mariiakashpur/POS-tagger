from __future__ import division

import math
import re
from random import shuffle

from collections import Counter, defaultdict
from itertools import izip
from pprint import pprint
from random import shuffle

from Token import Token
from Sentence import Sentence


class Corpus(object):
	def __init__(self, goldPath, predictedPath=None):
		self.goldPath = goldPath
		self.predictedPath = predictedPath
		self.sents = [] # all sents in corpus
		self.sent_stats = {}
		self.numTokens = 0 # count total tokens in corpus
		self.tags = set()
		self.tokens = []
		sent = Sentence()



		if predictedPath:
			with open(goldPath) as gf, open(predictedPath) as pf:
				for gline,pline in izip(gf, pf): # open two files simultaneously
					if gline.strip() and pline.strip(): # check if lines not empty
						gtoken_tag = re.split(r'\t', gline)
						ptoken_tag = re.split(r'\t', pline)
						if gtoken_tag[0] == ptoken_tag[0]:
							token = Token(gtoken_tag[0], gtoken_tag[1].strip(), ptoken_tag[1].strip()) # create new Token object
							sent.addToken(token)
							self.numTokens += 1 
						else:
							raise Exception("Files not in sync")
					else:
						self.sents.append(sent)
						sent = Sentence()
		else:
			# store all sentences from corpus
			sentences = []
			# store a sentence that consists of tokens
			sentence = []
			with open(goldPath) as gf:
				for line in gf: 
					# check if lines not empty
					if line.strip(): 
						# split line into token and tag as list elements
						token_tag = re.split(r'\t', line)
						# add a token object into sentence
						sentence.append(Token(token_tag[0].strip(), token_tag[1].strip()))
						# count total number of tokens
						self.numTokens += 1 
					else:
						# we have reached end of sentence (empty line)
						sentences.append(sentence)
						sentence = []

			prev = "prevnotekzist"
			following = "folnotekzist"
			for j, sentence in enumerate(sentences):
				for i, token in enumerate(sentence):
					# make sure we don't go beyond sentence length
					if i+1 < len(sentence):
						following = sentence[i+1]
					# if we reached end of current sentence - take following word as first word of next sentence
					elif j+1 < len(sentences):
						following = sentences[j+1][0]
					token.setPrev(prev)
					token.setFollowing(following)
					token.getNeighborFeatures()
					# print (vars(token))
					prev = token
					sent.addToken(token)
				self.sents.append(sent)
		 		sent = Sentence()



		# else:
		# 	sentences = []
		# 	sentence = []
		# 	with open(goldPath) as gf:
		# 		for line in gf: 
		# 			if line.strip(): # check if lines not empty
		# 				sentence.append(re.split(r'\t', line))
		# 				self.numTokens += 1 
		# 			else:
		# 				sentences.append(sentence)
		# 				sentence = []

		# 	prev = "prevnotekzist"
		# 	following = "folnotekzist"
		# 	for j, sentence in enumerate(sentences):
		# 		for i, token_tag in enumerate(sentence):
		# 			if i+1 < len(sentence):
		# 				following = sentence[i+1][0]
		# 			elif j+1 < len(sentences):
		# 				following = sentences[j+1][0][0]
		# 			token = Token(token_tag[0], token_tag[1].strip(), prev, following)
		# 			# pprint (vars(token))
		# 			prev = token_tag[0]
		# 			sent.addToken(token)
		# 		self.sents.append(sent)
		#  		sent = Sentence()

	def getNumTokens(self):
		return self.numTokens

	def getSents(self):
		return self.sents

	def randomTokens(self):
		random_tokens = shuffle(self.tokens)  
		return random_tokens

	def getSentStats(self): # !!! can't we do all calculation in init and here just return the result, just to avoid looping ?
		for sent in self.sents:
			token_stats = sent.getTokenStats()
			for tag in token_stats:
				#print token_stats[tag]
				if tag in self.sent_stats:
					self.sent_stats [tag]["TP"] += token_stats[tag]["TP"]
					self.sent_stats [tag]["FN"] += token_stats[tag]["FN"]
					self.sent_stats [tag]["FP"] += token_stats[tag]["FP"]
				else:
					self.sent_stats [tag] = token_stats[tag]
		#print self.sent_stats
		return self.sent_stats

	def getTags(self): # !!! can't we do all calculation in init and here just return the result, just to avoid looping ?
		tags = []
		for sent in self.getSents():
			for token in sent.getTokens():
				tags.append(token.getGoldPOS())
		self.tags = set(tags)
		#@todo check it, set.update
		return self.tags

	def getPairedTagsCorpus(self):
		tags = []
		for i,sent in enumerate(self.getSents()):
			for j,token in enumerate(sent.getTokens()):
				if i == 0 and j == 0:
					tags.append("#begin/" + token.getGoldPOS())
				elif i == len(self.getSents())-1 and j == len(sent.getTokens())-1:
					tags.append(token.getGoldPOS() + "/#end")
				elif i > 0 and j == 0:
					tags.append(token.getPrev().getGoldPOS() + "/" + token.getGoldPOS())
				else:
					tags.append(sent.getTokens()[j-1].getGoldPOS() + "/" + token.getGoldPOS())

		self.tags = set(tags)
		#@todo check it, set.update
		return self.tags

	def getPairedTagsSent(self):
		tags = []
		for sent in self.getSents():
			for j,token in enumerate(sent.getTokens()):
				if j == 0:
					tags.append("#begin/" + token.getGoldPOS())
				elif j == len(sent.getTokens())-1:
					tags.append(token.getGoldPOS() + "/#end")
				else:
					tags.append(sent.getTokens()[j-1].getGoldPOS() + "/" + token.getGoldPOS())

		self.tags = set(tags)
		#print tags
		#@todo check it, set.update
		return self.tags


	def resetSentStats(self):
		for sent in self.sents:
			sent.resetTokenStats()
		self.sent_stats = {}







    	










    
