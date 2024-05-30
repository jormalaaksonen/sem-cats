# Pirkko Suihkonen, 2006-2008, 2014, 2016-2017.
# Final version of the text describing the rules: 2024.
# Copyright: Pirkko Suihkonen 
# The Perl scripts for the analysis of the database and comments on 
# the guidelines of Regular Expressions: Jorma Laaksonen.
#
# The name of the language: English 
# The family: Indo-European languages 
# The sub-branch: Germanic languages 
# Language code, ISO 639: eng 
#
# The name of the project: 
# The ADPOS-CASE categories in English and Finnish. 
# The main goal of the project: 
# Parallel research of the English and Finnish ADPOS-CASE relators.
#
# Data: The King James Bible.
# https://www.biblegateway.com/versions/Kig-James-Version-KJV-Bible/#booklist.
# (April 2024)
# http://www.kingjamesbibleonline.org/ (Feb. 2015)
#
# Grammatical rules are defined as Regular Expressions. 
# The focus of the rules is on the ADPOS-CASE relators
# (prepositions in English and adpositions and case marking in Finnish)
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
# Helsinki: Kustannusosakeyhtiö Otava.
#
# Iivonen, Antti, Mari Horppila, Miika Heikkonen and Olli Rissanen (eds).
# 2000. Fonetiikan perussanasto. Helsingin yliopisto.
# https://helda.helsinki.fi/bistream/handle(10224/3513/index.htm. (2016)
#
# Karlsson, Fred. 1983[1982]. Suomen kielen äänne- ja muotorakenne
# (Phonological and Morphological Structure of the Finnish Language.)
# Porvoo/Helsinki/Juva: Werner Söderström Osakeyhtiö.
#
# Karlsson, Fred. 1987. Finnish Grammar. 
# Porvoo/Helsinki/Juva: Werner Söderström Osakeyhtiö.
#
# Koskenniemi, Kimmo. 1983. Two-Level Morphology: A General Computational Model
# for Word-Form Recognition and Production [Publications, 11].
# University of Helsinki, Department of General Linguistics.
#
# Koskenniemi, Kimmo. 1990. Finite-State parsing and disambiguation.
# In Hans Karlgren (ed.). Coling-90. Papers Presented in the 13th International
# Conference on Computational Linguistics on the Occasion of the 25th
# Anniversary of COLING and the 350th Anniversary of Helsinki University, 2.
# 229-242. Helsinki: Yliopistopaino.
#
# Laaksonen, Kaino and Anneli Lieko. 1998. Suomen kielen äänne- ja muoto-oppi
# (Phonetics and Morphology of the Finnish Language).
# Helsinki: Oy Finn Lectura Ab.
#
# Penttilä, Aarni. 1963. Suomen kielioppi (The Finnish Grammar).
# Porvoo|Helsinki: Werner Söderström Osakeyhtiö.
#
# Quirk, Randolph & Sidney Greenbaum, 1996[1973]. 
# A University Grammar of English. 
# Edinburg/Essex: Addison Wesley Longman Limited.
#
# Tuomi, Tuomo (ed.). 1980. Suomen kielen käänteissanakirja
# (Reverse Dictionary of Modern Standard Finnish)
# [Suomalaisen Kirjallisuuden Seuran Toimituksia, 274].
# Helsinki: The Finnish Literature Society.
#
# Webster's Ninth New Collegiate Dictionary. 1989.
# Springfield, Massachusetts, U.S.A.: Merriam-Webster Inc., Publishers.
#
# Webster's Dictionary 1828 (http://www.webstersdictionary1828.com/). (Aug. 2023)  
#
# For more information on the project, cf.
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
# 1.1. Consonants and sequences of consonants in the text
# (cf. Webster 1989[1983]: 37-39): 
#
C: (b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|w|x|z)
CC: (ng|sh|zh|th)
#
# 1.2. Vowels and sequences of vowels in the texts:
#
V: (a|e|i|o|u|y)
VL: (aa|ee|oo|uu)
DIPH: (ai|ae|ao|au|ay|ea|ei|eo|eu|ey|ia|ie|io|oa|oe|oi|ou|oy|ua|ue|ui|uy)
TRIPH: (aou|aye|eau|eye|ieu|oeu|uoy)
V-APP: (aw|ew|ow)
#
#
# 2. The structures of syllables
#
# Examples from the syllabic structures below deal only with literary forms 
# of words:
# 
SYLL-V: \w(V)
SYLL-VV: \w(VL|DIPH)
SYLL-CV: \w(C()V)
SYLL-CVV: \w(C()V()V)
SYLL-CCV: \w(C()C()V)
SYLL-CCVV: \w(C()C()V()V)
#
SYLL-VC: \w(V()C)
SYLL-VVC: \w(V()V()C)
SYLL-VCC: \w(V()C()C)
SYLL-CVC: \w(C()V()C)
SYLL-CVVC: \w(C()V()C)
SYLL-CVCC: \w(C()V()C()C)
SYLL-CCVCC: \w(C()C()V()C()C) 
SYLL-OP: \w(SYLL-V|SYLL-VV|SYLL-CV|SYLL-CVV|SYLL-CCV|SYLL-CCVV)
SYLL-CL: \w(SYLL-VC|SYLL-VVC|SYLL-VCC|SYLL-CVC|SYLL-CVVC|SYLL-CVCC|SYLL-CCVCC)
SYLL: \w(SYLL-OP|SYLL-CL)
#
#
# 3. The stress on the word-level
#  (The stress rules of English are not included.)
#
#
# II. MORPHOLOGY AND LEXICON
#
#
# 1. Classes of parts of speech
#
# 1.1. Nouns (not included)
#
# 1.2. Adjectives (not included)
#
# 1.2.1. Absolute adjectives
#
# 1.2.2. Relative adjectives:
#
#
# 1.3. Pronouns (lists; not included)
#
#
# 1.4. Numerals (lists; not included)
#
# 1.4.1. Cardinal numerals
#
# 1.4.2. Ordinal numerals
#
# 1.4.3. Fractions
#
#
# 1.5. Verbs (cf. section IV)
#
#
# 1.6. Particles (lists; not included)
#
# 1.6.1. Particles in the lexicon
#
# 1.6.2. Clitic particles
#
#
# 1.7. Conjunctions (lists; not included)
#
# 1.7.1. Coordinating conjunctions (a list)
#
# 1.7.2. Subordinating conjunctions (a list)
#
#
# 1.8. Articles
#
# 1.8.1. Indefinite articles: a, an
#
# 1.8.2. Definite articles: the
#
#
# 2. Word formation: examples from the structural means for developing
#    and modifying lexicon 
#
# 2.1. Word stems (not included)
#
# 2.1.1. Stem types of nouns
#
# 2.1.2. Stem types of verbs 
#
#
# 2.2. Prefixes in word formation, examples:
#
# Negative prefixes:
PREF-NEG: (un|non|dis|in)
# Reversative and privative prefixes:
PREF-RP: (un|de|dis)
# Pejorative prefixes:
PREF-PEJ: (mis|mal|pseudo)
# Prefixes of degree or size:
PREF-DS: (arch|super|out|sur|sub|over|under|hyper|ultra|mini)
# Prefixes of attitude:
PREF-ATT: (co|counter|anti|pro)
# Locative prefixes:
PREF-LOC: (super|sub|inter|trans)
# Prefixes of time and order:
PREF-TO: (fore|pre|post|ex|re)
# Number prefixes: 
PREF-NB: (uni|mono|bi|di|multi|poly)
# Other prefixes:
PREF-OT: (auto|neo|pan|proto|semi|vice)
# Conversion prefixes:
PREF-CNV: (be|en|a)
PREF: (PREF-NEG|PREF-RP|PREF-PEJ|PREF-DS|PREF-ATT|PREF-LOC|PREF-TO|
  PREF-NB|PREF-OT|PREF-CNV)
