from Evaluation import Evaluation
from Corpus import Corpus

class Training(object):
  def __init__(self, algorithm): # algorithm is instance of any algorithm class, e.g. MCP
    self.algorithm = algorithm

  def train(self, numIterations=100, testCorpusPath=None):
    for i in range(1, numIterations + 1):
      self.algorithm.train() # call train method from algorithm
      if i % 10 == 0:
        trainEval = Evaluation(self.algorithm.corpus)
        print "Training evaluation for", i, "iteration(s):\n", trainEval.format()
        self.algorithm.corpus.resetSentStats()
      if testCorpusPath:
        testCorpus = Corpus(testCorpusPath)
        self.setPredictedTags(testCorpus)
        testEval = Evaluation(testCorpus)
        print "Testing evaluation for", i, "iteration(s):\n",testEval.format()
        testCorpus.resetSentStats()


  def setPredictedTags(self, testCorpus):
    for sent in testCorpus.getSents():
      for token in sent.getTokens():
        predictedTag = self.algorithm.getBestTag(token)
        token.setPredictedPOS(predictedTag)
      

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
