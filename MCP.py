from __future__ import division
from collections import Counter, defaultdict
from random import shuffle
import math
from Perceptron import Perceptron



class MulticlassPerceptron(object): 

  def __init__(self, corpus):
    self.perceptrons = {}
    for tag in corpus.getTags():
      self.perceptrons[tag.strip()] = Perceptron(tag.strip())
    self.corpus = corpus

  @staticmethod
  def getDefaultTag():
    return "NN"

  def getPerceptronFromTag(self, tag):
    return self.perceptrons[tag]

  def getBestTag(self, token):
    currentBestScore = 0.0
    currentBestTag = self.getDefaultTag()
    for perceptron in self.perceptrons:
      if self.perceptrons[perceptron].getScore(token) > currentBestScore:
        currentBestScore = self.perceptrons[perceptron].getScore(token)
        currentBestTag = self.perceptrons[perceptron].getTag()
    return currentBestTag

  def train(self):
    for sent in self.corpus.getSents():
      for token in sent.getTokens():
        predictedTag = self.getBestTag(token)
        token.setPredictedPOS(predictedTag)
        if predictedTag == token.getGoldPOS():
          continue
        else:
          self.getPerceptronFromTag(predictedTag).reduceWeights(token)
          self.getPerceptronFromTag(token.getGoldPOS().strip()).increaseWeights(token)

  


