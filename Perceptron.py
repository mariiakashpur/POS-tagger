from __future__ import division
from collections import Counter, defaultdict
import math

class Perceptron(object): 

  def __init__(self, tag):
    self.featuresWeights = {}
    self.tag = tag

  def getScore(self):
    score = 0.0
    if self.featuresWeights: # not empty dict
      for feature in self.featuresWeights:
        score += self.featuresWeights[feature]
    return score









    
