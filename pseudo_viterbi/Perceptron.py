from __future__ import division
from collections import Counter, defaultdict
import math
from Token import Token


class Perceptron(object): 

  def __init__(self, tag):
    self.featuresWeights = defaultdict(float)
    self.tag = tag

  def getScore(self, token):
    tokenFeatures = token.getFeatures()
    # print tokenFeatures
    score = 0.0
    if self.featuresWeights: # check if not empty dict
      for tokenFeature in tokenFeatures: 
        if tokenFeature in self.featuresWeights:
          score += self.featuresWeights[tokenFeature]
    return score


  def getTag(self):
    return self.tag

  def increaseWeights(self, token):
    tokenFeatures = token.getFeatures()
    for feature in tokenFeatures:
      self.featuresWeights[feature] += 1

  def reduceWeights(self, token):
    tokenFeatures = token.getFeatures()
    for feature in tokenFeatures:
      self.featuresWeights[feature] -= 1

