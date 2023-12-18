#Pirkko Suihkonen, 2016 and 2017
#Copyright: Pirkko Suihkonen
#
# ADE (-lla/-ll‰)
#
# Agreement in NPs: 
# only one case marking is accepted in the NP:s which contain specifiers and 
# modifiers preceeding the lexical head which is a noun: 
# t‰+ll‰ piene+ll‰ poja+lla. 
#
# The words inside the parentheses contain the combinations <lla> and <ll‰> 
# which are homonymous with the indices of the adessive case 
# (fin.spec, Rule 1.2, ADE-C and adpositions) in Finnish. 
#
# Ambiguous structures:
# sill‰ = CONJ (62), 
# sill‰ = the adessive form of the demonstrative prnouns se.
#
# Nouns:
# Proper nouns, GEN (-n):
ADE-EXCL: ^(((drusilla|priskilla|silla|ulla)|
  ((drusilla|priskilla|silla|ulla)n))(POSS-SFX?CLT-SFX?)|
#
# Common nouns, GEN (-n):
  ((((esi|ilma|kaikki|tuomio|v‰ki|yli)?valla)|
  kulla|mulla|villa)n)(POSS-SFX?CLT-SFX?)|
# 
# Nouns, SG-NOM:
  (helle)(POSS-SFX?CLT-SFX?)|
#
# Adjectives
  (hell‰)(POSS-SFX?CLT-SFX?)|
#
# Verbs:
# Infinitives (V-back, -lla):
  ((ajatel|arvostel|astel|ennustel|harhail|iloitel|katsel|kiroil|
  koetel|kohdel|kuol|kuul|luetel|luul|majail|nuhdel|ol|oleskel|ommel|
  palvel|puhel|puhutel|rakennel|remahdel|rukoil|seurustel|sommitel|
  suositel|suudel|taistel|tavoitel|totel|tul|turmel|tutkistel|uhitel|
  vaellel|valhetel|varjel|viekoitel|voidel|voivotel)la)(CLT-SFX?)|
#
# Infinitives (V-back, -ll‰):
  ((heitel|hypel|k‰yskennel|kierrel|kysel|k‰vel|l‰mmitel|niel|nyˆkytel|
  oleskel|pidel|piileskel|riidel|syleil|vietel|viljel|
  v‰‰ristel|ylv‰stel)l‰)(CLT-SFX?)|
#
# Imperatives and connegatives:
  (kiell‰|sivalla|vaella)(CLT-SFX?)|
#
# Ambiguous (homonyms: infinitive and the adessive form of the 
# demonstrative adjective "sama": samoilla.
#
# Inflected forms:
# V-PRES. 1SG, 1PL:x1:
  ((puhalla|tallaa|uskalla|vaella)(n|mme))(CLT-SFX?)|
  (elle|kiell‰(n|mme))(CLT-SFX?)|
#
# Pass. Pres. (V-back (la-an))
  ((ennustel|huhuil|koetel|kuul|kuulustel|lankeil|nuhdel|ommel|palvel|pudistel|
  raadel|tavoitel|tul|valhetel|varjel|voidel)laan)(POSS-SFX?CLT-SFX?)|
#
# Pass. Pres. (V-front (l‰-‰n))
  ((hyv‰il|viljel|viskel)l‰‰n)
  (POSS-SFX?CLT-SFX?)|
#
# Particles:
  (kyll‰|kyll‰h‰n|kyll‰‰ns‰|kyll‰‰nne|kyll‰‰si|kyll‰si|kyll‰‰ns‰h‰n|
  todella|todellakin|
  v‰h‰ll‰p‰|tahallamme|tahallanne)|
#
# Adpositions taken into account in the file fin.spec:
# ON-POP|PRP-C: 
  (vasten|alla|p‰‰ll‰|partaalla|partailla|pinnalla|
  pohjalla|pohjilla|reunassa|reunoissa|reunalla|reunoilla)
  (POSS-SFX?CLT-SFX?)|
#
#  ON-PRP|POP-D: 
#ON-POP-D: (edess‰|edustalla|ohessa|‰‰ress‰)|
  (h‰nnill‰|j‰ljess‰|juurella|juurilla|kannoilla|kintereill‰|kohdalla|
  keskikohdalla|likell‰|l‰hell‰|luona|niskassa|paikalla|
  per‰ss‰|rinnalla|sivussa|sivuissa|sivulla|sivuilla|suulla|syrj‰ss‰|
  takana|v‰lill‰|vastap‰‰t‰|vieress‰|yll‰)(POSS-SFX?CLT-SFX?))
#
#Conjunction "sill‰", OT and NT:
#SILLA-CONJ: ((, |. |; |: |! |? |' |\" |- )sill‰))
#1. demonstrative "sill‰" in NPs marked with the adessive case:
#  (sill‰ (^@a?b?c?d?e?f?g?h?i?j?k?l?m?n?o?p?q?r?s?t?u?v?w?x?y?z?)ADE)|
#2. except habeo constructions and idioms:
#  (sill‰ (ole|oli|on|tavoin))|
#3. "sill‰" in restrictive relative clauses:
#  (sill‰, (joka|jolla|jonka|mink‰))|
#4. except demonstrative "sill‰" referring to objects mentioned in 
# before in the utteraces or in previous expressions:
#  ((syd‰memme|teot|makaat|maan) sill‰)|
# Lis‰ksi kaikki tapaukset, joissa "sill‰"-sanan ymp‰rill‰ on sanav‰li.
#  ( sill‰ )
