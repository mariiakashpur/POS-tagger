#!/usr/bin/env python

from Token import Token
from Sentence import Sentence
from Corpus import Corpus
from Evaluation import Evaluation
import sys

if len(sys.argv) != 3:
	print "Error: Please specify file names as arguments: gold corpus path and predicted corpus path"
	sys.exit()

print Evaluation(Corpus(sys.argv[1],sys.argv[2])).format() # gold; predicted