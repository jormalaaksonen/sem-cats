#
# Pirkko Suihkonen, 2006-2008, 2014, 2016-2017.
# Copyright: Pirkko Suihkonen
#
# Name of the language: Finnish		
# Family: Uralic languages	
# Sub-branch: Baltic-Finnic languages
# code: fin
#
# The name of the project: 
# The ADPOS-CASE categories in Finnish and English 
# The main goal of the project: 
# Comparative research of English and Finnish ADPOS-CASE relators
# (final version: 2017).
# The Perl scripts for the analysis of the database, and also comments 
# on the guidelines of the Regular Expressions: Jorma Laaksonen.
# 
# Referenes:
# Hakulinen 1968, Hakulinen & Karlsson 1979, Karlsson 1983, 
# Koskenniemi 1983, Laaksonen & Lieko 1998, Penttilä 1963, 
# Setälä 1970, & Tuomi (ed.) 1980.
# Iivonen, Antti, Mari Horppila, Miika Heikkonen & Olli Rissanen (eds). 2000.
# Fonetiikan perussanasto. Helsingin yliopisto. 
# https://helda.helsinki.fi/bitstream/handle/10224/3513/index.htm. (2016)
# Iivonen, Antti. 2000. Suomen fonetiikka (Phonetics of Finnish). 
# Web editor: Mietta Lennes. 
# www.helsinki.fi/puhetieteet/projektit/Finnish_Phonetics/hankekuvaus_eng.htm.
# (2016)
# On the references: see also the document Suihkonen & Laaksonen 2017: 
#
#
# THE RULES FOR THE ANALYSIS OF THE DATABASE
#
# The LENCA-projcet, Finnish (Suihkonen 2015):
# DIATHESIS:        ACT & PASS & RPASS & REFL & CAUS & ACAUS & SNTH & ANAL
# MOOD: 	    IND & IMP & IMP-OPT & POT & COND & EVID-ANA & INT-ANA & 
#  		    OBL-ANA & NARR-ANA
# TENSE: 	    PRES-SNTH & FUT-ANA & IMPRF & PERF & PLU-PERF
# ASPECT: 	    PRG-ANA & HAB-ANA & ITR-SNTH & PNCT-SNTH & SEMF-SNTH &
# 		    INGR-ANA & TRM-ANA & DUR-SNTH
#
# Grammar
# I. Phonology 
# 1. The sound system
#
#1.1. Consonants and consonant combinations (the letters marking
# consonants and consonant combinations)
# (consonant gradation: C-SGR = strong grade, C-WGR = weak grade):
C: (b|c|d|f|g|h|j|k|l|m|n|p|r|s|t|v)
CC: (hd|hj|hk|hl|hm|hn|hr|ht|hv|kk|kl|kr|ks|lh|lj|lk|ll|lm|lp|ls|lt|lv|mm|mp|
  nh|nn|ns|nt|nk|ng|pl|pr|pp|ps|rh|rj|rk|rm|rn|rp|rr|rs|rt|rv|sb|sk|sl|sm|sp|
  ss|st|sv|tj|tk|tr|ts|tt|tv)
CCC: (kst|ktr|ltr|mbr|mpl|mpr|mpt|ndr|nkr|nkt|nsl|ntr|rkt|skr|str|htr|ksl|
  lfr|lpt|lsn|lsp|mbl|mfl|ndh|nkm|nsn|nsv|ntl|ntn|ngsk|ptr|rnj|rpr|rpt|rsl|
  rtn|rtr|skv|spl|spr|stm|tsl|ksm|kts|lsm|ntg|ntv|pts|rdv|rkm|rks|rmj|rml|
  rnh|rrnh|tsk|tst|bsk|bst|btr|ksh|ksk|ksp|ksv|mph|nfl|nkl|nkv|nsf|nsm|nsp|
  psl|rgl|rkl|rkr|rpl|rsp|rsr|skv|std|stf|sth|stj|stp|sts|lkk|ltt|lss|nkk|
  ntt|nss|rkk|rtt|rss|rst)
C-SGR: (tt|kk|pp|mp|nt|nk|p|t|k|lt|rt|lke|rke|hke)
C-WGR: (t|k|p|mm|nn|nn|v|d|g|ll|rr|lje|rje|hje)
C-GRAD: (C-SGR|C-WGR)
C-S: (l|n|r)
#
#1.2. Vowels
# Single vovels (B = back, F = front, EI = the vowels e and i);
VB: (a|o|u)
VF: (y|ä|ö)
VEI: (e|i)
V: (VB|VF|VEI)
#
# Diphtongs (I = the diphtongs ending with i):
DIPH-B: (au|uo|ou|eu|iu|ia)
DIPH-F: (äy|yö|öy|ey|iy|ie)
DIPH-I: (yi|öi|äi|ui|oi|ai|ei)
DIPH: (DIPH-B|DIPH-F|DIPH-I)
#
# Long vowels (L = long vowel, VEI-L = long e and i, 
# VI-PL = long i (ii)):
VB-L: (aa|oo|uu)
VF-L: (yy|ää|öö)
VEI-L: (ee|ii)
VI-PL: (ii)
VL: (VB-L|VF-L|VEI-L|VI-PL)
#
# 2. The structure of syllables
#
# SYLL-VB = a syllable consisting of single back vowel,
# SYLL-VF = a syllable consisting of single front vowel,
# SYLL-VV = a syllable consisting of diphtongs or long vowels marked with
#           two vowels, 
# SYLL-CVB = a syllable consisting of a consonant and a back vowel, 
# SYLL-CVF = a syllable consisting of a consonant and a front vowel,
# SYLL-CVV = a syllable consisting of a consonant and a long vowel or 
#            a diphtong,
# SYLL-VC = a syllable consising of a vowel and  a consonant,
# SYLL-VVC = a syllable consisting of two vowels and a consonant, 
# SYLL-VCC = a syllable consisitng of a vowel and two consonants,
# SYLL-CVC = a syllable consisitng of a consonant, a vowel and a consonant,
# SYLL-CVVC = a syllable consisting of a consonant, two vowels, 
#             and a consonant,
# SYLL-CVCC = a syllable consisting of a consonant, a vowel, 
#             and two consonants.
# (strong open syllable (SYLL-OP-ST) and weak open syllable (SYLL-OP-W)):
#
# Syllables, examples:
# a:    apu:    SYLL-V: \w(V)
# aa:   aamu:   SYLL-VV: \w(V()V)
# ka:   katu:   SYLL-CV: \w(C()V)
# kaa:  kaatuu: SYLL-CVV: \w(C()V()V)
# ak:   akka:   SYLL-VC: \w(V()C)
# ais:  aisti:  SYLL-VVC: \w(V()V()C)
# ark:  arkki:  SYLL-VCC: \w(V()C()C)
# kuk:  kukka:  SYLL-CVC: \w(C()V()C)
# laak: laakso: SYLL-CVVC: \w(C()V()V()C)
# kars: karski: SYLL-CVCC: \w(C()V()C()C)
#
SYLL-VB: \w(VB)
SYLL-VF: \w(VF)
SYLL-VV: \w(VL|DIPH)
SYLL-CVB: \w(C()VB)
SYLL-CVF: \w(C()VF)
SYLL-CVV: \w(C()(VL|DIPH))
SYLL-VC: \w(V()C)
SYLL-VVC: \w(V()V()C)
SYLL-VCC: \w(V()C()C)
SYLL-CVC: \w(C()V()C)
SYLL-CVVC: \w(C()(VL|DIPH)()C)
SYLL-CVCC: \w(C()V()C()C)
SYLL-OP: \w(SYLL-VB|SYLL-VF|SYLL-VV|SYLL-CVB|SYLL-CVF|SYLL-CVV)
SYLL-CL: \w(SYLL-VC|SYLL-VVC|SYLL-VCC|SYLL-CVC|SYLL-CVVC|SYLL-CVCC)
SYLL: \w(SYLL-OP|SYLL-CL)
#
#
# 3. The stress on the word-level (the principal stress rules)
#
# STRSS-P = the principal stress on the first syllable;
# STRSS-S = the secondary stress on the third/pairless syllables; 
# STRSS-PS = a stressed syllable;
# STRSS-NS = a non-stressed syllable;
# the second and the fourth syllables are unstressed;
# STRSS-NS-D = an unstressed syllable containing a diphthong;
# STRSS-NS-L = an unstressed syllable containing a long vowel; 
# STRSS-NS-S = an unstressed syllable containing a short vowel.
# STRSS-NS-V = an unstressed syllable containing a short or long vowel; 
# 
STRSS-P: \w(SYLL)
STRSS-S: \w(SYLL()SYLL()SYLL)
STRSS-NS: \w((SYLL()SYLL)|(SYLL()SYLL()SYLL()SYLL)|
  (SYLL()SYLL()SYLL()SYLL()SYLL()SYLL))
