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
    self.features = []
    self.selfFeatures = []
    self.generateFeatures()

  def getText(self):
    return self.text

  def getGoldPOS(self):
    return self.goldPOS

  def getPredictedPOS(self):
    return self.predictedPOS

  def isLabeledCorrectly(self):
    return self.goldPOS == self.predictedPOS

  def setPrev(self, prev):
    self.prev = prev

  def getPrev(self):
    return self.prev 

  def setFollowing(self, following):
    self.following = following

  def getFollowing(self):
    return self.following 

  def generateFeatures(self):
    self.features.append("W=" + self.getText()) # feature word itself
    self.features.append("SUFF3=" + self.getText()[-3:]) # feature suffix - last 3 chars
    self.features.append("SUFF2=" + self.getText()[-2:]) # feature suffix - last 2 chars
    self.features.append("PREF3=" + self.getText()[0:3]) # feature prefix - first 3 chars
    self.features.append("PREF2=" + self.getText()[0:2]) # feature prefix - first 2 chars
    if re.search(r"^[A-Z]+$", self.getText()): # the word written in caps
      self.features.append("ALLCAP=yes") 
    else:
      self.features.append("ALLCAP=no")
    if re.search(r"^[A-Z].*", self.getText()): # the word begins with a cap
      self.features.append("BEGINCAP=yes") 
    else:
      self.features.append("BEGINCAP=no")
    if re.search(r"^\d+[/.,\d]*$", self.getText()): # the word is a number (CD)
      self.features.append("DIGIT=yes") 
    else:
      self.features.append("DIGIT=no")
    # create another variable for current token's features only; to avoid multiple appending of neighbors' features in getNeighborFeatures
    self.selfFeatures += self.features

  def getSelfFeatures(self):
    return self.selfFeatures

  def getNeighborFeatures(self):
    prev = self.getPrev()
    following = self.getFollowing()
    if type(prev) != str:
       for feature in prev.getSelfFeatures():
        newFeature = feature + "-1"
        self.features.append(newFeature)
    if type(following) != str:
      for feature in following.getSelfFeatures():
        newFeature = feature + "+1"
        self.features.append(newFeature)



    # if type(prev) == str:
    #   prevWord = prev
    # else:
    #   prevWord = prev.getText()
    # features.append("W-1=" + prevWord) # previous word

    # if type(following) == str:
    #   followingWord = following
    # else:
    #   followingWord = following.getText()
    # features.append("W+1=" + followingWord) # following word






  def setPredictedPOS(self, tag):
    self.predictedPOS = tag

  def getFeatures(self):
    return self.features



    
