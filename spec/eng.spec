#Pirkko Suihkonen, 2006-2008, 2014, 2016-2017 
#Copyright: Pirkko Suihkonen 
#
#The name of the language: English 
#The family: Indo-European languages 
#The sub-branch: Germanic languages 
#Code: eng 
#
# The name of the project: 
# The ADPOS-CASE categories in English and Finnish. 
# The main goal of the project: 
# Comparative research of the English and Finnish ADPOS-CASE relators
# (final version: 2017). 
# Grammatical rules are defined as Regular Expressions. 
# The Perl scripts for the analysis of the database, and comments on 
# the guidelines of Regular Expressions: Jorma Laaksonen.
#
# References: 
# Quirk, Randolph & Sidney Greenbaum, 1996[1973]. 
# A University Grammar of English. 
# Edinburg/Essex: Addison Wesley Longman Limited.
# Webster's Ninth New Collegiate Dictionary. A Merriam-Webstr.
# Merriam-Webster Inc., Publishers. Springfield, Massachsetts, U.S.A.
# On the references: see also the document Suihkonen & Laaksonen 2017
#
# 
# THE RULES FOR THE ANALYSIS OF THE DATABASE
#
# (The LENCA-project <<<<<<8Suihkonen 2015):
# DIATHESIS:       ACT & PASS & REFL & REC & CAUS & APPL & ANAL
# MOOD:            IND & IMP & POT & COND & SUBJ & INT-ANA & OBL-ANA
# TENSE:           PRES-SNTH & PAST-SNTH & FUT-ANA & PERF & PLU-PERF
# ASPECT:          IMPRF & PERF & PRG-ANA & HAB-ANA & PNCT-ANA & SEMF-ANA \
#                 & INGR-ANA & TRM-ANA & CONT
#
#
# A. Grammar
# Phonology
#1. The sound system
#
#1.1. Consonants and consonant combinations in the texts: 
C: (b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|w|x|z)
CC: (ng|sh|zh|th)
# th is used to mark voiced and unvoiced dental fricative, 
# ng is the palatar nasal,
# sh is voiceless palatoalveolar fricative, and 
# zh voiced palatoalveolar frictive.
#
#1.2. Vowels in the texts:
V: (a|e|i|o|u|y)
VL: (aa|ee|oo|uu)
DIPH: (ai|ae|ao|au|ay|ea|ei|eo|eu|ey|ia|ie|io|oa|oe|oi|ou|oy|ua|ue|ui|uy)
TRIPH: (aou|aye|eau|eye|ieu|oeu|uoy)
V-APP: (aw|ew|ow)
#
# Pronunciation: vowels, consonants, and combinations of sounds forming 
# phonologically distinctive sounds in pronouncing: 
#
# Central, closed, mid V (V = e upside-down): 
#  (a|ei|o|u|y|ah|ai|ea|ei|eo|ia|io|oa|oe|oi|ou|ow|ue|eau|
# Central, closed, mid V (V = e upside-down), the first syllable stressed:  
#  a|o|u|y|oe|oo|ou|
# Central, closed,  mid  V + r (V = e upside-down), second SYLL: 
#  ar|er|ir|or|re|ur|yr|eur|our|
# Central, closed, mid V + r (V = e upside-down), main stress, first SYLL: 
#       er|ir|or|ur|yr|ear|err|eur|irr|our|urr|yrrh|
# \a\: a|e|i|ae|ai|au|ay|ea|ei|
# \aa\ (<a> combined with a line above): a|e|ae|ai|ao|au|ay|ea|ee|ei|ey|ie|ui|
# \ä\: a|e|i|o|aa|ah|au|ea|ou|eau|
# Closed a (a with a dot above): a|ar|au|aar|
# a combined with closed u (u with a dot above): au|ou|ow|aou|
# \e\: a|e|i|u|ae|ai|ay|ea|ei|eo|ie|oe|ieu|
# \ee\ (e combined with a line above): e|i|y|ae|ay|ea|ee|ei|eo|ey|ie|oe|
# \i\: a |e|i|i|u|y|ea|ee|ei|ia|ie|ui|
# \ii\ (i combined with a line above): i|y|ai|ay|ei|ey|ie|oy|uy|aye|eye|
# \oo\: a|o|ao|au|eo|ew|oa|oe|oh|oo|ou|ow|ua|eau|
# Closed o (o combined with a dot above): a|o|ah|au|aw|eo|oa|ou|ow|
# Closed o (o combined with a dot above) and i: aw|eu|oi|oy|uoy|
# ü: o|u|w|eu|ew|oe|oo|ou|ue|ui|eew|ieu|oeu)
# Closed u (u combined with a dot above): o|u|oo|ou)
#
# Webster 1989[1983]: 37-39:
# Consonants: 
# \b\: |v|bb|bh|pb| 
# \ch\: c|ch|cz|si|te|teh| 

