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


    
