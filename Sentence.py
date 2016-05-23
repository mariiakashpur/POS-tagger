from collections import defaultdict

<<<<<<< HEAD
class Sentence(object):
 
=======
class Sentence(object): 
>>>>>>> 1ed2340993c46ee93a48cdaed17f74e2c2a93331
  def __init__(self):
    self.tokens = []
    self.token_stats = {}

  def addToken(self, token):
    self.tokens.append(token)

  def getTokens(self):
  	return self.tokens

  def getTokenStats(self):
    for token in self.getTokens(): # first iteration to collect all tags in both gold and predicted sent tagging
      gt = token.getGoldPOS()
      pt = token.getPredictedPOS()
      if not gt in self.token_stats:
        self.token_stats[gt] = {"TP":0, "FP":0, "FN":0}
      if not pt in self.token_stats:
        self.token_stats[pt] = {"TP":0, "FP":0, "FN":0}
    for token in self.getTokens():
      gt = token.getGoldPOS()
      pt = token.getPredictedPOS()
      if token.isLabeledCorrectly():
        self.token_stats[gt]["TP"] += 1 # tags coincide
      else:
        self.token_stats[gt]["FN"] += 1 # increment FN counter for gold tag
        self.token_stats[pt]["FP"] += 1 # increment FP counter for predicted tag
    return self.token_stats