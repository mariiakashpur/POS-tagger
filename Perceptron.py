from __future__ import division
from collections import Counter, defaultdict
import math
from Token import Token

class Perceptron(object): 

  def __init__(self, tag):
    self.featuresWeights = defaultdict(float)
    self.tag = tag

  def getScore(self, token):
    tokenFeatures = token.generateFeatures()
    score = 0.0
    if self.featuresWeights: # check if not empty dict
      for feature in self.featuresWeights:
        for tokenFeature in tokenFeatures:
          if feature == tokenFeature:
            score += self.featuresWeights[feature]
    return score

  def getTag(self):
    return self.tag

  def increaseWeights(self, token):
    tokenFeatures = token.generateFeatures()
    for feature in tokenFeatures:
      self.featuresWeights = self.featuresWeights[feature] + 1

  def reduceWeights(self, token):
    tokenFeatures = token.generateFeatures()
    for feature in tokenFeatures:
      self.featuresWeights = self.featuresWeights[feature] - 1



    
