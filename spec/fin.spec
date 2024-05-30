# Pirkko Suihkonen, 2006-2008, 2014, 2016-2017.
# Copyright: Pirkko Suihkonen
# Final version of the text describing the rules: 2024.
# The Perl scripts for the analysis of the database and also comments 
# on the guidelines of the Regular Expressions: Jorma Laaksonen.
#
# Name of the language: Finnish		
# The family: Uralic languages	
# The sub-branch: Baltic-Finnic languages
# Language code, ISO 639: fin
#
# The name of the project: 
# The ADPOS-CASE categories in Finnish and English. 
# The main goal of the project: 
# Parallel research of English and Finnish ADPOS-CASE relators.
#
# The data: Raamattu (The Bible). Vanha testamentti (The Old Testament). 1933.
# Uusi testamentti (The New Testament). 1938.
#
# Grammatical rules are defined as Regular Expressions. 
# The focus of the rules is on ADPOS-CASE relators (prepositions
# in English and adpositions and case marking in Finnish)
# and their occurrences in the text.
# The rules do not deal with the first and second arguments.
# 
#
#
# LITERATURE ON THE BACKGROUND OF THE PROJECT (examples):
#
# Hakulinen, Auli and Fred Karlsson. 1979. Nykysuomen lauseoppia
# (Syntax of the Modern Finnish)
# [Suomalaisen Kirjallisuuden Seuran Toimituksia (SKST) 350].
# Helsinki: Suomalaisen Kirjallisuuden Seura.
#
# Hakulinen, Lauri. 1968. Suomen kielen rakenne ja kehitys
# (The Structure and Development of the Finnish Language).
# Helsinki: Kustannusosakeyhti� Otava.
#
# Iivonen, Antti, Mari Horppila, Miika Heikkonen and Olli Rissanen (eds).
# 2000. Fonetiikan perussanasto. Helsingin yliopisto.
# https://helda.helsinki.fi/bistream/handle(10224/3513/index.htm. (2016)
#
# Karlsson, Fred. 1983[1982]. Suomen kielen ��nne- ja muotorakenne
# (Phonological and Morphological Structure of the Finnish Language.
# Porvoo/Helsinki/Juva: Werner S�derstr�m Osakeyhti�.
#
# Karlsson, Fred. 1987. Finnish Grammar. 
# Porvoo/Helsinki/Juva: Werner S�derstr�m Osakeyhti�.
#
# Koskenniemi, Kimmo. 1983. Two-level Morphology: A General Computational Model
# for Word-Form Recognition and Production [Publications, 11].
# University of Helsinki, Department of General Linguistics.
#
# Koskenniemi, Kimmo. 1990. Finite-State parsing and disambiguation.
# In Hans Karlgren (ed.). Coling-90. Papers presented in the 13th International
# Conference on Computational Linguistics on the occasion of the 25th
# Anniversary of COLING and the 350th Anniversary of Helsinki University, 2.
# 229-242. Helsinki: Yliopistopaino.
#
# Laaksonen, Kaino and Anneli Lieko. 1998. Suomen kielen ��nne- ja muoto-oppi
# (Phonetics and Morphology of the Finnish Language).
# Helsinki: Oy Finn Lectura Ab.
#
# Penttil�, Aarni. 1963. Suomen kielioppi (The Finnish Grammar).
# Porvoo|Helsinki: Werner S�derstr�m Osakeyhti�.
#
# Quirk, Randolph & Sidney Greenbaum, 1996[1973]. 
# A University Grammar of English. 
# Edinburg/Essex: Addison Wesley Longman Limited.
#
# Suihkonen, Pirkko. 2007. On Quantification in Finnish [Lincom Studies
# in Uralic Languages, 02]. Muenchen: Lincom GmbH. 
#
# Tuomi, Tuomo (ed.). 1980. Suomen kielen k��nteissanakirja
# (Reverse Dictionary of Modern Standard Finnish)
# [Suomalaisen Kirjallisuuden Seuran Toimituksia, 274].
# Helsinki: The Finnish Literature Society.
#
# Webster's Ninth New Collegiate Dictionary. 1989.
# Springfield, Massachusetts, U.S.A.: Merriam-Webster Inc., Publishers.
#
# Webster's Dictionary 1828. http://www.webstersdictionary1828.com/.
# (Aug. 2023)  
#
# More information on the project and references, cf. 
# Suihkonen, Pirkko and Jorma Laaksonen. 2024. Syntax and Semantics of
# Adpositions and Case Marking: Descriptions of Prepositions in English and
# Adpositions and Case Marking in Finnish within the Framework of a Parallel
# Database [Lincom Studies in Theoretical Linguistics, 69]. Muenchen: LINCOM GmbH.
#
#
#
# THE RULES FOR THE ANALYSIS OF THE DATABASE
#
# I. PHONOLOGY
#
# 1. The sound systems
#
# 1.1. Consonants and sequences of consonant:
# (consonant gradation: C-SGR = strong grade, C-WGR = weak grade):
#
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
#
#1.2. Vowels (and sequences of vowels)
#
# Single vovels (B = back, F = front, EI = the vowels e and i);
#
VB: (a|o|u)
VF: (y|�|�)
VEI: (e|i)
V: (VB|VF|VEI)
#
# Diphtongs (I = the diphtongs ending with i):
#
DIPH-B: (au|uo|ou|eu|iu|ia)
DIPH-F: (�y|y�|�y|ey|iy|ie)
DIPH-I: (yi|�i|�i|ui|oi|ai|ei)
DIPH: (DIPH-B|DIPH-F|DIPH-I)
#
# Long vowels (L = long vowel, VEI-L = long e and i, 
# VI-PL = long i (ii)):
#
VB-L: (aa|oo|uu)
VF-L: (yy|��|��)
VEI-L: (ee|ii)
VI-PL: (ii)
VL: (VB-L|VF-L|VEI-L|VI-PL)
#
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
# The second and the fourth syllables are unstressed;
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
# II. MORPHOLOGY AND LEXICON
#
# 1. The parts of speech system:
#
# The parts of speech system: nouns, adjectives, pronouns, numerals, 
# verbs, particles (including prepositions and adverbs) and
# conjunctions.
#
#
# 1.1. Nouns (not included)
#
#
# 1.2. Adjectives (not included
#
#
# 1.3. Pronouns
#
# PRON-POSS = the genitive forms of personal pronouns):
#
PRON-PERS: (min�|sin�|h�n|me|te|he)
PRON-ACC: (minut|sinut|h�net|meid�t|teid�t|heid�t|kenet)
PRON-POSS: (minun|sinun|h�nen|meid�n|teid�n|heid�n)
PRON-REFL: ((min�|sin�|h�n|me|te|he) itse)
PRON-DEM: (t�m�|tuo|se|n�m�|nuo|ne)
PRON-INTR: (kuka|kukaan|kukin|mik�|mikin|mik��n|ken|kenk��n|
  kumpi|kumpikin|kumpikaan|kumpainenkin|kumpainenkaan)
