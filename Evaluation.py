from __future__ import division
from collections import Counter, defaultdict
import math
import re
from itertools import izip
from Token import Token
from Sentence import Sentence
from Corpus import Corpus


class Evaluation(object):
	def __init__(self, Stats):
		self.corpus = Corpus("dev.col","dev-predicted.col") # STUPID, BUT WORKS :)
		self.Stats = Stats

	def precision(self, tag):
		try:
			precision = self.Stats[tag]["TP"] / (self.Stats[tag]["TP"] + self.Stats[tag]["FP"])
		except ZeroDivisionError:
			precision = 0
		return precision

	def recall(self,tag):
		try:
			recall = self.Stats[tag]["TP"] / (self.Stats[tag]["TP"] + self.Stats[tag]["FN"])	
		except ZeroDivisionError:
			recall = 0
		return recall

	def fscore(self, precision, recall):
		try:
			fScore = 2 * precision * recall / (precision + recall)
		except ZeroDivisionError:
			fScore = 0
		return fScore

	def evaluate(self):
		CorpEvaluation = {}
		totalFscore = 0
		totalPrecision = 0
		totalRecall = 0
		totalTP = 0
		for tag in self.Stats:
			totalTP += self.Stats[tag]["TP"]
			precision  = self.precision(tag)
			totalPrecision += precision
			recall = self.recall(tag)
			totalRecall += recall
			fScore = self.fscore(precision, recall)
			totalFscore += fScore
			CorpEvaluation[tag] = [precision]
			CorpEvaluation[tag].append(recall)
			CorpEvaluation[tag].append(fScore)
		#print self.Stats
		MicroEval = totalFscore / len(CorpEvaluation)
		# MacroEval starts here
		averagePrecision = totalPrecision / len(CorpEvaluation)
		averageRecall = totalRecall / len(CorpEvaluation)
		MacroEval =  2 * averagePrecision * averageRecall / (averagePrecision + averageRecall)
		
		accuracy = totalTP / self.corpus.getNumTokens()
		print accuracy
		print "MicroEval - ", MicroEval
		print "MacroEval - ", MacroEval
		return CorpEvaluation

	#def prettyPrint