# \d\: d|dd|dh|ed|ld|
# \f\: f|ff|gh|lf|ph|
# \g\: g|gg|gh|gu|
# \h\: g|h|j|ch|wh|
# \hw\: ju|wh|
# \j\: g|j|ch|dg|di|dj|gg|gi|jj|
# \k\:  c|k|q|cc|ch|ck|cq|cu|gh|kh|kk|lk|qu|cch|cqu|
# \kk (k underlined): h|ch|gh| 
# \l\: l|ll|lh|ln| 
# l preceding overshort o: l|al|el|le|yl| 
# \m\: m|gm|lm|mb|mh|mm|mn|chm|
# m preceding overshort o: en|ain|ernm|
# \n\: n|gn|kn|mn|mp|nn|pn|
# n preceding overshort o: en|on|ain|
# palatal nasal: n|nd|ng|ngg|ngu|
# \p\: p|ph|pp|
# \r\: r|rhrr|wr|rrh|
# \s\: c|s|z|ch|ci|ps|sc|ss|ts|t<|sch|sth|
# \sh\: c|s|ch|ci|sc|se|sh|si|sk|ss|ti|cgi|psh|sch|sci|ssi|chsi|
# \t\: t|bt|ct|et|ed|pt|th|tt|cht|ght|phth| 
# \th\: gh|th|ght|chth|phth|
# long th = th underlined: dd|dh|th|
# \v\: f|v|w|ph|vv|
# \w\: u|w|ju|ou|wh|
# \y\: i|j|y|
# \z\: s|z|x|cz|ss|ts|tz|zz|
# \zh\: g|j|si<zi|ssi)
# 
#
# 2. The structures of syllables
#
# Examples from the syllabic structures below deal only with literary forms 
# of words. These structures reflect only weakly the syllabic structure
# of words in spoken language. Affixation changes the syllabic structure.
# Syllabication of spoken language has to be specified separately.
# 
# Literal syllables, examples:
# i:    an-i-mal:       SYLL-V: \w(V)
# ei:   ei-gen-vec-tor: SYLL-VV: \w(V()V)
# be:   be-gin:         SYLL-CV: \w(C()V)
# day;  day-room:       SYLL-CVV: \w(C()V()V)
# gle:  an-gle:         SYLL-CCV: \w(C()C()V)
# free: free-dom:       SYLL-CCVV: \w(C()C()V()V)
#
# al:   fed-er-al:      SYLL-VC: \w(V()C)
# iar:  fa-mil-iar:     SYLL-VVC: \w(V()V()C)
# gen:  gen-er-al:      SYLL-CVC: \w(C()V()C)
# noon: noon:           SYLL-CVVC: \w(C()V()V()C)
# ea:   beat:           SYLL-CVVC: \w(C()V()V()C)
# gest: big-gest:       SYLL-CVCC: \w(C()V()C()C)
# thin: thin:           SYLL-CCVC: \w(C()C()V()C)
# grand: grand-mother:  SYLL-CCVCC: \w(C()C()V()C()C) 
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
# 3. The stress on the word-level (the principal stress rules)
# 
# 3.1. The principal stress on the root syllable (native words, 
# old words borrowed from French; 'king, 'kingly);
# W-STRESS-PF:  
# 3.2. The principal stress is on the penultimate syllable in words 
# in which the basic forms consist of three or more syllables: 
# photogra'phy, telegraph'ic (see above):
# W-STRESS-AP:
# 2.3. The principal stress is on the antepenultimate syllable 
# in the words borrowed from classical languages: tele'graphy, 
# W-STRESS-AP: 
# 3.4. The principal stress is on the syllable preceding the ending -ion:
# argumen'tation and adjectival ending -ic: pho'nemic.
# W-STRESS-D: 
# 3.5. The principal stress on the antepenultimate syllable in the words
# The principal stress is on the antepenultimate syllable in the words
# which have the adjectival ending -ian: 'library - libra'rian.
# W-STRESS-E: 
# 3.6. The principal stress is on the first member of compounds: 'black''bird:
# W-STRESS-F: 
# 3.7. The position of the principal stress on the homonymous words:
# The position of the principal stress separates the homonymous words which 
# lexically belong to verbs and nouns: N: 'contrast, V: cont'rast,
# N: 'present, V: pre'sent.
# W-STRESS-G: 
# 2.8. Secondary stress 
# The secondary stress (compounds, the second member: 'black''bird):
# W-STRESS-H:
# SYLL-UNSTRSS: (SYLL()(C)()(C)()V()(C) 
#
# Stress rules. ‘= principal stress, “= secondary stress (PF=the first syllable, AP=the 
# principal stress on the fourth syllable);
# V-UNSTR = unstressed vowel;
# STRSS-P = the principal stress on the root syllable;
# STRSS-S = the secondary stress on the third/pairless syllables; 
# STRSS-PS = a stressed syllable;
# STRSS-NS = a non-stressed syllable;
# the second and the fourth syllable are unstressed;
# STRSS-NS-D = an unstressed syllable containing a diphthong;
# STRSS-NS-V = an unstressed syllable containing a short or long vowel; 
# In addition to the basic rules (rules 1 and 2), 
# the stress rules have some varieties.
#
STRSS-PF: \w((SYLL|SYLL()SYLL))
STRSS-AP: \w(SYLL()SYLL()SYLL()SYLL)
STRSS-S: \w(SYLL()SYLL()SYLL)
STRSS-NS: \w((SYLL()SYLL)|(SYLL()SYLL()SYLL()SYLL)|
  (SYLL()SYLL()SYLL()SYLL()SYLL()SYLL))
