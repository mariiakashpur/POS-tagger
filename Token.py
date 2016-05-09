from __future__ import division
from collections import Counter, defaultdict
import math

class Token(object): 

  def __init__(self, text, goldPOS, predictedPOS=None):
    """Initializing data structures in the constructor."""
    self.text = text
    self.goldPOS = goldPOS
    self.predictedPOS = predictedPOS

  def getText(self):
    return self.text

  def getGoldPOS(self):
    return self.goldPOS

  def getPredictedPOS(self):
    return self.predictedPOS

  def isLabeledCorrectly(self):
    return self.goldPOS == self.predictedPOS

  def generateFeatures(self):
    features = []
    features.append("W=" + self.getText()) # feature word itself
    features.append("SUFF3=" + self.getText()[-3:]) # feature suffix - last 3 chars
    return features






    
