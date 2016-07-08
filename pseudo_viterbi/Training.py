from Evaluation import Evaluation
from Corpus import Corpus
import re

class Training(object):
  def __init__(self, algorithm): # algorithm is instance of any algorithm class, e.g. MCP
    self.algorithm = algorithm

  def train(self, numIterations=100, testCorpusPath=None):
    if testCorpusPath:
      testCorpus = Corpus(testCorpusPath)
    for i in range(1, numIterations + 1):
      self.algorithm.train() # call train method from algorithm
      if i % 10 == 0:
        trainEval = Evaluation(self.algorithm.corpus)
        print "Training evaluation for", i, "iteration(s):\n", trainEval.format()
        self.algorithm.corpus.resetSentStats()
        if testCorpusPath:
          self.setPredictedTags(testCorpus) 
          #self.createOutputFile(testCorpus)
          testEval = Evaluation(testCorpus)
          print "Testing evaluation for", i, "iteration(s):\n",testEval.format()
          testCorpus.resetSentStats() # !!! we can use prototype pattern(so we don't need to loop through sents): here testCorpus = testCorpus.getPrototype() and in Corpus::__init__ : self.prototype = self (google : python prototype)?
          # if i == numIterations:
          #   testEval.mistagedTokens()

  def setPredictedTags(self, testCorpus):
    for sent in testCorpus.getSents():
      for token in sent.getTokens():
        if token.getPrev() == "prevnotekzist":
          PairedPredictedTag = self.algorithm.getBestTag(token)
        else:
          PairedPredictedTag = self.algorithm.getBestTag(token, EndPredictedTag)
        EndPredictedTag = ''.join(re.findall(r"(/.+)", PairedPredictedTag)).strip("/")
        BeginPredictedTag = ''.join(re.findall(r"(.+/)", PairedPredictedTag)).strip("/")
        if EndPredictedTag == "#end":
          token.setPredictedPOS(BeginPredictedTag)
        else:
          token.setPredictedPOS(EndPredictedTag)

  def createOutputFile(self, corpus):
    with open("Tagged_viterbi.txt", "w") as f:
      for sent in corpus.getSents():
        for token in sent.getTokens():
          f.write(str(token.text) + "\t" + str(token.predictedPOS) + "\n")
          f.write("\n")


      

  # def predict(self, corpus):
  #   predictions = []
  #   for sent in corpus.getSents():
  #     sentTokens = []
  #     for token in sent.getTokens():
  #       sentTokens.append({token.getText(): self.algorithm.getBestTag(token)})
  #     predictions.append(sentTokens)
  #   return predictions

  # def createOutputFile(self, predictions, predictedPath):
  #   with open(predictedPath, "w") as f:
  #     for sent in predictions:
  #       for token in sent:
  #         f.write(str(token.keys()[0]) + "\t" + str(token.values()[0]) + "\n")
  #       f.write("\n")