STRSS-PS: \w((SYLL)|(SYLL()SYLL()SYLL))
#
STRSS: \w(STRSS-PF|STRSS-AP|STRSS-S|STRSS-NS|STRSS-PS)
#
#
# B. Lexicon and morphology
# I. Word stems
# 1. Stem types of nouns
# 
# There are changes in the ends of the stems of nouns in the case, when the 
# plural endings -s and -es are combined with the ends of words. 
#
# A distinctive property of nouns in English is that many of them are 
# homonymous with verbs. The nominal and verbal functions of these words 
# is separated with the stress relationships. 
#To be continued ...
#
# 2. Stem types of verbs
# 
# In verbal morphology, there are changes in some verb stems, when the 
# participle forms -ing (PCPL-) and -ed (PCPL-II and the PAST tense suffix) 
# are combined with them. The same changes take place, when the ancient 
# personal endings -th (3SG) and -st (2SG) are combined with certain verb 
# stems. The rules for describing the variation of stems are 
# presented in describing the combinations of verbs and participle and 
# past tense suffixes and personal marking.

# VERB-STEM: +th
# VERB-STEM: +e+th
# VERB-STEM: -y+th => -ie+th
# VERB-STEM: -VC+th => -VCC+th
#
#VERB-STEM: -y+e+st => ie+st
#VERB-STEM: -d+st
#VERB-STEM: -C+est => CC+est
#VERB-STEM: -V+d+st
#VERB-STEM: -C+ed+st 
#Verbs, R+st
#Verbs, R+e+st 
#
#
# II. Nominal morphology
#
# Classes of parts of speech
#
# Nouns
#
# 1. Number
#
# Singular is unmarked
#
# Plural: 
# (a) the plural is marked with the suffix -s. and after aveolar and
# post-alveolar fricatives (s, z, sh, zh) the plural suffix s is combined
# with -e: = > -es.
# (b) The vowel-e (dummy e) disappears before the suffix -es. 
# (c) The words having the word-final -o (e.g. potato) are combined with
# the plural ending -es: potatoes.
# (d) In the unstressed position, the word-final -y is changed to -ie:
# family => families, but boy, boyes. 
# (e) A great number of plural forms are lexicalized in English.
#
PL-I: \w(s)
PL-II: \w((s|z|sh|zh)es)
PL-III: \w((oe|ie)s)
PL: (PL-I|PL-II|PL-III)
#
# To be continued
#
# Adjectives
#
# Pronouns
#
# Conjunctions:
#
# 2. Possession marking
#
# In English, possession is marked with the genitive forms of personal 
# and interrogative pronouns.
#
#Possessive pronouns: (my|your|his|her|our|their|yours|ours|theirs)
#Genitive: 1) -'s and of
#
# 1.3. Structural means for developing and modifying lexicon
#
# 1.3.1. Prefixes in word formation
# Negative prefixes:
PREF-NEG: (un|non|dis|in)
# Reversative and privative prefixes:
PREF-RP: (un|de|dis)
# Pejorative prefixes:
PREF-PEJ: (mis|mal|pseudo)
# Prefixs of degree or size:
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
# 3.2. Particles as modifiers in word formation
# To be continued...
#
# 3.2.1. Particles in modifying nouns
# To be continued...
#
#Particles or phrases corresponding some clitic particles in Finnish:
#
CLT-W: (also|too|even|(not even)|weather|why|(is it)|(if only))
#
#
# 3.2.2. Particles in modifying verbs
# To be continued...
#
# Here: take into account the particles from the WordNet verb list.
#
#
# 4. Case marking
#
# In addition to the dictionary form (basic form), English has only one 
# formally marked case: genitive. The use of prepositions forms the  
# principal structural method in adjusting words in the contexts in English.
# On the prepositional system of English, c.f. ADPOS-CASE relators. 
#  
# To be continued.
#  
# 4.1. Nominative/absolutive
#
# The unmarked dictionary form is the basic form of nomnals.
# Nominative/absolutive (the dictionary form) is distinguished in the
# singular and plural forms. 
#
# 4.2. Genitive
#
# The rule GEN only distinguish the genitive forms.  The rule does not
# contain restrictors needed for generating the plural forms.
#
GEN: \w(((s|z|ch|sh|dz)es)|((se|ze)es)|of)
#
#
#Noun phrase (NP), English
#PRP + N
#PRP + A + N
#PRP + PRON-POSS + A + N
#PRP + (PRON-POSS +) (A +) N
#PRP + (PRON-DEM +) (PRON-DET +) (PRON-POSS +) (A +) N
#
# III. Inflection of verbs
# 
# 1. The verbs dealt with the project
#
# (a) The collection of verbs in the database: the list of verbs: 
# eng-verbs-database-may-2017.txt. 
# In the list, the dictionary forms are marked with the character "#".
# (b) The list of verbs of the project Wordnet: wordnet (/proj/lenca/wordnet).
# (c) The irregular verbs separated from the list of verbs in the Wordnet: 
# eng-irregular-verbs-cats-txt.txt. Different tense forms are separated from 
# the list of irregular verbs: IRREG-PRES, IRREG-PAST, IRREG-PERF-I, 
# and IRREG-PERF-II.
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
#INCLUDELIST: eng-verbs-test-be.txt VERB-TEST-BE
#INCLUDELIST: eng-verbs-test-bring.txt VERB-TEST-BRING
#INCLUDELIST: eng-verbs-test-come.txt VERB-TEST-COME
#INCLUDELIST: eng-verbs-test-flow.txt VERB-TEST-FLOW
#INCLUDELIST: eng-verbs-test-go.txt VERB-TEST-GO
#INCLUDELIST: eng-verbs-test-take.txt VERB-TEST-TAKE
#
INCLUDELIST: eng-verbs-som.txt VERB-TEST-@ 
#
INCLUDELIST: eng-verbs-som-loc.txt VERBS-SOM-LOC
INCLUDELIST: eng-verbs-som-ad-loc.txt VERBS-SOM-AD-LOC
#
INCLUDE: ENG-INF.spec
INCLUDE: ENG-VERBS-FINITE-TEST.spec
#
#INCLUDE: eng-disamb-AD-IN-EXCL.spec
#INCLUDE: eng-disamb-AD-ON-EXCL.spec
#INCLUDE: eng-disamb-AD-OUT-EXCL.spec
#INCLUDE: eng-disamb-DE-IN-EXCL.spec
#INCLUDE: eng-disamb-DE-ON-EXCL.spec
#INCLUDE: eng-disamb-DE-OUT-EXCL.spec
#
# Eliminating prepositions which modify verbs:
#
INCLUDE: eng-complex-verbs-EXCL.spec
#
#
# 2. Verbal nominal forms
# 2.1. Infinitive (INF)
# 
# The rules on verbal morphology (WN-etc.) in the Perl-script: /script/kwic:
# ACT, INF = WN-VERB = dictionary forms of verbs in WordNet. The following 
# rule moves the set of the dictionary forms of verbs to the category 
# infinitive (INF). 
#
# The infinitive forms of verbs are marked with the particle "to" 
# which precedes the dictionary forms of verbs: sing, go, etc. 
# The particle "to" before the verbs is distinguished from the database 
# with the disambiguation rule given in the file "eng-disamb-AD-ON.spec".
#
#
# 2.2. Participles: present participle (PCPL-I) and past participle (PCPL-II)
#
# The PCPL-I is formed with the suffix -ing and the PCPL-II is formed with the suffix -ed.
# The PCPL-II suffix is identical with the past tense marker.
# In the regular forms, the suffixes are combined with the word stem without changing the
# roots. In some verbs, adjusting the suffixes in the word stems are gone by causing
# some changes in the ends of the word stems. 
#
# When endings -ing and –ed are combined with the stems of verbs which ends with consonants 
# and the vowels -a, -i, -o, -u, y, the combinations do not cause any changes in the verb stems. 
# The rules of changes in combinations of participle suffixes and verb stems:
# (a) Deletion of -e: -e => zero: the word-final -e is dropped before the endings -ing and -ed.
# Exceptions: the final -e is not dropped before the ending -ing and -ed in the following 
# environments: -ee, -ye, -oe, and -ge: agree - agreed, dye - dyed, hoe - hoed, signe -signed.
# (b) The verbs ending with -y, -Cy => Ci
# (c) Doubling of consonants: 
# Final consonants (except x) are doubled in the case, when a morphological ending begins
#  with a vowel and when the preceding vowel is stressed and spelled with a single letter: 
# bar - barring - barred, permit - permitting - permitted.
# There is no doubling, when the preceding vowel is unstressed, or it is written with two letters: 
# enter - entered, dread - dreaded, visit - visited, stoop - stooped, de`velop - de`veloped.
# Doubling of consonants, exceptions: -g => -gg-, -c => -ck-
# (the combination -ck- denotes orthographically long consonants which with other consonants
# is marked with double consonants): humbug - humbuggin, trafic - traficked. 
# (In the British English the rule concerns also the following consonants -l, -m, and -p: -l => 
# -ll, -m => -mm, -p => -pp; with the consonant -p, also the structure without doupling exists)   
# (not x and the approximants w and j).)
# 
#VERB-DBL:  \w(V()C()C(ed|ing))
#
#PCPL-I: (((d|t)|((V-UNSTRSS(gg|ck))|
#  (c|f|h|k|p|q|s)| (bb|cc|dd|ff|gg|hh|kk|ll|mm|nn|pp|qq|rr|ss|tt|zz)|
#  (C(V-UNSTRSS|V()V)C))ing)
#
#PCPL-II: ((dde|tte)d)|
#  ((V-UNSTRSS(gg|ck))|
#  (c|f|h|k|p|q|s)|
#  (bb|cc|dd|ff|gg|hh|kk|ll|mm|nn|pp|qq|rr|ss|tt|zz)|
#  (C(V-UNSTRSS|VV)C)ed)
#
# The participle-rules are in the kwic-skript.
PCPL-I: (VERBS-PCPL-PRES)
PCPL-II: (VERBS-PCPL-PAST)
PCPL: (PCPL-I|PCPL-II)
#
#
# 2.3. Personal inflection
#
# In the modern standard English, only the third person in the singular form (3SG) is marked 
# (-s) in personal inflection. In the database consisting of a translation of the Bible, the third 
# person in the singular in the present tense is marked with the suffix -th, and the second person 
# in the present and the past tense forms is marked with the suffix -st. 
#
# On the ancient personal endings:
# (a) The third singular personal ending: 3SG:
# In the data, the ending -th in the ends of words is located after -e: > (e)th. 
# This third singular ending is found also after the past tense ending -ed (see below).  
#
# Homonymous words in the database are eliminatd with the disambiguation rules
# in the file "eng-disamb-PERS.spec".
#
# The rules marking the personal endings of verbs of the 2nd and 3rd persons 
# are in the kwic-script.
#
V-1SG: (VERBS-BASIC)
#VERBS-2SG: (((b|c|d|f|g|h|j|k|l|m|n|p|r|s|t|w|x|z(e)?)st)|(VERBS-BASIC))
#SG2: (ENG-VERBS-2SG)
#V-3SG: (((b|c|d|f|g|h|j|k|l|m|n|p|r|s|t|w|x|z(e)?))(th|s))
#SG3: (ENG-VERBS-3SG|VERBS-PRES-3SG)
V-1PL: (VERBS-BASIC)
V-2PL: (VERBS-BASIC)
V-3PL: (VERBS-BASIC)
VERB-PERS: (V-1SG|VERBS-2SG|VERBS-3SG|VERBS-3SG|V-1PL|V-2PL|V-3PL)
# 
#
# 2.4. Auxiliaries
#
# The basic forms of auxiliaries:
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
# 2.4.1. Personal inflection of the non-modal auxiliaries 
#
# The auxiliary verbs "be", "have" and "do" are neutral, and the other 
# auxiliary verb forms also are modal. The auxiliary verbs "shall" and 
# "will" are also used in forming complex tense forms.
#
#ACT, PRES, the verb "be":	
ACT-BE-PRES-1SG: (am)
ACT-BE-PRES-2SG: (are)
ACT-BE-PRES-3SG: (is)
ACT-BE-PRES-1PL: (are)
ACT-BE-PRES-2PL: (are)
ACT-BE-PRES-3PL: (are)
ACT-BE-PRES: (ACT-BE-PRES-1SG|ACT-BE-PRES-2SG|ACT-BE-PRES-3SG|
  ACT-BE-PRES-1PL|ACT-BE-PRES-2PL|ACT-BE-PRES-3PL)
