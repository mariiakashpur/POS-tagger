<<<<<<< HEAD
class Training(object):
  def __init__(self, algorithm): # algorithm is instance of any algorithm class, e.g. MCP
    self.algorithm = algorithm

  def train(self, numIterations=100):
    for i in range(numIterations):
      self.algorithm.train() # call train method from algorithm


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
=======
from Token import Token
from Sentence import Sentence
from Corpus import Corpus
from Perceptron import Perceptron
from MCP import MulticlassPerceptron


class Training(object):
  def __init__(self, corpus, MCP):
      self.corpus = corpus
      self.MCP = MCP
      # self.eval = self.evaluate() # ensure that all needed variables are set

  def train(self):
    for i in range(100):
      for token in self.corpus.randomTokens():
      	predictedTag = self.MCP.getBestTag(token)
        if predictedTag == token.getGoldPOS():
        	continue
        else:
        	MCP.getPerceptronFromTag(predictedTag).reduceWeights(token)
            MCP.getPerceptronFromTag(token.getGoldPOS).increaseWeights(token)


    
>>>>>>> 1ed2340993c46ee93a48cdaed17f74e2c2a93331
