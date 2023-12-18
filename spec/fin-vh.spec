#Appendix I. The Categories denoting adpositional phrases in Finnish (30-06-2015).

#https://login.helsinki.fi/idp/Authn/HyLogin®
#Pirkko Suihkonen, 2006, 2007, 2015
#Copyright: Pirkko Suihkonen

#Name: Finnish		
#Family: Uralic languages	
#Sub-branch: Baltic-Finnic languages
#code: fin

#The suffixes which can be located after the case endings:
#1) Possessive suffixes: +n|+si|+mme|+nne|+n|+nsa|+ns‰
#2) Clitic particles: +ko|+kˆ|+kin|+kaan|+k‰‰n|+han|+h‰n|+pa|+p‰|+ka|+k‰
#B=back vowel, F=front vowel, HB=the illative ending of the type hVn, SV=illative ending of the type sVVn, VB/F=illative of the type Vn. 
POSS-SFX-B: (ni|si|mme|nne|an|nsa)
POSS-SFX-F: (ni|si|mme|nne|‰n|ns‰)
POSS-SFX: (POSS-SFX-B|POSS-SFX-F)
CLT-SFX-B: (kin|han|ka|kaan|ko|pa)
CLT-SFX-F: (kin|h‰n|k‰|k‰‰n|kˆ|p‰)
CLT-SFX: (CLT-SFX-B|CLT-SFX-F)

PTV-B: (ta|a)
PTV-F: (t‰|‰)
PTV: (PTV-B|PTV-F)
INE-B: ssa
INE-F: ss‰
INE: (INE-B|INE-F)
ELA-B: sta
ELA-F: st‰
ELA: (ELA-B|ELA-F)
ILL-HB: (han|hon|hun|hen|hin)
ILL-HF: (h‰n|hˆn|hyn|hen|hin)
ILL-VB: (an|on|un)
ILL-VF: (‰n|ˆn|yn)
ILL-SV: (seen|siin)
ILL: (ILL-VB|ILL-VB|ILL-HB|ILL-HF|ILL-SV)
ADE-B: lla
ADE-F: ll‰
ADE: (ADE-B|ADE-F)
ABL-B: lta
ABL-F: lt‰
ABL: (ABL-B|ABL-F)
ALL: lle 
ABE-B: tta
ABE-F: tt‰
ABE: (ABE-B|ABE-F)
ESS-B: na
ESS-F: n‰
ESS: (ESS-B|ESS-F)
TRL: (ksi|kse)
GEN: (n|den|tten)
INST: in
COM: ne
#
#The vowel harmony rules are not specified in the regular expressions:
#The plural suffixes are not separated: check the distribution of the plural suffixes.
#In the texts, the case endings with the front vowel do not occur in
#the non-compound words with the back vowel in the stem and vice versa.
#

#1. Location of an object:
# IN-C, IN-PRP, IN-POP 

#1.1. Location of an object in|inside of smth: 
IN-C: (INE|ADE)(POSS-SFX?CLT-SFX?)
IN-PRP:
IN-POP: (((kohda|keske)ADE-B))|((silmi|sis‰|ede)INE-F))(POSS-SFX?CLT-SFX?) 


#1.2. Location of an object on or in touch with smth:
ON-C: ADE((POSS-SFX)CLT-SFX?) 
ON-PRP:  
ON-POP: (((ede|p‰‰|ymp‰ri)ADE-F)|((h‰nn‰|nen‰)INE-F)|((juure|kohda|noka|pohja)INE-B)|((a|juure|kohda|huipu|huipui|pohja)ADE-B)|(vasten|vastaan))(POSS-SFX?CLT-SFX?) 


#1.3. Location of an object outside of smth:
OUT-C: (ADE|TRL|PTV)(POSS-SFX?CLT-SFX?) 
OUT-PRP: (vastap‰‰t‰|(kahtapuol(en|in|ta))|liki|((like|l‰he|keske)ADE))(POSS-SFX?CLT-SFX?)
OUT-POP: (vastap‰‰t‰|(kahtapuol(en|in|ta))|liki|takana|((a|((ala|ulko|yl‰)puole)|edusta|juure|kannoi|keskivaihei|taho|nurki|paikoi|puole|kupee|partaa|sivu|suunna|ulottuvi)ADE-B)|OUT-POP: (ede|h‰nni|j‰lji|kinterei|like|l‰he|liepei|l‰hettyvi|v‰li|ymp‰ri|y)ADE-F)|((jouko|keskuude|ohe|pari)INE-B)|((j‰lje|per‰|piele|syrj‰|viere)INE-F)|((kupee|puole|ulottuvi|suunna|poske|juure)(ADE-B|INE-B)))((ede|keske|l‰histˆ)(ADE-F|INE-F)))(POSS-SFX?CLT-SFX?) 