STRSS-PS: \w((SYLL)|(SYLL()SYLL()SYLL))
STRSS-NS-D: \w((SYLL)?()(C)?DIPH)
STRSS-NS-L: \w((SYLL)?()(C)?VL)
STRSS-NS-S: \w((SYLL)?()(SYLL-CVB|SYLL-CVF))
#
#
# 4. Lexicon and morphology 
# 4.1. Stem types of nouns
#
# The stem types: (a) consonant stems and (b) weak and (c) strong vowel stems.
# a) Consonant stems: consonant stems: vet+tä.
#    Strong and weak vowel stems: the stem participates in consonant gradation.
# b) Weak vowel stem: vesi - vede+n;  
# c) Strong vowel stem: vesi - vete+nä;
# A number of words have only vowel stems: 
# kissa - kissa+n - kissa+na, pullo - pullo+n - pullo+a.
#
# When the stem types are counted by distinguishing the consonant stems 
# and different types of vowel stems, the number of stem types is three.
# This classification concerns both nouns and verbs. 
# When more varieties of in stems is taken into account, the number of
# stem types is 20. According to more specific descriptions,
# the number of stem types of nouns is even 82,
# and the number of stem types of verbs is 22  
# (Nykysyomen sanakirja; Laaksonen & Lieko 1998: 30).
# 
# STEM-C = consonant stem, 
# STEM-V = vowel stem, 
# STEM-V-B = stem consisting of back vowels and e and i, 
# STEM-V-F = stem consisting of front vowels and e and i.
# STEM-V-S = strong vowel stem,
# STEM-V-V = unchangeable vowel stem.
#
STEM-C: \w(SYLL-CL) 
STEM-V: \w(SYLL-OP)
STEM-V-B: \w(VB|VEI)
STEM-V-F: \w(VF|VEI)
STEM-V-S: \w((k|p|t)()V)
STEM-V-V: \w(V()V)
STEM-N: \w(STEM-V-B|STEM-V-F|STEM-C|STEM-V|STEM-V-S|STEM-V-V)
#
# Stems of nouns: more detailed descriptions:
# talo: talo+n, kissa: kissa+n, 
STEM-AOU: \w((C|CC)(a|ä|o|ö|u|y))
# tunti: tunti+a, tunni+n, vartti: varti+n, vartti+a 
STEM-I: \w((C|CC|CCC)i)
# kivi: kive+n, lahti: lahde+n, lahte+a
STEM-IE: \w(((C|CC|CCC)(i|e)))
# kieli: kiele+n, kiel+tä, ääni: ääne+n, ään+tä
STEM-VVC-S: w(((V)()(V)()C-S)(i|e))
# vesi: vede+n, vet+tä
STEM-TI: \w(((e|äi)()(s|rs|d|rr|t|rt))(i|e))
# paras: pare+mpi
STEM-MPI: \w(e(mpi|mpa|mpä|mma|mmä))
# vene: venee+n
STEM-EK: \w(ee|et)
# nalle: nalle+n, nalle+i+n
STEM-E: \w(ke|le)
# ihminen: ihmistä
STEM-NEN: \w(nen|se|s)
# ajatus: sajatukse+n, ajatus+ta
STEM-KSE: \w(s|kse)
# taivas: taivaa+n, taivas+ta
STEM-A: \w(s|as)
# rikkaus: rikkaude+n
STEM-DE: \w(s|de|te|t)
# kolmas: kolmanne+n, kolmat+ta, kolmante+na, kolmans+i+a
STEM-NNE: \w(s|t|nne|nte|ns)
# avain: avaime+n, avain+ta
STEM-ME: \w(n|me)
# huoleton: huolettoma+n
STEM-TON: \w(n|ttoma|ttomä)
# suurin: suurimpa+na, suurimma+ksi
STEM-MM: \w(n|mpa|mma|mpä|mmä)
# askel: askele+n, manner: mantere+n
STEM-LE: \w(n|le|ne|re)
# Vartalo suljettu tilapäisesti.
# ol+lut: ol+lee+n
STEM-EE: \w(t|ee)
# olut: olue+n
STEM-UT: \w(ut|yt|ue|ye)
# kevät: kenää+n, mies: miehe+n
STEM-AT: \w(ät|ää|es|ehe)
#
# 4.2. Stem types of verbs
#
# The number of stem types of verbs: seven.
# 
# a) sano+va, laula+va; open syllable with one vowel,
STEM-VA: \w((SYLL)()(C)()(V))
# b) Contracted verbs: katket+a: katkes+i, maalat+a: maalas+i+n,
STEM-CONTR: \w((C)()(V)()(C))
# ITA: havait+a: havaitse+n, tarvit+a: tarvitse+n
STEM-ITA: \w((it)|(in)|(itse))
# ETA: kylmet+ä: kylmene+e, kalvet+a: kalpene+i
STEM-ETA: \w((et|((e)ne)))
# DA-I-verbs: saa+da: saan, vie+dä: vie+n,
STEM-DA-I: \w((VL)|(DIPH))
# DA-II-verbs: tupakoi+da: tupakoi, tupakoi+t, havainnoi+da: havainnoi+n
STEM-DA-II: \w((i|u|b|d|k|l|m|n|p|s|t|v)(oi|öi)) 
# STA-, LA-, NA-, RA-verbs: nous+ta: nouse+n, juos+ta: juokse+n,
# tul+la: tule+t, men+nä: mene+vät, pur+ra: pure+e
# nous+ta: nouse+e
# SE: \w((s(e)))
# 
STEM-LA-NA-RA-SE: \w((l|n|r|s)(e))
#
STEM-VOW: (STEM-VA|STEM-CONTR|STEM-ITA|STEM-ETA|STEM-DA-I|STEM-DA-II|
  STEM-LA-NA-RA-SE)
#
# i) the verbs which consist of two- or three syllables, and 
# which have the vowel stem ending with long -a/-ä formed with- aa/-ää
# or with a vowel and -a/-ä (([a|o|u]a)|([y|ä|ö|e|i]ä));
# ii) the two-syllabic words ending with the combinations ([k|n|r|s]e)).
#
#
# II. Morphology and Lexicon
# 
# The parts of speech system in Finnish consists of nons, andjectives,
# pronouns, numerals (all together nominal)s, verbs and particles. 
# All of them contain several subgroups. Nouns, adjectives and verbs
# can be called open classes, because they accept relatively easily
# new members. New members are also accept to particles, but the 
# number of those which can be called lexical formatives: pronouns, 
# numerals and adpositions, is more stone-fixed.
#  
# II. Nominal morphology
#
# 1. Number
#
# The numbers are singular and plural. 

# Singular: singular is unmarked. 
#
# Plural: 
#
PL-T: (V()t)
PL-J: (V()j()(a|ä|en))
PL-JP: (V()j()(a|ä|e))
PL-I: ((C|V)()i)
PL: (PL-T|PL-J|PL-JP|PL-I)
#
# PL-T: +t in the nominative form, 
# PL-J: +j+ before the plural genitive -en and the partitive endings -a and -ä,
# PL-JP: -j- before -a, -ä, and-e,
# PL-I: in all the other cases.
# 
#
# 2. Possession marking
#
# Possession in Finnish is expressed with genitive forms of personal
# and interrogative pronouns and possessive suffixes. The syntactic
# position of the pronouns marking possession has influence on the use of
# possessive suffixes with the pronominal marking of possession.  
#
POSS-C: (minun|sinun|hänen|meidän|teidän|heidän|kenen|keiden|minkä)
#
# Possessive suffixes
# The suffixes which are loated after the case endings:
# +ni|+si|+mme|+nne|+nsa|+nsä|an|än|en
#
POSS-SFX-B: \w(ni|si|mme|nne|an|nsa|en)
POSS-SFX-F: \w(ni|si|mme|nne|än|nsä|en)
POSS-SFX: \w(POSS-SFX-B|POSS-SFX-F)
POSS-SFX-BV: \w(ni|si|mme|nne|nsa)
POSS-SFX-FV: \w(ni|si|mme|nne|nsä)
POSS-SFX-V: \w(POSS-SFX-BV|POSS-SFX-FV)
#
# 1.3. Structural means for developing and modifying lexicon
# 
# In Finnish, affixation forms the main means in developing and modifying
# lexicon. Suffixes are used in developing and generating differences in  
# meanings of words, and grammatical suffixes are used in specifying the
# relations of words in the contexts. Finnish has also some prefixes.
# such as ei-, epä-, oma-, etc. A special method in forming compounds 
# are the shortened word forms called “casus componens”: ihminen + kunta 
# => ihmis#kunta. Clitic particles are used in particular in adjusting 
# utterances in eventualities. Also lexical particles have an important 
# function in modifying predicates and utterances in general.
# 
# 1.3. Prefixes in word formation
# Examples from the use of prefixes:
#
# Negative prefixes:
PREF-NEG: (ei|epä)
# Locative prefixes:
PREF-LOC: (yli|ali|etu|taka|etä|lähi|jälki|sisä|ulko|haja)
# Number prefixes:
PREF-NB: (uni|mono|bi|di|multi|poly)
# Other prefixes
PREF-OT: (esi|vara|oma|iki)
#
#
# 1.3.2. Particles as modifiers in word formation
#
# 1.3.2.1. Particles in modifying nouns
#
# Clitic particles
# Clitic particles: +ko|+kö|+kin|+kaan|+kään|+han|+hän|+pa|+pä|+kä
# ((INTR: +ko|+kö)|(PI-POS: +kin)|(PI-NEG: +kaan|+kään)|
# (FOC: +han|+hän|+pa|+pä)|(CONJ: +ka|+kä))
#
CLT-SFX-B: \w(kin|han|kaan|ko|pa)
CLT-SFX-F: \w(kin|hän|kä|kään|kö|pä)
CLT-SFX: \w(CLT-SFX-B|CLT-SFX-F)
#
#
# 1.3.2.2. Particles in modifying verbs
#
# To be continued.
#
#
# 1.4. Case marking
#
#Finnish has rich case marking. Case marking deasl with nominals and
# verbal nominal form. Case marking is used as a partial method also 
# in adpositional system. Adpositiaonal system is used side by side of 
# case marking.
#
# Accusative: -t, combined only with personal pronouns: e.g. minut, and 
# the interrogative ken 'who': kenet. Considered here lexicalizations.
#
# 1.4.1. Nominative/absolutive
#
# Nominative is unmarked. Nominative is distinguished in the singular
# and plural forms.
#
# 1.4.2. Accusative
# The formal accusative case can be distinguished from seven pronouns:
#
ACC: (minut|sinut|hänet|meidät|teidät|heidät|kenet)
#
# 1.4.3. Genitive: SG: -n, PL:-den/tten
# The genitive suffixe in the singular form is combined
# with the weak vowel stem: talo+n, kylä+n.
# the genitive plural endings form are combined 
# with the singular and plural stems: 
# ma+i+den, ma+i+tten, pyh+i+en, pyhä+i+n, kisso+j+en, kissa+i+n.    
# The genitive -n in the word ends is subsumed with the -n of 
# the possessive suffixes: talo+ni, kylä+nsä; ma+i+den+sa, ma+i+tten+sa, 
# pyh+i+en+sä, pyhä+i+n+sä, kisso+j+en+sa, kissa+i+nsa.
# The suffix -ten: after consonants:
# The suffix -en: after a short i and j which is after a short vowel:
# The suffixes -den/-tten: after diphtongs and the long i marked with -ii-.
# Obs. the comments on the combinatoric and free variants and 
# variations after the words consisting of three or more syllables.
#
GEN-SG: \w(((SYLL-OP)?())<n>)
GEN-PL-C: \w(((SYLL-CL)?()<ten>))
GEN-PL-P-C: \w(((SYLL-CL)?())(<te>)(POSS-SFX))
GEN-PL-EN: \w(V()(i|j)()<en>)
GEN-PL-P-EN: \w((V()(i|j)<e>)(POSS-SFX))
GEN-PL-IN: \w(V()(a|e|o|u|y|ä|ö)()<in>)
GEN-PL-P-IN: \w((V()(a|e|o|u|y|ä|ö)<i>)(POSS-SFX))
GEN-PL-DT: \w((DIPH|PL-I)()(<den>|<tten>))
GEN-PL-P-DT: \w((DIPH|PL-I)(<de>|<tte>)(POSS-SFX))
GEN: (GEN-SG|GEN-PL-C|GEN-PL-P-C|GEN-PL-EN|GEN-PL-P-EN|GEN-PL-IN|
  GEN-PL-P-IN|GEN-PL-DT|GEN-PL-P-DT)