#
#ACT, PAST, the verb "be":	
ACT-BE-PAST-1SG: (was)
ACT-BE-PAST-2SG: (were)
ACT-BE-PAST-3SG: (was)
ACT-BE-PAST-1PL: (were)
ACT-BE-PAST-2PL: (were)
ACT-BE-PAST-3PL: (were)
ACT-BE-PAST: (ACT-BE-PAST-1SG|ACT-BE-PAST-2SG|ACT-BE-PAST-3SG|
  ACT-BE-PAST-1PL|ACT-BE-PAST-2PL|ACT-BE-PAST-3PL)
#
#ACT, PERF, the verb “be” (e.g. have/has been)
ACT-BE-PERF-1SG: (have been)
ACT-BE-PERF-2SG: (have been)
ACT-BE-PERF-3SG: (has been)
ACT-BE-PERF-1PL: (have been)
ACT-BE-PERF-2PL: (have been)
ACT-BE-PERF-3PL: (have been)
ACT-BE-PERF: (ACT-BE-PERF-1SG|ACT-BE-PERF-2SG|ACT-BE-PERF-3SG|
  ACT-BE-PERF-1PL|ACT-BE-PERF-2PL|ACT-BE-PERF-3PL)
#
#ACT, PLUPERF, the verb “be” (e.g. have/has been)
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
#ACT, PAST, the verb "have":	
ACT-HAVE-PAST-1SG: (had)
ACT-HAVE-PAST-2SG: (had)
ACT-HAVE-PAST-3SG: (had)
ACT-HAVE-PAST-1PL: (had)
ACT-HAVE-PAST-2PL: (had)
ACT-HAVE-PAST-3PL: (had)
ACT-HAVE-PAST: (ACT-HAVE-PAST-1SG|ACT-HAVE-PAST-2SG|ACT-HAVE-PAST-3SG|
  ACT-HAVE-PAST-1PL|ACT-HAVE-PAST-2PL|ACT-HAVE-PAST-3PL)