PRON-REL: (joka|kuka|mik�)
PRON-Q: (yksi|joka|joku|er�s|toinen|muu|muutama|muutamat|sama|
  jompikumpi|kumpikin|kumpikaan|kumpainenkin|kumpainenkaan|
  kukin|kukaan|mikin|mik��n|
  jokainen|kukin|molemmat|kaikki|
  moni|monet|monta|usea|useat|useampi|useimmat)
PRON-REC: ((toinen toisensa)|(toinen toistaan))
PRON-ADV: (t��ll�|tuolla|siell�|miss�|kaikkialla)
#
PRON: (PRON-PERS|PRON-ACC|PRON-POSS|PRON-REFL|PRON-DEM|PRON-INTR|
  PRON-REL|PRON-Q|PRON-REC|PRON-ADV)
#
#
# 1.4. Numerals (not included) 
#
# 1.4.1. Cardinals
#
# 1.4.2. Ordinals
#
# 1.4.3. Fractions
#
#
# 1.5. Verbs (not included; cf. section IV)
#
#
# 1.6. Particles (lists, not included)
#
# 1.6.1. Particles in the lexicon
#
# 1.6.2. Clitic particles
#
#
# 1.7.Conjunctions (not included)
#
# 1.7.1. Coordinative conjunctions
#
# 1.7.2. Subordinative conjunctions 
#
#
# 1.8. Articles (not available)
#
#
# 2. Word formation
# 
# In Finnish, affixation forms the main means in developing and modifying
# lexicon.
#
#
# 2.1. Word stems
#
# 2.1.1. Stem types of nouns
#
# The stem types: (a) consonant stems and (b) weak and (c) strong vowel stems.
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
# Stem types of nouns: 
# 
STEM-AOU: \w((C|CC)(a|�|o|�|u|y))
STEM-I: \w((C|CC|CCC)i)
STEM-IE: \w(((C|CC|CCC)(i|e)))
STEM-VVC-S: w(((V)()(V)()C-S)(i|e))
STEM-TI: \w(((e|�i)()(s|rs|d|rr|t|rt))(i|e))
STEM-MPI: \w(e(mpi|mpa|mp�|mma|mm�))
STEM-EK: \w(ee|et)
STEM-E: \w(ke|le)
STEM-NEN: \w(nen|se|s)
STEM-KSE: \w(s|kse)
STEM-A: \w(s|as)
STEM-DE: \w(s|de|te|t)
STEM-NNE: \w(s|t|nne|nte|ns)
STEM-ME: \w(n|me)
STEM-TON: \w(n|ttoma|ttom�)
STEM-MM: \w(n|mpa|mma|mp�|mm�)
STEM-LE: \w(n|le|ne|re)
STEM-EE: \w(t|ee)
STEM-UT: \w(ut|yt|ue|ye)
STEM-AT: \w(�t|��|es|ehe)
#
#
# 2.1.2. Stem types of verbs
#
STEM-VA: \w((SYLL)()(C)()(V))
STEM-CONTR: \w((C)()(V)()(C))
STEM-ITA: \w((it)|(in)|(itse))
STEM-ETA: \w((et|((e)ne)))
STEM-DA-I: \w((VL)|(DIPH))
STEM-DA-II: \w((i|u|b|d|k|l|m|n|p|s|t|v)(oi|�i)) 
# 
STEM-LA-NA-RA-SE: \w((l|n|r|s)(e))
#
STEM-VOW: (STEM-VA|STEM-CONTR|STEM-ITA|STEM-ETA|STEM-DA-I|STEM-DA-II|
  STEM-LA-NA-RA-SE)
#
#
# 2.2. Prefixes in word formation, examples:
#
# Negative prefixes:
PREF-NEG: (ei|ep�)
# Locative prefixes:
PREF-LOC: (yli|ali|etu|taka|et�|l�hi|j�lki|sis�|ulko|haja)
# Number prefixes:
PREF-NB: (uni|mono|bi|di|multi|poly)
# Other prefixes
PREF-OT: (esi|vara|oma|iki)
#
#
# III. INFLECTIONAL MORPHOLOGY
# 
# 1. Nominal morphology
#
# 1.1. Number
#
# The numbers are singular and plural. 
#
# 1.1. Singular
#
# Singular is unmarked. 
#
# 1.2. Plural: 
#
PL-T: (V()t)
PL-J: (V()j()(a|�|en))
PL-JP: (V()j()(a|�|e))
PL-I: ((C|V)()i)
PL: (PL-T|PL-J|PL-JP|PL-I)
#
#
# 2. Possession marking
#
# Possession in Finnish is expressed with the genitive forms 
# and possessive suffixes. 
# The rule POSS-C contains the genitive forms of the personal pronouns
# and the interrogative pronouns ken (who)and mik� (what). 
#
POSS-C: (minun|sinun|h�nen|meid�n|teid�n|heid�n|kenen|keiden|mink�)
#
# Possessive suffixes
# The suffixes which are located after the case endings:
#
POSS-SFX-B: \w(ni|si|mme|nne|an|nsa|en)
POSS-SFX-F: \w(ni|si|mme|nne|�n|ns�|en)
POSS-SFX: \w(POSS-SFX-B|POSS-SFX-F)
POSS-SFX-BV: \w(ni|si|mme|nne|nsa)
POSS-SFX-FV: \w(ni|si|mme|nne|ns�)
POSS-SFX-V: \w(POSS-SFX-BV|POSS-SFX-FV)
#
#
#
# 3. Case marking
#
# Case marking deals with nominals and verbal nominal forms.
# Case marking is used as a partial method also in adpositional system.
# Adpositions are used side by side of case marking.
#
#
# 3.1. Nominative 
#
# Nominative is unmarked. Nominative is distinguished in the singular
# and plural forms.
#
#
# 3.2. Accusative
#
# The formal accusative case have the following forms: -0 (zero), -n, -t
# (for the case of disambiguation, cf. sections 1.2., 3.1. and 3.3.).
# On the accusative, cf. e.g. Hakulinen 1968: 85-86; Karlsson 1987: 94-98.
# The rules do not concern the accusative (on marking the semantically
# closed second arguments, cf. Suihkonen 2007).
# In the rules, the accusative is marked in the following pronouns:
# minut|sinut|h�net|meid�t|teid�t|heid�t|kenet. 
#
ACC: (minut|sinut|h�net|meid�t|teid�t|heid�t|kenet)
#
#
# 3.3. Genitive: SG: -n; PL: -den, -tten, -en, -in, -ten
#
GEN-SG: \w(((SYLL-OP)?())<n>)
GEN-PL-C: \w(((SYLL-CL)?()<ten>))
GEN-PL-P-C: \w(((SYLL-CL)?())(<te>)(POSS-SFX))
GEN-PL-EN: \w(V()(i|j)()<en>)
GEN-PL-P-EN: \w((V()(i|j)<e>)(POSS-SFX))
GEN-PL-IN: \w(V()(a|e|o|u|y|�|�)()<in>)
GEN-PL-P-IN: \w((V()(a|e|o|u|y|�|�)<i>)(POSS-SFX))
GEN-PL-DT: \w((DIPH|PL-I)()(<den>|<tten>))
GEN-PL-P-DT: \w((DIPH|PL-I)(<de>|<tte>)(POSS-SFX))
GEN: (GEN-SG|GEN-PL-C|GEN-PL-P-C|GEN-PL-EN|GEN-PL-P-EN|GEN-PL-IN|
  GEN-PL-P-IN|GEN-PL-DT|GEN-PL-P-DT)