# GEN-PL-P-EN poistettu väliaikaisesti.
#
# 1.4.4. Partitive
# in the words which have only one stem variant, the partitive endings
# are combined with the strong vowel stem, and in the words which
# have two stem types, the suffixes are combined with the consonant stem.
# 1. the suffixes -a and -ä: 
# after the short vowels and -j- in syllables without the principal stress: 
# auto+a, tuole+j+a, köyhä+ä, kävelijä+ä;
# 2. the suffixes -ta and -tä: 
# a) after consonants: varvas+ta, kirves+tä;
# b) after the end vowels of the word stems with the principal stress: 
# suo+ta, tie+tä;
# c) after the long vowels and diphtongs in the stems with non-principal 
# stress, and after the vowel combinations developed with contractions:
# varpa+i+ta, kynttilö+i+tä;
# d) after the stems ending with a syllable consisting of one vowel: 
# autio+ta, kylmiö+tä.
#
PTV-B: \w((((SYLL)?C()VB)|((SYLL)?C()VB()j))<a>)
PTV-F: \w((((SYLL)?C()VF)|((SYLL)?C()VF()j))<ä>)
PTV-TB: \w(C|SYLL-CVV|(SYLL()SYLL)|(SYLL()SYLL()SYLL)<ta>)
PTV-TF: \w(C|SYLL-CVV|(SYLL()SYLL)|(SYLL()SYLL()SYLL)<tä>)
PTV-TB-LD: \w(((SYLL)?()SYLL-CVV)|((SYLL)?()SYLL)<ta>)
PTV-TF-LD: \w(((SYLL)?()SYLL-CVV)|((SYLL)?()SYLL)<tä>)
PTV-TB-VS: \w(((((SYLL)?()SYLL)VB)ta)<ta>)
PTV-TF-VS: \w(((((SYLL)?()SYLL)VF)ta)<tä>)
PTV: \w(PTV-B|PTV-F|PTV-TB|PTV-TF|PTV-TB-LD|PTV-TF-LD|PTV-TB-VS|PTV-TF-VS)
#
#PTV-TB-VS|PTV-TF-VS: nämä olivat poistetut)
#
# 1.4.5. Essive: -na/-nä
# the essive suffix is combined with the strong vowel stems:
# (porttina, härkänä):
#
ESS-B: \w(<na>)(POSS-SFX?CLT-SFX?)
ESS-F: \w(<nä>)(POSS-SFX?CLT-SFX?)
ESS: \w(ESS-B|ESS-F)
INCLUDE: fin-disamb-ESS.spec
#
# 1.4.6. Translative: -kse/-ksi
# the translative suffix is combined with the weak vowel stems:
# (kukiksi, ystävikseen):
TRL-E: \w(<kse>)(POSS-SFX?CLT-SFX?)
TRL-I: \w(<ksi>)(POSS-SFX?CLT-SFX?)
TRL: \w(TRL-E|TRL-I)
INCLUDE: fin-disamb-TRL.spec
#
# 1.4.7. Inessive: the inessive suffixes are -ssa/-ssä
# the suffixes are combined with the weak vowel stems:
INE-B: \w(<ssa>)(POSS-SFX?CLT-SFX?)
INE-F: \w(<ssä>)(POSS-SFX?CLT-SFX?)
INE: \w(INE-B|INE-F)
#
# 1.4.8. Elative: the elative suffixes are -sta/-stä
# the suffixes are combined with the weak vowel stems:
ELA-B: \w(<sta>)(POSS-SFX?CLT-SFX?)
ELA-F: \w(<stä>)(POSS-SFX?CLT-SFX?)
ELA: \w(ELA-B|ELA-F)
#
# 1.4.9. Illative: the illative suffixes: -Vn, -hVn, -seen, and -siin
# a) -Vn ((a|o|u|y|ä|ö|e|i)n): after the short vowel of syllables 
# which do not have principal stress;
# b) -hVn ((han|hon|hun|hyn|hän|hön|hen|hin): after the stems having
# the principal stress, and stems which do not have the principal stress
# and which are ending with a diphtong;
# -seen: after the non-stressed stems or the stems having the secondary 
# stress and a diphtong 
# (au|uo|ou|eu|iu|äy|yö|öy|ey|iy|yi|öi|äi|ui|oi|ai|ie|ei);
# -siin: after the non-stressed stem or the stem having the secondary 
# stress and a long vowel (aa|oo|uu|yy|ää|öö|ee|ii);
#
ILL-SE-P: \w((((C)*()(V)*(VL))<see>)(POSS-SFX-V))(CLT-SFX?)
ILL-SE: \w(((C)*()(V)*(VL))<seen>)(POSS-SFX?CLT-SFX?)
ILL-SV-P: \w(((((V)(C)|(CC))*()(DIPH-I))<sii>)(POSS-SFX-V))(CLT-SFX?)
ILL-SV: \w((((C)|(CC))*()(DIPH-I))<siin>)(POSS-SFX?CLT-SFX?)
ILL-VBF-P: \w((((a|o|u|y|ä|ö|e|i)*
  (kst|ktr|ltr|mbr|mpl|mpr|mpt|ndr|nkr|nkt|nsl|ntr|rkt|skr|str|htr|ksl|
  lfr|lpt|lsn|lsp|mbl|mfl|ndh|nkm|nsn|nsv|ntl|ntn|ngsk|ptr|rnj|rpr|rpt|rsl|
  rtn|rtr|skv|spl|spr|stm|tsl|ksm|kts|lsm|ntg|ntv|pts|rdv|rkm|rks|rmj|rml|
  rnh|rrnh|tsk|tst|bsk|bst|btr|ksh|ksk|ksp|ksv|mph|nfl|nkl|nkv|nsf|nsm|nsp|
  psl|rgl|rkl|rkr|rpl|rsp|rsr|skv|std|stf|sth|stj|stp|sts|lkk|ltt|lss|nkk|
  ntt|nss|rkk|rtt|rss|rst|
  hd|hj|hk|hl|hm|hn|hr|ht|hv|kk|kl|kr|ks|lh|lj|lk|ll|lm|lp|ls|lt|lv|mm|mp|
  nh|nn|ns|nt|nk|ng|pl|pr|pp|ps|rh|rj|rk|rm|rn|rp|rr|rs|rt|rv|sk|sl|sm|sp|
  ss|st|sv|tj|tk|tr|ts|tt|tv|
  b|d|f|g|h|j|k|l|m|n|p|r|s|t|v)*)
  (a<a>|o<o>|u<u>|y<y>|ä<ä>|ö<ö>|e<e>|i<i>))(POSS-SFX))(CLT-SFX?)
ILL-VBF: \w(((a|o|u|y|ä|ö|e|i)*
  (kst|ktr|ltr|mbr|mpl|mpr|mpt|ndr|nkr|nkt|nsl|ntr|rkt|skr|str|htr|ksl|
  lfr|lpt|lsn|lsp|mbl|mfl|ndh|nkm|nsn|nsv|ntl|ntn|ngsk|ptr|rnj|rpr|rpt|rsl|
  rtn|rtr|skv|spl|spr|stm|tsl|ksm|kts|lsm|ntg|ntv|pts|rdv|rkm|rks|rmj|rml|
  rnh|rrnh|tsk|tst|bsk|bst|btr|ksh|ksk|ksp|ksv|mph|nfl|nkl|nkv|nsf|nsm|nsp|
  psl|rgl|rkl|rkr|rpl|rsp|rsr|skv|std|stf|sth|stj|stp|sts|lkk|ltt|lss|nkk|
  ntt|nss|rkk|rtt|rss|rst|
  hd|hj|hk|hl|hm|hn|hr|ht|hv|kk|kl|kr|ks|lh|lj|lk|ll|lm|lp|ls|lt|lv|mm|mp|
  nh|nn|ns|nt|nk|ng|pl|pr|pp|ps|rh|rj|rk|rm|rn|rp|rr|rs|rt|rv|sk|sl|sm|sp|
  ss|st|sv|tj|tk|tr|ts|tt|tv|
  b|d|f|g|h|j|k|l|m|n|p|r|s|t|v)*)
  (a<an>|o<on>|u<un>|y<yn>|ä<än>|ö<ön>|e<en>|i<in>))(POSS-SFX?CLT-SFX?)
ILL-HBF-P: \w((((V)|(VL)|(DIPH))
  (<ha>|<ho>|<hu>|<hy>|<hä>|<hö>|<he>|<hi>))(POSS-SFX-V))(CLT-SFX?)
ILL-HBF: \w(((V)|(VL)|(DIPH))
  (<han>|<hon>|<hun>|<hyn>|<hän>|<hön>|<hen>|<hin>))(POSS-SFX?CLT-SFX?)
ILL: \w(ILL-SV-P|ILL-SV|ILL-VBF|ILL-VBF-P|ILL-SE-P|ILL-SE|
  ILL-HBF-P|ILL-HBF)
#
# 1.4.10. Adessive: -lla/-llä
# DIPHB: (au|uo|ou|eu|iu)
# the suffixes are combined with the weak vowel stems:
ADE-B: \w(<lla>)(POSS-SFX?CLT-SFX?)
ADE-F: \w(<llä>)(POSS-SFX?CLT-SFX?)
ADE: \w(ADE-B|ADE-F)
#
# 1.4.11. Ablative: -lta/-ltä
# the suffixes are combined with the weak vowel stems:
ABL-B: \w(<lta>)(POSS-SFX?CLT-SFX?)
ABL-F: \w(<ltä>)(POSS-SFX?CLT-SFX?)
ABL: \w(ABL-B|ABL-F)
#
# 1.4.12. Allative: -lle
# the suffix is combined with the weak vowel stems:
ALL: \w(<lle>)(POSS-SFX?CLT-SFX?) 
#
# 1.4.13. Abessive: -tta/-ttä 
# the abessive suffix is combined with the weak vowel stems
# (kirjoitta, päivittä; onko tieto vokaalista sijan edellä tarpeen?):
ABE-B: \w(<tta>)(POSS-SFX?CLT-SFX?)
ABE-F: \w(<ttä>)(POSS-SFX?CLT-SFX?)
ABE: \w(ABE-B|ABE-F)
#
# 1.4.14. Instructive: -n
# the suffix is combined with the weak vowel stem
# (kahden, kaikin keinoin):
#INST: \w((PL-I)?()<n>)
#
# 1.4.15. Comitative: -ne
# the suffix is combined with the plural stem
# (koirineen, kaikkine ystävineen):
COM: \w((PL-I)?()<ne>)
#
CASE: \w(GEN|PTV|ESS|TRL|ADE|ABL|ALL|INE|ELA|ILL|ABE|COM)
#
#
# Nouns
# 
# Adjectives
#
# Pronouns, Finnish 
#
#PRON-POSS = the genitive forms of personal pronouns):
#
PRON-PERS: (minä|sinä|hän|me|te|he)
PRON-ACC: (minut|sinut|hänet|meidät|teidät|heidät|kenet)
PRON-POSS: (minun|sinun|hänen|meidän|teidän|heidän)
PRON-REFL: ((minä|sinä|hän|me|te|he) itse)
PRON-DEM: (tämä|tuo|se|nämä|nuo|ne)
PRON-INTR: (kuka|kukaan|kukin|mikä|mikin|mikään|ken|kenkään|
  kumpi|kumpikin|kumpikaan|kumpainenkin|kumpainenkaan)