#
# ACT-PERF: the present forms of the verb "have" and the PCPL-II form of the verb "be":	
ACT-HAVE-PERF-1SG: (have had)
ACT-HAVE-PERF-2SG: (have had)
ACT-HAVE-PERF-3SG: (has had)
ACT-HAVE-PERF-1PL: (have had)
ACT-HAVE-PERF-2PL: (have had)
ACT-HAVE-PERF-3PL: (have had)
ACT-HAVE-PERF: (ACT-HAVE-PERF-1SG|ACT-HAVE-PERF-2SG|ACT-HAVE-PERF-3SG|
  ACT-HAVE-PERF-1PL|ACT-HAVE-PERF-2PL|ACT-HAVE-PERF-3PL)
#
# ACT, PLU-PERF: the past forms of the verb "have" and the PCPL-II form of the verb "be": 	
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
#ACT, PAST, the verb "do":	
ACT-DO-PAST-1SG: (did)
ACT-DO-PAST-2SG: (did)
ACT-DO-PAST-3SG: (did)
ACT-DO-PAST-1PL: (did)
ACT-DO-PAST-2PL: (did)
ACT-DO-PAST-3PL: (did)
ACT-DO-PAST: (ACT-DO-PAST-1SG|ACT-DO-PAST-2SG|ACT-DO-PAST-3SG|
  ACT-DO-PAST-1PL|ACT-DO-PAST-2PL|ACT-DO-PAST-3PL)
#
#ACT, PERF, the verb “do” (e.g. have/has done)
ACT-DO-PERF-1SG: (have done)
ACT-DO-PERF-2SG: (have done)
ACT-DO-PERF-3SG: (has done)
ACT-DO-PERF-1PL: (have done)
ACT-DO-PERF-2PL: (have done)
ACT-DO-PERF-3PL: (have done)
ACT-DO-PERF: (ACT-DO-PERF-1SG|ACT-DO-PERF-2SG|ACT-DO-PERF-3SG|
  ACT-DO-PERF-1PL|ACT-DO-PERF-2PL|ACT-DO-PERF-3PL)
