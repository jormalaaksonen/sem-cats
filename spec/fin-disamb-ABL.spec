#Pirkko Suihkonen, 2016 & 2017
# Copyright: Pirkko Suihkonen
#
# ABL (-lta/-lt‰)
#
# Agreement in NPs: 
# only one case marking is accepted in the NPs which contain specifiers 
# and modifiers preceeding the lexical head which is a noun: 
# t‰+lt‰ piene+lt‰ poja+lta. 
#
# The words inside the parentheses contain the combinations "lta" and "lt‰" 
# which are homonymous with the indices of the ablative case 
# (fin.spec, Rule 2.2, ABL-C and adpositions) in Finnish. 
#
# The ambiguous word forms contain the combinations -lta-/-lt‰ in the stems, 
# or inflected word forms: the partitive forms of nouns and adjectives,
# or verbs containing the derivative suffixes -lta-/-lt‰- which participate 
# in the consonant gradation: vihelt‰‰, polttaa, etc. 
# 
# Nouns and adjectives:
# N, SG-NOM:
ABL-EXCL: ^((ilta|kulta|multa|((kuningas|tuomio|v‰ki)?valta))
  (POSS-SFX?CLT-SFX-B?)|
#
# N, SG-ILL (V-back, -an): 
  (ilta|kulta|multa|((kuningas|tuomio|v‰ki)valta)an)
  (POSS-SFX?CLT-SFX-B?)|
#
# N-SG-PTV (V-back; -ta):
  ((((juudan|asdodin|aramin)?kiel)|kyynel|miel|((pihti)?piel)|syl|tiil)t‰)
  (POSS-SFX?CLT-SFX-F?)|
#
# N-SG-PTV (V-front; -t‰):
  ((((‰iti|etel‰|etu|l‰nsi|loppu|miehen|pohjois|riita|sis‰)?puol)|
  huol|kannel|nuol|taival|tul|((it‰)?tuul))ta)(POSS-SFX?CLT-SFX-B?)|
#
# N, SG-GEN (V-back, -n):
  ((vaskialtaa|telta)n)(CLT-SFX-B?)|
#
# Verbs (stem: -ta, -t‰):
  ((v‰lt‰|malta|polta|(valta(si)?))(n|t|mme|tte))(CLT-SFX-B?)|
  ((puhalta|suojelta|vaelta|tulta)(ko|en))|((kielt‰)kˆ)|
  (malta|polta|v‰lt‰)(CLT-SFX-B?)|
#
# Verbs (INFII, Instructive (INST): -s-tan):
  (((edus|haas|julis|lois|omis|paljas|puhdis|raas|ratsas|ripus|
  tarkas|tunnus|vahvis)ta)en)|
#
# Verbs (INFII, Instructive (INST): -st‰-en):
  (((ryˆs|s‰‰s|s‰es|v‰is|ylis)t‰)en)|
#
# Particles:
  (kauttaaltaan|lopulta)(CLT-SFX-B?)|
#
# Adpositions:
# DE-ON-PRP|POP-C:
  (((a|huipu|huipui|kupee|lae|partaa|pohja|reuna)lta)|
  ((juure|kohda|kupee|noka|pohja|reuna|varre|varsi)sta)|
  ((p‰‰|per‰)lt‰)|((h‰nn‰|nen‰)st‰))(POSS-SFX?CLT-SFX-B?)|
#
# DE-ON-PRP|POP-D:
  (((edusta|juure|juuri|kannoi|kohda|lae|pinna|sivu|suu)lta)|
  ((‰‰re|ede|viere)(lt‰|st‰))|
  ((h‰nni|j‰lji|kinterei|like|l‰he|p‰‰|viere|y)lt‰)|
  ((ohe|niska|poske|sivu)sta)|
  ((j‰lje|per‰|piele|syrj‰)st‰)|
  (takaa))(POSS-SFX?CLT-SFX?))
# Adpositions containing the strings -lta/-lt‰, but which do not belong to the groups C and D:
#  (((puo(le)?)|suunna|taho|varre|varsi)lta)(POSS-SFX?CLT-SFX-B?)|
#  ((keske|peri|sis‰|v‰li|ymp‰ri)lt‰)(POSS-SFX?CLT-SFX-F?))