PRON-REL: (joka|kuka|mikä)
PRON-Q: (yksi|joka|joku|eräs|toinen|muu|muutama|muutamat|sama|
  jompikumpi|kumpikin|kumpikaan|kumpainenkin|kumpainenkaan|
  kukin|kukaan|mikin|mikään|
  jokainen|kukin|molemmat|kaikki|
  moni|monet|monta|usea|useat|useampi|useimmat)
PRON-REC: ((toinen toisensa)|(toinen toistaan))
PRON-ADV: (täällä|tuolla|siellä|missä|kaikkialla)
#
PRON: (PRON-PERS|PRON-ACC|PRON-POSS|PRON-REFL|PRON-DEM|PRON-INTR|
  PRON-REL|PRON-Q|PRON-REC|PRON-ADV)
#24.12. Pronominit oli poistettu.
#
#Numerals
#
#Conjunctions:
#
#COORDINATIVE CONJUNCTIONS
#SUBORDINATIVE-CONJ: 
#
#Noun phrase (NP), Finnish
#N+CASE
#A + N+CASE
#DET + A + N+CASE
#N+GEN + POP
#A + N+PTV + POP
#(DET+) (A+) (N+PTV|N+GEN) + POP
#
# 2. Inflection of verbs
#
# Verbal inflection has rich morphology in Finnish. This concerns both 
# word formation and inflectional system. The descriptions of categories
# listed below deal in particular with grammatical categories. The 
# richness of varieties found in verbal inflection are comparable with
# those found in nominal inflection. Also the varieties in verbal stems 
# are comparable with those found in nominal inflection.
#
# The verbs in the database are introduced from the file fin-verbs.txt 
# to the kwic-file for processing operations. The verbs are used with
# the help of the following rule:
#
# 2.1. The verbs dealt with the project
# To be continued.
# The verbs in the database are introduced from the file fin-verb.txt
# to the kwic-file for processing operations. The verbs are used with
# the help of the following rule:
#
#
#VERB-DATA: VERB-LIST 
#INCLUDELIST: VERB-LIST-NON-FINITE
#INCLUDELIST: FIN-VERBS-BASIC
INCLUDELIST: fin-verbs-database-march-2018.txt VERBS-DATA
INCLUDELIST: fin-verbs-finite-test.txt VERBS-FINITE-TEST
INCLUDELIST: fin-verbs-data-finite-forms.txt VERBS-FINITE
INCLUDELIST: fin-verbs-sample.txt VERBS-SAMPLE
INCLUDELIST: fin-verbs-som.txt VERBS-SOM
INCLUDELIST: fin-verbs-som-april-2018.txt VERBS-SOM-LONG
#
INCLUDELIST: fin-verbs-som-loc.txt VERB-SOM-LOC
INCLUDELIST: fin-verbs-som-ad-loc.txt VERB-SOM-AD-LOC
#
#INCLUDELIST: fin-verbs-test-olla.txt VERB-TEST-OLLA
#INCLUDELIST: fin-verbs-test-virrata.txt VERB-TEST-VIRRATA
#INCLUDELIST: fin-verbs-test-vieda.txt VERB-TEST-VIEDA
#INCLUDELIST: fin-verbs-test-tuoda.txt VERB-TEST-TUODA
#INCLUDELIST: fin-verbs-test-menna.txt VERB-TEST-MENNA
#INCLUDELIST: fin-verbs-test-tulla.txt VERB-TEST-TULLA
#
INCLUDE: fin-disamb-VERBS-EXCL.spec
#
INCLUDELIST: fin-verbs-som.txt VERB-TEST-@ 
#
#
# 2.4. Verbal nominal forms
# 2.4.1. Infinitives
#
# The verbs in the Finnish database are collected in the list called
# fin-verbs.txt which in the kwic-file are introduced with the name
# ?????
# In the list, the dictionary forms are marked with the character “#”.
# 
# The infinitive forms in Finnish are marked with suffixes:
#
#INF-I: ol+la, men+nä, 
#INF-I:  (a|ä|ta|tä|da|dä|la|lä|na|nä|ra|rä)
# cf. also saa+da, vie+dä, etc.
# with the consonant stems of verbs having one stem, and with the 
# strong vowel stems of the verbs having consonant and vowel stems: 
# INF-II: ol+le+ssa, men+ne+ssä, 
# INF-II: (e|de|te|le|ne|re)
# INF-III: ole+ma+ssa, mene+mä+ssä, 
# INF-III: (ma|mä)
# INF-IV: ole+minen, mene+minen, 
# INF-IV: (minen|(mis(ta|tä)))
# INF-V: ole+maisillaan, mene+mäisillään
# INF-V: ((maisilla|mäisillä)POSS-SX)
#
INF-I: \w(((STEM-C)|(STEM-V-S))()((a|ä|da|dä|la|lä|na|nä|ra|rä|ta|tä)))
INF-II: \w((((STEM-C)|(STEM-V-S))()(e(de|le|ne|re|te)))(INE-F|INE-B))
INF-III-B: \w(((STEM-V-S)()(ma|mi))()(INE-B|ADE-B|ELA-B|ILL-VBF|ILL-HBF))
INF-III-F: \w(((STEM-V-S)()(mä|mi))()(INE-F|ADE-F|ELA-F|ILL-VBF|ILL-HBF))
INF-III: \w(INF-III-B|INF-III-F)
INF-IV: \w((STEM-V-S)()((minen)|(mis)()(PTV)))
INF-V: \w(((STEM-V-S)()(maisilla|mäisillä))()(POSS-SFX))
VERB-BE-INF-I: ((ol)la)
INF: \w(INF-I|INF-II|INF-III-F|INF-III-B|INF-IV|INF-V|VERB-BE-INF-I)
#
# INF from the verbs in the database: fin-INF.
#
# 2.4.2. Participles
#
# ACT-PCPL-I: ole+va, mene+vä: the suffix -vA is connected to
# strong vowel stems and to the passive stems.
# a) the suffixes -lUt, -nUt, -rUt, -sUt and 
# b) the suffixes -lee-, -nee-, -ree-, and -see- are connected to
# the strong vowel stems of verbs having only one stem, and
# the consonant stems of the verbs having two stems.
# The suffixes in group b) occur before case endings.
#  
ACT-PCPL-I-VA: \w((STEM-VA)(va|vä))
ACT-PCPL-I-CONTR: \w((STEM-CONTR)(va|vä))
ACT-PCPL-I-ITA: \w((STEM-ITA)(va|vä))
ACT-PCPL-I-ETA: \w((STEM-ETA)(va|vä))
ACT-PCPL-I-DA-I: \w((STEM-DA-I)(va|vä))
ACT-PCPL-I-DA-II: \w((STEM-DA-II)(va|vä))
ACT-PCPL-I-LA-NA-RA-SE: \w((STEM-LA-NA-RA-SE)(va|vä))
ACT-PCPL-I: (ACT-PCPL-I-VA|ACT-PCPL-I-CONTR|ACT-PCPL-I-ITA|ACT-PCPL-I-ETA|
  ACT-PCPL-I-DA-I|ACT-PCPL-I-DA-II|ACT-PCPL-I-LA-NA-RA-SE)
#
ACT-PCPL-II-VA: \w((STEM-VA)(nut|nyt|neet))
ACT-PCPL-II-DA-I: \w((STEM-DA-I)(nut|nyt))
ACT-PCPL-II-DA-II: \w((DIPH|VB-L|VF-L)(nut|nyt))
ACT-PCPL-II-LNRS-SG: \w((l|n|r|s)((l|n|r|s)(ut|yt)))
ACT-PCPL-II-LNRS-PL: \w((l|n|r|s)eet)
ACT-PCPL-II-CASE: \w((nee|nei)(INE-F|ADE-F|ELA-F|ABL-F|ILL-VBF|ILL-HBF|ALL))
ACT-PCPL-II: (ACT-PCPL-II-VA|ACT-PCPL-II-DA-I|ACT-PCPL-II-DA-II|
  ACT-PCPL-II-LNRS-SG|ACT-PCPL-II-LNRS-PL|ACT-PCPL-II-CASE)
#
ACT-PCPL-AG-B: \wma(INE-B|ADE-B|ELA-B|ABL-B|ALL|ILL-VBF|ILL-HBF) 
ACT-PCPL-AG-F: \wmä(INE-F|ADE-F|ELA-F|ABL-F|ALL|ILL-VBF|ILL-HBF)
ACT-PCPL-AG-PL: \wmi(INE-F|ADE-F|ELA-F|ABL-F|ALL|ILL-VBF|ILL-HBF)
ACT-PCPL-AG: (ACT-PCPL-AG-B|ACT-PCPL-AG-F|ACT-PCPL-AG-PL)
#
ACT-PCPL-NEG: \w(V()((maton|mätön)|((mattoma|mättömä)()(CASE))))
ACT-PCPL: (ACT-PCPL-I|ACT-PCPL-II|ACT-PCPL-AG|ACT-PCPL-NEG)
#
PASS-PCPL-I-SG: \w(((VL|DIPH|STEM-V-S)(ta|tä))(va|vä))
PASS-PCPL-I-PL: \w(((VL|DIPH|STEM-V-S)(ta|tä))(v(i))
  (INE-F|ADE-F|ELA-F|ABL-F|ALL|ILL-VBF|ILL-HBF))
PASS-PCPL-I: \w(PASS-PCPL-I-SG|PASS-PCPL-I-PL)
PASS-PCPL-II-S: \w((VL|DIPH|STEM-LA-NA-RA-SE)(du|dy|lu|ly|ru|ry|tu|ty|u|y)
  (i)(INE-F|ADE-F|ELA-F|ABL-F|ALL|ILL-VBF|ILL-HBF))
