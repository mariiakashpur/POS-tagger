from __future__ import division
from collections import Counter, defaultdict
import math
import re

class Token(object): 

  def __init__(self, text, goldPOS, predictedPOS=None):
    """Initializing data structures in the constructor."""
    self.text = text
    self.goldPOS = goldPOS
    self.predictedPOS = predictedPOS
    self.features = self.generateFeatures()

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
    features.append("SUFF2=" + self.getText()[-2:]) # feature suffix - last 2 chars
    features.append("PREF3=" + self.getText()[0:3]) # feature prefix - first 3 chars
    features.append("PREF2=" + self.getText()[0:2]) # feature prefix - first 2 chars
    if re.search(r"^[A-Z]+", self.getText()): # the word written in caps
      features.append("ALLCAP=yes") 
    else:
      features.append("ALLCAP=no")
    if re.search(r"^[A-Z].*", self.getText()): # the word begins with a cap
      features.append("BEGINCAP=yes") 
    else:
      features.append("BEGINCAP=no")
    if re.search(r"^\d+[/.,\d]*$", self.getText()): # the word is a number (CD)
      features.append("DIGIT=yes") 
    else:
      features.append("DIGIT=no")
    return features

  def setPredictedPOS(self, tag):
    self.predictedPOS = tag

  def getFeatures(self):
    return self.features



    
