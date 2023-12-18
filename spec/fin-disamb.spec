#! /usr/bin/perl -s
#Pirkko Suihkonen, 2016
#Copyright: Pirkko Suihkonen
#
#Sanojen vartaloiden monitulkintaisuuksien eliminointia
#Pirkko Suihkonen, 2015
#Copyright: Pirkko Suihkonen

#Name: Finnish		
#Family: Uralic languages	
#Sub-branch: Baltic-Finnic languages
#code: fin
#
#The rules contain information on vowel harmony rules.
#
#The suffixes which can be located after the case endings:
#1) Possessive suffixes: +n|+si|+mme|+nne|+n|+nsa|+nsÃ¤
#2) Clitic particles: +ko|+kÃ¶|+kin|+kaan|+kÃ¤Ã¤n|+han|+hÃ¤n|+pa|+pÃ¤|+ka|+kÃ¤
#
POSS-SFX-B: (ni|si|mme|nne|an|nsa)
POSS-SFX-F: (ni|si|mme|nne|än|nsä)
POSS-SFX: (POSS-SFX-B|POSS-SFX-F)
CLT-SFX-B: (kin|han|ka|kaan|ko|pa)
CLT-SFX-F: (kin|hän|kä|kään|kö|pä)
CLT-SFX: (CLT-SFX-B|CLT-SFX-F)

PTV-B: (ta|a)
PTV-F: (tä|ä)
PTV: (PTV-B|PTV-F)

INE-B: ssa
INE-F: ssä
INE: (INE-B|INE-F)

ELA-B: sta
ELA-F: stä
ELA: (ELA-B|ELA-F)

ILL-HB: (han|hon|hun|hen|hin)
ILL-HF: (hän|hön|hyn|hen|hin)
ILL-VB: (an|on|un)
ILL-VF: (än|ön|yn)
ILL-SV: (seen|siin)
ILL: (ILL-VB|ILL-VB|ILL-HB|ILL-HF|ILL-SV)

ADE-B: lla
ADE-F: llä
ADE: (ADE-B|ADE-F)

ABL-B: lta
ABL-F: ltä
ABL: (ABL-B|ABL-F)

ALL: lle 

ABE-B: tta
ABE-F: ttä
ABE: (ABE-B|ABE-F)

ESS-B: na
ESS-F: nä
ESS: (ESS-B|ESS-F)

TRL-E: kse
TRL-I: ksi
TRL: (TRL-E|TRL-I)

GEN: (n|den|tten)

INST: in

COM: ne

STEM-B: [aou]
STEM-F: [yäöie]
STEM: (STEM-B|STEM-F)

INF2-B: essa
INF2-F: essä
INF2: (INF2-B|INF2-F)

#(a1)The locative, delocative, and add-locative cases combined with the last stem vowels:

STEM-B: [aeiou](INE-B|ADE-B|ELA-B|ABL-B)
STEM-F: [eiyäö](INE-F|ADE-F|ELA-F|ABL-F)
STEM: ([hjklmnprstv]((a(a))(an|han))|((o(o))(on|hon))|((u(u))(un|hun))|((e(e))(en|hen))|((i(i))(in|hin))((ö(ö))(ön|hön))||((y(y))(yn|hyn))|((ä(ä))(än|hän))

STEM-B: [aeiou](ELA-B|ABL-B)
STEM-F: [eiyäö](ELA-F|ABL-F)

STEM-B: [aeiou](ALL|ILL-HB|ILL-SV)
STEM-F: [eiyäö](ALL|ILL-HF|ILL-SV)
#
#(a2) The locative, delocative, and addlocative cases combined with the stems of verbal nominal forms  (IIIinf, IVinf, and Vinf, and Ipcpl, IIpcpl, and IIIpcpl are treated as dverbal derivational suffixes):

INF2: [e[de|le|ne|re|te]](INE-F|INE-B))
INF3-B: [m(a|i)](INE-B|ADE-B|ELA-B|ILL-VB)
INF3-F: [m(ä|i)](INE-F|ADE-F|ELA-F|ILL-VF)
#
PCPL-PRES-B: [v[a|i]](INE-B|ADE-B|ELA-B|ABL-B|ILL-VB|lALL)
PCPL-PRES-F: [v[ä|i]](INE-F|ADE-F|ELA-F|ABL-F|ILL-VF|ALL)
#
PCPL-PAST-B: [[lnrs]ee]|[[dtlr]u(i)](INE-B|ADE-B|ELA-B|ABL-B|ILL-VB|ALL)
PCPL-PAST-F: [[lnrs]ee]|[dtl|r]y(i)](INE-F|ADE-F|ELA-F|ABL-F|ILL-VF|ALL)
PCPL-PAST-SV: [[lnrs][(ee|ei)]](ILL-SV|ALL)
#
PCPL-AG-B: (ma|mi)(INE-B|ADE-B|ELA-B|ABL-B|ALL|ILL-VB) 
PCPL-AG-F: (mä|mi)(INE-F|ADE-F|ELA-F|ABL-F|ALL|ILL-VF)
#
-v 'huomassa|vallassa|alussa|lopulla|vailla|ymmÃ¤llÃ¤|kanssa|huomasta|sijasta|lopusta|puolesta|hamasta|mukaan|vaille'