PASS-PCPL-II-L: \w((VL|DIPH|V)(ttu|tty|tu|ty))
PASS-PCPL-II: (PASS-PCPL-II-S|PASS-PCPL-II-L)
PASS-PCPL: (PASS-PCPL-I|PASS-PCPL-II)
# 
PCPL: (ACT-PCPL|PASS-PCPL)
#
#
# 2.3. Personal inflection
#
#1SG: (n)
#2SG: (t)
#3SG: ((a|o|u|ä|ö|y|e|i)|zero)
#1PL: (mme)
#2PL: (tte)
#3PL: (vat|vät)
#PERS: (1SG|2SG|3SG|1PL|2PL|3PL)
#PASS-PERS: ((a|ä|i)n)
#
VERB-1SG: \w((V)()(n))
VERB-2SG: \w((V)()(t))
VERB-3SG: \w((V)()(V))
VERB-1PL: \w((V)()(mme))
VERB-2PL: \w((V)()(tte))
VERB-3PL: \w((V)()(vat|vät))
VERB-PERS-I: (VERB-2SG|VERB-3SG|VERB-1PL|VERB-2PL|VERB-3PL)
VERB-PERS-II: (VERB-2SG|VERB-1PL|VERB-2PL|VERB-3PL)
#
VERB-PERS: (VERB-PERS-I|VERB-PERS-II)
#
#
# 2.4. Auxiliaries 
#
# The auxiliaries distinguish tense and mood categories.
#
#The basic forms of auxiliaries:
VERB-AUX-PRES: (olen|olet|on|olemme|olette|ovat)
VERB-AUX-PAST: (olin|olit|oli|olimme|olitte|olivat)
VERB-AUX-COND: (olisin|olisit|olisi|olisimme|olisitte|olisivat)
VERB-AUX-IMP:  (olkoon|oltakoon|olko)
VERB-AUX-PASS-PRES: (on PASS-PCPL-II)
VERB-AUX-PASS-PAST: (oli PASS-PCPL-II)
VERB-AUX-NEG: (en|et|ei|emme|ette|eivät|eihän|eikä|eikö|eiköhän|eipä|eiväthän|
  eivätkä|eivätkö|emmekä|emmekö|enhän|ethän|etkä|etkö|
  älä|älkää|älköön|älkäämme|
  ellen|ellet|ellei|ellemme|ellette|elleivät|
  jollen|jollet|jollei|jollemme|jollette|jolleivät)
VERB-AUX: (VERB-AUX-PRES|VERB-AUX-PAST|VERB-AUX-COND|VERB-AUX-IMP|
  VERB-AUX-PASS-PRES|VERB-AUX-PASS-PAST|VERB-AUX-NEG)
#
#
VERB-MOD: (haluta|halua|haluaa|haluaako|haluaisimme|haluaisin|haluamme|
  haluan|haluat|haluatte|haluavat|halusi|halusimme|halusimmekin|
  osata|osaa|osaan|osaatko|osaatte|osaavat|osaisi|osaisinko|osaisitko|
  osaisimme|osaisitte|osaisivat|osanneet|osannut|osata|
  pitää|pitäisi|pitänee|pidä|pitääkin|pitääkö|pitääköhän|pitäisi|pitäisikö|
  pitäisiköhän|pitänyt|piti|pitihän|pitikö|pitänee|
  tahtoa|tahdo|tahdoimme|tahdoin|tahdoit|tahdoitte|tahdomme|tahdommeko|
  tahdon|tahdonpa|tahdot|tahdotko|tahdotte|tahdotteko|tahdottiin|
  tahdota|tahtoen|tahtoi|tahtoiko|tahtoisi|tahtoisimme|tahtoisin|
  tahtoisinkaan|tahtoisinkin|tahtoisinpa|tahtoivat|tahtomatta|
  tahtoneet|tahtonut|tahtoo|tahtooko|tahtovan|tahtovansa|tahtovat| 
  täytyy|täytyisi|täytynee|tätyi|täytyisi|täytynyt|täytyy|täytyyhän|
  täytyykö|täytyypä|
  voida|voi|voidaan|voidakseen|voidakseni|voidaksenne|voidaksensa|voikaan|
  voiko|voikohan|voimme|voimmekaan|voimmeko|voin|voineet|voinko|voinut|
  voipa|voisi|voisimme|voisimmeko|voisin|voisinhan|voisinkaan|voisinko|
  voisit|voisitkin|voisitte|voisivat|voit|voitaisiin|voitko|voitte|
  voitteko|voittepa|voitu|voivan|voivani|voivanne|voivansa|
  voivasi|voivat|voivatko|voivatkohan)
#
# 2.4.1. Personal inflection of auxiliaries
#
ACT-BE-PRES-PERS-1SG: \w((ole)()VERB-1SG)
ACT-BE-PRES-PERS-2SG: \w((ole)()VERB-2SG)
ACT-BE-PRES-PERS-3SG: \w(on)
ACT-BE-PRES-PERS-1PL: \w((ole)()VERB-1PL)
ACT-BE-PRES-PERS-2PL: \w((ole)()VERB-2PL)
ACT-BE-PRES-PERS-3PL: \w(o(VERB-3PL))
ACT-BE-PRES-PERS: (ACT-BE-PRES-PERS-1SG|ACT-BE-PRES-PERS-2SG|
  ACT-BE-PRES-PERS-3SG|ACT-BE-PRES-PERS-1PL|
  ACT-BE-PRES-PERS-2PL|ACT-BE-PRES-PERS-3PL)
#
ACT-BE-PAST-PERS-1SG: \w((oli)()VERB-1SG)
ACT-BE-PAST-PERS-2SG: \w((oli)()VERB-2SG)
ACT-BE-PAST-PERS-3SG: \w(oli)
ACT-BE-PAST-PERS-1PL: \w((oli)()VERB-1PL)
ACT-BE-PAST-PERS-2PL: \w((oli)()VERB-2PL)
ACT-BE-PAST-PERS-3PL: \w(oli()VERB-3PL)
ACT-BE-PAST-PERS: (ACT-BE-PAST-PERS-1SG|ACT-BE-PAST-PERS-2SG|
  ACT-BE-PAST-PERS-3SG|ACT-BE-PAST-PERS-1PL|
  ACT-BE-PAST-PERS-2PL|ACT-BE-PAST-PERS-3PL)
#
ACT-BE-COND-I: \w(((ol)isi) (VERB-PERS-II))
ACT-BE-COND-II: (ACT-BE-COND-I ACT-PCPL-II)
ACT-BE-POT-I: \w(((lie)ne) (VERB-PERS-I))
ACT-BE-POT-II: ((ACT-BE-POT-I) (ACT-PCPL-II))
ACT-BE-POT: (ACT-BE-POT-I|ACT-BE-POT-II)
#
#VERB-NEG-PERS-1SG: \w(((e)VERB-1SG)((ACT-IMP-VERB-BE-2SG)|ollut|COND-I|liene)
#VERB-NEG-PERS-2SG: \w(((e)VERB-2SG)(ole|ollut|COND-I|liene)
#VERB-NEG-PERS-3SG: \w(((e)i) (ole|ollut|COND-I|POT-I)
#VERB-NEG-PERS-1PL: \w(((e)VERB-1PL)(ole|ollut|COND-I|POT-I)
#VERB-NEG-PERS-2PL: \w(((e(VERB-2PL)(ole|ollut|COND-I|POT-I))))
#VERB-NEG-PERS-3PL: \w(((e)i)VERB-3PL)(ole|ollut|COND-I|POT-I)
#
#VERB-NEG-PERS-1SG: \w((e)()(VERB-1SG))
#VERB-NEG-PERS-2SG: \w((e)()(VERB-2SG))
#VERB-NEG-PERS-3SG: \w((e)i)
#VERB-NEG-PERS-1PL: \w((e)()(VERB-1PL))
#VERB-NEG-PERS-2PL: \w((e)()(VERB-2PL))
#VERB-NEG-PERS-3PL: \w(((e)i)()(VERB-3PL))
#VERB-NEG-PERS: (VERB-NEG-PERS-1SG|VERB-NEG-PERS-2SG|VERB-NEG-PERS-3SG|
#  VERB-NEG-PERS-1PL|VERB-NEG-PERS-2PL|VERB-NEG-PERS-3PL)
#
ACT-BE: (ACT-BE-PRES-PERS|ACT-BE-PAST-PERS|ACT-BE-COND-I|
  ACT-BE-COND-II|ACT-BE-POT-I|ACT-BE-POT-II)
#
ACT-BE-HAVE: (ACT-BE)
#
AUX: (ACT-BE-HAVE)
#
# poistettu tilapäisestiä ACT-NEG_PERS.18.12.18
# 
#NEG
# ACT-NEG-PRES; 
# 1SG: e+n, 2SG: e+t, 3SG: ei, 1PL: e+mme, 2PL: e+tte, 3PL: ei+vät 
#
# Passive forms of the negative verb:
# VERB-PASS-NEG-PERS: (VERB-NEG-PERS-3SG)  
# ((VERB-BE-INF-I|VERB-BE-PCPL-II|VERB-BE-COND-I|
# VERB-BE-COND-I VERB-BE-PCPL-II|VERB-BE-POT-Ioltane))
#
#VERB-ACT-PERF-PRES: (VERB-BE-PRES-PERS()ACT-PCPL-II) 
#VERB-ACT-PERF-PAST: (VERB-BE-PAST-PERS()ACT-PCPL-II) 
#
#
# 2.3. Diathesis
#
#
# 2.3.1. Active
#
#
# Active is unmarked.
#
#
# 2.3.2. Passive
#
# The passive is formed with the suffixes +ta+/+tä+ which are realized as
# +ta+, +tä+, +da+, +dä+, +la+, +lä+, +na+, +nä+, +ra+, +rä+, +a+, +ä+:
# nuku+ta+an, pes+tä+än, ui+da+an, vie+dä+än, tul+la+an, niel+lä+än,
# pan+na+nan, men+nä+än, pur+ra+an, vier+rä+än, surr+a+an, pelät+ä+än.
# The periphrastic passive forms are formed with some auxiliaries,
# and for thatreason, infletion of auxiliaries has to be presented before
# formation of passives.
#
#
# 2.3.1. Rules for forming passives