#2. Movement of an object from in|on|outside of another object (delocation):
#2.1. Movement of an object from inside of smth: 
DE-IN-C: ELA(POSS-SFX?CLT-SFX?)
DE-IN-PRP: 
DE-IN-POP: (((juure|kohda)ELA-B)|((sis‰|keske|keskemm‰|silmi)ELA-F)|((sis‰|keskemm‰)ABL-F)|keskemp‰‰)(POSS-SFX?CLT-SFX?)


#2.2. Movement of an object from on smth: 
DE-ON-C: ABL(POSS-SFX?CLT-SFX?) 
DE-ON-PRP: 
DE-ON-POP: ((huipu|huipui|noka|pohja)ABL-B)((nen‰|p‰‰|ymp‰ri)ABL-F)(POSS-SFX?CLT-SFX?) 


#2.3. De-location of an object from outside of smth: 
DE-OUT-C: ABL(POSS-SFX?CLT-SFX?)
DE-OUT-PRP: ((keskivaihe)ABL-B)((keske|like|l‰he)ABL-F)(POSS-SFX?CLT-SFX?)

DE-OUT-POP: (((a|alapuole|edusta|juure|kupee|keskivaihei|kohda|partaa|paikoi|pohja|puole|sivu|suunna|taho|ulkopuole|ulottuvi|yl‰puole|ede|h‰nni|kannoilta)ABL-B)j‰lji|kinterei|keske|liepeill‰|hettyvi|like|l‰he|v‰li|y|ymp‰ri|)ABL-F)|((jaloi|jouko|keskuude|ohe|poske|puole|sea)ELA-B)|((j‰lje|syrj‰)ELA)|((kohda|noka|suunna|ulottuvi|varre)(ABL-B|ELA-B))|((ede|ee|keske|l‰histˆ|n‰kyvi|per‰|piele|viere)(ABL-F|ELA-F))|(vastap‰‰t‰|takaa|luota|tykˆ‰))(POSS-SFX?CLT-SFX?)


#3. Ad-location of an object into|onto|to outside of smth
#3.1. Ad-location of an object into|to inside of smth: 
ADD-IN-C: (ILL|TRL)((POSS-SFX)CLT-SFX?)
ADD-IN-PRP: 
ADD-IN-POP: ((kohta|valta)ILL)|(sis‰)ILL)(POSS-SFX?CLT-SFX?) 


#3.2. Ad-location t of an object onto smth:
ADD-ON-C: ALL(POSS-SFX?CLT-SFX?)
ADD-ON-PRP: 
ADD-ON-POP: ((p‰‰|y)ALL-F)(POSS-SFX?CLT-SFX?)


#3.3. Ad-location to outside of smth:
ADD-OUT-C: ALL(POSS-SFX?CLT-SFX?)
ADD-OUT-PRP: (vastap‰‰t‰|(kahtapuol(en|in))|ulkopuolelle)(POSS-SFX?CLT-SFX?)
ADD-OUT-POP: ((vastap‰‰t‰|(kahtapuol(en|in|ta))|ymp‰ri|keskemm‰(ksi)|taa(kse)|luo(kse)|tykˆ)|((a|alapuole|edusta|ede|juure|j‰lji|huipu|h‰nni|kannoi|keske|keskivaihei|kinterei|kupee|liepei|like|l‰he|l‰hettyvi|l‰histˆ|paikoi|partaa|pohja|puole|sis‰|suunna|ulkopuole|v‰li|yl‰puole|ulottuvi|ymp‰ri)ALL)|((alkup‰‰|p‰‰)ILL-HF)|(joukko|juure|j‰lke|kohta|loppu|nokka|ohe|piele|piiri|poske|puole|puoliv‰li|v‰li|suunta|ulottuvi|varte|viere|v‰li)ILL-VB)|
((nen‰|per‰)ILL-VF)(POSS-SFX?CLT-SFX?)


#3.4. Translocation of an object with regard to through, along, over, and under another object 
#4.1. Terms denoting different types of contacts between objects (CNTS):
TRNS-IN-C: 
TRNS-IN-PRP: 
TRNS-IN-POP: (halki|kautta|lomassa|l‰pi|poikki|(lomi|l‰vi|poiki)tse)(POSS-SFX?CLT-SFX?)


#4.2. Terms denoting different types of locations and movements objects outside of another object (LMOS):
TRNS-EXTR-C:
TRNS-EXTR-PRP:
TRNS-EXTR-POP: (((ali|alapuoli|edi|kupei|ohi|p‰‰lli|sivui|tai|ulkopuoli|vieri|v‰li|yli|yl‰puoli|ymp‰ri)tse)|ali|a|yli|ohi|ymp‰ri|takaa|pitkin|v‰list‰|alapuolella)(POSS-SFX?CLT-SFX?)