#
#
# 2.3. Particles modifying verbs:
#
# (cf. the WordNet verb list and 
# the files dealing with disambiguation of English)
#
#
# III. NOMINAL MORPHOLOGY
# 
#
# 1. Number
#
# 1.1. Singular
# Singular is unmarked.
#
# 1.2. Plural (the rules are not included)
#
#
# 2. Possession marking
#
# In English, possession is marked with possessive pronouns (cf. II: 4.2.)
# and with the genitive case.
#
#
# 3. The case system
#
# 3.1. Nominative
#
# The nominative form is unmarked. 
#
# 3.2. Genitive (not included)
#
#  
# IV. INFLECTION OF VERBS 
# 
# 1. The verbs examined on the project
#
# The data collected from verbs contains the following subgroups:
# (a) The collection of verbs in the database: the list of verbs: 
# eng-verbs-database-may-2017.txt. 
# In the list, the dictionary forms are marked with the character "#".
# (b) The list of verbs of the project Wordnet: wordnet (/proj/lenca/wordnet).
# (c) The irregular verbs separated from the list of verbs in the Wordnet: 
# eng-irregular-verbs-cats-txt.txt. Different tense forms are separated from 
# the list of irregular verbs: IRREG-PRES, IRREG-PAST, IRREG-PERF-I, 
# and IRREG-PERF-II.
#
# The verbs in the database are introduced from the file
# eng-verbs-database-may-2017-txt to the kwic-file for processing
# operations with the help of the file INCLUDELIST.
#
INCLUDELIST: eng-verbs.txt VERB-LIST
INCLUDELIST: eng-verbs-basic.txt VERBS-BASIC
#
INCLUDELIST: eng-verbs-database-march-2018.txt ENG-VERBS-DATA
INCLUDELIST: eng-verbs-data-finite-forms.txt ENG-VERBS-FINITE
INCLUDELIST: eng-verbs-finite-test.txt VERBS-FINITE-TEST
INCLUDELIST: eng-verbs-sample.txt ENG-VERBS-SAMPLE
INCLUDELIST: eng-verbs-som.txt ENG-VERBS-SOM
INCLUDELIST: eng-verbs-som-april-2018.txt VERBS-SOM-LONG
#
INCLUDELIST: eng-verbs-som-loc.txt VERB-SOM-LOC
INCLUDELIST: eng-verbs-som-ad-loc.txt VERB-SOM-AD-LOC
#
INCLUDELIST: eng-verbs-test-be.txt VERB-TEST-BE
INCLUDELIST: eng-verbs-test-bring.txt VERB-TEST-BRING
INCLUDELIST: eng-verbs-test-come.txt VERB-TEST-COME
INCLUDELIST: eng-verbs-test-flow.txt VERB-TEST-FLOW
INCLUDELIST: eng-verbs-test-go.txt VERB-TEST-GO
INCLUDELIST: eng-verbs-test-take.txt VERB-TEST-TAKE
#
INCLUDELIST: eng-verbs-som.txt VERB-TEST-@ 
#
INCLUDELIST: eng-verbs-som-loc.txt VERBS-SOM-LOC
INCLUDELIST: eng-verbs-som-ad-loc.txt VERBS-SOM-AD-LOC
#
INCLUDE: ENG-INF.spec
INCLUDE: ENG-VERBS-FINITE-TEST.spec
#
#
# Eliminating the particles which modify verbs:
#
INCLUDE: eng-complex-verbs-EXCL.spec
#
#
# 2. Verbal nominal forms
#
# 2.1. Infinitive (INF):
# 
# The infinitive forms of verbs are combined with the particle "to" 
# which precedes the dictionary forms of verbs. 
# The rule ENG-INF.spec moves the set of the dictionary forms of verbs
# to the category infinitive (INF). 
#
#
# 2.2. Participles: present participle (PCPL-I) and past participle (PCPL-II):
#
# The PCPL-I is formed with the suffix -ing and the PCPL-II is formed
# with the suffix -ed.
#
PCPL-I: (VERBS-PCPL-PRES)
PCPL-II: (VERBS-PCPL-PAST)
PCPL: (PCPL-I|PCPL-II)
#
#
# 3. Personal inflection
#
# In the modern standard English, only the third person in the singular form (3SG)
# is marked in personal inflection (the suffix -s). 
#
# On the old personal endings:
# In the database consisting of an old translation of the Bible, 
# the third person in the present tense singular form 
# is marked with the suffix -th, and the second person in the present 
# and the past tense forms is marked with the suffix -st.
#   
# The rules marking the personal endings of verbs of the 2nd and 3rd persons 
# are in the kwic-script.
#
# The rules VERBS-2SG, SG2, V-3SG and SG3 are not activated.
#
V-1SG: (VERBS-BASIC)
#VERBS-2SG: (((b|c|d|f|g|h|j|k|l|m|n|p|r|s|t|w|x|z(e)?)st)|(VERBS-BASIC))
#SG2: (ENG-VERBS-2SG)
#VERBS-3SG: (((b|c|d|f|g|h|j|k|l|m|n|p|r|s|t|w|x|z(e)?))(th|s))
#SG3: (ENG-VERBS-3SG|VERBS-PRES-3SG)
V-1PL: (VERBS-BASIC)
V-2PL: (VERBS-BASIC)
V-3PL: (VERBS-BASIC)
VERB-PERS: (V-1SG|VERBS-2SG|VERBS-3SG|VERBS-3SG|V-1PL|V-2PL|V-3PL)
# 
#
# 4. Auxiliaries
#
# 4.1. Auxiliaries in the text:
#
VERB-AUX: (be|am|are|is|was|wast|were|wert|been|being|
  have|had|hadst|has|hast|hath|having|
  do|doeth|did|diddest|didst|doing|done|
  can|cannot|could|couldest|
  may|mayest|might|mightest|
  shall|shalt|should|shouldest|
  will|willeth|willing|wilt|would|
  must|(ought to)|(oughtest to))
VERB-MOD: (can|cannot|could|couldest|
  may|mayest|might|mightest|
  shall|shalt|should|shouldest|
  will|willeth|willing|wilt|would|
  must|(ought to)|(oughtest to))
#
#
# 4.2. Personal inflection of the auxiliaries be, do, and have
# (standard English), not activated:
#
# The auxiliary verbs "shall" and "will" which are modal verbs
# are also used in forming complex tense forms.
#
# ACT, PRES, the verb "be":	
ACT-BE-PRES-1SG: (am)
ACT-BE-PRES-2SG: (are)
ACT-BE-PRES-3SG: (is)
ACT-BE-PRES-1PL: (are)
ACT-BE-PRES-2PL: (are)
ACT-BE-PRES-3PL: (are)
ACT-BE-PRES: (ACT-BE-PRES-1SG|ACT-BE-PRES-2SG|ACT-BE-PRES-3SG|
  ACT-BE-PRES-1PL|ACT-BE-PRES-2PL|ACT-BE-PRES-3PL)
#
# ACT, PAST, the verb "be":	
ACT-BE-PAST-1SG: (was)
ACT-BE-PAST-2SG: (were)
ACT-BE-PAST-3SG: (was)
ACT-BE-PAST-1PL: (were)
ACT-BE-PAST-2PL: (were)
ACT-BE-PAST-3PL: (were)
ACT-BE-PAST: (ACT-BE-PAST-1SG|ACT-BE-PAST-2SG|ACT-BE-PAST-3SG|
  ACT-BE-PAST-1PL|ACT-BE-PAST-2PL|ACT-BE-PAST-3PL)
#
# ACT, PERF, the verb "be" (e.g. have/has been)
ACT-BE-PERF-1SG: (have been)
ACT-BE-PERF-2SG: (have been)
ACT-BE-PERF-3SG: (has been)
ACT-BE-PERF-1PL: (have been)
ACT-BE-PERF-2PL: (have been)
ACT-BE-PERF-3PL: (have been)
ACT-BE-PERF: (ACT-BE-PERF-1SG|ACT-BE-PERF-2SG|ACT-BE-PERF-3SG|
  ACT-BE-PERF-1PL|ACT-BE-PERF-2PL|ACT-BE-PERF-3PL)
#
# ACT, PLUPERF, the verb "be" (e.g. have/has been)
ACT-BE-PLUPERF-1SG: (had been)
ACT-BE-PLUPERF-2SG: (had been)
ACT-BE-PLUPERF-3SG: (had been)
ACT-BE-PLUPERF-1PL: (had been)
ACT-BE-PLUPERF-2PL: (had been)
ACT-BE-PLUPERF-3PL: (had been)
ACT-BE-PLUPERF: (ACT-BE-PLUPERF-1SG|ACT-BE-PLUPERF-2SG|
  ACT-BE-PLUPERF-3SG|ACT-BE-PLUPERF-1PL|ACT-BE-PLUPERF-2PL|
  ACT-BE-PLUPERF-3PL)
#
#ACT, PRES, the verb "have":	
ACT-HAVE-PRES-1SG: (have)
ACT-HAVE-PRES-2SG: (have)
ACT-HAVE-PRES-3SG: (has)
ACT-HAVE-PRES-1PL: (have)
ACT-HAVE-PRES-2PL: (have)
ACT-HAVE-PRES-3PL: (have)
ACT-HAVE-PRES: (ACT-HAVE-PRES-1SG|ACT-HAVE-PRES-2SG|
  ACT-HAVE-PRES-3SG|ACT-HAVE-PRES-1PL|ACT-HAVE-PRES-2PL|
  ACT-HAVE-PRES-3PL)
#
# ACT, PAST, the verb "have":	
ACT-HAVE-PAST-1SG: (had)
ACT-HAVE-PAST-2SG: (had)
ACT-HAVE-PAST-3SG: (had)
ACT-HAVE-PAST-1PL: (had)
ACT-HAVE-PAST-2PL: (had)
ACT-HAVE-PAST-3PL: (had)
ACT-HAVE-PAST: (ACT-HAVE-PAST-1SG|ACT-HAVE-PAST-2SG|ACT-HAVE-PAST-3SG|
  ACT-HAVE-PAST-1PL|ACT-HAVE-PAST-2PL|ACT-HAVE-PAST-3PL)
#
# ACT-PERF: the present forms of the verb "have" and the PCPL-II form of
# the verb "be":	
ACT-HAVE-PERF-1SG: (have had)
ACT-HAVE-PERF-2SG: (have had)
ACT-HAVE-PERF-3SG: (has had)
ACT-HAVE-PERF-1PL: (have had)
ACT-HAVE-PERF-2PL: (have had)
ACT-HAVE-PERF-3PL: (have had)
ACT-HAVE-PERF: (ACT-HAVE-PERF-1SG|ACT-HAVE-PERF-2SG|ACT-HAVE-PERF-3SG|
  ACT-HAVE-PERF-1PL|ACT-HAVE-PERF-2PL|ACT-HAVE-PERF-3PL)
