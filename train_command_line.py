from Corpus import Corpus
from MCP import MulticlassPerceptron
from Training import Training
import sys

if len(sys.argv) != 3:
	print "Error: Please specify file names as arguments: training file and testing file."
	sys.exit()

training = Training(MulticlassPerceptron(Corpus(sys.argv[1])))# train file
training.train(3, sys.argv[2])# test file

