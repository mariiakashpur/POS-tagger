from __future__ import division
from collections import Counter, defaultdict
import math
import re
from itertools import izip
from Token import Token
from Sentence import Sentence
from Corpus import Corpus


class Evaluation():
	def __init__(self, Corpus):
		self.Corpus = Corpus

	def evaluate(self):
		CorpEvaluation = {}
		totalFscore = 0
		totalPrecision = 0
		totalRecall = 0
		totalTP = 0
		for tag in self.Corpus.getSentStats():
			totalTP += self.Corpus.getSentStats()[tag]["TP"]
			try:
				precision = self.Corpus.getSentStats()[tag]["TP"] / (self.Corpus.getSentStats()[tag]["TP"] + self.Corpus.getSentStats()[tag]["FP"])
				totalPrecision += precision
				recall = self.Corpus.getSentStats()[tag]["TP"] / (self.Corpus.getSentStats()[tag]["TP"] + self.Corpus.getSentStats()[tag]["FN"])
				totalRecall += recall
				fScore = 2 * precision * recall / (precision + recall)
				totalFscore += fScore
			except ZeroDivisionError:
				precision = 0
				recall = 0
				fScore = 0
			CorpEvaluation[tag] = [precision]
			CorpEvaluation[tag].append(recall)
			CorpEvaluation[tag].append(fScore) 
		MicroEval = totalFscore / len(CorpEvaluation)
		# MacroEval starts here
		averagePrecision = totalPrecision / len(CorpEvaluation)
		averageRecall = totalRecall / len(CorpEvaluation)
		MacroEval =  2 * averagePrecision * averageRecall / (averagePrecision + averageRecall)
		print "MicroEval - ", MicroEval
		print "MacroEval - ", MacroEval
		#tokens_list = Sentence().addToken()
		print tokens_list
		return CorpEvaluation

	def prettyPrint


