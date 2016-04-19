from __future__ import division
from collections import Counter, defaultdict
import math, re
from itertools import izip
from Token import Token
from Sentence import Sentence
from Corpus import Corpus


class Result():
	def __init__(self, CorpStats):
		self.CorpStats = CorpStats

	def Evaluation(self):
		CorpEvaluation = {}
		totalFscore = 0
		totalPrecision = 0
		totalRecall = 0
		totalTP = 0
		for tag in self.CorpStats:
			totalTP += self.CorpStats[tag]["TP"]
			try:
				precision = self.CorpStats[tag]["TP"] / (self.CorpStats[tag]["TP"] + self.CorpStats[tag]["FP"])
				totalPrecision += precision
				recall = self.CorpStats[tag]["TP"] / (self.CorpStats[tag]["TP"] + self.CorpStats[tag]["FN"])
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




	#def PrettyPrint(self):
		#for tag in self.CorpStats