#
# ACT, PLU-PERF: the past forms of the verb "have" and the PCPL-II form of
# the verb "be": 	
ACT-HAVE-PLUPERF-1SG: (had had)
ACT-HAVE-PLUPERF-2SG: (had had)
ACT-HAVE-PLUPERF-3SG: (had had)
ACT-HAVE-PLUPERF-1PL: (had had)
ACT-HAVE-PLUPERF-2PL: (had had)
ACT-HAVE-PLUPERF-3PL: (had had)
ACT-HAVE-PLUPERF: (ACT-HAVE-PLUPERF-1SG|ACT-HAVE-PLUPERF-2SG|
  ACT-HAVE-PLUPERF-3SG|ACT-HAVE-PLUPERF-1PL|ACT-HAVE-PLUPERF-2PL|
  ACT-HAVE-PLUPERF-3PL)
#
# ACT, PRES, the verb "do":	
ACT-DO-PRES-1SG: (do)
ACT-DO-PRES-2SG: (do)
ACT-DO-PRES-3SG: (does)
ACT-DO-PRES-1PL: (do)
ACT-DO-PRES-2PL: (do)
ACT-DO-PRES-3PL: (do)
ACT-DO-PRES: (ACT-DO-PRES-1SG|ACT-DO-PRES-2SG|ACT-DO-PRES-3SG|
  ACT-DO-PRES-1PL|ACT-DO-PRES-2PL|ACT-DO-PRES-3PL)
#
# ACT, PAST, the verb "do":	
ACT-DO-PAST-1SG: (did)
ACT-DO-PAST-2SG: (did)
ACT-DO-PAST-3SG: (did)
ACT-DO-PAST-1PL: (did)
ACT-DO-PAST-2PL: (did)
ACT-DO-PAST-3PL: (did)
ACT-DO-PAST: (ACT-DO-PAST-1SG|ACT-DO-PAST-2SG|ACT-DO-PAST-3SG|
  ACT-DO-PAST-1PL|ACT-DO-PAST-2PL|ACT-DO-PAST-3PL)
#
# ACT, PERF, the verb "do" (e.g. have/has done)
ACT-DO-PERF-1SG: (have done)
ACT-DO-PERF-2SG: (have done)
ACT-DO-PERF-3SG: (has done)
ACT-DO-PERF-1PL: (have done)
ACT-DO-PERF-2PL: (have done)
ACT-DO-PERF-3PL: (have done)
ACT-DO-PERF: (ACT-DO-PERF-1SG|ACT-DO-PERF-2SG|ACT-DO-PERF-3SG|
  ACT-DO-PERF-1PL|ACT-DO-PERF-2PL|ACT-DO-PERF-3PL)
#
# ACT, PLUPERF, the verb "do" (e.g. had done)
ACT-DO-PLUPERF-1SG: (had done)
ACT-DO-PLUPERF-2SG: (had done)
ACT-DO-PLUPERF-3SG: (had done)
ACT-DO-PLUPERF-1PL: (had done)
ACT-DO-PLUPERF-2PL: (had done)
ACT-DO-PLUPERF-3PL: (had done)
ACT-DO-PLUPERF: (ACT-DO-PLUPERF-1SG|ACT-DO-PLUPERF-2SG|
  ACT-DO-PLUPERF-3SG|ACT-DO-PLUPERF-1PL|ACT-DO-PLUPERF-2PL|
  ACT-DO-PLUPERF-3PL)
#
ACT-BE: (ACT-BE-PRES|ACT-BE-PAST|ACT-BE-PERF|ACT-BE-PLUPERF)
#
ACT-HAVE: (ACT-HAVE-PRES|ACT-HAVE-PAST|ACT-HAVE-PERF|
  ACT-HAVE-PLUPERF)
#
ACT-BE-HAVE: (ACT-BE-PRES|ACT-BE-PAST|ACT-BE-PERF|ACT-BE-PLUPERF|
  ACT-HAVE-PRES|ACT-HAVE-PAST|ACT-HAVE-PERF|ACT-HAVE-PLUPERF)
#
AUX: (ACT-BE-PRES|ACT-BE-PAST|ACT-BE-PERF|ACT-BE-PLUPERF|
  ACT-HAVE-PRES|ACT-HAVE-PAST|ACT-HAVE-PERF|ACT-HAVE-PLUPERF|
  ACT-DO-PRES|ACT-DO-PAST|ACT-DO-PERF|ACT-DO-PLUPERF)
#
#
# 5. Diathesis
#
# 5.1. Active
#
# Active is unmarked.
#
# 5.2. Passive
#
# 5.3. Rules for forming passive forms:
#
PASS-PRES: (ACT-BE-PRES PCPL-II)
PASS-PAST: (ACT-BE-PAST PCPL-II)
PASS-PERF: ((ACT-HAVE-PRES) been (PCPL-II))
PASS-PLUPERF: ((ACT-HAVE-PAST) been (PCPL-II))
PASS-FUT: ((shall|will) be PCPL-II)
PASS-TENSE: (PASS-PRES|PASS-PAST|PASS-PERF|PASS-PLUPERF|PASS-FUT)
#
PASS-PRES-PROG: (ACT-BE-PRES PCPL-I)
PASS-PAST-PROG: (ACT-BE-PAST PCPL-I)
PASS-PERF-PROG: ((ACT-HAVE-PRES) been (PCPL-I))
PASS-PLUPERF-PROG: ((ACT-HAVE-PAST) been (PCPL-I))
PASS-TENSE-PROG: (PASS-PRES-PROG|PASS-PAST-PROG|PASS-PERF-PROG|
  PASS-PLUPERF-PROG)
#
#1SG/1PL should be & PCPL-PAST, 2/3SG/2/3PL would be & PCPL-PAST
PASS-COND-I: ((should|would) be (PCPL-II))
#
# Conditional I (I/we should / she/he/you/they would be called)
PASS-COND-II: ((should|would) (have been) (PCPL-II))
#
PASS-COND: (PASS-COND-I|PASS-COND-II)
#
VERB-PASS: (PASS-TENSE|PASS-TENSE-PROG|PASS-COND-I)
#
#
# 6. Moods
#
# 6.1. Indicative
#
# Indicative is not formally marked.
# 
#
# 6.2. Conditional
#
# English has two conditionals: Conditional Present (Conditional I), and
# Conditional Past (Conditional II).
#
#Active, conditional I (ACT-COND-I, e.g. should/would go)
ACT-COND-I-1SG: (should VERBS-BASIC)
ACT-COND-I-2SG: (would VERBS-BASIC)
ACT-COND-I-3SG: (would VERBS-BASIC)
ACT-COND-I-1PL: (should VERBS-BASIC)
ACT-COND-I-2PL: (would VERBS-BASIC)
ACT-COND-I-3PL: (would VERBS-BASIC)
ACT-COND-I: (ACT-COND-I-1SG|ACT-COND-I-2SG|ACT-COND-I-3SG|
  ACT-COND-I-1PL|ACT-COND-I-2PL|ACT-COND-I-3PL)
#
# Active, conditional II (ACT, COND-II, e.g. should/would have gone)
ACT-COND-II-1SG: (should have PCPL-II)
ACT-COND-II-2SG: (would have PCPL-II)
ACT-COND-II-3SG: (would have PCPL-II)
ACT-COND-II-1PL: (should have PCPL-II)
ACT-COND-II-2PL: (would have PCPL-II)
ACT-COND-II-3PL: (would have PCPL-II)
ACT-COND-II: (ACT-COND-II-1SG|ACT-COND-II-2SG|ACT-COND-II-3SG|
  ACT-COND-II-1PL|ACT-COND-II-2PL|ACT-COND-II-1PL)
#
ACT-COND: (ACT-COND-I|ACT-COND-II)
# 
# I/we should have had, he/she/it/you/they would have called)
COND-I: ((should|would) VERBS-BASIC)
#
# I/we should have written, he would have called)
COND-II: ((should|would) (have (PCPL-II))) 
#
COND: (COND-I|COND-II)
#
#
# 6.3. Potential
#
# There is no grammatical mood such as potential in English. 
#
#
# 6.4. Imperative 
#
# Simple and complex forms: simple imperative forms are the dictionary forms 
# of verbs e.g. come, etc. Complex direct or indirect commands are formed 
# with some auxiliaries: e.g. you should go, you have to go, you must go, etc.
#
ACT-IMP: (VERBS-BASIC)
#
#
# 6.5. Subjunctive (not included)
# 
#
# 7. Tense forms 
#
# The tense forms in English are structurally (a) simple and (b) periphrastic.
# The prefiphrastic tense forms are formed with auxiliaries which are marked
# with personal inflection.
#
#
# 7.1. The simple basic tense forms:
#
# 7.1.1. Present (PRES): 
#
# The present tense is unmarked.
#
ACT-PRES: ((VERBS-BASIC)()(VERB-PERS))
#
#
# 7.1.2. Past (PAST):
#
# The regular simple past tense forms are the same as the PERF-II.
# In the irregular verbs, the past tense forms are defined to be lexical. 
# Regular past tense forms are formed with the suffix -ed.
#
# ACT-PAST: (VERBS-PAST)
# 
#
# 7.1.3. Perfect:
#
# The regular perfect tense form consists of the auxiliary "have" 
# in the regular present tense form and from the lexical verb in the PCPL-II form
# (cf. IV.2.2.). 
#
ACT-PERF: ((have|has) (PCPL-II))
#
#
# 7.1.4. Pluperfect: 
#
# The pluperfect form contains the past tense form of the auxiliary "have" and
# the past participle form (PCPL-II) of the lexical verb.
#
ACT-PLUPERF: ((had) (PCPL-II))
#
PERF-PAST: ((had) (VERB-PCPL-PAST))
#
#
# 7.1.5. Future
#
#
# Active, future I (ACT, FUT-I, e.g. shall/will go)
ACT-FUT-I-1SG: (shall VERBS-BASIC)
ACT-FUT-I-2SG: (will VERBS-BASIC)
ACT-FUT-1-3SG: (will VERBS-BASIC)
ACT-FUT-I-1PL: (shall VERBS-BASIC)
ACT-FUT-I-2PL: (will VERBS-BASIC)
ACT-FUT-I-3PL: (will VERBS-BASIC)
ACT-FUT-I: (ACT-FUT-I-1SG|ACT-FUT-I-2SG|ACT-FUT-1-3SG|
  ACT-FUT-I-1PL|ACT-FUT-I-2PL|ACT-FUT-I-3PL)
