from Evaluation import Evaluation

class Training(object):
  def __init__(self, algorithm): # algorithm is instance of any algorithm class, e.g. MCP
    self.algorithm = algorithm

  def train(self, numIterations=100):
    for i in range(numIterations):
      self.algorithm.train() # call train method from algorithm

      trainEval = Evaluation(self.algorithm.corpus)
      print trainEval.format()
      self.algorithm.corpus.resetSentStats()





  def predict(self, corpus):
    predictions = []
    for sent in corpus.getSents():
      sentTokens = []
      for token in sent.getTokens():
        sentTokens.append({token.getText(): self.algorithm.getBestTag(token)})
      predictions.append(sentTokens)
    return predictions

  def createOutputFile(self, predictions, predictedPath):
    with open(predictedPath, "w") as f:
      for sent in predictions:
        for token in sent:
          f.write(str(token.keys()[0]) + "\t" + str(token.values()[0]) + "\n")
        f.write("\n")