#
#ACT, PLUPERF, the verb “be” (e.g. had done)
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
# 2.5. Diathesis
#
# 2.4.1. Active
# Active: unmarked.
# See the personal marking (above), and moods, tense forms, and verbal 
# nominal forms below.
#
#
# 2.4.2. Passive
# Passive: complex tense forms formed with the auxiliary “be” and 
# its various tense forms.
#
# The passive of the second person is the dictionary form of verbs.
# The compound passive forms: having been & PCPL-II: having been gone.
# The perphrastiv passive forms are formed with some auxiliaries,
# and for that reason, inflection of auxiliaries has to be presented
# before definitions.
#
#PASS, INF-PRES
#to have been & PCPL-II: to have been gone:
#PASS-PRES: ((have|has) been PCPL-PCP-II)
#	
# Passive, infinitive present (to be called):
# PASS-INF-PRES: (to be (VERB-PCPL-PAST-A|VERB-PCPL-PAST-B))
# 
#PASS, INF-PERF
#to be & PCPL-PAST: #to be gone
#
# Passive, infinitive, perfect (to have been called)
# PASS-INF-PERF: (to have been (VERB-PCPL-PAST-A|VERB-PCPL-PAST-B)) 
#
# Passive, participle, perfect (called)
# (VERB-PCPL-PAST-A|VERB-PCPL-PAST-B)) 
#
# Passive, particple, present (being called)
# PASS-PCPL-PRES: (being (VERB-PCPL-PAST-A|VERB-PCPL-PAST-B))
##
# Passive, compound participle, past (having been called)
# PASS-PCPL-PRES: (being (VERB-PCPL-PAST-A|VERB-PCPL-PAST-B))
#
#PASS, PCPL-I: being gone
#being & PCPL-PAST
#
# Passive, participle, perfect, perifrastic (being called)
# PASS-PCPL-PERF: ((VERB-PCPL-PRES-A|VERB-PCPL-PRES-B) 
#  (being (VERB-PCPL-PAST-A|VERB-PCPL-PAST-B)))
#
# 2.4.3. Rules for forming passive forms
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
# 2.6. Moods
#
# 2.6.1. Indicative
#
# Indicative is not marked formally.
# 
# 2.6.2. Conditional
#
# English has two conditionals separated with tense marking: conditional present and 
# conditional past:
# Conditional Present (Conditional I): complex forms formed with the auxiliaries 
# should and would and the dictionary for of verbs.
# Conditional Past (Conditional II): complex forms formed with the auxiliaries should and 
#would and the present tense forms of the auxiliary have.
#
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
# 2.6.3. Potential
# There is no grammatical mood such as potential in English. 
# To be continued.
POT: (may)
#
#
#2.6.4. Imperative 
#
# Simple and complex forms: simple imperative forms are the dictionary forms 
# of verbs e.g. come, go. Complex direct or indirect commands are formed 
# with some auxiliaries denoting various aspects of modalities: e.g. 
# you should go, you have to go, you must go, etc.
#
ACT-IMP: (VERBS-BASIC)
#
#
# 2.6.5. Subjunctive 
# 
#to be continued.
#
#
# 2.7. Tense forms 
#
# The tense forms in English are structurally simple and periphrastic.
# The prefiphrastic forms are formed with auxiliaries which are marked
# with personal inflecion.
#
#
# 2.7.1. The simple basic tense forms
#
#(a) Present (PRES): 
# the present tense is unmarked. The personal marking concerns the old forms of 
# the second and third tense forms, and the personal marking of the 3SG forms. 
#
ACT-PRES: ((VERBS-BASIC)()(VERB-PERS))
#
# (b) Past (PAST): 
# The regular simple past tense forms are the same as the PERF-II. In the irregular verbs, the 
# past tense forms are lexical. 
# Regular past tense forms are formed with the suffix -ed and the irregular tense forms, see above:
#
#ACT-PAST: (VERBS-PAST)
# 
# Regular and irregular tense forms, see above:
#
# (c) The perfect (PERF): 
# The regular perfect tense form consists of the auxiliary “have” containing regular present
# tense marking and from the lexical verb in the PCPL-II form (I have called, he has been).
#Present perfect (have+PRES + PCPL-II: I have called, he has been)
ACT-PERF: ((have|has) (PCPL-II))
#
# (d) Pluperfect:
# The past tense form of the auxiliary have + the past participle form (PCPL-II) of the lexical
# verb: had called)
ACT-PLUPERF: ((had) (PCPL-II))
#
# (d) The pluperfect (PLU-PERF):
# The regular pluperfect tense form consists of the auxiliary “have” in the past tense form
# and from the lexical verb in the PCPL-II form (I had called, he had been).
#PERF-PAST: ((had) (VERB-PCPL-PAST))
#
# (e) Future
# will ('ll) + V-INF without to particle, all persons
# (shall + V-INF without to particle, 1SG, 1PL; he will sleep)
#
# Future I (Future present: I/we shall be, he/she/you/they will have)
#FU-PRES: ((shall|will) VERB-INF) => FUT-I
#
# Future II (Future past perfect: will/shall + have +PCPL-PRES:
# I/we shall have had / he/she/it/you/they  will have spoken)
#FUT-PAST: ((shall|will) (have (VERB-PCPL-PAST)))  => FUT-II
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
# ACT-PAST puuttuu.
FUT: (ACT-FUT-I|ACT-FUT-II)
#
#
# 2.7.2.The progressive tense forms
#
# (a) Progressive present: 
# Perifrastic tense form formed with the present tense forms of the auxiliary “be” and the
# PCPL-I of the lexical verb in the dictionary form (he is writing). 
# PRES-PROG: ((am|is|are) (VERB-PCPL-PRES-A|VERB-PCPL-PRES-B))
#
# (b) Progressive past: 
# Perifrastic tense forms formed with the past tense forms of the auxiliary “be” and the
# PCPL-I in the lexical main verb in the dictionary form (he was running).
# PAST-PROG: ((was|were) (VERB-PCPL-PRES-A|VERB-PCPL-PRES-B))
#
# (c) The progressive perfect: 
# Perifrastic tense form formed with the present tense forms of the auxiliary “have”, 
# the PCPL-II form of the auxiliary “be” and the PCPL-I form of the lexical verb 
# in the dictionary form (he has been singing).
# PERF-PRES-PROG: (((have|has) been) (VERB-PCPL-PAST-A|VERB-PCPL-PAST-B)) 
#
# (d) The progressive pluperfect: 
# Perifrastic tense form formed with the past tense form of the auxiliary “have”, 
# the PCPL-II form of the auxiliary “be” and the PCPL-I form of the lexical verb
# in the dictionary form (he had been talking).
# PERF-PAST-PROG: ((had) (been) (VERB-PCPL-PRES-A|VERB-PCPL-PRES-B))
# 
#
# 2.8.2. Progressive tense forms
#
#Active, progressive present (ACT-PRES-PROG, e.g. am/is/are running)
ACT-PRES-PROG-1SG: (am PCPL-I)
ACT-PRES-PROG-2SG: (are PCPL-I)
ACT-PRES-PROG-3SG: (is PCPL-I)
ACT-PRES-PROG-1PL: (are PCPL-I)
ACT-PRES-PROG-2PL: (are PCPL-I)
ACT-PRES-PROG-3PL: (are PCPL-I)
ACT-PRES-PROG: (ACT-PRES-PROG-1SG|ACT-PRES-PROG-2SG|ACT-PRES-PROG-3SG|
  ACT-PRES-PROG-1PL|ACT-PRES-PROG-2PL|ACT-PRES-PROG-3PL)