#
#Active, future II (ACT-FUT-II; e.g. shall/will have PCPL-II):	
ACT-FUT-II-1SG: (shall have PCPL-II)
ACT-FUT-II-2SG: (will have PCPL-II)
ACT-FUT-II-3SG: (will have PCPL-II)
ACT-FUT-II-1PL: (shall have PCPL-II)
ACT-FUT-II-2PL: (will have PCPL-II)
ACT-FUT-II-3PL: (will have PCPL-II) 
ACT-FUT-II: (ACT-FUT-II-1SG|ACT-FUT-II-2SG|ACT-FUT-II-3SG|
  ACT-FUT-II-1PL|ACT-FUT-II-2PL|ACT-FUT-II-3PL)
# 
# Active, future III (ACT-FUT-III, e.g. am/is/are going to run)	
ACT-FUT-III-1SG: (am going VERBS-BASIC)
ACT-FUT-III-2SG: (are going VERBS-BASIC)
ACT-FUT-III-3SG: (is going VERBS-BASIC)
ACT-FUT-III-1PL: (are going VERBS-BASIC)
ACT-FUT-III-2PL: (are going VERBS-BASIC)
ACT-FUT-III-3PL: (are going VERBS-BASIC)
ACT-FUT-III: (ACT-FUT-III-1SG|ACT-FUT-III-2SG|ACT-FUT-III-3SG|
  ACT-FUT-III-1PL|ACT-FUT-III-2PL|ACT-FUT-III-3PL)
#
ACT-FUT: (ACT-FUT-I|ACT-FUT-II|ACT-FUT-III)
ACT-TENSE: (ACT-PRES|ACT-PERF|ACT-PLUPERF|ACT-FUT)
FUT: (ACT-FUT-I|ACT-FUT-II)
#
#
# 7.2.1. Active, progressive present (ACT-PRES-PROG):
#
ACT-PRES-PROG-1SG: (am PCPL-I)
ACT-PRES-PROG-2SG: (are PCPL-I)
ACT-PRES-PROG-3SG: (is PCPL-I)
ACT-PRES-PROG-1PL: (are PCPL-I)
ACT-PRES-PROG-2PL: (are PCPL-I)
ACT-PRES-PROG-3PL: (are PCPL-I)
ACT-PRES-PROG: (ACT-PRES-PROG-1SG|ACT-PRES-PROG-2SG|ACT-PRES-PROG-3SG|
  ACT-PRES-PROG-1PL|ACT-PRES-PROG-2PL|ACT-PRES-PROG-3PL)
#
# 
# 7.2.2. Active, progressive past (ACT-PAST-PROG):
#
ACT-PAST-PROG-1SG: (was PCPL-I)
ACT-PAST-PROG-2SG: (were PCPL-I)
ACT-PAST-PROG-3SG: (was PCPL-I)
ACT-PAST-PROG-1PL: (were PCPL-I)
ACT-PAST-PROG-2PL: (were PCPL-I)
ACT-PAST-PROG-3PL: (were PCPL-I)
ACT-PAST-PROG: (ACT-PAST-PROG-1SG|ACT-PAST-PROG-2SG|ACT-PAST-PROG-3SG|
  ACT-PAST-PROG-1PL|ACT-PAST-PROG-2PL|ACT-PAST-PROG-3PL)
# 
# 
# 9.2.3. Active, progressive perfect ACT-PERF-PROG):
#
ACT-PERF-PROG-1SG: (have been PCPL-I)
ACT-PERF-PROG-2SG: (have been PCPL-I)
ACT-PERF-PROG-3SG: (has been PCPL-I)
ACT-PERF-PROG-1PL: (have been PCPL-I)
ACT-PERF-PROG-2PL: (have been PCPL-I)
ACT-PERF-PROG-3PL: (have been PCPL-I)
ACT-PERF-PROG: (ACT-PERF-PROG-1SG|ACT-PERF-PROG-2SG|ACT-PERF-PROG-3SG|
  ACT-PERF-PROG-1PL|ACT-PERF-PROG-2PL|ACT-PERF-PROG-3PL)
#
# 7.2.4. Active, progressive pluperfect ACT-PLUPERF-PROG):
#
ACT-PLUPERF-PROG-1SG: (had been PCPL-I)
ACT-PLUPERF-PROG-2SG: (had been PCPL-I)
ACT-PLUPERF-PROG-3SG: (had been PCPL-I)
ACT-PLUPERF-PROG-1PL: (had been PCPL-I)
ACT-PLUPERF-PROG-2PL: (had been PCPL-I)
ACT-PLUPERF-PROG-3PL: (had been PCPL-I)
ACT-PLUPERF-PROG: (ACT-PLUPERF-PROG-1SG|ACT-PLUPERF-PROG-2SG|
  ACT-PLUPERF-PROG-3SG|ACT-PLUPERF-PROG-1PL|ACT-PLUPERF-PROG-2PL|
  ACT-PLUPERF-PROG-3PL)
#
ACT-TENSE-PROG: (ACT-PRES-PROG|ACT-PAST-PROG|ACT-PERF-PROG|ACT-PLUPERF-PROG)
#
#
VERB-FINITE: (ACT-TENSE|ACT-TENSE-PROG|ACT-COND|
  PASS-TENSE|PASS-TENSE-PROG|PASS-COND)
# 
# VERB-NON-FINITE: (INF|PCPL)
#
# The infinitive forms are defined with the following rule: VERB-INF: (to VERB)
# The file "kwic" in the script-directory contains the link VERB-LIST
# which introduces the file "eng-verbs-database-may-2017.txt" to be available
# for connecting the predicate-verbs and ADPOS-CASE relators for examining
# combinations of predicates and ADPOS-CASE relators in the texts. 
# The name is changed to VERB-DATA to concern only the verbs in the database.
#
VERB-ALL: (VERBS|VERBS-PRES-3SG|VERBS-PAST|PCPL|VERBS-2SG)
#
# VERB-SAMPLE: (ENG-SAMPL-VERB)
#
#
# V. ADPOS-CASE RELATORS: PREPOSITIONS IN ENGLISH 
#
# 1. Location of an object: IN, ON and OUT categories: 
#
# 1.1. Location of an object in, inside of a closed space (IN-PRP-A, IN-POP-B)
# and inside a bordered space, in a group, or between objects (IN-PRP-B, IN-POP-B):
#
IN-C: 
IN-PRP-A: ((in (a|an|the|my|your|his|her|its|our|their)
  (eye|heart|sight|eyes|hearts|sights) (of))|
  (within|inside|in))
IN-PRP-A-XX: (IN-PRP-A (\w+))
IN-POP-A:
IN-PRP-B: ((in (the (bottom|middle|midst|centre)) (of))|
  (round about between)|
  (in (the|my|your|his|her|our|their|its) (hand|hands) (of))|
  (between|amid|among|amongst|midst))
IN-PRP-B-XX: (IN-PRP-B (\w+))
IN-POP-B:
IN-ADP: (IN-PRP-A|IN-PRP-B)
IN: (IN-ADP)
IN-XX: (IN (\w+))
INCLUDE: eng-disamb-IN-EXCL.spec
#
# 1.2.Location of an object on or in touch on the surface of an object
# (ON-PRP-C, ON-POP-C), and outside of an object or a landmark, not far from them
# (ON-PRP-D, ON-POP-D):
#
ON-C: 
ON-PRP-C: (against|beneath|beside|on|upon|under|underneath)
ON-PRP-C-XX: (ON-PRP-C (\w+))
ON-POP-C:
ON-PRP-D: (((in|on) the (two) (ends|tops) of)|
  ((upon (the|my|your|his|her|its|our|their) 
  (edge|head|heads|tip|top|tops|post|root)) of)|
  ((at|upon) ((the|my|your|his|her|its|our|their) 
  (base|bottom|brink|hand|hands)) of)|
  ((on|upon) ((the) base) (of))|
  (over (against|before|beside)))
ON-POP-D: 
ON-PRP-D-XX: (ON-PRP-D (\w+))
ON-ADP: (ON-PRP-C|ON-PRP-D)
ON: (ON-ADP)
ON-XX: (ON-ADP (\w+))
INCLUDE: eng-disamb-ON-EXCL.spec
#
# The terms front, midst, inside, and outside have to be evaluated with respect to 
# connections with prepositions.
#
# 1.3. Location of an object outside (OUT) of or at a distance from an object
# or a landmark (OUT-PRP-E OUT-POP-E), and outside of another object,
# the distance not specified (far or near) (OUT-PRP-F, OUT-POP-F):
#
OUT-C:
OUT-PRP-E: (((close|next) to)|(above (to|unto|upon))|
  ((at|before) (them|(their hands))|
  (above|after|at|before|behind|below|near|nearer|nearby|nigh|opposite)))