# Passive, imperative
# PASS-IMP: ol+ta+koon, 
# PASS-IMP-NEG: ol+ta+ko, 
# PASS-IMP: ((ta|tta|tä|ttä)(koon|köön))
# PASS-IMP-NEG: ((äl|köön|kää|kööt) (VERB-V(ko|kö)))
# XXX. The rules for forming passive
# Liitä passiivimuotoihin tempusta koskevat tiedot!
# PASS-PRES: ol+la+an, men+nä+än, 
# PASS-PAST: ol+t+i+in, men+t+i+in, 
# PASS-PERF: o+n ol+tu, o+n men+ty, 
# PASS-PERF-PAST: ol+i ol+tu, ol+i men+ty, 
#PASS-PRES: (t|ta|tä|la|lä|na|nä|ra|rä)
#PASS-PAST: (ti|li|ni|ri|tti|lli|nni|rri)
#PASS-PERF:  (on (PASS-PCPL-PERF))
#PASS- PERF-PAST:  (oli (PASS-PCPL-PERF))
#
PASS-I: \w(((((V)()(V))|(C))()(ta|tä|da|dä|la|lä|na|nä|ra|rä|a|ä))()
  (an|än|in))
#
PASS-II: \w((((C)()(V))()(tta|ttä|ta|tä))()((an|än|in)))
#
PASS: (PASS-I|PASS-II)
#
PASS-PRES: ((PASS-I|PASS-II)(V|koon|köön))
PASS-PAST: ((PASS-I|PASS-II)i)
PASS-PERF: (on (PASS-PCPL-II|PASS-PCPL-II))
PASS-PLUPERF: (oli (PASS-PCPL-II|PASS-PCPL-II))
#
#  
#TENSE: (ACT-TENSE|PASS-TENSE)
#
# Imperative, NEG:
# älä ole, älä mene, 
# äl+kö+ön, äl+kä+ämme, äl+kä+ä, äl+kö+öt & CO-NEG: ol+ta+ko, men+kö
# PASS: äl+kö+ön ol+ta+ko, men+tä+kö
# PASS-POT-CO-NEG: ei ol+ta+ne, ei men+tä+ne, 


# 2.6. Moods
#
# The grammatical moods in Finnish are indicative, conditional, 
# potential and imperative. Indicative is unmarked. The other moods
# are marked with special suffixes. The words in the ndicative, imperative,
# and potential are marked with tense categories whihc are present 
# (unmarked), past (called as imperfect in grammars), perfect, and
# pluperfect.  
#
# 2.6.1. Indicative
#
#Indicative in Finnish is not marked formally.
#
#  
# 2.6.2. Conditional 
#
# Conditional in Finnish is formed with the suffix +isi+ which in 
# in simple conditional form is connected to the lexical verb, and
# in the periphrastic conditional form to auxiliary “olla”. In this
# periphrastic form, the lexical verb is in the second participle form.
# In the passive participle form, the passive marker (suffix) precedes
# the conditional suffix.
#
#The conditional inflection of the auxiliary 'olla:
# ol+isi+n, ol+isi+t, ol+isi, ol+isi+mme, ol+isi+tte, ol+isi+vat, 
#
ACT-COND-I: \w(((STEM-V-S)()isi)()(VERB-PERS-II))
#
# COND-PERF (COND-II): 
# ol+isi+n ol+lut, ol+isi+t ol+lut, ol+isi ol+lut, 
# ol+isi+mme ol+lee+t, ol+isi+tte ol+lee+t,
# ol+isi+vat ol+lee+t, ol+isi+n men+nyt, ol+isi+t men+nyt, ol+isi men+nyt, 
# ol+isi+mme men+nee+t, ol+isi+tte men+nee+t, ol+isi+vat men+nee+t, 
#
ACT-COND-II: \w(ACT-BE-COND-I ACT-PCPL-II)
#
ACT-COND: (ACT-COND-I|ACT-COND-II)
#
# PASS-COND: ol+ta+isi+in, men+tä+isi+in
VERB-PASS: \w((PASS-I)|(PASS-II)()(an|än|in))
#
PASS-COND-I: \w((((STEM-V)()(PASS-I|PASS-II))()(isi))()(VERB-PASS))
#
# PASS-COND-PERF: ol+isi ol+tu, ol+isi men+ty, 
PASS-COND-II: (olisi (PASS-PCPL-II))
#
PASS-COND: (PASS-COND-I|PASS-COND-II)
#
COND: (ACT-COND|PASS-COND)
#
# Dec. 19, 2018: verbien taivutus suljettu tiedoston ALL-EXCL mukanaan tuomien virheiden vuoksi.
# Tarkastettava, mitä sääntöjä sisältyy eri sääntöryhmii. Näihin tehdyt muutokset
# aiheuttivat ongelmia. 
#
# 2.6.3. Potential
# 
# POT-PRES-FUT (POT-I): 
# men+ne+n, men+ne+t, men+ne+e, men+ne+mme, men+ne+tte, men+ne+vät
# Auxiliary: lie+ne+n, lie+ne+t, lie+ne+e, lie+ne+mme, lie+ne+tte, lie+ne+vät,#
#
# PASS-COND-II:
#
# POT-PERF (POT-II): 
# lie+ne+n ol+lut, lie+ne+t ol+lut, lie+ne+e ol+lut, 
# lie+ne+mme ol+le+et, lie+ne+tte ol+le+et, lie+ne+vät ol+le+et, 
# liene+n men+nyt, liene+t men+nyt, liene+e men+nyt, 
# liene+mme men+ne+et, liene+tte men+ne+et, liene+vät men+ne+et 
#2.8.4. The rules for forming potential
#
#POT-I: (le|ne|re|se)PERS)
#POT-II: ((lie(PERS)) (V(PCPL-PERF)))
#
ACT-POT-I: \w(((STEM-V-S|STEM-C)()(le|ne|re|se))VERB-PERS-I)
ACT-POT-II: \w(((liene)VERB-PERS-I)ACT-PCPL-II)
ACT-POT: (ACT-POT-I|ACT-POT-II)
#
# PASS-POT-I: ol+ta+ne+en, men+tä+ne+en
# PASS-POT-II: lie+ne+e ol+tu, lie+ne+e men+ty
PASS-POT-I: (((PASS-I)|(PASS-II))()(VERB-PASS))
PASS-POT-II: ((liene)(VERB-PASS) (PASS-PCPL-II|PASS-PCPL-II-L))
#
PASS-POT: (PASS-POT-I|PASS-POT-II)
#
POT: (ACT-POT|PASS-POT)
#
#
# 2.6.4. Imperative
#
# ACT-IMP: 
#IMP-2SG: (zero = R)
#IMP-3SG: (ko+on|kö+ön)
#IMP-1PL: ((ka+a|kä+ä)()PERS-1PL)
#IMP-2PL: (ka+a|kä+ä)
#IMP-3PL: (ko+ot|kö+öt)
#IMP-CONNEG: (ko|kö)
#IMP-NEG: (äl(kö+ön|kä+ä|kö+öt) (VERB-V(ko|kö)))
#
# Active & passive, imperative:
ACT-IMP-2SG: (STEM-V)
ACT-IMP-3SG: ((STEM-V-S|STEM-C)(koon|köön)) 
ACT-IMP-1PL: ((STEM-V-S|STEM-C)((kaa|kää)()(VERB-1PL)))
ACT-IMP-2PL: ((STEM-V-S|STEM-C)(kaa|kää)) 
ACT-IMP-3PL: ((STEM-V-S|STEM-C)((koo|köö)()(VERB-3PL)))
#
ACT-IMP-PERS: (ACT-IMP-2SG|ACT-IMP-3SG|ACT-IMP-1PL|ACT-IMP-2PL|ACT-IMP-3PL)
#
# Active, imperative, the negative verb:
ACT-IMP-NEG-2SG: (älä STEM-V)
ACT-IMP-NEG-3SG: (älköön (STEM-V(ko|kö)))
ACT-IMP-NEG-1PL: (älkäämme (STEM-V(ko|kö)))
ACT-IMP-NEG-2PL: (älkää (STEM-V(ko|kö)))
ACT-IMP-NEG-3PL: (älkööt (STEM-V(ko|kö)))
#
# CO-NEG: ole, SG: ol+lut, PL: ol+lee+t, SG & PL:ol+isi, SG & PL: lie+ne
VERB-CONNEG: (ACT-IMP-2SG|PASS-PCPL-I|PASS-PCPL-II)
#
ACT-IMP-NEG: (ACT-IMP-NEG-2SG|ACT-IMP-NEG-3SG|ACT-IMP-NEG-1PL|
  ACT-IMP-NEG-2PL|ACT-IMP-NEG-3PL|VERB-CONNEG)
