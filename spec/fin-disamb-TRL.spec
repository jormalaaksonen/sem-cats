#Pirkko Suihkonen (Copyright), 2016 and 2018
#
#
#TRL (-kse/ksi)
#
# The words in the group N-LEX conatin words in which the combination
# "kse|ksi" is found in the word stems in the nomintive and illative forms,
# and in some particles which are leksicalized forms of word forms
# representing different classes of parts of speecn. 
#
# N-LEX: 
TRL-EXCL: ^((yksi|kaksi|kahdeksan|kahdeksaan|yhdeksän|yhdeksään|
  yksitoista|kaksitoista|kahdeksantoista|kahdeksaantoista|yhdeksäntoista|
  yhdeksääntoista|yksinäinen|kaksinainen|
  erikseen|eriksensä|itsekseen|itseksensä)|
#
# The combinations "kse|ksi" occur also in the genitive and illative forms
# of nouns ending with -s in the nominative form (asumus, kiusaus, etc.): 
#
  (((asumu|jeesu|kadotu|keräy|kiusau|kristu|lupau|pyhity|rangaistu|
  rikkomu)(kse|ksi)(n|en|in))(POSS-SFX?CLT-SFX?)))
#