OUT-PRP-E-XX: (OUT-PRP-E (\w+))
OUT-POP-E:  
OUT-PRP-F: ((in the (beginning|direction|front|opposite|quarter))|
  ((at|in|on) (the|my|your|his|her|thine|its|our|their) (side|sides) of)|
  (on the outside of)|
  (within (reach|range) of)|
  (at a distance of)|(round about)|
  ((on|upon|on) the (east|west|south|north) (side|sides) of)|
  (on (the|my|your|his|her|its|thine|our|their) (left|right) hand of)|
  ((on|upon) (side|sides) of)|
  ((on|upon) (a|an|the) (one|other|side) of)|
  ((on|upon) two sides of)|
  (upon (after|at|behind|before|below|under))|
  (round about (after|behind|below|near|nigh|under|upon))|
  (next (to|unto))|
  (on high)|
  (outside|around|beyond|round))
OUT-PRP-F-XX: (OUT-PRP-F (\w+))
OUT-POP-F: 
OUT: (OUT-PRP-E|OUT-PRP-F)
OUT-XX: (OUT (\w+))
INCLUDE: eng-disamb-OUT-EXCL.spec
#
#
# 2. Movement of an object from in, on, outside of another object 
# (delocation):
#
# 2.1. Movement of an object from in, inside of a closed space
# (DE-IN-PRP-A, DE-IN-POP-A) and from inside a partly closed space or between
# other objects (DE-IN-PRP-B, DE-IN-POP-B):
#
DE-IN-C: 
DE-IN-PRP-A: ((from (the|my|your|his|her|its|our|their) 
  (eye|eyes|heart|hearts|sight|sights) (of))|
  ((from|out) (within|inside)))
DE-IN-PRP-A-XX: (DE-IN-PRP-A (\w+))
DE-IN-POP-A:
DE-IN-PRP-B: (((from|off|out) (between|amid|among|amongst|in))|
  ((off|from|out) (the) (middle|midst|centre|bottom|hand|hands) (of)))
DE-IN-PRP-B-XX: (DE-IN-PRP-B (\w+))
DE-IN-POP-B: 
DE-IN: (DE-IN-PRP-A|DE-IN-PRP-B)
DE-IN-XX: (DE-IN (\w+))
#
INCLUDE: eng-disamb-DE-IN-EXCL.spec
#
#
# 2.2. Movement of an object from on smth: movement of an object from on or
# in touch with the surface of another object or a landmark (DE-ON-PRP-C, 
# DE-ON-POP-C), or not far from them (DE-ON-PRP-D, DE-ON-POP-D):
#
DE-ON-C:
DE-ON-PRP-C: ((from|off|out) (against|beneath|beside|on|upon|under|underneath))
DE-ON-POP-C:
DE-ON-PRP-D: (((from|off|out) (in|on) the (two) (ends|tops) of)|
  (((from|off|out) (upon (the|my|your|his|her|its|our|their) 
  (edge|head|heads|tip|top|tops|post|root)) of))|
  ((from|off|out) (at|upon) ((the|my|your|his|her|its|our|their) 
  (base|bottom|brink|hand|hands)) of)|
  ((from|off|out) ((in|on|upon) ((the) base) (of)))|
  ((from|off|out) (over) (against|before|beside|on|upon|under|underneath))|
  (from|out|off))
DE-ON-POP-D:
DE-ON-PRP-C-XX: (DE-ON-PRP-C (\w+))
DE-ON-PRP-D-XX: (DE-ON-PRP-D (\w+))
DE-ON: (DE-ON-PRP-C|DE-ON-PRP-D)
DE-ON-XX: (DE-ON (\w+))
#
INCLUDE: eng-disamb-DE-ON-EXCL.spec
#
# 2.3. Delocation of an object from outside of another object or  a landmark
# (DE-OUT-PRP-E, DE-OUT-POP-E), and from outside of an object or a landmark,
# the distance is vaguely expressed (DE-OUT-PRP-F, DE-OUT-POP-F):
#
DE-OUT-C: 
DE-OUT-PRP-E: ((from|off|out) (above|after|at|before|behind|below|
  opposite|outside|near|nearby|nearer|nigh))
DE-OUT-PRP-E-XX: (DE-OUT-PRP-E (\w+))
DE-OUT-POP-E:  
DE-OUT-PRP-F: (((from|off|out) ((around|beyond|round)
  (the (beginning|direction|edge|end|opposite|quarter|side|sides))) of)|
  ((from|out|off) (on the outside of))|
  (((from|off|out) (at the (side|both sides))) of)|
  (from (within) (reach|range) of)|
  (from a distance of)|
  (from round about)|
  (from ((on|upon) the (east|west|south|north) (side|sides)) of)|
  ((from on the (left|right)) (hand|side) of)|
  ((from|out) (the|my|our|his|her|thine|its|their) (side|sides) of)|
  (from on high)|
  (from (the) outside of)|
  (out ((at) the (edge|head)))|
  (out of)|
  (from (outside|around|round|beyound)))
DE-OUT-PRP-F-XX: (DE-OUT-PRP-F (\w+))
DE-OUT-POP-OUT-F: 
DE-OUT: (DE-OUT-PRP-E|DE-OUT-PRP-F)
DE-OUT-XX: (DE-OUT (\w+))
#
INCLUDE: eng-disamb-DE-OUT-EXCL.spec
#
#
# 3. Movement of an object into, onto, and to outside of smth 
# 3.1. Movement of an object into, to inside of a closed space
# (DIR-IN-PRP-A and DIR-IN-POP-A) and to inside a partly closed space
# or between other objects (DIR-IN-PRP-B and DIR-IN-POP-B):
# 
AD-IN-C: 
AD-IN-PRP-A: (((into|to) (the|my|your|his|her|its|our|their)
  (eye|heart|eyes|hearts|mouth) (of))|
  (into))
AD-IN-PRP-A-XX: (AD-IN-PRP-A (\w+))
AD-IN-POP-A:
AD-IN-PRP-B: (((down|into|to|unto|up) (between|amid|among|amongst|midst|in))|
  ((into|to) (the) (middle|midst|centre))|
  (over into)|
  (up (among|in))|
  (out into)|
  (up in)|
  (in unto)|
  ((unto|to) (the (sight|sights)) of))
AD-IN-PRP-B-XX: (AD-IN-PRP-B (\w+))
AD-IN-POP-B: 
AD-IN: (AD-IN-PRP-A|AD-IN-PRP-B)
AD-IN-XX: (AD-IN (\w+))
#
INCLUDE: eng-disamb-AD-IN-EXCL.spec
#
# 3.2. Movement of an object on or in touch with the surface of another object
# (DIR-ON-PRP-IT, DIR-ON-POP-IT), and outside of an object, not far from it
# (DIR-ON-PRP-NF and DIR-ON-POP-NF): 
#
AD-ON-C: 
AD-ON-PRP-C: ((onto (against|on|upon))|
  (onto (the) (bottom|head|heads|edge|edges|end|ends|side|sides|top|tops))|
  (out (on|upon))|
  (over (against|upon))|
  (to|unto))
AD-ON-PRP-C-XX: (AD-ON-PRP-C (\w+))
AD-ON-POP-C:
AD-ON-PRP-D: (((down|to|unto|up) (beneath|beside|under|underneath))|
  ((down|onto|to|unto|up) the (front|edge|edges|head|heads|tip|top|tops|
  post|posts|root|roots|side|sides) of)|
  ((down|onto|to|unto|up) (the|my|your|his|her|its|our|their) 
  (brink|brinks|front|edge|edges|head|heads|tip|top|tops|post|posts|
  roots) of)|
  (off unto)|
  (aside (after|to|into|unto|from|out)))
AD-ON-PRP-D-XX: (AD-ON-PRP-D (\w+))
AD-ON-POP-D: 
AD-ON: (AD-ON-PRP-C|AD-ON-PRP-D)
AD-ON-XX: (AD-ON (\w+))
#
INCLUDE: eng-disamb-AD-ON-EXCL.spec
#
# 3.3. Movement of an object outside of the  object (DIR-OUT-PRP-E, 
# DIR-OUT-POP-E), and outside of an object, the distance or relationship 
# with the object is vaguely expressed (DIR-OUT-PRP-F and DIR-OUT-POP-F):
#
AD-OUT-C:
AD-OUT-PRP-E: (((down|to|unto|up) (above|after|at|before|behind|beyond|
  near|nearby|nearer|nigh|over|round))|
  (round (about) (to|unto))|
  (over (to|unto))|
  ((down|unto|up) close to)|
  (close by)|
  (near (to|unto|before|of))|
  ((close|next) to)|
  (down|up))
