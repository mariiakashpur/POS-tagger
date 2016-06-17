from __future__ import division
from collections import Counter, defaultdict
import random
import math
from Perceptron import Perceptron



class MulticlassPerceptron(object): 

  def __init__(self, corpus):
    self.perceptrons = {}
    self.intermPerceptrons = {} #BATCH LEARNING
    for tag in corpus.getTags():
      self.perceptrons[tag.strip()] = Perceptron(tag.strip())
      self.intermPerceptrons[tag.strip()] = Perceptron(tag.strip())
    self.corpus = corpus

  @staticmethod
  def getDefaultTag():
    return "NN"

  def getPerceptronFromTag(self, tag):
    return self.perceptrons[tag]

  def getIntermPerceptronFromTag(self, tag):
    return self.intermPerceptrons[tag]

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
      for token in random.sample(sent.getTokens(), len(sent.getTokens())):
        predictedTag = self.getBestTag(token)
        token.setPredictedPOS(predictedTag)
        if predictedTag == token.getGoldPOS():
          continue
        else:
          self.getIntermPerceptronFromTag(predictedTag).reduceWeights(token)
          self.getIntermPerceptronFromTag(token.getGoldPOS().strip()).increaseWeights(token)
    self.perceptrons = self.intermPerceptrons

          # self.getPerceptronFromTag(predictedTag).reduceWeights(token)
          # self.getPerceptronFromTag(token.getGoldPOS().strip()).increaseWeights(token)

  