#
PASS-IMP: ((((STEM-V-S)|(STEM-C))()(((t)ta)|((t)tä)))()(koon|köön))
#
PASS-IMP-NEG: (älköön (STEM-V(ta|tä)(ko|kö)))
#
#PASS-IMP: (PASS-IMP-PERS|PASS-IMP-NEG|VERB-CONNEG)
#
IMP: (ACT-IMP-PERS|ACT-IMP-NEG|PASS-IMP|PASS-IMP-NEG)
#
#
# 2.6.5. Subjunctive
#
# There is no subjunctive mood in Finnish (cf. e.g. Englis). To be continued.
#
#
# 2.7. Tense forms
# The tense forms in Finnisha are simple and periphrastic.
# The periphrastic forms are formed wsith auxiliaries which are marked
# with personal inflection.
#
# 2.7.1. The simple basic tense forms
#
# (a) Present tense:
# ACT-PRES: ole+n, ole+t, o+n, ole+mme, ole+tte, o+vat
# mene+n, mene+t, mene+e, mene+mme, mene+tte, mene+vät 
#
ACT-PRES: \w((STEM-V)()(VERB-PERS-I))
#
ACT-PAST: \w((i)()(STEM-V)()(VERB-PERS-II))
#
# (b) Past tense:
# ol+i+n, ol+i+t, ol+i+t, ol+i+mme, ol+i+tte, ol+i+vat, 
# men+i+n, men+i+t, men+i, men+i+mme, men+i+tte, men+i+vät
#
# (c) Perfect tense: 
# PERF-I (ACT-PERF): 
# ole+n ol+lut, olet ol+lut, on ol+lut, 
# olemme ol+leet, ol+lette ol+leet, o+vat ol+leet, 
# ole+n men+nyt, ole+t men+nyt, o+n men+nyt, 
# ole+mme men+nee+t, ole+tte men+nee+t,o+vat men+nee+t
# 
ACT-PERF: ((VERB-AUX-PRES) (ACT-PCPL-II))
#
# (d) PERF-II (pluperfect):
# ACT-PERF-PAST: 
# ol+i+n ol+lut, ol+i+t ol+lut, ol+i+mme ol+lee+t, 
# ol+i+tte ol+lee+t, ol+i+vat ol+lee+t, 
# ol+i+n men+nyt, ol+i+t men+nyt, ol+i men+nyt, 
# ol+i+mme men+nee+t, ol+i+tte men+nee+t, ol+i+vat men+nee+t
#
ACT-PLUPERF: ((VERB-AUX-PAST) (ACT-PCPL-II))
# 
#ACT-TENSE: (ACT-PRES|ACT-PAST|ACT-PERF|ACT-PLUPERF)
#
# (e) Future
# Finnish has no future tense form marked with specific tense suffixes. 
# Future is expressed (a) with the present  tense form, and its
# relationship to the future is included in the context, and (b)
# also with the verb "tulla" which is combined with the verb marked
# with tje INF-III ending combined with the illative case endings.
# The verb "tulla" is marked with ersonal endings: tule+n teke+mä+än
# (de+INF-III+ILL). This type of futer corresponds to the FUT-II in English: 
# PERS be doing to marked with the illative form of the lexical verb:
# tule+n teke+mään. This type of future corresponds to the FUT-II in English:
# PERS be going to V. In the FUT-II rules, the tense and passive suffixes
# are given directly to the rule. They could also be generated by
# forming the rule with the help of sub-rules for marking tense and
# diathesis.
#
#ACT-FUT-II: ((tul(en|et|ee|in|it|i)) (\w(INF-III)ILL))
#
#PASS-FUT-II: ((tul(laan|tiin)) (\w(INF-III)ILL))
#
# A sort of future tense is also included in the necessive structure, 
# i.e. the phrase which is formed with the verb "olla" 'be' marked
# personal endings combined with the passive participle form.
# The agent is marked with the genitive case form combined with the noun
# or with the genitive form of the pronouns: minun 'of I', etc.
#
NECESS: (on (PASS-PCPL-I))
# 
#
# 2.7.2. The progressive tense forms
# 
# The progressive tense forms are not considered as a grammatical 
# category in Finnish. However, progressive tense forms in English
# are directly translatable into Finnish. 
#
# (a) Present progressive (olla+PRES+PERS VERB+INF-III+INE: olen 
# laulamassa 'I am singing', hän on kirjoittamassa 'he was writing'.
#
# (b) Past progressive (olla+PAST+PERS VERB+INF-III+INE
# hän oli juoksemassa ‘he was running’.
#
# (c) Perfect, progressive (olla+PRES+PERS olla+PERF-II VERB+INF-III+INE
#  hän on ollut kirjoittamassa 'he has been writing'.
#
# (d) Pluperfect, progressive (olla+PAST+PERS olla+PERF-II 
# VERB+INF-III+INE: hän oli ollut kirjoittamassa ‘he had been writing’.
# writing, he had beeng talking)
#
#PRES-PROG: olla+PRES+PERS & VERB+INF-III+INE
#PAST-PROG: olla+PAST+PERS & VERB+INF-III+INE
#PERF-PROG: olla+PERF+PERS & (VERB+INF-III+INE
#PLU-PERF-PROG: olla+PLUPERF+PERS & VERB+INF-III+INE
#
ACT-TENSE: (ACT-PRES|ACT-PAST|ACT-PERF|ACT-PLUPERF)
#
PASS-TENSE: (PASS-PRES|PASS-PAST|PASS-PERF|PASS-PLUPERF)
#
VERB-FINITE: (ACT-TENSE|PASS|COND|POT|IMP) 
#
VERB-NON-FINITE: (INF|PCPL)
#
# C. Adjectives
# To be continued.
#
# D. Pronouns
# To be continued.
#
# E. Particles
# To be continued.
# 
# F. Conjunctions
# To be continued.
#
# III. Disambiguating temporal words from the database
#
INCLUDE: fin-disamb-TEMP-WORDS.spec
#
# IV. Prepositions
#
# II. ADPOS-CASE RELATORS: Case marking and adpositions in Finnish
#
# FIN.SPEC-rules: case marking and adpositions
# April 2, 2014: the last elements of abbreviations are replaced with 
# the minuscules used in the article in Table 6. The last elements in 
# the abbreviations presented before the groups with capital letters 
# are replaced with small letters (Suihkonen & Laaksonen, Table 6).
#
#1. Location of an object:

# IN, ON and OUT categories 
# In most cases, the adpositions in Finnish are postpositions, but also prepositions are found. The categories of adpositions: prepositons (PRP) and postpositoin (POP) are foremost syntactic categories.

#1.1. Location of an object in (IN), inside of a closed space (IN-PRP-A, 
# IN-POP-A) and inside a bordered space, in a group, 
# or between other objects (IN-PRP-B, IN-POP-B): 
#
IN-C: \wINE(POSS-SFX?CLT-SFX?)
IN-PRP-A: 
IN-POP-A: ((silmissä|sisäpuolella|sisässä|sisällä|sydämessä)
  (POSS-SFX?CLT-SFX?))
IN-PRP-B:  
IN-POP-B: ((joukossa|keskellä|parissa|perällä|seassa|välissä)
  (POSS-SFX?CLT-SFX?))
IN-ADP: (IN-POP-A|IN-POP-B)
INCLUDE: fin-disamb-IN-EXCL.spec
IN: (IN-C|IN-ADP)
#
#
#1.2. Location of an object on (ON) or in touch with the surface of an object 
# (ON-PRP-C, ON-POP-C), and outside of an object or a landmark, 
# not far from it (ON-PRP-D, ON-POP-D). 
# The adposition 'keskellä' is an example from on adpositions,
# which may occur in closed and open environments):
#
ON-C: \wADE(POSS-SFX?CLT-SFX?)
ON-PRP-C:
ON-POP-C: ((alla|huipulla|päällä|partaalla|partailla|pinnalla|
  pinnassa|pohjalla|pohjilla|reunassa|reunoissa|reunalla|reunoilla|
  vasten)(POSS-SFX?CLT-SFX?))
ON-PRP-D:
ON-POP-D: (((edessä|ohessa|ääressä|
  hännillä|jäljessä|juurella|juurilla|kannoilla|kintereillä|kohdalla|
  keskikohdalla|likellä|lähellä|luona|niskassa|paikalla|
  perässä|rinnalla|sivussa|sivuissa|sivulla|sivuilla|suulla|syrjässä|
  takana|välillä|vastapäätä|vieressä|yllä)(POSS-SFX?CLT-SFX?))|
  liki)
INCLUDE: fin-disamb-ON-EXCL.spec
ON-ADP: (ON-POP-C|ON-POP-D)
INCLUDE: fin-disamb-ON-C-EXCL.spec
ON: (ON-C|ON-ADP)

#1.3. Location of an object outside (OUT) of or at a distance from an object or
# a landmark (OUT-PRP-E, OUT-POP-F), and outside of another object, the distance 
# not specified (far or near)OUT-PRP-F and OUT-POP-F):
#
OUT-C: 
OUT-PRP-E: 
OUT-POP-E: ((äärellä|edellä|edustalla|kahtapuolen|kahtapuolin|kahtapuolta)|
  (keskivaiheilla|lähistöllä|lähettyvillä|liepeillä|lopussa|nurkalla|
  nurkilla|puolella|((ala|etu|ylä)puolella))(POSS-SFX?CLT-SFX?))
OUT-PRP-F:
OUT-POP-F: ((tienoilla|taholla|tahoilla)|(paikoilla|suunnassa|suunnalla|
  syrjässä|ulkopuolella|ulottumattomissa|ympärillä)(POSS-SFX?CLT-SFX?))
OUT-ADP: (OUT-POP-E|OUT-POP-F)
OUT: (OUT-ADP)
#
#2. Movement of an object from in, on, outside of another object (delocation):
# 2.1. Movement of an object from in (IN), inside of a closed space (DE-PRP-IN-A, 
# DE-POP-IN-A) and from inside a partly closed space or between other objects 
# (DE-IN-PRP-B, DE-IN-POP-B).
#
DE-IN-C: \wELA(POSS-SFX?CLT-SFX?)
DE-IN-PRP-A: 
DE-IN-POP-A: ((silmistä|sisäpuolelta|sisältä|sisästä|sydämestä)
  (POSS-SFX?CLT-SFX?))
DE-IN-PRP-B: 
DE-IN-POP-B: ((joukosta|keskeltä|keskestä|parista|perältä|seasta|
  välistä)(POSS-SFX?CLT-SFX?))
DE-IN-ADP: (DE-IN-POP-A|DE-IN-POP-B)
INCLUDE: fin-disamb-DE-IN-EXCL.spec
DE-IN: (DE-IN-C|DE-IN-ADP)

#2.2. Movement of an object from on smth: 
# Movement of an object from ON or in touch with the surface of an object 
# (DE-ON-PRP-C, DE-ON-POP-C), and to outside of an object or a landmark, 
# not far from them (DE-ON-C), DE-ON-PRP-D, DE-ON-POP-D).
#
DE-ON-C: \wABL(POSS-SFX?CLT-SFX?)
DE-ON-PRP-C:
DE-ON-POP-C: ((alta|hännästä|(huipu(lta|ilta))|juuresta|kohdasta|
  (kupee(sta|lta))|laelta|nenästä|nokasta|päältä|partaalta|perältä|
  (pinna(lta|sta))|(pohja(lta|sta))|(reun(alta|oilta))|(reun(asta|oista))|
  varresta|varsista)(POSS-SFX?CLT-SFX?))
DE-ON-PRP-D:  
DE-ON-POP-D: ((((keskikohda(lta|sta))|
  hänniltä|jäljestä|juurelta|juurilta|kintereiltä|
  läheltä|likeltä|niskasta|ohesta|
  perästä|rinnalta|(sivu(sta|ista|lta|ilta))|suulta|syrjästä|
  takaa|väliltä|vierestä|yltä)(POSS-SFX?CLT-SFX?))|
  (kohdalta|kohdaltani|kohdaltasi|kohdaltamme|kohdaltanne|
  kohdaltansa|kohdaltaan)|
  (edestä|edestäni|edestäsi|edestänsä|edestämme|edestänne|edestään|
  edestänsä)|
  (luota|luotani|luotasi|luotaan|luotansa|luotamme|luotanne))
DE-ON-ADP: (DE-ON-POP-C|DE-ON-POP-D)
INCLUDE: fin-disamb-DE-ON-EXCL.spec
DE-ON: (DE-ON-C|DE-ON-ADP)

# 2.3. Delocation of an object from outside of another object: 
# Movement outside, onto or in touch with the surface of an object or a landmark 
# (DE-OUT-PRP-E, DE-OUT-POP-E), and to outside of an object or a landmark, 
# not far from the, (DE-OUT-PRP-F, DE-OUT-POP-F). 
#
DE-OUT-C: 
DE-OUT-PRP-E: 
DE-OUT-POP-E: ((ääreltä|edustalta|kannoilta|keskivaiheilta|lähettyviltä|
  lähistöltä|liepeiltä|lopusta|nurkalta|nurkilta|
  puolelta|((ala|etu|ylä)puolelta))(POSS-SFX?CLT-SFX?))