AD-OUT-PRP-E-XX: (AD-OUT-PRP-E (\w+))
AD-OUT-POP-E:  
AD-OUT-PRP-F:  (((down|to|unto|up) (the) (beginning|direction|edge|edges|end|
  ends|opposite|quarter) of)|
  ((down|to|unto|up) (the) (outside of))|
  ((down|to|unto|up) the (middle|midst))|
  ((down|to|unto|up) (within) (reach|range) of)|
  ((down|to|unto|up) (a|the) distance of)|
  ((down|to|unto|up) (the) (east|west|south|north|my|his|her|your|our|their) 
  (side|sides) of)|(up above)|
  ((down|to|unto|up) (the) (one|another|two) sides of)|
  ((to the right) (hand|side) of)|
  ((to|unto) ((the) on high))|
  (up to)|
  ((to|unto) (the) (edge|end|side|sides)))
AD-OUT-POP-F:  
AD-OUT-PRP-F-XX: (AD-OUT-PRP-F (\w+))
AD-OUT: (AD-OUT-PRP-E|AD-OUT-PRP-F)
AD-OUT-XX: (AD-OUT (\w+))
# 
LOC: (IN|ON|OUT)
LOC-XX: (LOC (\w+))
DE-LOC: (DE-IN|DE-ON|DE-OUT)
DE-LOC-XX: (DE-LOC (\w+))
AD-LOC: (AD-IN|AD-ON|AD-OUT)
AD-LOC-XX: (AD-LOC (\w+))
#
INCLUDE: eng-disamb-AD-OUT-EXCL.spec
INCLUDE: eng-disamb-ALL-EXCL.spec
#
#
# 4. Translocation of an object: 
#
# 4.1. Translocation regard to closed or partly closed space or between objects:
#
TRNS-INT-C: 
TRNS-INT-PRP: (across|through|throughout|via)
TRNS-INT-POP:
TRNS-INT: (TRNS-INT-PRP)
TRNS-INT-XX: (TRNS-INT (\w+))
#
#
# 4.2. Translocation of an object with regard to open space
#
TRNS-EXT-C:
TRNS-EXT-PRP: (along|by|over|past|till|toward|towards|until|
  (by the (side|sides) of)|
  (from over)|
  (up (to|by))|(over (till|toward))|
  (past unto))
TRNS-EXT-POP:
TRNS-EXT: (TRNS-EXT-PRP)
TRNS-EXT-XX: (TRNS-EXT (\w+))
TRNS: (TRNS-EXT|TRNS-INT)
#
# Some of these carry vaguely information on direction of movements,
# c.f. e.g. "toward".
#
INCLUDE: eng-disamb-TRNS-EXCL.spec
#
#
# 5. Terms denoting special temporal situations):
#
# Eliminating temporal expressions from the database:
# 
TIME-C: 
TIME-PRP: ((in the time of)|
  ((at|in|for|on) (the) (afternoon|day|days|evening|
  month|morning|night|noon|year|(decennium(s))|century|
  (end of this year))))
TIME-POP:
TIME: (TIME-PRP)
TIME-XX: (TIME (\w+))
#
# Disambiguating temporal words from the database:
#
INCLUDE: eng-disamb-TEMP-WORDS.spec
#
#
# 6. Prepositions denoting various circumstantial relationships (CIRC)
# (reason, motive, stimulus, reaction. support, accompaniment, close relationship,
# states of affairs, hindrance, opposition, standards, measurements, strengthening
# expressions, exceptions, negative condition, partiality or involvement of
# an eventuality, agent, ground, source, origin, ingredient)
#
CIRC-C: 
CIRC-PRP: (besides|except|despite (against)|of|(in spite of)|(because of)|
  (on the basis of)|(by virtue of)|(out of the grouond)|(over to)|
  (in (a|the) consequence of)|(on the ground(s) of)|(for the sake of)|
  (on account of)|((due|opposite|owing) to)|(in the (way|ways) of)|
  (with (regard|regards|respect) to)|
  (on (the) (account|consequence) of)|(into account)|(instead of)|
  (for the reason of)|(round about (for|with))|
  (regarding|with|without)|(according to)|(on behalf of)|
  (with (the) (aid|help) of)|(on behalf of)|
  (in (the) (connection|contact) of)|((according|thanks) to)|
  (from without)|(on the name of)|
  (off to)|(out of)|(down with)|(for of)|(up for)) 
CIRC-POP: 
CIRC: (CIRC-PRP)
CIRC-XX: (CIRC (\w+))
#
#
# 7. Single lexical prepositions
PRP-SGNL: (above|across|after|against|along|amid|among|amongst|around|
  at|before|behind|below|beneath|beside|between|beyond|by|despite|
  down|during|except|for|from|in|inside|into|midst|near|nearer|nearby|
  nigh|of|off|on|onto|opposite|out|outside|over|past|regarding|round|
  since|through|throughout|till|to|toward|towards|under|underneath|
  until|unto|up|upon|with|within|without)
#
IN-SGNL:  (in|within|inside|between|amid|among|amongst|midst)
#
ON-SGNL:  (against|on|upon|under|underneath|beneath|beside|nigh)
#
OUT-SGNL: (above|after|at|before|behind|below|nearby|
  around|beyond|round|near|nearby|nearer)
#
DE-IN-SGNL: (from (within|inside))
#
DE-ON-SGNL: ((from|off|out) (against|off|on|upon|under|underneath|nigh))
#
DE-OUT-SGNL: (((from|off|out) (above|after|at|before|behind|below|nearby|
  around|beyond|round|near|nearby|nearer))|(out before))
#
AD-IN-SGNL: (into)
#
AD-ON-SGNL: ((down|into|to|up) (between|amid|among|amongst|midst|on|upon))
#
AD-OUT-SGNL: (((to|onto) (against|under|underneath))|
  (onto)|((down|into|to|up) (beneath|beside|nigh)))
#
#
# 8. Complex prepositions
#
IN-CMPL: ((in the eye of)|
  (in the eyes of)|
  (in the heart of)|
  (in the hearts of)|
  (in the sight of)|
  (in the sights of)|
  (in the bottom)|
  (in the middle)|
  (in the midst)|
  (in the centre)|
  (in the middle of)|
  (in the midst of)|(at the bottom))
#
DE-IN-CMPL: ((from within)|
  (from inside)|
  (out within)|
  (out inside)|
  (off within)|
  (off inside)|
  (from (the) eye of)|
  (from (the) eyes of)|
  (from (the) heart of)|
  (from (the) hearts of)|
  (from (the) sights of)|
  (from among)|
  (from amongst)|
  (from amid)|
  (from between)|
  (out among)|
  (out amongst)|
  (out amid)|
  (out between)|
  (out midst of)|
  (off among)|
  (off amongst)|
  (off amid)|
  (off midst of)|
  (from out of)|
  (from (the) middle of)|
  (from (the) midst of)|
  (from (the) centre of)|
  (from (the) out of)|
  (off the midst (of))|
  (out the middle (of))|
  (out the midst (of))|
  (round (about) within)|
  (round (about) between))
#
AD-IN-CMPL: ((down (the) eye of)|
  (down (the) eyes of)|
  (down among)|
  (down between)|
  (down (the) heart of)|
  (down (the) hearts of)|
  (down (the) sight of)|
  (down (the) sights of)|
  (down amongst)|
  (down midst)|
  (into (the) eye of)|
  (into (the) eyes of)|
  (into (the) heart of)|
  (into (the) hearts of)|
  (into (the) sight of)|
  (into (the) sights of)|
  (into the hands)|
  (into the middle)|
  (into the midst)|
  (into the sides of)|
  (into the tops of)|
  (into (the) midst of)|
  (into (the) hand of)|
  (into (the) hands of)|
  (into (the) mouth of)|
  (into (the) sides of)|
  (into (the) top of)|
  (into (the) tops of)|
  (down between)|
  (down amid)|
  (down among)|
  (into among)|
  (into amongst)|
  (into midst)|
  (into (the) centre)|
  (to (the) middle)|
  (into (the) middle)|
  (into midst)|
  (into between)|
  (into amid)|
  (out in of)|
  (out into of)|
  (out in)|
  (out into)|
  (out of)|
  (to (the) eye of)|
  (to (the) eyes of)|
  (to (the) heart of)|
  (to (the) hearts of)|
  (to (the) sight of)|
  (to (the) sights of)|
  (to among)|
  (to amongst)|
  (to the hands (of))|
  (to the midst (of))|
  (to the mouth of)|
  (to amid)|(to between)|
  (to (the) centre)|
  (to the midst of)|
  (to the mouth of)|
  (unto the midst of)|
  (up among)|
  (up in)|
  (up (the) eye of)|
  (up (the) eyes of)|
  (up (the) heart of)|
  (up (the) hearts of)|
  (up (the) sight of)|
  (up (the) sights of)|
  (up between)|
  (up amid)|
  (up among)|
  (up in)|
  (up amongst)|
  (up midst))
#
ON-CMPL: ((at the (both) sides of)|
  (at the bottom of)|
  (in the (two) ends of)|
  (in the (two) tops of)|
  (in (the) base of)|
  (in the end of)|
  (in the hand of)|
  (in the hands of)|
  (in (the) behind of)|
  (in (the) front of)|
  (close to)|
  (in (the) side of)|
  (in (the) sides of)|
  (in (the) front of)|
  (next to)|
  (on (the) edge of)|
  (on (the) root of)|
  (on (the) top of)|
  (on (the) base of)|
  (on (the) side of)|
  (on (the) sides of)|
  (on the edge of)|
  (on the head of)|
  (on the heads of)|
  (over against)|
  (over before)|
  (upon (the) edge of)|
  (upon (the) root of)|
  (upon (the) top of)|
  (upon (the) head of)|
  (upon (the) tip of)|
  (upon (the) top of)|
  (upon (the) tops of)|
  (upon (the) post of)|
  (upon (the) root of)|
  (upon (the) base of)|
  (upon (the) side of)|
  (upon (the) sides of)|
  (upon the brink)|
  (round about (on|upon)))
