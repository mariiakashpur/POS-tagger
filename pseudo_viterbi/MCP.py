from __future__ import division
from collections import Counter, defaultdict
import random
import math
from Perceptron import Perceptron
from Corpus import Corpus
from Token import Token
import re
import random



class MulticlassPerceptron(object): 

  def __init__(self, corpus):
    self.perceptrons = {}
    #self.intermPerceptrons = {} #BATCH LEARNING
    for tag in corpus.getPairedTagsCorpus(): #corpus level
    # for tag in corpus.getPairedTagsSent(): #sentence level
      self.perceptrons[tag] = Perceptron(tag)
      #self.intermPerceptrons[tag] = Perceptron(tag)
    self.corpus = corpus

  #@staticmethod
  def getDefaultTag(self):
    perceptronsKeys = self.perceptrons.keys()
    return random.choice(perceptronsKeys)

  def getPerceptronFromTag(self, tag):
    return self.perceptrons[tag]

  # def getIntermPerceptronFromTag(self, tag):
  #   return self.intermPerceptrons[tag]

  def getBestTag(self, token, PrevTagEnd=None):
    currentBestScore = 0.0
    if PrevTagEnd:
      currentBestTag = self.getDefaultTag()
      for perceptron in self.perceptrons:
        perceptronTag = self.perceptrons[perceptron].getTag()
        # "or" statement needed for sentence level only
        if ''.join(re.findall(r"(.+/)", perceptronTag)).strip("/") == PrevTagEnd: #or (PrevTagEnd == "#end" and ''.join(re.findall(r"(.+/)", perceptronTag)).strip("/") == "#begin"):
          if self.perceptrons[perceptron].getScore(token) > currentBestScore:
            currentBestScore = self.perceptrons[perceptron].getScore(token)
            currentBestTag = perceptronTag

    else:
      currentBestTag = "#begin/" + token.getGoldPOS()
      for perceptron in self.perceptrons: 
        if self.perceptrons[perceptron].getScore(token) > currentBestScore:
          currentBestScore = self.perceptrons[perceptron].getScore(token)
          currentBestTag = self.perceptrons[perceptron].getTag()

    return currentBestTag

  def train(self):
    for sent in self.corpus.getSents():
      for token in sent.getTokens():
        if token.getPrev() == "prevnotekzist":
          predictedTag = self.getBestTag(token)
        else:
          predictedTag = self.getBestTag(token, EndPredictedTag)
        EndPredictedTag = ''.join(re.findall(r"(/.+)", predictedTag)).strip("/")
        BeginPredictedTag = ''.join(re.findall(r"(.+/)", predictedTag)).strip("/")
        if EndPredictedTag == "#end":
          token.setPredictedPOS(BeginPredictedTag)
        else:
          token.setPredictedPOS(EndPredictedTag)
        if  EndPredictedTag == token.getGoldPOS():
          continue
        else:
          #self.getIntermPerceptronFromTag(predictedTag).reduceWeights(token)
          self.getPerceptronFromTag(predictedTag).reduceWeights(token)
          oppositeTag = BeginPredictedTag + "/" + token.getGoldPOS().strip()
          if oppositeTag in self.perceptrons.keys(): # to avoid the situation when perceptron for some tag doesn't exist
            #self.getIntermPerceptronFromTag(oppositeTag).increaseWeights(token)
            self.getPerceptronFromTag(oppositeTag).increaseWeights(token)
    # self.perceptrons = self.intermPerceptrons

          # self.getPerceptronFromTag(predictedTag).reduceWeights(token)
          # self.getPerceptronFromTag(token.getGoldPOS().strip()).increaseWeights(token)

  