DE-OUT-PRP-F: 
DE-OUT-POP-F: ((tienoilta|taholta|tahoilta|paikalta|paikoilta|suunnasta|
  suunnalta|syrjäastä|ulkopuolelta|ulottumattomista|ympäriltä)
  (POSS-SFX?CLT-SFX?))
DE-OUT-ADP: (DE-OUT-POP-E|DE-OUT-POP-F)
DE-OUT: (DE-OUT-ADP)
#
INCLUDE: fin-disamb-DE-OUT-EXCL.spec
#
#3. Add-location of an object into|onto|to outside of smth
#3.1. Movement of an object into, to inside of a closed space (DIR-IN-PRP-CL, 
# DIR-IN-POP-CL) and to inside a partly closed space or between other objects 
# (DIR-IN-PRP-BCL, DIR-IN-POP-BCL): 
#
AD-IN-C: \wILL(POSS-SFX?CLT-SFX?)
AD-IN-PRP-A:
AD-IN-POP-A: ((silmiin|sisään|sisälle|sisäpuolelle|sydämeen)
  (POSS-SFX?CLT-SFX?))
AD-IN-PRP-B:
AD-IN-POP-B: ((joukkoon|keskelle|pariin|sekaan|väliin|välii)
  (POSS-SFX?CLT-SFX?))
AD-IN-ADP: (AD-IN-POP-A|AD-IN-POP-B)
INCLUDE: fin-disamb-AD-IN-EXCL.spec
AD-IN: (AD-IN-C|AD-IN-ADP)
#
#3.2. Movement of an object on or in touch with the surface of another object 
# (DIR-ON-PRP-A, DIR-ON-POP-A), and outside of an object, not far from it 
# (DIR-ON-PRP-B and DIR-ON-POP-B). 
#
AD-ON-C: \wALL(POSS-SFX?CLT-SFX?)
AD-ON-PRP-C: 
AD-ON-POP-C: (((häntää|juuree|kupeesee|nenää|nokkaa|pohjaa|reunaa)
  (POSS-SFX))|
  ((alle|häntään|huipulle|huipuille|juureen|kohtaan|kupeeseen|
  nenään|nokkaan|partaalle|päälle|perään|pieleen|pohjaan|pohjalle|
  reunaan|reunalle|suuhun|suihin|varteen)(POSS-SFX?CLT-SFX?)))
AD-ON-PRP-D: 
AD-ON-POP-D: ((ääreen|eteen|hännille|jäljille|juurelle|
  juurille|kintereille|kohdalle|kupeelle|lähelle|
  likelle|luo|luokse|niskaan|oheen|paikalle|päähän|päihin|perälle|
  poskeen|rinnalle|sivulle|sivuille|sivuun|suulle|syrjään|
  taa|taakse|tykö|viereen|vierelle|ylle|yläpuolelle)(POSS-SFX?CLT-SFX?)|
  ((etee|niskaa|päähä|syrjää|välille|vieree)(POSS-SFX)))
AD-ON-ADP: (AD-ON-POP-C|AD-ON-POP-D)
INCLUDE: fin-disamb-AD-ON-EXCL.spec
AD-ON: (AD-ON-C|AD-ON-ADP)

#3.3. Movement of an object outside of the  object (DIR-OUT-PRP-C, DIR-OUT-POP-C), and 
# outside of an object, the distance or relationship with the object is not specified (AD-OUT-PRP-D and AD-OUT-POP-D). 
#
AD-OUT-PRP-E: 
AD-OUT-POP-E: ((äärelle|edelle|edustalle|kannoille|keskivaiheille|
  lähettyville|lähistölle|loppuun|iepeille|nurkalle|nurkille)
  (POSS-SFX?CLT-SFX?))
AD-OUT-PRP-F:
AD-OUT-POP-F: ((((etu|ulko)puolelle)|paikoille|suuntaan|suunnalle|
  syrjään|tahoille|taholle|tienoille|ulottumattomiin|ympärille)
  (POSS-SFX?CLT-SFX?))
AD-OUT-ADP: (AD-OUT-POP-E|AD-OUT-POP-F)
AD-OUT: (AD-OUT-ADP)
#
LOC: (IN|ON|OUT)
DE-LOC: (DE-IN|DE-ON|DE-OUT)
AD-LOC: (AD-IN|AD-ON|AD-OUT)
#
INCLUDE: fin-disamb-AD-OUT-EXCL.spec
#
#4. Translocation of an object with regard to through, along, over, 
# under and outside of another object. INT = internal, EXT = external.
#

#
TRNS-INT-C: 
TRNS-INT-PRP:
TRNS-INT-POP: ((halki|kautta|läpi|poikki)|((keskitse|sisäpuolitse)
  (POSS-SFX?CLT-SFX?)))
TRNS-INT: (TRNS-INT-POP)
#
TRNS-EXT-C: 
TRNS-EXT-PRP:
TRNS-EXT-POP: ((myöten|pitkin|ali|yli|ohi|kohti|kohden|asti|saakka)|
  ((alitse|alapuolitse|editse|kupeitse|vieritse|ohitse|
  päällitse|sivuitse|taitse|välitse|ylitse|yläpuolitse|ulkopuolitse)
  (POSS-SFX?CLT-SFX?)))
TRNS-EXT: (TRNS-EXT-POP)
TRNS: (TRNS-EXT|TRNS-INT)
#
INCLUDE: fin-disamb-ALL-EXCL.spec
#
#5. Terms denoting special temporal situations):
#5.1. Temporal; terms denoting points of time vaguely). 
#
TIME-C:
TIME-PRP: 
TIME-POP: (((aika(an|na))|(aiko(i(na|hin)))|
  (kynnykse(llä|ltä|lle))|(puoliväli(ssä|stä|in))|
  (keskivaihei(lla|lta|lle))|korvilla|
  vaiheilla|vaihteessa|(väli(llä|ltä|lle))|
  (jälke(inen|en|isenä|iseen|eni|esi|ensä|enmme|enne|eisenä|eiseen))|
  perästä)(CLT-SFX?))
TIME: (TIME-POP)
#
#5.2. Temporal: terms denoting beginning, end  points or limits of time (TIME-LIM). The translative case occurs with numerals denoting exact points of time and nouns denoting times, such as päivä 'day': 
#selkään ?
#(marked with the adessive, ablative, and allative case endings)
#
#6. CIRCUMSTANTIALS
#6.1. Basic conditions: agent, ground, source, origin, ingredient, states of
# affairs:
#
CIRC-PRP: 
#  eduksi|hyväksi|kiusaksi|varten|
#  vastoin|vuoksi|kera|kanssa|myötä|mukana|turviin|valtaan)
CIRC-POP: (((johtuen|johdosta|koskien|mukaan|mukaisesti|nojalla|
  nimessä|nimessäsi|nimessään|nimessänsä|nimeen|nimiin|
  perusteella|suhteesta|suhteen|suhteessa|aloitteesta|ansiosta|
  mielestä|määräyksestä|pakottamana|pakottamina|
  sijasta|sijaan|sijaasi|sijaansa|sijalle|sijallensa|
  johdolla|toimesta)|((eduks(i|e))|(hyväks(i|e))|(kiusa(ksi|kse|lla))|
  (mieliks(i|e))|mieleen|takia|tautta|tavoin|tähden|täydeltä|varten|
  (vara(kse|ksi|lla|lle|an))|tähte|vuoksi|vuokse)|
  (armoi|avu(lla|llani|llasi|llaan|llamme|llanne|llansa))|
  (hoiva(ssa|sta))|hoiviin|(hoima(ssa|sta))|
  (hotei(ssa|ista|siin))|
  (huoma(ssa|sta|an|asi|ansa))|
  (huosta(ssa|sta|an|asi|ssasi))|
  kanssa|(keske(nään|nänne|nänsä))|
  (kera(lla|llani|llasi|llaan|llansa))|
  (käsi(ssä|issään|issäni|issäsi|issänne|stä|istä|istäni|istäsi|istään|
  istänne|istänsä|istänsä|in|ini|isi|insä|imme))|(kynsi(ssä|stä|in))|
  muassa|(muka(na|an|ani|asi|ansa|amme))|myötä|
  (valla(ssa|sta))|(valta(an|anne|ansa))
  (turvi(ssa|sta|in|ini|ssansa))|
  (voima(lla|llani|llasi|llaan|llansa|llamme|llanne))|
  (yhteyde(ssä|stä))|(yhteyte(en|ensä))|
  lisäksi|ilman|paitsi|vastoin|vastuksinta|
  (armo(illa|sta))|huolimatta|kustannuksella|(lisäks(i|e))|
  lukuunottamatta|(sija(an|ssa|sta))|suhteessa|
  (tasa(lla|lle))|(tila(lla|lta|lle))|uhalla|vailla|
  kaltainen|(kaltaise(ksi|kse))|(näköinen|näköise(ksi|kse))|
  suuruinen|suuruise|suuruiseksi|suuruisekse|
  vertainen|vertaista)(POSS-SFX?CLT-SFX?))
CIRC: (CIRC-POP)
#
#BASE-C:

# 1.Cause reason, motive, stimulus, reaction, 
#  purpose, target, manners, means, instruments: 
# kautta: esim. "Mooseksen kautta", tai "erämaan kautta"
# 4. Support, accompaniment, close relationship:
# 3. Hindrance, opposition, standards, measurements, strengthening 
# expressions, exceptions, negative condition, partiality or involvement 
# in an eventuality: 
#
#
TW-IN-EXCL: (IN-EXCL)
TW-DE-IN-EXCL: (DE-IN-EXCL)
TW-AD-IN-EXCL: (AD-IN-EXCL)
TW-ON-EXCL: (ON-EXCL)
TW-ON-C-EXCL: (ON-C-EXCL)
TW-DE-ON-EXCL: (DE-ON-EXCL)
TW-AD-ON-EXCL: (AD-ON-EXCL)
TW-OUT-EXCL: (xyz)
TW-DE-OUT-EXCL: (DE-OUT-EXCL)
TW-AD-OUT-EXCL: (AD-OUT-EXCL)
TW-TRNS-EXCL: (xyz)
#TW-TIME-EXCL: (xyz)
#TW-CIRC-EXCL: (xyz)
TW-ALL-EXCL: (ALL-EXCL)
#
#
END: 