#
# Active, progressive past (ACT-PAST-PROG, e.g. was/were running)
ACT-PAST-PROG-1SG: (was PCPL-I)
ACT-PAST-PROG-2SG: (were PCPL-I)
ACT-PAST-PROG-3SG: (was PCPL-I)
ACT-PAST-PROG-1PL: (were PCPL-I)
ACT-PAST-PROG-2PL: (were PCPL-I)
ACT-PAST-PROG-3PL: (were PCPL-I)
ACT-PAST-PROG: (ACT-PAST-PROG-1SG|ACT-PAST-PROG-2SG|ACT-PAST-PROG-3SG|
  ACT-PAST-PROG-1PL|ACT-PAST-PROG-2PL|ACT-PAST-PROG-3PL)
# 
# Active, progressive perfect ACT-PERF-PROG, e,g, have/has been running)
ACT-PERF-PROG-1SG: (have been PCPL-I)
ACT-PERF-PROG-2SG: (have been PCPL-I)
ACT-PERF-PROG-3SG: (has been PCPL-I)
ACT-PERF-PROG-1PL: (have been PCPL-I)
ACT-PERF-PROG-2PL: (have been PCPL-I)
ACT-PERF-PROG-3PL: (have been PCPL-I)
ACT-PERF-PROG: (ACT-PERF-PROG-1SG|ACT-PERF-PROG-2SG|ACT-PERF-PROG-3SG|
  ACT-PERF-PROG-1PL|ACT-PERF-PROG-2PL|ACT-PERF-PROG-3PL)
#
# Active, progressive pluperfect ACT-PLUPERF-PROG, e,g, have/has been running)
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
#ACT-PAST: WN-VERB-PRET
#ACT-PCPL-I: WN-VERB-PCPL-PERF
#ACT-PCPL-II: WN-VERB-PCPL-PRES
#ACT-PERF: 
#ACT-PLUPERF: 
#
VERB-FINITE: (ACT-TENSE|ACT-TENSE-PROG|ACT-COND|
  PASS-TENSE|PASS-TENSE-PROG|PASS-COND)
# 
# VERB-NON-FINITE: (INF|PCPL)
#
# The Perl-script contains the following rule: #VERB-INF: (to VERB)
# The file "kwic" in the script-directory contains the link VERB-LIST,
# which introduces the file "eng-verbs-database-may-2017.txt" to be available
# for connecting the predicate-verbs and ADPOS-CASE relators for examining
# combinations of predicates and ADPOS-CASE relators in the texts. 
# The name is changed to VERB-DATA to concern only the verbs in the database.
#
VERB-ALL: (VERBS|VERBS-PRES-3SG|VERBS-PAST|PCPL|VERBS-2SG)
#
#VERB-SAMPLE: (ENG-SAMPL-VERB)
#
#
# C. Adjectives
#
#
# D. Pronouns
#
#
# E. Particles
#
#
# F. Conjunctions
#
#
# G. Prepositions
#
#
# IV. ADPOS-CASE RELATORS: Prepositions in English
#
#1. Locational prepositions
#1.1. Location of an object: IN, ON and OUT categories 
#
#1.1.1. Location of an object in, inside of a closed space (IN-PRP-A, IN-POP-B) and inside a bordered space, in a group, or between objects (IN-PRP-B, IN-POP-B)
#
IN-C: 
IN-PRP-A: ((in (a|an|the|my|your|his|her|its|our|their)
  (eye|heart|sight|eyes|hearts|sights) (of))|
  (within|inside|in))