#
DE-ON-CMPL: ((from against)|
  (from off)|
  (from on)|
  (from upon)|
  (from under)|
  (from underneath)|
  (from on (the) edge of)|
  (from next to)|
  (from on (the) root of)|
  (from on (the) top of)|
  (from upon (the) edge of)|
  (from upon (the) root of)|
  (from upon (the) top of)|
  (from (the) (two) ends of)|
  (from (the) (two) tops of (of))|
  (from the end of)|
  (from the top of)|
  (from on the top)|
  (from on the hand)|
  (from (on) the hands)|
  (from (on) the end)|
  (from after)|
  (from behind)|
  (from beneath)|
  (from beside)|
  (from nigh)|
  (from of)|
  (from out)|
  (from beside)|
  (from nigh)|
  (from on (the) edge)|
  (from on (the) head)|
  (from on (the) post)|
  (from on (the) heads)|
  (from on (the) side)|
  (from on (the) sides)|
  (from on (the) tip)|
  (from on (the) top)|
  (from upon (the) edge)|
  (from upon (the) head)|
  (from upon (the) heads)|
  (from off)|(from out)
  (from upon (the) post)|
  (from upon (the) root)|
  (from of)|(from on)|
  (from upon (the) side)|
  (from upon (the) sides)|
  (from off)|(from out)|
  (from upon (the) tip)|
  (from upon (the) top)|
  (from upon (the) tops)|
  (from close to)|
  (from next to)|
  (from (at) (the) bottom (of))|
  (from (at) (the) side (of))|
  (from (at) (the) sides (of))|
  (off against)|
  (off off)|
  (off on)|
  (off upon)|
  (off under)|
  (off of)|
  (off underneath)|
  (off beside)|
  (off nigh)|(of out)|
  (off upon)|
  (out against)|
  (out off)|
  (out on)|
  (out upon)|
  (out under)|
  (ouf of)|
  (out underneath)|
  (out beside)|
  (out nigh)|
  (out after)|
  (out behind)|
  (out upon the tip of)|
  (out upon the top of)|
  (out upon the tops of)|
  (out beneath)|(out on)|
  (out upon)|(round about from))
#
AD-ON-CMPL: ((aside after)|
  (aside to)|
  (aside into)|
  (aside unto)|
  (aside from)|
  (aside out)|
  (down beneath)|
  (onto beneath)|
  (to beneath)|
  (up beneath)|
  (down beside)|
  (onto beside)|
  (to beside)|
  (up beside)|
  (down nigh)|
  (onto nigh)|
  (to nigh)|
  (up nigh)|
  (down (the) brink of)|
  (down (the) brinks of)|
  (down (the) front of)|
  (down (the) head of)|
  (down (the) heads of)|
  (down (the) mouth of)|
  (down (the) post of)|
  (down (the) posts of)|
  (down (the) roots of)|
  (down (the) side of)|
  (down (the) sides of)|
  (down (the) tip of)|
  (down (the) top of)|
  (down (the) tops of)|
  (down (the) close to)|
  (down (the) next to)|
  (down (the) side of)|
  (down (the) sides of)|
  (into (the) brink of)|
  (into (the) brinks of)|
  (into (the) front of)|
  (into (the) head of)|
  (into (the) heads of)|
  (into (the) mouth of)|
  (into (the) post of)|
  (into (the) posts of)|
  (into (the) roots of)|
  (into (the) side of)|
  (into (the) sides of)|
  (into (the) tip of)|
  (into (the) top of)|
  (into (the) tops of)|
  (into (the) close to)|
  (into (the) bottom of)|
  (into (the) head of)|
  (into (the) edge of)|
  (into (the) side of)|
  (into (the) sides of)|
  (into (the) next to)|
  (into (the) hand of)|
  (into (the) hands of)|
  (into (the) side of)|
  (into (the) sides of)|
  (off unto)|(off upon)|
  (onto (the) brink of)|
  (onto (the) brinks of)|
  (onto (the) front of)|
  (onto (the) head of)|
  (onto (the) heads of)|
  (onto (the) mouth of)|
  (onto (the) post of)|
  (onto (the) posts of)|
  (onto (the) roots of)|
  (onto (the) side of)|
  (onto (the) sides of)|
  (onto (the) tip of)|
  (onto (the) top of)|
  (onto (the) tops of)|
  (out to)|(out unto)|
  (out upon)|
  (to (the) brink of)|
  (to (the) brinks of)|
  (to (the) front of)|
  (to (the) head of)|
  (to (the) heads of)|
  (to (the) mouth of)|
  (to (the) post of)|
  (to (the) posts of)|
  (to (the) roots of)|
  (to (the) side of)|
  (to (the) sides of)|
  (to (the) tip of)|
  (to (the) top of)|
  (to (the) tops of)|
  (to at)|
  (to (the) (right) hand of)|
  (to (the) (right) hands of)|
  (to (the) (right) end of)|
  (to (the) (right) ends of)|
  (to (the) close to)|(to (the) next to)|
  (to the brink)|
  (to (the) side of)|
  (to (the) sides of)|  
  (unto (the) end of)|
  (unto (the) ends of)|
  (unto (the) edge of)|
  (unto the head)|
  (unto the top (of))|
  (up (the) brink of)|
  (up (the) brinks of)|
  (up (the) front of)|
  (up (the) head of)|
  (up (the) heads of)|
  (up (the) mouth of)|
  (up (the) post of)|
  (up (the) posts of)|
  (up (the) roots of)|
  (up (the) side of)|
  (up (the) sides of)|
  (up (the) tip of)|
  (up (the) top of)|
  (up (the) tops of)|
  (up (the) close to)|
  (up (the) next to)|
  (up (the) side of)|
  (up (the) sides of)|
  (up beneath)|
  (nigh unto)|
  (in unto))
#
OUT-CMPL: ((above to)|(above unto)|(above upon)|
  (at the side of)|(at the sides of)|(at a distance of)|(at of)|
  (at one side of)|(at other side of)|(at a side of)|(at two sides of)|
  (in the beginning (of))|(in the direction of)|(in (the) front of)|
  (in the opposite of)|(in the quarter of)|(in the side of)|
  (in the sides of)|
  (near to)|(near unto)|(next unto)|
  (nigh at)|(nigh before)|(nigh by)|(nigh of)|(nigh over against)|
  (on the east side of)|(on the west side of)|(on the south side of)|
  (on the north side of)|(on the east sides of)|(on the west sides of)|
  (on the south sides of)|(on the north sides of)|(on the right side of)|
  (on high)|(on the outside of)|(on the right hand of)|
  (round after)|(round about)|(round behind)|(round in)|
  (round (about) unto)|(round (about) upon)|
  (upon the east side of)|(upon the west side of)|(upon the south side of)|
  (upon the north side of)|(upon the east sides of)|(upon the west sides of)|
  (upon the south sides of)|(upon the north sides of)|
  (upon after)|(upon at)|(upon behind)|(upon before)|
  (within reach of)|(within range of)|(round about (behind|after)))
#
DE-OUT-CMPL: ((from above)|(from after)|(from at)|(from before)|
  (from behind)|(from below)|(from nearby)|(from beyond)|
  (from close to)|(from on high)|(out before)|
  (from around)|(from beyond)|(from round)|(from near)|
  (from nearby)|(from out of)|(from the beginning of)|
  (from the direction of)|(from the edge of)|(from the end of)|
  (from the opposite of)|(from the quarter of)|(from the side of)|
  (from the sides of)|(from on the outside of)|(from at the side of)|
  (from at the sides of)|(from (within) reach of)|
  (from (within) range of)|(from at a distance of)|
  (from on the east side of)|(from on the west side of)|
  (from on the south side of)|(from on the north side of)|
  (from on the east sides of)|(from on the west sides of)|
  (from on the south sides of)|(from on the north sides of)|
  (from upon the east side of)|(from upon the west side of)|
  (from upon the south side of)|(from upon the north side of)|
  (from upon the east sides of)|(from upon the west sides of)|
  (from upon the south sides of)|(from upon the north sides of)|
  (from on the right hand of)|(from on the right side of)|
  (from on high)|(from outside)|(from the sides of)|(from round)|
  (from the quarter of)|(from the end of)|
  (from near)|(out nearby)|(from out of)|(from the beginning of)|  
  (off around)|(from beyond)|(from round)|(from near)|
  (off nearby)|(from out of)|(from the beginning of)|
  (off the direction of)|(from the edge of)|
  (off the opposite of)|(off on the outside of)|(off at the side of)|
  (off the side of)|(off at the sides of)|(off above)|(off after)|
  (off at)|(off before)|(off behind)|(off below)|(off nearby)|
  (out above)|(out after)|(out at)|(out before)|(out behind)|
  (out below)|(out nearby)|(out around)|(from beyond)|(out at)|
  (out the direction of)|(from the edge of)|(from the end of)|
  (out the opposite of)|(from the quarter of)|(out the side of)|
  (out on the outside of)|(out at the side of)|(out at the sides of)|
  (out (at) the edge)|(out (at) the head)|(out of))
