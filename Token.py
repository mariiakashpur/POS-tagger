from __future__ import division
from collections import Counter, defaultdict
import math

class Token: 

  def __init__(self, text, goldPOS, predictedPOS):
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









    