IN-PRP-A-XX: (IN-PRP-A (\w+))
IN-POP-A:
IN-PRP-B: ((in (the (bottom|middle|midst|center)) (of))|
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
#1.1.2. Location of an object on or in touch with the surface of an object (ON-PRP-C, ON-POP-C), and outside of an object or a landmark,  not far from them (ON-PRP-D, ON-POP-D)
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
# The terms front, midst, inside, and outside have to be evaluated wrt 
# connections with prepositions.
#
#1.1.3. Location of an object outside (OUT) of or at a distance from an object or a landmark (OUT-PRP-E OUT-POP-E), and outside of another object, the distance not specified (far or near) (OUT-PRP-F, OUT-POP-F)
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
#1.2. Movement of an object from in, on, outside of another object 
#(delocation)
#1.2.1. Movement of an object from in, inside of a closed space (DE-IN-PRP-A, DE-IN-POP-A) and from inside a partly closed space or between other objects (DE-IN-PRP-B, DE-IN-POP-B)
#
DE-IN-C: 
DE-IN-PRP-A: ((from (the|my|your|his|her|its|our|their) 
  (eye|eyes|heart|hearts|sight|sights) (of))|
  ((from|out) (within|inside)))
DE-IN-PRP-A-XX: (DE-IN-PRP-A (\w+))
DE-IN-POP-A:
DE-IN-PRP-B: (((from|off|out) (between|amid|among|amongst|in))|
  ((off|from|out) (the) (middle|midst|center|bottom|hand|hands) (of)))
DE-IN-PRP-B-XX: (DE-IN-PRP-B (\w+))
DE-IN-POP-B: 
DE-IN: (DE-IN-PRP-A|DE-IN-PRP-B)
DE-IN-XX: (DE-IN (\w+))
#
INCLUDE: eng-disamb-DE-IN-EXCL.spec
#
# 1.2.2. Movement of an object from on smth: movement of an object from on or in touch with the surface of another object or a landmark (DE-ON-PRP-C, 
# DE-ON-POP-C), or not far from them (DE-ON-PRP-D, DE-ON-POP-D)
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
#1.2.3. Delocation of an object from outside of another object or  a landmark (DE-OUT-PRP-E, DE-OUT-POP-E), and from outside of an object or a landmark, the distance is vaguely expressed (DE-OUT-PRP-F, DE-OUT-POP-F)
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
#1.3. Movement of an object into, onto, and to outside of smth 
#1.3.1. Movement of an object into, to inside of a closed space (DIR-IN-PRP-A and DIR-IN-POP-A) and to inside a partly closed space or between other objects (DIR-IN-PRP-B and DIR-IN-POP-B).
# 
AD-IN-C: 
AD-IN-PRP-A: (((into|to) (the|my|your|his|her|its|our|their)
  (eye|heart|eyes|hearts|mouth) (of))|
  (into))
AD-IN-PRP-A-XX: (AD-IN-PRP-A (\w+))
AD-IN-POP-A:
AD-IN-PRP-B: (((down|into|to|unto|up) (between|amid|among|amongst|midst|in))|
  ((into|to) (the) (middle|midst|center))|
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
#1.3.2. Movement of an object on or in touch with the surface of another object (DIR-ON-PRP-IT, DIR-ON-POP-IT), and outside of an object, not far from it (DIR-ON-PRP-NF and DIR-ON-POP-NF). 
#
AD-ON-C: 
AD-ON-PRP-C: ((onto (against|on|upon))|
  (onto (the) (bottom|head|edge|end|ends|side|sides|top|tops))|
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
#1.3.3. Movement of an object outside of the  object (DIR-OUT-PRP-E, 
# DIR-OUT-POP-E), and outside of an object, the distance or relationship 
# with the object is vaguely expressed (DIR-OUT-PRP-F and DIR-OUT-POP-F). 
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
#INCLUDE: eng-disamb-AD-LOC-EXCL.spec
#
# 1. 3.4. Translocation of an object: 
# 1.3.4.1. Translocation regard to closed or partly closed space or between objects
#
TRNS-INT-C: 
TRNS-INT-PRP: (across|through|throughout|via)
TRNS-INT-POP:
TRNS-INT: (TRNS-INT-PRP)
TRNS-INT-XX: (TRNS-INT (\w+))
#
# 1.3.4.2. Translocation of an object with regard to open space
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
#INCLUDE: eng-disamb-adverbs-EXCL.txt
#
# Eliminating temporal expressions from the database:
# 
INCLUDE: eng-disamb-TRNS-EXCL.spec
#
#2. Terms denoting special temporal situations):
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
INCLUDE: eng-disamb-TEMP-WORDS.spec
#
#3. Prepositions denoting various circumstantial relationships (CIRC) (reason, motive, stimulus, reaction. support, accompaniment, close relationship, states of affairs, hindrance, opposition, standards, measurements, strengthening expressions, exceptions, negative condition, partiality or involvement of an eventuality, agent, ground, source, origin, ingredient)
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
# 4. Single lexical prepositions
PRP-SGNL: (above|across|after|against|along|amid|among|amongst|around|
  at|before|behind|below|beneath|beside|between|beyond|by|despite|
  down|during|except|for|from|in|inside|into|midst|near|nearer|nearby|
  nigh|of|off|on|onto|opposite|out|outside|over|past|regarding|round|
  since|through|throughout|till|to|toward|towards|under|underneath|
 y until|unto|up|upon|with|within|without)
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
#5. Complex prepositions
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
  (in the center)|
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
  (from (the) center of)|
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
  (into (the) center)|
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
  (to (the) center)|
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
