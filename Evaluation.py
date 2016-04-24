from __future__ import division
from collections import Counter, defaultdict, OrderedDict
import math
from Token import Token
from Sentence import Sentence
from Corpus import Corpus


class Evaluation(object):
	def __init__(self, corpus):
		self.corpus = corpus
		self.stats = self.corpus.getSentStats()
		self.accuracy = 0
		self.macro = 0
		self.micro = 0
		self.eval = self.evaluate() # ensure that all needed variables are set


	def countPrecision(self, tag):
		try:
			precision = self.stats[tag]["TP"] / (self.stats[tag]["TP"] + self.stats[tag]["FP"])
		except ZeroDivisionError:
			precision = 0
		return precision

	def countRecall(self,tag):
		try:
			recall = self.stats[tag]["TP"] / (self.stats[tag]["TP"] + self.stats[tag]["FN"])	
		except ZeroDivisionError:
			recall = 0
		return recall

	def countFscore(self, precision, recall):
		try:
			fScore = 2 * precision * recall / (precision + recall)
		except ZeroDivisionError:
			fScore = 0
		return fScore

	def evaluate(self):
		corpEvaluation = {} 
		totalTP = 0
		totalFP = 0
		totalFN = 0
		totalFscore = 0

		for tag in self.stats:
			totalTP += self.stats[tag]["TP"]
			totalFP += self.stats[tag]["FP"]
			totalFN += self.stats[tag]["FN"]

			precision = self.countPrecision(tag)
			recall = self.countRecall(tag)
			fScore = self.countFscore(precision, recall)


			corpEvaluation[tag] = [precision] # precision under index 0 
			corpEvaluation[tag].append(recall) # recall under index 1
			corpEvaluation[tag].append(fScore) # fscore under index 2
			totalFscore += fScore

		self.accuracy = totalTP / self.corpus.getNumTokens()
		self.macro = totalFscore / len(corpEvaluation) 
		self.micro = self.countFscore(totalTP / (totalTP + totalFP), totalTP / (totalTP + totalFN))

		return corpEvaluation

	def format(self):
		output = "accuracy: %s\nmacroaverage: %s\nmicroaverage: %s\n" % (str(round(self.accuracy, 3)), str(round(self.macro, 3)), str(round(self.micro, 3))) 
		for tag in self.eval:
			output += "%s ==> precision: %s\trecall: %s\tf-score: %s\n" % (tag.strip().ljust(5), str(round(self.eval[tag][0], 3)).ljust(5), 
				                                                          str(round(self.eval[tag][1], 3)).ljust(5), str(round(self.eval[tag][2], 3)).ljust(5))
		return output