#4.3. Terms denoting different typs of distances between objects (DSTS):
DSTS-C:
DSTS-PRP:
DSTS-POP: ((asti|saakka|kohti|kesken|kohdalla|kohtaan|l‰htien|puoliv‰liss‰|(alkup‰‰|loppup‰‰|p‰‰|v‰li)ss‰)|((keskemm‰|v‰li)st‰)|keskell‰|keskemp‰‰|v‰litse)(POSS-SFX?CLT-SFX?) 


#5.1. Temporal limits of eventualities (TLE): 
TLE-C: TRL|PTV(POSS-SFX?CLT-SFX?)
TLE-PRP: (ennen|j‰lkeen)(POSS-SFX?CLT-SFX?)
TLE-POP: (j‰lkeen|koommin|asti|saakka|ohi|per‰st‰|selk‰‰n|kynnyksell‰|keskivaiheilla|parissa|puoliv‰liss‰|v‰lill‰|aikaan|aikoihin|suunnilleen|pintaan|((keskimmai|pinna)INE-VB)|((hujakoi|keskivaihei|korvi|tienoi|vaihei)ADE-B))(POSS-SFX?CLT-SFX?)
#(marked with the adessive, ablative, and allative case endings)


#6. CIRCUMSTANTIALS

#6.1. Manners, means, instruments, amounts:
MAN-C: (ESS|TRL|PTV|ADE)(POSS-SFX?CLT-SFX?)
MAN-PRP:
MAN-POP: (kanssa|kautta|kera|tavoin|((avu|kera|lai|uha|voima)ADE-B)|(arvosta|t‰ydelt‰|tasalla|tasalle)(POSS-SFX?CLT-SFX?) ) 


#6.2. Cause, reason, motive, stimulus and reaction: 
CAUS-C: ADE((POSS-SFX)CLT-SFX?) 
CAUS-PRP:
CAUS-POP: (((kiusa|mieli|vuo)TRL)|((puole|sija)ELA-B)|kiusalla|mieleen|per‰‰n|tautta|takia|t‰hden|vasten|vastoin)(POSS-SFX?CLT-SFX?)


#6.3. Basic conditions: agent, ground, source, origin, standards, ingredient
BASE-C: 
BASE-PRP:
BASE-POP: (((aloittee|johdo|toime)ELA-B)|((miele|m‰‰r‰yk)ELA-F)johtuen|mukaan|pakottamana|((noja|perustee)ADE-B)|((ansio|toime|puole|suhtee)ELA-B)|nimeen|suhteen|suhteessa|koskien)(POSS-SFX?CLT-SFX?) 


# 6.4.Direction: recipient, purpose, goal and target: 
TRG-C: 
TRG-PRP: 
TRG-POP: (((edu|hyv‰)TRL)|(koh(den|taan|ti))|varten)(POSS-SFX?CLT-SFX?) 


#6.5. Support, accompaniment, close relationship, states of affairs:
CNJ-C: COM(POSS-SFX?CLT-SFX?) 
CNJ-PRP:
CNJ-POP: (kesken|myˆt‰|suhteen|varaksi|luo|luokse|luota|((luo|muka)ESS-B)|((hampai|hoiva|hoima|huoma|huosta|hotei|kan|matka|mua|turvi|valla|yhteyde)INE-B)|((hoiva|hoima|huoma|huosta|hotei|matka|turvi)ELA-B)|((k‰si|kynsi|kynsi|yhteyde)ELA-F)|((huoma|huosta|matka|hoivi|turvi|valta|vara|k‰si|kynsi|yhteyte)ILL-VB)|((juttusi|puhei|puole|vara)(ADE-B|ABL-B|ALL)))(POSS-SFX?CLT-SFX?)


#6.6. Hindrance, opposition, state of affairs, standards, strengthening expressions, exceptions, negative condition, partiality or involvement of an eventuality: 
STAF-C: ABE(POSS-SFX?CLT-SFX?)
STAF-PRP: 
STAF-POP: ((ilman|lis‰ksi|paitsi|vailla|vaille|vastoin|vastuksinta|turvin|varaksi|syrj‰‰n|turviin|syrj‰ss‰|mielest‰)|
	((niska|sija|suhtee|turvi)INE)|
	((huolima|lukuunottama)ABE)|
	((armo|niska|sija|turvi)ELA)|
	((niska|sija|vara)ILL)|
	((armoi|kustannukse|niskoi|tila|uha|vara)ADE)|
	((niskoi|tila)ABL)|
	((niskoi|tila)ALL))(POSS-SFX?CLT-SFX?)