#
#
# 3.4. Partitive: -a, -�, -ta, -t�
#
PTV-B: \w((((SYLL)?C()VB)|((SYLL)?C()VB()j))<a>)
PTV-F: \w((((SYLL)?C()VF)|((SYLL)?C()VF()j))<�>)
PTV-TB: \w(C|SYLL-CVV|(SYLL()SYLL)|(SYLL()SYLL()SYLL)<ta>)
PTV-TF: \w(C|SYLL-CVV|(SYLL()SYLL)|(SYLL()SYLL()SYLL)<t�>)
PTV-TB-LD: \w(((SYLL)?()SYLL-CVV)|((SYLL)?()SYLL)<ta>)
PTV-TF-LD: \w(((SYLL)?()SYLL-CVV)|((SYLL)?()SYLL)<t�>)
PTV-TB-VS: \w(((((SYLL)?()SYLL)VB)ta)<ta>)
PTV-TF-VS: \w(((((SYLL)?()SYLL)VF)ta)<t�>)
PTV: \w(PTV-B|PTV-F|PTV-TB|PTV-TF|PTV-TB-LD|PTV-TF-LD|PTV-TB-VS|PTV-TF-VS)
#
#
# 3.5. Essive: -na, -n�
#
ESS-B: \w(<na>)(POSS-SFX?CLT-SFX?)
ESS-F: \w(<n�>)(POSS-SFX?CLT-SFX?)
ESS: \w(ESS-B|ESS-F)
INCLUDE: fin-disamb-ESS.spec
#
#
# 3.6. Translative: -kse, -ksi
#
TRL-E: \w(<kse>)(POSS-SFX?CLT-SFX?)
TRL-I: \w(<ksi>)(POSS-SFX?CLT-SFX?)
TRL: \w(TRL-E|TRL-I)
INCLUDE: fin-disamb-TRL.spec
#
#
# 3.7. Inessive: -ssa, -ss�
#
INE-B: \w(<ssa>)(POSS-SFX?CLT-SFX?)
INE-F: \w(<ss�>)(POSS-SFX?CLT-SFX?)
INE: \w(INE-B|INE-F)
#
#
# 3.8. Elative: -sta, -st�
#
ELA-B: \w(<sta>)(POSS-SFX?CLT-SFX?)
ELA-F: \w(<st�>)(POSS-SFX?CLT-SFX?)
ELA: \w(ELA-B|ELA-F)
#
#
# 3.9. Illative: -Vn, -hVn, -seen, and -siin
#
ILL-SE-P: \w((((C)*()(V)*(VL))<see>)(POSS-SFX-V))(CLT-SFX?)
ILL-SE: \w(((C)*()(V)*(VL))<seen>)(POSS-SFX?CLT-SFX?)
ILL-SV-P: \w(((((V)(C)|(CC))*()(DIPH-I))<sii>)(POSS-SFX-V))(CLT-SFX?)
ILL-SV: \w((((C)|(CC))*()(DIPH-I))<siin>)(POSS-SFX?CLT-SFX?)
ILL-VBF-P: \w((((a|o|u|y|�|�|e|i)*
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
  (a<a>|o<o>|u<u>|y<y>|�<�>|�<�>|e<e>|i<i>))(POSS-SFX))(CLT-SFX?)
ILL-VBF: \w(((a|o|u|y|�|�|e|i)*
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
  (a<an>|o<on>|u<un>|y<yn>|�<�n>|�<�n>|e<en>|i<in>))(POSS-SFX?CLT-SFX?)
ILL-HBF-P: \w((((V)|(VL)|(DIPH))
  (<ha>|<ho>|<hu>|<hy>|<h�>|<h�>|<he>|<hi>))(POSS-SFX-V))(CLT-SFX?)
ILL-HBF: \w(((V)|(VL)|(DIPH))
  (<han>|<hon>|<hun>|<hyn>|<h�n>|<h�n>|<hen>|<hin>))(POSS-SFX?CLT-SFX?)
ILL: \w(ILL-SV-P|ILL-SV|ILL-VBF|ILL-VBF-P|ILL-SE-P|ILL-SE|
  ILL-HBF-P|ILL-HBF)
#
#
# 3.10. Adessive: -lla, -ll�
#
ADE-B: \w(<lla>)(POSS-SFX?CLT-SFX?)
ADE-F: \w(<ll�>)(POSS-SFX?CLT-SFX?)
ADE: \w(ADE-B|ADE-F)
#
#
# 3.11. Ablative: -lta, -lt�
#
ABL-B: \w(<lta>)(POSS-SFX?CLT-SFX?)
ABL-F: \w(<lt�>)(POSS-SFX?CLT-SFX?)
ABL: \w(ABL-B|ABL-F)
#
#
# 3.12. Allative: -lle
#
ALL: \w(<lle>)(POSS-SFX?CLT-SFX?) 
#
#
# 3.13. Abessive: -tta, -tt� 
#
ABE-B: \w(<tta>)(POSS-SFX?CLT-SFX?)
ABE-F: \w(<tt�>)(POSS-SFX?CLT-SFX?)
ABE: \w(ABE-B|ABE-F)
#
#
# 3.14. Instructive: -n (not included)
#
#
# 3.15. Comitative: -ne
#
COM: \w((PL-I)?()<ne>)
#
#
# Case
#
CASE: \w(GEN|PTV|ESS|TRL|ADE|ABL|ALL|INE|ELA|ILL|ABE|COM)
#
#
# 3.16. Particles
# 3.16.1. Clitic particles
#
CLT-SFX-B: \w(kin|han|kaan|ko|pa)
CLT-SFX-F: \w(kin|h�n|k�|k��n|k�|p�)
CLT-SFX: \w(CLT-SFX-B|CLT-SFX-F)
#
#
#
# IV. INFLECTION OF VERBS
#
# The verbs in the database are introduced from the file fin-verbs.txt 
# to the kwic-file for processing operations. The verbs are used with
# the help of the file INCLUDELIST.
#
#
# 1. The verbs examined on the project
#
#VERB-DATA: VERB-LIST 
#INCLUDELIST: VERB-LIST-NON-FINITE
#INCLUDELIST: FIN-VERBS-BASIC
#
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
INCLUDELIST: fin-verbs-test-olla.txt VERB-TEST-OLLA
INCLUDELIST: fin-verbs-test-virrata.txt VERB-TEST-VIRRATA
INCLUDELIST: fin-verbs-test-vieda.txt VERB-TEST-VIEDA
INCLUDELIST: fin-verbs-test-tuoda.txt VERB-TEST-TUODA
INCLUDELIST: fin-verbs-test-menna.txt VERB-TEST-MENNA
INCLUDELIST: fin-verbs-test-tulla.txt VERB-TEST-TULLA
#
INCLUDE: fin-disamb-VERBS-EXCL.spec
#
INCLUDELIST: fin-verbs-som.txt VERB-TEST-@ 
#
#
# 2. Verbal nominal forms
# 2.1. Infinitives
#
# The verbs in the Finnish database are collected in the list called
# fin-verbs.txt.  In the list, the dictionary forms are marked with
# the character "#".
# The infinitive forms in Finnish are marked with suffixes:
#
INF-I: \w(((STEM-C)|(STEM-V-S))()((a|�|da|d�|la|l�|na|n�|ra|r�|ta|t�)))
INF-II: \w((((STEM-C)|(STEM-V-S))()(e(de|le|ne|re|te)))(INE-F|INE-B))
INF-III-B: \w(((STEM-V-S)()(ma|mi))()(INE-B|ADE-B|ELA-B|ILL-VBF|ILL-HBF))
INF-III-F: \w(((STEM-V-S)()(m�|mi))()(INE-F|ADE-F|ELA-F|ILL-VBF|ILL-HBF))
INF-III: \w(INF-III-B|INF-III-F)
INF-IV: \w((STEM-V-S)()((minen)|(mis)()(PTV)))
INF-V: \w(((STEM-V-S)()(maisilla|m�isill�))()(POSS-SFX))
VERB-BE-INF-I: ((ol)la)
INF: \w(INF-I|INF-II|INF-III-F|INF-III-B|INF-IV|INF-V|VERB-BE-INF-I)
#
# INF from the verbs in the database: fin-INF.
#
# 2.2. Participles
#
# ACT-PCPL-I and ACT-PRPL-II:
#  
ACT-PCPL-I-VA: \w((STEM-VA)(va|v�))
ACT-PCPL-I-CONTR: \w((STEM-CONTR)(va|v�))
ACT-PCPL-I-ITA: \w((STEM-ITA)(va|v�))
ACT-PCPL-I-ETA: \w((STEM-ETA)(va|v�))
ACT-PCPL-I-DA-I: \w((STEM-DA-I)(va|v�))
ACT-PCPL-I-DA-II: \w((STEM-DA-II)(va|v�))
ACT-PCPL-I-LA-NA-RA-SE: \w((STEM-LA-NA-RA-SE)(va|v�))
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
# AGENT PCPL:
#
ACT-PCPL-AG-B: \wma(INE-B|ADE-B|ELA-B|ABL-B|ALL|ILL-VBF|ILL-HBF) 
ACT-PCPL-AG-F: \wm�(INE-F|ADE-F|ELA-F|ABL-F|ALL|ILL-VBF|ILL-HBF)
ACT-PCPL-AG-PL: \wmi(INE-F|ADE-F|ELA-F|ABL-F|ALL|ILL-VBF|ILL-HBF)
ACT-PCPL-AG: (ACT-PCPL-AG-B|ACT-PCPL-AG-F|ACT-PCPL-AG-PL)
#
# PCPL-NEG:
#
ACT-PCPL-NEG: \w(V()((maton|m�t�n)|((mattoma|m�tt�m�)()(CASE))))
ACT-PCPL: (ACT-PCPL-I|ACT-PCPL-II|ACT-PCPL-AG|ACT-PCPL-NEG)
#
# PASS-PCPL-I-SG and PASS-PCPL-I-PL:
#
PASS-PCPL-I-SG: \w(((VL|DIPH|STEM-V-S)(ta|t�))(va|v�))
PASS-PCPL-I-PL: \w(((VL|DIPH|STEM-V-S)(ta|t�))(v(i))
		   (INE-F|ADE-F|ELA-F|ABL-F|ALL|ILL-VBF|ILL-HBF))
PASS-PCPL-I: \w(PASS-PCPL-I-SG|PASS-PCPL-I-PL)
#
# PASS-PCPL-II and PASS-PCPL-II:
#
PASS-PCPL-II-S: \w((VL|DIPH|STEM-LA-NA-RA-SE)(du|dy|lu|ly|ru|ry|tu|ty|u|y)
  (i)(INE-F|ADE-F|ELA-F|ABL-F|ALL|ILL-VBF|ILL-HBF))
PASS-PCPL-II-L: \w((VL|DIPH|V)(ttu|tty|tu|ty))
PASS-PCPL-II: (PASS-PCPL-II-S|PASS-PCPL-II-L)
#
# PASS-PCPL:
#
PASS-PCPL: (PASS-PCPL-I|PASS-PCPL-II)
# 
# PCPL:
#
PCPL: (ACT-PCPL|PASS-PCPL)
#
#
2.3. Personal inflection
#
VERB-1SG: \w((V)()(n))
VERB-2SG: \w((V)()(t))
VERB-3SG: \w((V)()(V))
VERB-1PL: \w((V)()(mme))
VERB-2PL: \w((V)()(tte))
VERB-3PL: \w((V)()(vat|v�t))
VERB-PERS-I: (VERB-2SG|VERB-3SG|VERB-1PL|VERB-2PL|VERB-3PL)
VERB-PERS-II: (VERB-2SG|VERB-1PL|VERB-2PL|VERB-3PL)
#
VERB-PERS: (VERB-PERS-I|VERB-PERS-II)
#
#
# 2.4. Auxiliaries 
#
# Auxiliaries "olla" and "ei":
#
VERB-AUX-PRES: (olen|olet|on|olemme|olette|ovat)
VERB-AUX-PAST: (olin|olit|oli|olimme|olitte|olivat)
VERB-AUX-COND: (olisin|olisit|olisi|olisimme|olisitte|olisivat)
VERB-AUX-IMP:  (olkoon|oltakoon|olko)
VERB-AUX-PASS-PRES: (on PASS-PCPL-II)
VERB-AUX-PASS-PAST: (oli PASS-PCPL-II)
VERB-AUX-NEG: (en|et|ei|emme|ette|eiv�t|eih�n|eik�|eik�|eik�h�n|eip�|eiv�th�n|
  eiv�tk�|eiv�tk�|emmek�|emmek�|enh�n|eth�n|etk�|etk�|
  �l�|�lk��|�lk��n|�lk��mme|
  ellen|ellet|ellei|ellemme|ellette|elleiv�t|
  jollen|jollet|jollei|jollemme|jollette|jolleiv�t)
VERB-AUX: (VERB-AUX-PRES|VERB-AUX-PAST|VERB-AUX-COND|VERB-AUX-IMP|
  VERB-AUX-PASS-PRES|VERB-AUX-PASS-PAST|VERB-AUX-NEG)
#
#
VERB-MOD: (haluta|halua|haluaa|haluaako|haluaisimme|haluaisin|haluamme|
  haluan|haluat|haluatte|haluavat|halusi|halusimme|halusimmekin|
  osata|osaa|osaan|osaatko|osaatte|osaavat|osaisi|osaisinko|osaisitko|
  osaisimme|osaisitte|osaisivat|osanneet|osannut|osata|
  pit��|pit�isi|pit�nee|pid�|pit��kin|pit��k�|pit��k�h�n|pit�isi|pit�isik�|
  pit�isik�h�n|pit�nyt|piti|pitih�n|pitik�|pit�nee|
  tahtoa|tahdo|tahdoimme|tahdoin|tahdoit|tahdoitte|tahdomme|tahdommeko|
  tahdon|tahdonpa|tahdot|tahdotko|tahdotte|tahdotteko|tahdottiin|
  tahdota|tahtoen|tahtoi|tahtoiko|tahtoisi|tahtoisimme|tahtoisin|
  tahtoisinkaan|tahtoisinkin|tahtoisinpa|tahtoivat|tahtomatta|
  tahtoneet|tahtonut|tahtoo|tahtooko|tahtovan|tahtovansa|tahtovat| 
  t�ytyy|t�ytyisi|t�ytynee|t�tyi|t�ytyisi|t�ytynyt|t�ytyy|t�ytyyh�n|
  t�ytyyk�|t�ytyyp�|
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
# Negation: NEG (the rules are not activated)
#
#
ACT-BE: (ACT-BE-PRES-PERS|ACT-BE-PAST-PERS|ACT-BE-COND-I|
  ACT-BE-COND-II|ACT-BE-POT-I|ACT-BE-POT-II)
#
ACT-BE-HAVE: (ACT-BE)
#
AUX: (ACT-BE-HAVE)
#
# 
# 2.5. Diathesis
#
# 2.5.1. Active
#
# Active is unmarked.
#
#
# 2.5.2. Passive
#
# The passive is formed with the suffixes +ta+/+t�+.
# Realization of the passive is dependent on the context of the passive suffix
# (+ta+, +t�+, +da+, +d�+, +la+, +l�+, etc.)
#
#
# 2.5.1. Rules for forming passive forms:
#
PASS-I: \w(((((V)()(V))|(C))()(ta|t�|da|d�|la|l�|na|n�|ra|r�|a|�))()
  (an|�n|in))
#
PASS-II: \w((((C)()(V))()(tta|tt�|ta|t�))()((an|�n|in)))
#
PASS: (PASS-I|PASS-II)
#
PASS-PRES: ((PASS-I|PASS-II)(V|koon|k��n))
PASS-PAST: ((PASS-I|PASS-II)i)
PASS-PERF: (on (PASS-PCPL-II|PASS-PCPL-II))
PASS-PLUPERF: (oli (PASS-PCPL-II|PASS-PCPL-II))
#
#  
# 2.6. Moods
#
# The grammatical moods in Finnish are indicative, conditional, 
# potential and imperative. Indicative is unmarked. The other moods
# are marked with category suffixes. The words in the indicative, imperative,
# and potential are marked with tense categories which are present 
# (unmarked), past (called as imperfect in the grammars), perfect, and
# pluperfect.  
#
#
# 2.6.1. Indicative:
#
# Indicative in Finnish is not marked formally.
#
#  
# 2.6.2. Conditional: 
#
# Conditional in Finnish is formed with the suffix +isi+ which in 
# simple conditional form (ACT-COND-I) is connected to the lexical verb, and
# in the periphrastic conditional form (ACT-COND-II) to auxiliary "olla"
# and the lexical verb is in the second participle form.
# In the passive form, the passive marker (suffix) precedes
# the conditional suffix.
#
ACT-COND-I: \w(((STEM-V-S)()isi)()(VERB-PERS-II))
#
# COND-PERF (COND-II): 
#
ACT-COND-II: \w(ACT-BE-COND-I ACT-PCPL-II)
#
ACT-COND: (ACT-COND-I|ACT-COND-II)
#
# PASS-COND:
#
VERB-PASS: \w((PASS-I)|(PASS-II)()(an|�n|in))
#
PASS-COND-I: \w((((STEM-V)()(PASS-I|PASS-II))()(isi))()(VERB-PASS))
#
# PASS-COND-PERF:
#
PASS-COND-II: (olisi (PASS-PCPL-II))
#
PASS-COND: (PASS-COND-I|PASS-COND-II)
#
COND: (ACT-COND|PASS-COND)
#
#
# 2.6.3. Potential:
#
# Potential is formed with the suffix -ne- (men+ne+e). 
# In the case that the stem consonant is -l, -r-, or -s-, the potential suffix
# has the forms -le, -re- and -se- (tul+le-e, etc.) (ACT-POT-I).
# The potential form of verb "olla" (to be) is "liene" marked with personal endings.
# It is also used as the auxiliary form with the past participle form (PCPL-II)
# in forming the perfect tense form (ACT-POT-II).
# In the passive form, the passive suffix precedes the potential suffix.
#
ACT-POT-I: \w(((STEM-V-S|STEM-C)()(le|ne|re|se))VERB-PERS-I)
ACT-POT-II: \w(((liene)VERB-PERS-I)ACT-PCPL-II)
ACT-POT: (ACT-POT-I|ACT-POT-II)
#
PASS-POT-I: (((PASS-I)|(PASS-II))()(VERB-PASS))
PASS-POT-II: ((liene)(VERB-PASS) (PASS-PCPL-II|PASS-PCPL-II-L))
#
PASS-POT: (PASS-POT-I|PASS-POT-II)
#
POT: (ACT-POT|PASS-POT)
#
#
# 2.6.5. Imperative:
#
# The imperative endings are given in the active and passive
# imperative rules (cf. the rules ACT-IMP-).
# 
# Active & passive, imperative:
#
ACT-IMP-2SG: (STEM-V)
ACT-IMP-3SG: ((STEM-V-S|STEM-C)(koon|k��n)) 
ACT-IMP-1PL: ((STEM-V-S|STEM-C)((kaa|k��)()(VERB-1PL)))
ACT-IMP-2PL: ((STEM-V-S|STEM-C)(kaa|k��)) 
ACT-IMP-3PL: ((STEM-V-S|STEM-C)((koo|k��)()(VERB-3PL)))
#
ACT-IMP-PERS: (ACT-IMP-2SG|ACT-IMP-3SG|ACT-IMP-1PL|ACT-IMP-2PL|ACT-IMP-3PL)
#
# Active, imperative, the negative verb:
#
ACT-IMP-NEG-2SG: (�l� STEM-V)
ACT-IMP-NEG-3SG: (�lk��n (STEM-V(ko|k�)))
ACT-IMP-NEG-1PL: (�lk��mme (STEM-V(ko|k�)))
ACT-IMP-NEG-2PL: (�lk�� (STEM-V(ko|k�)))
ACT-IMP-NEG-3PL: (�lk��t (STEM-V(ko|k�)))
#
VERB-CONNEG: (ACT-IMP-2SG|PASS-PCPL-I|PASS-PCPL-II)
#
ACT-IMP-NEG: (ACT-IMP-NEG-2SG|ACT-IMP-NEG-3SG|ACT-IMP-NEG-1PL|
  ACT-IMP-NEG-2PL|ACT-IMP-NEG-3PL|VERB-CONNEG)
#
PASS-IMP: ((((STEM-V-S)|(STEM-C))()(((t)ta)|((t)t�)))()(koon|k��n))
#
PASS-IMP-NEG: (�lk��n (STEM-V(ta|t�)(ko|k�)))
#
IMP: (ACT-IMP-PERS|ACT-IMP-NEG|PASS-IMP|PASS-IMP-NEG)
#
#
# 2.6.6. Subjunctive
#
# There is no subjunctive mood in Finnish (cf. English).
#
#
# 2.7. Tense forms
#
# Finnish has simple and periphrastic tense forms.
# The periphrastic tense forms are formed with auxiliaries marked
# with personal inflection.
#
#
# 2.7.1. The simple basic tense forms:
#
# (a) Present tense:
#
ACT-PRES: \w((STEM-V)()(VERB-PERS-I))
#
# (b) Past tense:
#
ACT-PAST: \w((i)()(STEM-V)()(VERB-PERS-II))
#
# (c) Perfect tense:
#
ACT-PERF: ((VERB-AUX-PRES) (ACT-PCPL-II))
#
# (d) Pluperfect tense:
#
ACT-PLUPERF: ((VERB-AUX-PAST) (ACT-PCPL-II))
# 
# (e) Future 
#
# Finnish has no future tense form marked with specific tense suffixes. 
# Future is expressed (a) with the present tense form, and its
# relationship to the future is included in the context, and (b)
# also with the potential form of the verb "tulla" which is combined
# with the verb marked with the INF-III ending combined with
# the illative case endings.
#
#
# 2.7.2. The progressive tense forms (not activated)
# 
#
# 2.8. The summaries of tense forms:
#
ACT-TENSE: (ACT-PRES|ACT-PAST|ACT-PERF|ACT-PLUPERF)
#
PASS-TENSE: (PASS-PRES|PASS-PAST|PASS-PERF|PASS-PLUPERF)
#
VERB-FINITE: (ACT-TENSE|PASS|COND|POT|IMP) 
#
VERB-NON-FINITE: (INF|PCPL)
#
#
#
# IV. ADPOS-CASE RELATORS:
# Case marking and adpositions in Finnish
#
# Case marking system is important in denoting locations and movements
# of objects. The adpositional system is used side by side with case marking.
# The categories of adpositions: prepositions (PRP) and postpositions (POP).
#
#
# 1. Location of an object: IN, ON and OUT categories 
#
# 1.1. Location of an object in (IN), inside of a closed space (IN-PRP-A, 
# IN-POP-A) and inside of a bordered space, in a group, 
# or between other objects (IN-PRP-B, IN-POP-B): 
#
IN-C: \wINE(POSS-SFX?CLT-SFX?)
IN-PRP-A: 
IN-POP-A: ((silmiss�|sis�puolella|sis�ss�|sis�ll�|syd�mess�)
  (POSS-SFX?CLT-SFX?))
IN-PRP-B:  
IN-POP-B: ((joukossa|keskell�|parissa|per�ll�|seassa|v�liss�)
  (POSS-SFX?CLT-SFX?))
IN-ADP: (IN-POP-A|IN-POP-B)
INCLUDE: fin-disamb-IN-EXCL.spec
IN: (IN-C|IN-ADP)
#
#
# 1.2. Location of an object on (ON) or in touch with the surface of an object 
# (ON-PRP-C, ON-POP-C), and outside of an object or a landmark, 
# not far from it (ON-PRP-D, ON-POP-D):
#
ON-C: \wADE(POSS-SFX?CLT-SFX?)
ON-PRP-C:
ON-POP-C: ((alla|huipulla|p��ll�|partaalla|partailla|pinnalla|
  pinnassa|pohjalla|pohjilla|reunassa|reunoissa|reunalla|reunoilla|
  vasten)(POSS-SFX?CLT-SFX?))
ON-PRP-D:
ON-POP-D: (((edess�|ohessa|��ress�|
  h�nnill�|j�ljess�|juurella|juurilla|kannoilla|kintereill�|kohdalla|
  keskikohdalla|likell�|l�hell�|luona|niskassa|paikalla|
  per�ss�|rinnalla|sivussa|sivuissa|sivulla|sivuilla|suulla|syrj�ss�|
  takana|v�lill�|vastap��t�|vieress�|yll�)(POSS-SFX?CLT-SFX?))|
  liki)
INCLUDE: fin-disamb-ON-EXCL.spec
ON-ADP: (ON-POP-C|ON-POP-D)
INCLUDE: fin-disamb-ON-C-EXCL.spec
ON: (ON-C|ON-ADP)
#
#
# 1.3. Location of an object outside (OUT) of or at a distance from an object or
# a landmark (OUT-PRP-E, OUT-POP-F), and outside of another object, the distance 
# is not specified (far or near)OUT-PRP-F and OUT-POP-F):
#
OUT-C: 
OUT-PRP-E: 
OUT-POP-E: ((��rell�|edell�|edustalla|kahtapuolen|kahtapuolin|kahtapuolta)|
  (keskivaiheilla|l�hist�ll�|l�hettyvill�|liepeill�|lopussa|nurkalla|
  nurkilla|puolella|((ala|etu|yl�)puolella))(POSS-SFX?CLT-SFX?))
OUT-PRP-F:
OUT-POP-F: ((tienoilla|taholla|tahoilla)|(paikoilla|suunnassa|suunnalla|
  syrj�ss�|ulkopuolella|ulottumattomissa|ymp�rill�)(POSS-SFX?CLT-SFX?))
OUT-ADP: (OUT-POP-E|OUT-POP-F)
OUT: (OUT-ADP)
#
#
# 2. Movement of an object from in, on, outside of another object (delocation):
#
# 2.1. Movement of an object from in (IN), inside of a closed space (DE-PRP-IN-A, 
# DE-POP-IN-A) and from inside a partly closed space or between other objects 
# (DE-IN-PRP-B, DE-IN-POP-B):
#
DE-IN-C: \wELA(POSS-SFX?CLT-SFX?)
DE-IN-PRP-A: 
DE-IN-POP-A: ((silmist�|sis�puolelta|sis�lt�|sis�st�|syd�mest�)
  (POSS-SFX?CLT-SFX?))
DE-IN-PRP-B: 
DE-IN-POP-B: ((joukosta|keskelt�|keskest�|parista|per�lt�|seasta|
  v�list�)(POSS-SFX?CLT-SFX?))
DE-IN-ADP: (DE-IN-POP-A|DE-IN-POP-B)
INCLUDE: fin-disamb-DE-IN-EXCL.spec
DE-IN: (DE-IN-C|DE-IN-ADP)
#
#
# 2.2. Movement of an object from on smth: 
# Movement of an object from ON or in touch with the surface of an object 
# (DE-ON-PRP-C, DE-ON-POP-C), and to outside of an object or a landmark, 
# not far from them (DE-ON-C), DE-ON-PRP-D, DE-ON-POP-D):
#
DE-ON-C: \wABL(POSS-SFX?CLT-SFX?)
DE-ON-PRP-C:
DE-ON-POP-C: ((alta|h�nn�st�|(huipu(lta|ilta))|juuresta|kohdasta|
  (kupee(sta|lta))|laelta|nen�st�|nokasta|p��lt�|partaalta|per�lt�|
  (pinna(lta|sta))|(pohja(lta|sta))|(reun(alta|oilta))|(reun(asta|oista))|
  varresta|varsista)(POSS-SFX?CLT-SFX?))
DE-ON-PRP-D:  
DE-ON-POP-D: ((((keskikohda(lta|sta))|
  h�nnilt�|j�ljest�|juurelta|juurilta|kintereilt�|
  l�helt�|likelt�|niskasta|ohesta|
  per�st�|rinnalta|(sivu(sta|ista|lta|ilta))|suulta|syrj�st�|
  takaa|v�lilt�|vierest�|ylt�)(POSS-SFX?CLT-SFX?))|
  (kohdalta|kohdaltani|kohdaltasi|kohdaltamme|kohdaltanne|
  kohdaltansa|kohdaltaan)|
  (edest�|edest�ni|edest�si|edest�ns�|edest�mme|edest�nne|edest��n|
  edest�ns�)|
  (luota|luotani|luotasi|luotaan|luotansa|luotamme|luotanne))
DE-ON-ADP: (DE-ON-POP-C|DE-ON-POP-D)
INCLUDE: fin-disamb-DE-ON-EXCL.spec
DE-ON: (DE-ON-C|DE-ON-ADP)
#
#
# 2.3. Delocation of an object from outside of another object: 
# Movement from outside, onto or in touch with the surface of an object
# or a landmark (DE-OUT-PRP-E, DE-OUT-POP-E), and to outside of an object
# or a landmark, not far from the, (DE-OUT-PRP-F, DE-OUT-POP-F). 
#
DE-OUT-C: 
DE-OUT-PRP-E: 
DE-OUT-POP-E: ((��relt�|edustalta|kannoilta|keskivaiheilta|l�hettyvilt�|
  l�hist�lt�|liepeilt�|lopusta|nurkalta|nurkilta|
  puolelta|((ala|etu|yl�)puolelta))(POSS-SFX?CLT-SFX?))
DE-OUT-PRP-F: 
DE-OUT-POP-F: ((tienoilta|taholta|tahoilta|paikalta|paikoilta|suunnasta|
  suunnalta|syrj�ast�|ulkopuolelta|ulottumattomista|ymp�rilt�)
  (POSS-SFX?CLT-SFX?))
DE-OUT-ADP: (DE-OUT-POP-E|DE-OUT-POP-F)
DE-OUT: (DE-OUT-ADP)
#
INCLUDE: fin-disamb-DE-OUT-EXCL.spec
#
#
# 3. Add-location of an object into|onto|to outside of smth
#
# 3.1. Movement of an object into, to inside of a closed space (DIR-IN-PRP-CL, 
# DIR-IN-POP-CL) and to inside a partly closed space or between other objects 
# (DIR-IN-PRP-BCL, DIR-IN-POP-BCL): 
#
AD-IN-C: \wILL(POSS-SFX?CLT-SFX?)
AD-IN-PRP-A:
AD-IN-POP-A: ((silmiin|sis��n|sis�lle|sis�puolelle|syd�meen)
  (POSS-SFX?CLT-SFX?))
AD-IN-PRP-B:
AD-IN-POP-B: ((joukkoon|keskelle|pariin|sekaan|v�liin|v�lii)
  (POSS-SFX?CLT-SFX?))
AD-IN-ADP: (AD-IN-POP-A|AD-IN-POP-B)
INCLUDE: fin-disamb-AD-IN-EXCL.spec
AD-IN: (AD-IN-C|AD-IN-ADP)
#
#
# 3.2. Movement of an object on or in touch with the surface of another object 
# (DIR-ON-PRP-A, DIR-ON-POP-A), and outside of an object, not far from it 
# (DIR-ON-PRP-B and DIR-ON-POP-B):
#
AD-ON-C: \wALL(POSS-SFX?CLT-SFX?)
AD-ON-PRP-C: 
AD-ON-POP-C: (((h�nt��|juuree|kupeesee|nen��|nokkaa|pohjaa|reunaa)
  (POSS-SFX))|
  ((alle|h�nt��n|huipulle|huipuille|juureen|kohtaan|kupeeseen|
  nen��n|nokkaan|partaalle|p��lle|per��n|pieleen|pohjaan|pohjalle|
  reunaan|reunalle|suuhun|suihin|varteen)(POSS-SFX?CLT-SFX?)))
AD-ON-PRP-D: 
AD-ON-POP-D: ((��reen|eteen|h�nnille|j�ljille|juurelle|
  juurille|kintereille|kohdalle|kupeelle|l�helle|
  likelle|luo|luokse|niskaan|oheen|paikalle|p��h�n|p�ihin|per�lle|
  poskeen|rinnalle|sivulle|sivuille|sivuun|suulle|syrj��n|
  taa|taakse|tyk�|viereen|vierelle|ylle|yl�puolelle)(POSS-SFX?CLT-SFX?)|
  ((etee|niskaa|p��h�|syrj��|v�lille|vieree)(POSS-SFX)))
AD-ON-ADP: (AD-ON-POP-C|AD-ON-POP-D)
INCLUDE: fin-disamb-AD-ON-EXCL.spec
AD-ON: (AD-ON-C|AD-ON-ADP)
#
# 3.3. Movement of an object to outside of the  object (DIR-OUT-PRP-C,
# DIR-OUT-POP-C), and outside of an object, the distance or relationship
# with the object is not specified (AD-OUT-PRP-D and AD-OUT-POP-D): 
#
AD-OUT-PRP-E: 
AD-OUT-POP-E: ((��relle|edelle|edustalle|kannoille|keskivaiheille|
  l�hettyville|l�hist�lle|loppuun|iepeille|nurkalle|nurkille)
  (POSS-SFX?CLT-SFX?))
AD-OUT-PRP-F:
AD-OUT-POP-F: ((((etu|ulko)puolelle)|paikoille|suuntaan|suunnalle|
  syrj��n|tahoille|taholle|tienoille|ulottumattomiin|ymp�rille)
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
#
# 4. Translocation of an object with regard to through, along, over, 
# under and outside of another object. INT = internal, EXT = external
#
TRNS-INT-C: 
TRNS-INT-PRP:
TRNS-INT-POP: ((halki|kautta|l�pi|poikki)|((keskitse|sis�puolitse)
  (POSS-SFX?CLT-SFX?)))
TRNS-INT: (TRNS-INT-POP)
#
TRNS-EXT-C: 
TRNS-EXT-PRP:
TRNS-EXT-POP: ((my�ten|pitkin|ali|yli|ohi|kohti|kohden|asti|saakka)|
  ((alitse|alapuolitse|editse|kupeitse|vieritse|ohitse|
  p��llitse|sivuitse|taitse|v�litse|ylitse|yl�puolitse|ulkopuolitse)
  (POSS-SFX?CLT-SFX?)))
TRNS-EXT: (TRNS-EXT-POP)
TRNS: (TRNS-EXT|TRNS-INT)
#
INCLUDE: fin-disamb-ALL-EXCL.spec
#
#5. Terms denoting special temporal situations)
#
#5.1. Temporal; terms denoting points of time vaguely): 
#
TIME-C:
TIME-PRP: 
TIME-POP: (((aika(an|na))|(aiko(i(na|hin)))|
  (kynnykse(ll�|lt�|lle))|(puoliv�li(ss�|st�|in))|
  (keskivaihei(lla|lta|lle))|korvilla|
  vaiheilla|vaihteessa|(v�li(ll�|lt�|lle))|
  (j�lke(inen|en|isen�|iseen|eni|esi|ens�|enmme|enne|eisen�|eiseen))|
  per�st�)(CLT-SFX?))
TIME: (TIME-POP)
#
#
# 5.2. Temporal terms
#
# This group collects terms denoting beginning,
# end  points or limits of time (TIME-LIM):
#
# Disambiguating temporal words from the database:
#
INCLUDE: fin-disamb-TEMP-WORDS.spec
#
# In addition to the temporal terms, also several case endings
# are used in temporal expressiongs.
#
#
# 6. Circumstantial
#
# 6.1. The group "Circumstantial" contains various adpositions denoting
# differnt kinds of conditions, such as agent, ground, source, origin,
# ingredient, and states of affairs:
#
# CIRC-PRP (not included)
#
CIRC-POP: (((johtuen|johdosta|koskien|mukaan|mukaisesti|nojalla|
  nimess�|nimess�si|nimess��n|nimess�ns�|nimeen|nimiin|
  perusteella|suhteesta|suhteen|suhteessa|aloitteesta|ansiosta|
  mielest�|m��r�yksest�|pakottamana|pakottamina|
  sijasta|sijaan|sijaasi|sijaansa|sijalle|sijallensa|
  johdolla|toimesta)|((eduks(i|e))|(hyv�ks(i|e))|(kiusa(ksi|kse|lla))|
  (mieliks(i|e))|mieleen|takia|tautta|tavoin|t�hden|t�ydelt�|varten|
  (vara(kse|ksi|lla|lle|an))|t�hte|vuoksi|vuokse)|
  (armoi|avu(lla|llani|llasi|llaan|llamme|llanne|llansa))|
  (hoiva(ssa|sta))|hoiviin|(hoima(ssa|sta))|
  (hotei(ssa|ista|siin))|
  (huoma(ssa|sta|an|asi|ansa))|
  (huosta(ssa|sta|an|asi|ssasi))|
  kanssa|(keske(n��n|n�nne|n�ns�))|
  (kera(lla|llani|llasi|llaan|llansa))|
  (k�si(ss�|iss��n|iss�ni|iss�si|iss�nne|st�|ist�|ist�ni|ist�si|ist��n|
  ist�nne|ist�ns�|ist�ns�|in|ini|isi|ins�|imme))|(kynsi(ss�|st�|in))|
  muassa|(muka(na|an|ani|asi|ansa|amme))|my�t�|
  (valla(ssa|sta))|(valta(an|anne|ansa))
  (turvi(ssa|sta|in|ini|ssansa))|
  (voima(lla|llani|llasi|llaan|llansa|llamme|llanne))|
  (yhteyde(ss�|st�))|(yhteyte(en|ens�))|
  lis�ksi|ilman|paitsi|vastoin|vastuksinta|
  (armo(illa|sta))|huolimatta|kustannuksella|(lis�ks(i|e))|
  lukuunottamatta|(sija(an|ssa|sta))|suhteessa|
  (tasa(lla|lle))|(tila(lla|lta|lle))|uhalla|vailla|
  kaltainen|(kaltaise(ksi|kse))|(n�k�inen|n�k�ise(ksi|kse))|
  suuruinen|suuruise|suuruiseksi|suuruisekse|
  vertainen|vertaista)(POSS-SFX?CLT-SFX?))
CIRC: (CIRC-POP)
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