#
AD-OUT-CMPL: ((down above)|(down among)|(down amongst)|(down at)|
  (down before)|(down below)|(down behind)|(down from)|(down near)|
  (down nearby)|(down nearer)|(down over)|(down unto)|(down the middle)|
  (down (the) direction of)|(down (the) edge of)|(down (the) edges of)|
  (down (the) end of)|(down (the) opposite of)|(down (the) quarter of)|
  (down (the) east side of)|(down (the) west side of)|
  (down (the) south side of)|(down (the) north side of)|
  (down (the) east sides of)|(down (the) west sides of)|
  (down (the) south sides of)|(down (the) north sides of)|
  (down (the) beginning of)|(down the middle)|(down the midst)|
  (down (within) reach of)|(down (within) range of)|(down a distance of)|
  (out at)|(out behind)|(out before)|(out after)|
  (to before)|(to below)|(to behind)|(to from)|(to near)|(to nearby)|
  (to nearer)|(to over)|(to unto)|(unto above)|(to the outside (of))|
  (to (the) direction of)|(to (the) edge of)|(to (the) edges of)|
  (to (the) end of)|(to the ends of)|(to (the) opposite of)|
  (to (the) quarter of)|(to the middle)|(to the midst (of))|
  (to (the) beginning of)|
  (to (within) reach of)|(to (within) range of)|(to (the) east side of)|
  (to (the) west side of)|(to a distance of)|(to (the) south side of)|
  (to (the) north side of)|(to (the) east sides of)|(to (the) west sides of)|
  (to (the) south sides of)|(to (the) north sides of)|(to the right hand of)|
  (to the right side of)|(to (the) on high)|(to above)|(to among)|(to amongst)|
  (unto among)|(unto amongst)|(unto (the) beginning of)|(unto (the) side)|
  (unto (the) sides)|(unto at)|(unto before)|(unto below)|(unto behind)|
  (unto from)|(unto near)|(unto nearby)|(unto nearer)|(unto over)|(unto above)|
  (unto (the) direction of)|(unto (the) edge of)|(unto (the) edges of)|
  (unto the end of)|(unto (the) opposite of)|(unto (the) quarter of)|
  (unto (the) outside (of))|(unto the middle (of))|
  (unto the midst (of))|(unto a distance of)|(unto (within) reach of)|
  (unto (within) range of)|(unto the side (of))|(unto (the) east side of)|
  (unto the ends (of))|(unto (the) west side of)|(unto (the) south side of)|
  (unto (the) north side of)|(unto (the) east sides of)|
  (unto (the) west sides of)|(unto (the) south sides of)|
  (unto (the) north sides of)|(unto (the) edge)|(unto (the) end (of))|
  (up above)|(up among)|(up amongst)|(up at)|(up before)|(up below)|
  (up behind)|(up from)|(up near)|(up nearby)|(up nearer)|(up over)|
  (up unto)|(up to)|(unto close to)|(up close to)|(out after)|
  (up (the) beginning of)|(up (the) direction of)|(up (the) edge of)|
  (up (the) edges of)|(up (the) end of)|(up (the) opposite of)|(up to)|
  (up (the) quarter of)|(down (the) outside of)|(to (the) outside of)|
  (up (within) reach of)|(up (within) range of)|(up the middle)|
  (up the midst)|(up a distance of)|(up (the) east side of)|
  (up (the) west side of)|(up (the) south side of)|(up (the) outside of)|
  (up (the) north sides of)|(up (the) east sides of)|(up (the) west sides of)|
  (up (the) south sides of)|(up (the) north sides of)|(round about (to|unto)))
#
LOC-INDF-CMPL: 
# 
DE-LOC-INDF-CMPL: (away from)
#
AD-LOC-IDF-CMPL: 
#
PRP-TRNS-CMPL: ((close by)|(along with)|(by the side of)|(by the sides of))
#
PRP-CIRC-CMPL: ((because of)|(on behalf of)|(round about (for|with)))
#
#PRP-CMPL: (IN-CMPL|DE-IN-CMPL|AD-IN-CMPL|ON-CMPL|DE-ON-CMPL|AD-ON-CMPL|
#  OUT-CMPL|DE-OUT-CMPL|AD-OUT-CMPL|DE-LOC-INDF-CMPL|PRP-TRNS-CMPL)
#
PRP-CMPL: (IN-CMPL|DE-IN-CMPL|AD-IN-CMPL|ON-CMPL|DE-ON-CMPL|AD-ON-CMPL|
  OUT-CMPL|DE-OUT-CMPL|AD-OUT-CMPL|DE-LOC-INDF-CMPL|PRP-TRNS-CMPL|
  PRP-CIRC-CMPL)
#
INCLUDE: eng-disamb-PRP-CMPL-EXCL.spec
#
#    ((above to)|(above unto)|(above upon)|(according to)|
#  (aside after)|(aside from)|(aside into)|(aside out)|(aside to)|
#  (aside unto)|(at the bottom of)|(at the day)|(at the evening)|(at night)|
#  (at the noon)|(at the side of)|(because of)|
#  (by the brink)|(by the side of)|(by the sides of)|(close by)|(close to)|
#  (despite against)|(down among)|(down among)|(down at)|(down before)|
#  (down between)|(down by)|(down from)|(down in)|(down over)|
#  (down the middle)|(down unto)|(down with)|
#  (for the days)|(for the day)|(for the morning)|
#  (from above)|(from after)|(from among)|(from before)|
#  (from behind)|(from behind)|(from beneath)|
#  (from beside)|(from between)|(from beyond)|
#  (from of)|(from off)|(from on)|(from on high)|(from out)|(from out of)|
#  (from over)|(from the beginning of)|(from the end of)|(from the eyes of)|
#  (from the hand of)|(from the hands of)|(from the middle of)|
#  (from the midst of)|(from the sides of)|(from the top of)|(from under)|
#  (from within)|(from without)|(instead of)|
#  (in the beginning of)|(in the bottom)|(in the day)|(in the days)|
#  (in the end of)|(in the evening)|(in the eyes of)|(in the front of)|
#  (in the hand of)|(in the hands of)|(in the heart of)|(in the hearts of)|
#  (in the middle)|(in the middle of)|(in the midst)|(in the midst of)|
#  (in the month)|(in the morning)|(in the night)|(in the side of)|
#  (in the sides of)|(in the sight of)|(in the time of)|(in the top of)|
#  (in the two ends of)|(in the way of)|(in the ways of)|(in the year)|
#  (inspite of)|(into the hand of)|(into the hands of)|(into the heart of)|
#  (into the middle)|(into the midst)|(into hands of)|(into side(s) of)|
#  (into the mouth of)|(into the sides of)|(into the top of)|(into top of)|
#  (into the tops of)|(next unto)|(nigh before)|(nigh over against)|
#  (off against)|(off among)|(off before)|(off out of)|(off to)|
#  (off unto)|(off upon)|
#  (on behalf of)|(on high)|(on the day)|(on the east side of)|
#  (on the edge of)|(on the side of)|(on the sides of)|(on the name of)|
#  (on the north side of)|(on the outside of)|(on the south side of)|
#  (on the top of)|(on the west side of)|
#  (out after)|(out against)|(out among)|(out at the side of)|(out at)|
#  (out beneath)|(out in)|(out before)|(out behind)|
#  (out into)|(out of)|(out to)|(out unto)|(out upon)|
#  (past unto)|(round about unto)|(round about upon)|(round after)|
#  (round behind)|(round in)|(thanks to)|(to top of)|(to the ends of)|
#  (to in)|(to the brink of)|(to the end)|(to the end of)|(to the hands of)|
#  (to the midst)|(to the midst of)|(to the mouth of)|(to the outside of)|
#  (to the side of)|(to the top of)|(to the west side of)|
#  (unto above)|(unto the east side of)|(unto to edge)|(unto the edge of)|
#  (unto the end)|(unto the end of)|(unto the ends of)|(unto the head)|
#  (unto the midst)|(unto the midst of)|(unto the other side of)|
#  (unto the outside of)|(unto the side of)|(unto the south side)|
#  (unto the top)|(unto the sides of)|(unto the tops of)|
#  (up above)|(up among)|(up at)|(up before)|(up beneath)|(up between)|
#  (up by)|(up for)|(up from)|(up in)|(up over)|(up to)|(up unto)|
#  (upon before)|(upon the brink)|(upon the edge of)|(upon the head of)|
#  (upon the side of)|(upon the sides of)|(upon the tip of)|(upon the top)|
#  (upon the top of)|(upon the tops of))
#
#
TW-IN-EXCL: (IN-EXCL)
TW-DE-IN-EXCL: (DE-IN-EXCL)
TW-AD-IN-EXCL: (AD-IN-EXCL)
TW-ON-EXCL: (ON-EXCL)
TW-DE-ON-EXCL: (DE-ON-EXCL)
TW-AD-ON-EXCL: (AD-ON-EXCL)
TW-OUT-EXCL: (OUT-EXCL)
TW-DE-OUT-EXCL: (DE-OUT-EXCL)
TW-AD-OUT-EXCL: (AD-OUT-EXCL)
TW-TRNS-EXCL: (TRNS-EXCL)
#TW-TIME-EXCL: (xzy)
#TW-CIRC-EXCL: (xzy)
TW-ALL-EXCL: (ALL-EXCL)
TW-PRP-CMPL-EXCL: (PRP-CMPL-EXCL)
#
#
END:
