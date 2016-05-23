from __future__ import division

import math
import re
from random import shuffle

from collections import Counter, defaultdict
from itertools import izip

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
							token = Token(gtoken_tag[0], gtoken_tag[1], ptoken_tag[1]) # create new Token object
							sent.addToken(token)
							self.numTokens += 1 
						else:
							raise Exception("Files not in sync")
					else:
						self.sents.append(sent)
						sent = Sentence()
		else:
			with open(goldPath) as gf:
				for line in gf: 
					if line.strip(): # check if lines not empty
						token_tag = re.split(r'\t', line)
						token = Token(token_tag[0], token_tag[1]) # create new Token object
						self.tokens.append(token)
						sent.addToken(token)
					else:
						self.sents.append(sent)
						sent = Sentence()


	def getNumTokens(self):
		return self.numTokens

	def getSents(self):
		return self.sents

	def randomTokens(self):
		random_tokens = shuffle(self.tokens)
        
		return random_tokens

	def getSentStats(self):
		for sent in self.sents:
			token_stats = sent.getTokenStats()
			for tag in token_stats:
				if tag in self.sent_stats:
					self.sent_stats [tag]["TP"] += token_stats[tag]["TP"]
					self.sent_stats [tag]["FN"] += token_stats[tag]["FN"]
					self.sent_stats [tag]["FP"] += token_stats[tag]["FP"]
				else:
					self.sent_stats [tag] = token_stats[tag]
		return self.sent_stats

	def getTags(self):
		for sent in self.getSents():
			for token in sent.getTokens():
				self.tags.update(token.getGoldPOS())
		return self.tags


    	










    
