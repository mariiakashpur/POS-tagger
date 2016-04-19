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
		for tag in self.CorpStats:
			try:
				precision = self.CorpStats[tag]["TP"] / (self.CorpStats[tag]["TP"] + self.CorpStats[tag]["FP"])
				recall = self.CorpStats[tag]["TP"] / (self.CorpStats[tag]["TP"] + self.CorpStats[tag]["FN"])
				fScore = 2 * precision * recall / (precision + recall)
			except ZeroDivisionError:
				precision = 0
				recall = 0
				fScore = 0
			CorpEvaluation[tag] = [precision]
			CorpEvaluation[tag].append(recall)
			CorpEvaluation[tag].append(fScore)
		return CorpEvaluation




	#def PrettyPrint(self):
		#for tag in self.CorpStats