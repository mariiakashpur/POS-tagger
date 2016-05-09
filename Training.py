from Token import Token
from Sentence import Sentence
from Corpus import Corpus
from Perceptron import Perceptron
from MCP import MulticlassPerceptron


class Training(object):
  def __init__(self, corpus):
      self.corpus = corpus
      # self.eval = self.evaluate() # ensure that all needed variables are set

  def train(self):
    for i in range(100):
      for sent in self.corpus.getSents():
        for token in sent.getTokens():
          predictedTag = MCP.getBestTag(token)


# def train(corpus):

# {
#   for i in 0..100 { // for each training iteration
#     for token in corpus.tokens {
#       predictedLabel = mcp.getBestLabel(token) // lets assume: token.goldLabel should be NN but predictedLabel is VB
#       if (predictedLabel == token.getGoldLabel) {
#         // nothing
#       } else {
#         mcp.getPerceptron(predictedLabel).subtractWeights(token)
#         mcp.getPerceptron(token.goldLabel).addWeights(token)
#       }



    
