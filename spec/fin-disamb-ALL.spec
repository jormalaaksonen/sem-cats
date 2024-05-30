#Pirkko Suihkonen (Copyright), 2016 and 2017
#
#
# ALL (-lle)
#
# Agreement in NPs: 
# only one case marking is accepted in the NP:s which contain specifiers and 
# modifiers preceeding the lexical head which is a noun: 
# t‰+lle piene+lle poja+lle. 
#
# The words inside the parentheses contain the combination <lle> 
# which is homonymous with the indices of the allative case 
# (fin.spec, Rule 1.2, ADE-C and adpositions) in Finnish. 
#
# Nouns:
ALL-EXCL: ^((helle)|
#
# V, POT + PI-NEG: 
  (tullekaan)|
#
# V, INF-II, INST:_
  ((luulle|olle|kuolle|kuulle|tulle)n)|
#
# V, PCPL, PAST, GEN:
  (((kuol|kuul|ol)lee)n)(POSS-SFX?CLT-SFX?)|
#
# ADV: 
  (vaille)|
#
# CONJ (combinations of verbs and conjunctions, 
# called conditional conjunctions):
  (elle(n|t|i|mme|tte|iv‰t))|
  (jolle(n|t|i|mme|tte|ivat))|
#
# DIR-ON-POP-C: 
  (h‰nt‰‰n|juureen|kohtaan|kupeeseen|nen‰‰n|nokkaan|per‰‰n|
  pieleen|pohjaan|p‰‰h‰n|suuhun|syrj‰‰n|varteen|vasten)|
  (alle|p‰‰lle|huipulle|huipuille|partaalle|per‰lle|pohjalle|
  reunalle|
  h‰nt‰‰|juuree|kupeesee|nen‰‰|nokkaa|pohjaa|reunaa)(POSS-SFX?CLT-SFX?)|
#
# DIR-ON-POP-D: 
  (eteen|j‰lkeen|kohdalle|liki|luo|oheen|pieleen|poskeen|sivuun|
  niskaan|per‰‰n|p‰‰h‰n|viereen|suuhun|syrj‰‰n|
  ‰‰relle|edelle|edustalle|h‰nnille|j‰ljille|juurelle|juurille|
  kannoille|kintereille|kupeelle|likelle|l‰helle|luokse|rinnalle|
  sivulle|sivuille|suulle|taakse|tykˆ|vierelle|ylle|yl‰puolelle|
  etee|niskaa|p‰‰h‰|syrj‰‰|vieree)(POSS-SFX?CLT-SFX?))
# Adpositions which do not belong to the groups DIR-ON-PRP-C or DIR-ON-PRP-D:
# ALL-EXCL-ADPOS: 
#  ((ulko|etu|taka|etel‰|pohjois)puolelle)|
#  (keskelle|vierille|kohdalle|v‰lille|ymp‰rille)(POSS-SFX?CLT-SFX?))
#


