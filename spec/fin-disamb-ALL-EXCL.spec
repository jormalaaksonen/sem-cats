#Pirkko Suihkonen, 2016 and 2017
#Copyright: Pirkko Suihkonen
#
#INE (-ssa/-ss�)
#
# Agreement in NPs: 
# only one case marking is accepted in the NP:s which contain specifiers 
# and modifiers preceeding the lexical head which is a noun:
# t�+ss� piene+ss� poja+ssa. 
#
# The words inside the parentheses contain the combinations <ssa> and <ss�> 
# which are homonymouos with the indices of the inesseive case 
# (fin.spec, Rule 1.1, INE-C and adpositions) in Finnish. 
#
# Sanat "syd�mess�, syd�miss�, sis�ss�, silmiss�, v�liss�", ovat sek� substantiiveja ett� adpositioita. Sanaluokkien jakauma on tarkastettava tekstist�, 
#
# N-PRP, SG-NOM:
ALL-EXCL: ^((gassa|hadassa|massa|missa|rissaan|ussa)|
#
# PRP-N, foreign words, illative (-an):
  ((gassa|hadassa|massa|missa|rissaan|ussa)an)|
#
# Adpositions mentioned in the file fin.spec: 
# IN-POP-A: 
  ((silmi|sis�|syd�me)ss�)(POSS-SFX?CLT-SFX?)|
  (tulen liekiss� keskell�)|
#
# IN-POP-B: 
  ((v�liss�|per�ll�|seassa)(POSS-SFX?CLT-SFX?))|
#
#
# ADE (-lla/-ll�)
#
# Agreement in NPs: 
# only one case marking is accepted in the NP:s which contain specifiers and 
# modifiers preceeding the lexical head which is a noun: 
# t�+ll� piene+ll� poja+lla. 
#
# The words inside the parentheses contain the combinations <lla> and <ll�> 
# which are homonymous with the indices of the adessive case 
# (fin.spec, Rule 1.2, ADE-C and adpositions) in Finnish. 
#
# Ambiguous structures:
# sill� = CONJ (62), 
# sill� = the adessive form of the demonstrative prnouns se.
#
# Nouns:
# Proper nouns, GEN (-n):
  ((drusilla|priskilla|silla|ulla)|
  ((drusilla|priskilla|silla|ulla)n))(POSS-SFX?CLT-SFX?)|
#
# Common nouns, GEN (-n):
  ((((esi|ilma|kaikki|tuomio|v�ki|yli)?valla)|
  kulla|mulla|villa)n)(POSS-SFX?CLT-SFX?)|
# 
# Nouns, SG-NOM:
  (helle)(POSS-SFX?CLT-SFX?)|
#
# Adjectives
  (hell�)(POSS-SFX?CLT-SFX?)|
#
# Verbs:
# Infinitives (V-back, -lla):
  ((ajatel|arvostel|astel|ennustel|harhail|iloitel|katsel|kiroil|
  koetel|kohdel|kuol|kuul|luetel|luul|majail|nuhdel|ol|oleskel|ommel|
  palvel|puhel|puhutel|rakennel|remahdel|rukoil|seurustel|sommitel|
  suositel|suudel|taistel|tavoitel|totel|tul|turmel|tutkistel|uhitel|
  vaellel|valhetel|varjel|viekoitel|voidel|voivotel)la)(CLT-SFX?)|
#
# Infinitives (V-back, -ll�):
  ((heitel|hypel|k�yskennel|kierrel|kysel|k�vel|l�mmitel|niel|ny�kytel|
  oleskel|pidel|piileskel|riidel|syleil|vietel|viljel|
  v��ristel|ylv�stel)l�)(CLT-SFX?)|
#
# Imperatives and connegatives:
  (kiell�|sivalla|vaella)(CLT-SFX?)|
#
# Ambiguous (homonyms: infinitive and the adessive form of the 
# demonstrative adjective "sama": samoilla.
#
# Inflected forms:
# V-PRES. 1SG, 1PL:x1:
  ((puhalla|tallaa|uskalla|vaella)(n|mme))(CLT-SFX?)|
  (elle|kiell�(n|mme))(CLT-SFX?)|
#
# Pass. Pres. (V-back (la-an))
  ((ennustel|huhuil|koetel|kuul|kuulustel|lankeil|nuhdel|ommel|palvel|pudistel|
  raadel|tavoitel|tul|valhetel|varjel|voidel)laan)(POSS-SFX?CLT-SFX?)|
#
# Pass. Pres. (V-front (l�-�n))
  ((hyv�il|viljel|viskel)l��n)
  (POSS-SFX?CLT-SFX?)|
#
# Particles:
# (kyll�|kyll�h�n|kyll��ns�|kyll��nne|kyll��si|kyll�si|kyll��ns�h�n|
#  todella|todellakin|
#  v�h�ll�p�|tahallamme|tahallanne)|
#
# Adpositions taken into account in the file fin.spec:
# ON-POP|PRP-C: 
#  (vasten|alla|p��ll�|partaalla|partailla|pinnalla|
#  pohjalla|pohjilla|reunassa|reunoissa|reunalla|reunoilla)
#  (POSS-SFX?CLT-SFX?)|
#
#  ON-PRP|POP-D:
#  ON-POP-D: (edess�|edustalla|ohessa|��ress�)|
#  (h�nnill�|j�ljess�|juurella|juurilla|kannoilla|kintereill�|kohdalla|
#  keskikohdalla|likell�|l�hell�|luona|niskassa|paikalla|
#  per�ss�|rinnalla|sivussa|sivuissa|sivulla|sivuilla|suulla|syrj�ss�|
#  takana|v�lill�|vastap��t�|vieress�|yll�)(POSS-SFX?CLT-SFX?)|
#
#Conjunction "sill�", OT and NT:
#SILLA-CONJ: ((, |. |; |: |! |? |' |\" |- )sill�))
#1. demonstrative "sill�" in NPs marked with the adessive case:
#  (sill� (^@a?b?c?d?e?f?g?h?i?j?k?l?m?n?o?p?q?r?s?t?u?v?w?x?y?z?)ADE)|
#2. except habeo constructions and idioms:
#  (sill� (ole|oli|on|tavoin))|
#3. "sill�" in restrictive relative clauses:
#  (sill�, (joka|jolla|jonka|mink�))|
#4. except demonstrative "sill�" referring to objects mentioned in 
# before in the utteraces or in previous expressions:
#  ((syd�memme|teot|makaat|maan) sill�)|
# Lis�ksi kaikki tapaukset, joissa "sill�"-sanan ymp�rill� on sanav�li.
#  ( sill� )
#
#
# ELA (-sta/-st�)
# Agreement in NPs: 
# and modifiers preceeding the lexical head which is a noun:
# t�+st� piene+st� poja+sta. 
###
# The words inside the parentheses contain the combinations <sta> and <st�> 
# which are homonymous with the indices of the elaive case 
# (fin.spec, Rule 2.1, ELA-C and adpositions) in Finnish. 
#
# Nouns
# Proper nouns (ELA-EXCL-PRP):
  (artahsastan|bistan|nehustan|parmastan)|
  ((festus|herodes|jeesus|johannes|kornelius|barabbas|barnabas|elias|
  jeremias|juudas|antikristus|kristus|lasarus|sakarias|
  saulus|tammus|tiitus)ta)(POSS-SFX?CLT-SFX?)|
#
# Common nouns:
# CN: NOM/A (zero): 
  (alusta|evankelista|edusta|hopeajalusta|iskulasta|jalusta|kaista|
  kiista|lista|maapalsta|musta|palsta|peltopalsta|perusta|riista|saasta|
  selusta|vaskijalusta)(POSS-SFX?CLT-SFX?)|
#
# CN: PTV (V-back, -ta; kun sija m��ritell��n siten, ett� se liittyy
# heikkoon vokaalivartaloon, voidaan kaikki konsonanttiloppuiset 
# partitiivit poistaa):
  ((ahdistus|ajatus|allas|anteeksiantamis|anteeksiantamus|arvoitus|
  asukas|asumus|aviorikos|avustus|elatus|enkeliruhtinas|esaias|filippus|
  ep�jumalanpalvelus|erotus|esikois|hajaannus|hallitus|hapatus|
  harjoittamis|hautaamis|hautaus|heilutus|heikontumis|helpotus|
  herjaus|ihmislas|ihokas|hevos|hius|huojennus|jeesus-las|opetuslas|
  jous|juhlakokous|julistus|jumalanpalvelus|juomis|juopumus|kangas|
  kansalais|kantamis|kantamus|katselmus|kattamis|kauhistus|kehoitus|
  kerros|kerskaamis|kerskaus|kertomus|kiitos|kirjoittamis|kirjoitus|
  kirkastumis|kirous|kirvoitus|kompastus|korjaamis|korotus|korvaus|
  kukistumis|kultarengas|kultakudos|kuningas|kunnioitus|kuolinsuitsutus|
  kurittamis|kuritus|kutsumis|kuukautis|kuuluttamis|kuvaus|lammas|
  (lapseksi(-)?ottamis)|las|liikuttamis|lohdutus|lukemis|lunastus|luopumus|
  luottamus|lupaus|mooses|muukalais|muutos|muurirakennus|nais|nauttimis|
  nuorukais|neitos|ohjaus|oinas|oksennus|olemus|omais|opettamis|opas|
  opetus|oras|osoittamis|ottamis|paastoamis|paheksumis|pahennus|
  pakolais|pakkosiirtolais|palaamis|palkkalais|palmikoimis|palvelus|
  palvelustoimitus|(papin(-)?ihokas)|pappispalvelus|parannus|
  parantamis|parjaus|p��nalais|p��si�islammas|pelastus|pellavakangas|
  pensas|perustamis|perustus|petos|pilkkaamis|pitalis|pohjois|
  poistamis|polttamis|porras|profetoimis|puhdistus|puhkeamis|
  pukeutumis|punonnais|puolustautumis|pyh�kk�palvelus|p�yt�palvelus|
  raavas|rakennus|rakentumis|raastosaalis|rangaistus|rannerengas|
  rasitus|ratsuhevos|rengas|reunus|riistosaalis|rikkomus|rikos|
  ripustamis|ruhtinas|rukous|ruoskimis|ruumis|ry�st�saalis|saalis|
  saamis|saas|sanomis|sekoitus|seos|sortumis|sinettisormus|sitomis|
  siunaus|skyyttalais|sotapalvelus|sovitus|suitsutus|sukurutsaus|
  suorittamis|suosionosoitus|suositus|suunemilais|suuttumus|
  syntiuhrikauris|sy�tt�raavas|taikomis|taivas|tallaamis|tapaus|
  tarkoitus|tarsolais|tavoittelemis|teos|teuras|todistus|toimittamis|
  toteutumis|tulemis|tulemus|tuntemis|tuntemus|tuomis|uhraamis|
  uskallus|vaellus|vaeltamis|vahvistus|vahvistumis|vaikerrus|
  vainoamis|valittamis|valivaliolammas|valkenemis|valmistamis|
  vanhus|vannomis|vapautus|varas|varis|varvas|varoitus|
  (vaski(allas|hakas|jous|rengas))|veronhuojennus|vastaus|vastustus|
  vaunuhevos|vavistus|v�entungos|vedenpaisumus|velallis|verenvuodatus|
  veronhuojennus|vertaus|vieras|vihaamis|vihollis|virvoitus|vitsaus|
  yl�snousemus|ymp�rileikkaus)ta)(POSS-SFX?CLT-SFX?)|
#
# CN: PTV (V-front, -t�):
  ((h�vi�mis|ammonilais-iljetys|eteis|ev�s|henk�ys|hillitsemis|
  hylk��mis|hyv�ksymis|hyv�ntekemis|h�mm�stys|h�p�isemis|h�v�istys|
  h��m�tys|h�vitys|ies|ihmis|ihmisymm�rrys|ik�v�imis|ilmestymis|
  ilmestys|ilvehtimis|itsens�hillitsemis|jalkamies|j�lkel�is|j�nis|
  j�rjestys|j��nn�s|keih�s|kest�mis|k�rsimys|k�ytt�mis|k��ntymys|
  kiert�mis|l�himm�is|levi�mis|lis��mis|maanj�ristys|m��r�ys|
  menemis|menestys|merkitys|mets�kyyhkys|
  ((murha|p��|p��llys|p��t�s|per�|ratsu|sadanp��|valio|viha|
  viidenkymmenenp��)?mies)|p��si�is|pelk��mis|pesemis|peseytymis|
  poisviemis|pylv�s|pyydys|pyyt�mis|s��s|s��t�mys|selitys|
  siki�mis|sotamies|synnytt�mis|syyt�s|sy�mis|teett�mis|tekemis|
  t�ytel�is|t�yttymis|t�ytt�mis|ter�s|v�hent�mis|v�hennys|v�ijytys|
  vasenk�tis|veis|veljes|viemis|vihkimis|vihkiytymis|
  ylistys|ylist�mis|yltymis|ymm�rrys)t�)(POSS-SFX?CLT-SFX?)|
#
# A: PTV (V-back, -ta): 
  ((aamuis|ahdas|aikais|ainokais|aineellis|anakilais|anatotilais|
  aramilais|daanilais|edomilais|egyptin-aikais|arvois|arvokas|
  arvollis|aviollis|erikois|erinomais|esikuvallis|etumais|etiopialais|
  filistealais|halpasukuis|halkeamis|harhaoppis|harras|haureellis|
  hebrealais|heikkouskois|helakanpunais|herkullis|hiljais|hurskas|
  hyv�nhajuis|ihotautis|iankaikkis|i�nikuis|ikuis|ilmais|jalosukuis|
  jaspis|jokavuotis|juutalais|kaikenkaltais|kaikkinais|kaikkivaltias|kallis|
  kallisarvois|kaltais|kaikenkaltais|kapinallis|karvais|karvas|
  kastei|katoavais|kaukais|kaunis|keskin�is|kirkas|keskin�is|
  kohtuullis|kolmitahkois|kompastuvais|kookas|korkuis|kreikkalais|
  kultais|kuninkaallis|kunniallis|kuolevais|kuvannollis|kuvapatsas|
  liukas|luonnollis|luvallis|lyhytaikais|maallis|mahdollis|makedonialais|
  miehenpuolis|mieluis|mink�kaltais|monilukuis|mooabilais|muinais|
  mukais|muotois|omais|nasaretilais|onnellis|otollis|pahanlaatuis|
  paljas|pallonmuotois|paras|patsas|pellavais|pellavapukuis|pitalitautis|
  petollis|pitalis|pohjoispuolis|puolis|puhdas|purppuranpunais|
  puutteenalais|raikas|rakas|rakentavais|raskas|rauhallis|rikas|
  rikollis|ruhtinaallis|runsas|rupis|ruumiillis|saastais|
  sairas|salais|samankaltais|seitsenhaarais|senkaltais|senpuoleis|
  seurakunnankokous|sielullis|sotakelpois|sotakuntois|sovelias|
  suitsevais|sulois|suolais|taidollis|taivaallis|taivais|
  tapais|tarpeellis|tasais|tavallis|t�m�nkaltais|totis|tulevais|
  tulis|turmiollis|t�h�nastis|ulkonais|uppiniskais|urhoollis|
  vaarallis|vahingollis|vaikeatajuis|vaivais|vajavais|vakallis|
  vakituis|valheellis|valkois|vanhurskas|vasullis|velallis|
  vertais|vihollis|viisas|villais|virsta|v�kivaltais|voimallis|
  yht�mittais|ylenpalttis|ylimm�ispapillis)ta)(POSS-SFX?CLT-SFX?)|
#
# A: PTV (V-front, -t�): 
  ((egyptil�is|edellis|eksytt�v�is|ensimm�is|entis|er�s|hengellis|
  h�pe�llis|hy�dyllis|hy�tymist�|ihmeellis|ilmeis|imev�is|it�is|jisreelil�is|
  jokap�iv�is|keskin�is|leevil�is|nurjasyd�mis|n�k�is|n�yrtyv�is|
  nykyis|oikeamielis|p��llimm�is|perillis|pett�v�is|p�iv�llis|
  pysyv�is|rehellis|runsasvetis|samanmielis|siivek�s|synnytt�v�is|
  syntis|syyllis|terveellis|t�ydellis|t�ytel�is|v�h�is|veljellis|
  veljes|viimeis|vilpillis|yhteis|yht�l�is|yksin�is|ylh�is|ylimm�is|
  ymm�rt�v�is)t�)(POSS-SFX?CLT-SFX?)|

# ELA-EXCL-PRN:
  ((((jol|kahden|kaiken|mink�|mink��n|sel|tuol|t�l)lais)|
  ((mink�|saman|sen|t�m�n)kaltais)|
  jokais|mois|semmois)ta)(POSS-SFX?CLT-SFX?)|
#
# NUM, -toista: 
  (((yhdell�|yhdelle|yhden|yhdennen|yhtenten�|yhten�|yhdenness�|yhdenteen|
  yhdes|yksi|kahdet|kahden|kahtena|kahdella|kahdelle|kahdesta|kahteen|
  kahta|kahdeksi|kahdessa|kahdes|kahtena|kahden|kahdennen|kahdentena|
  kahdennella|kahdennelle|kahdennesta|kahdenteenteen|kahdennetta|
  kahdenneksi|kahdennessa|kahdenteen|kahdes|kahdetta|kaksi|
  kolme|kolmannesta|kolmantena|kolmas|kolmen|kolmesta|kolme|
  nelj�|nelj�n|nelj�nnen|nelj�nteen|nelj�nten�|nelj�st�|nelj�tt�|
  nelj�s|nelj�tt�|
  viisi|viiteen|viideksi|viiden|viidennen|viidenten�|viidennell�|
  viidett�|viides|viidell�|viiteen|
  kuusi|kuuden|kuudentena|kuudes|kuusi|
  seitsem�n|seitsem�s|seitsem�st�|seitsem�nten�|
  kahdeksas|kahdeksan|kahdeksantena|kahdeksan|
  yhdeks�n|yhdeks�nten�|yhdeks�nnes|yhdeks�s)toista)|
  (kymmentuhantista)|
  (puolen|puolta|puoltatoista))(CLT-SFX?)|
#
# V-INF-I (V-back, -ta):
  ((ilmais|katkais|nous|puhkais|rohkais|sokais|valkais|vapis)ta)|
#
# V-INF-I (V-front, -t�):
  ((jylis)t�)|
#
# V-IMP (V-back, zero):
  (aavista|ahdista|anasta|arvosta|asusta|ennusta|haasta|harrasta|
  innosta|julista|kallista|kasta|katsasta|kirkasta|korosta|kosta|
  kukista|loista|lunasta|maista|matkusta|muista|nosta|mullista|
  notkista|omista|opasta|osta|paista|paljasta|muista|nosta|osta|
  paljasta|pelasta|poista|ponnista|puolusta|pudista|purista|
  raasta|rakasta|rangaista|ratkaista|ratsasta|ripusta|suista|tarkasta|
  teurasta|todista|tunnusta|uudista|vahvista|valista|valjasta|
  valmista|varasta|varusta)(CLT-SFX?)|
#
# V-IMP (V-back, -kaa, -koon, ko):
  ((aavista|ahdista|anasta|arvosta|asusta|ennusta|haasta|harrasta|
  innosta|julista|kallista|kasta|katsasta|kirkasta|korosta|kosta|
  kukista|loista|lunasta|maista|matkusta|muista|nosta|notkista|mullista|
  notkista|omista|opasta|osta|paista|paljasta|muista|nosta|osta|
  paljasta|pelasta|poista|ponnista|puolusta|pudista|purista|
  raasta|rakasta|rangaista|ratkaista|ratsasta|ripusta|suista|tarkasta|
  teurasta|todista|tunnusta|uudista|vahvista|valista|valjasta|
  valmista|varasta|varusta)(kaa|koon|ko))|
#
# V-IMP (V-front, zero):
  (��nest�|�est�|edist�|erist�|est�|h�v�ist�|j�rjest�|jylist�|keih�st�|
  kest�|kirist�|p��st�|pest�|piest�|pist�|pyydyst�|rev�ist�|riist�|
  rynnist�|ry�st�|s��st�|s�est�|sy�st�|t�hyst�|v��rist�|v�ist�|virkist�|
  yhdist�|ylist�)(CLT-SFX?)|
#
# V-IMP (V-front, -k��, -k��n, -k�):
  ((��nest�|�est�|edist�|erist�|est�|h�v�ist�|j�rjest�|jylist�|keih�st�|
  kest�|kirist�|p��st�|pest�|piest�|pist�|pyydyst�|rev�ist�|riist�|
  rynnist�|ry�st�|s��st�|s�est�|sy�st�|t�hyst�|v��rist�|v�ist�|virkist�|
  yhdist�|ylist�)(k��|k��n|k�))(CLT-SFX?)|
#
# INF-I, (V-back, -ta)
#
# INF-I, (V-front, -t�)
  ((h�v�is|jylis|rev�is|sy�s)t�)(CLT-SFX?)|
#
# V: INF-II, INSM (V-back, -en):
  ((aavista|ahdista|anasta|arvosta|asusta|ennusta|haasta|harrasta|
  innosta|julista|kallista|kasta|katsasta|kirkasta|korosta|kosta|
  kukista|loista|lunasta|maista|matkusta|muista|nosta|mullista|
  notkista|omista|opasta|osta|paista|paljasta|muista|nosta|osta|
  paljasta|pelasta|poista|ponnista|puolusta|pudista|purista|
  raasta|rakasta|rangaista|ratkaista|ratsasta|ripusta|suista|tarkasta|
  teurasta|todista|tunnusta|uudista|vahvista|valista|valjasta|
  valmista|varasta|varusta)en)(CLT-SFX?)|
#
# V: INF-II, INSM (V-front, -en):
  ((��nest�|�est�|edist�|erist�|est�|h�v�ist�|j�rjest�|jylist�|keih�st�|
  kest�|kirist�|p��st�|pest�|piest�|pist�|pyydyst�|rev�ist�|riist�|
  rynnist�|ry�st�|s��st�|s�est�|sy�st�|t�hyst�|v��rist�|v�ist�|virkist�|
  yhdist�|ylist�)en)(CLT-SFX?)|
#
# V-ACT, 1SG/1PL-PRES, V-back):
  ((aavista|ahdista|anasta|arvosta|asusta|ennusta|haasta|harrasta|
  innosta|julista|kallista|kasta|katsasta|kirkasta|korosta|kosta|
  kukista|loista|lunasta|maista|matkusta|muista|nosta|mullista|
  notkista|omista|opasta|osta|paista|paljasta|muista|nosta|osta|
  paljasta|pelasta|poista|ponnista|puolusta|pudista|purista|
  raasta|rakasta|rangaista|ratkaista|ratsasta|ripusta|suista|tarkasta|
  teurasta|todista|tunnusta|uudista|vahvista|valista|valjasta|
  valmista|varasta|varusta)(n|mme))(CLT-SFX?)|
#
# V-ACT, 1SG/1PL-PRES, V-front):
  ((��nest�|�est�|edist�|erist�|est�|j�rjest�|keih�st�|kest�|kirist�|
  p��st�|pist�|pyydyst�|riist�|rynnist�|ry�st�|s��st�|s�est�|t�hyst�|
  v��rist�|v�ist�|virkist�|yhdist�|ylist�)(n|mme))(CLT-SFX?)|
#
# V-PASS, PRES (V-back, -taan):
  (((halkais|nous|rangais)ta)an)(CLT-SFX?)|
#
# V-PASS, PRES (V-back, -taan):
  (((h�v�is|p��s|sy�s)t�)�n)(CLT-SFX?)|
#
# Adpositions which are included in the adposition rules:
  (sis�st�|v�list�)(POSS-SFX?CLT-SFX?)|
#  seasta, silmist�, syd�mest�
# Adpositions:
  (huostaan|laista)(CLT-SFX?)|
#
# Adverbs (V-back): 
#  (vasta|vastaan|ainoastaan|nousemistaan|uudestaan)(CLT-SFX?)|
#
# Adverbs (V-front):
#  (ennest��n|j�rjest��n|siirtymist��n|v�henemist��n|v�istymist��n|
#  yksist��n)(CLT-SFX?)|
#
#  (VERBS-SOM (aasi|aasisi|aasinsa|aasien|��ni|��nen|ihon|ihanan|uusi|
#  osata|uskoa)))
#
# ABL (-lta/-lt�)
#
# Agreement in NPs: 
# only one case marking is accepted in the NP:s which contain specifiers 
# and modifiers preceeding the lexical head which is a noun: 
# t�+lt� piene+lt� poja+lta. 
#
# The words inside the parentheses contain the combinations <lta> and <lt�> 
# which are homonymous with the indices of the ablative case 
# (fin.spec, Rule 2.2, ABL-C and adpositions) in Finnish. 
#
# The ambiguous word forms contain the combinations -lta-/-lt� in the stems, 
# or inflected word forms: the partitive forms of nouns and adjectives,
# or verbs containing the derivative suffixes -lta-/-lt�- which participate 
# in the consonant gradation: vihelt��, polttaa, etc. 
# 
# Nouns and adjectives:
# N, SG-NOM:
  (ilta|kulta|multa|((kuningas|tuomio|v�ki)?valta))
  (POSS-SFX?CLT-SFX-B?)|
#
# N, SG-ILL (V-back, -an): 
  (ilta|kulta|multa|((kuningas|tuomio|v�ki)valta)an)
  (POSS-SFX?CLT-SFX-B?)|
#
# N-SG-PTV (V-back; -ta):
  ((((juudan|asdodin|aramin)?kiel)|kyynel|miel|((pihti)?piel)|syl|tiil)t�)
  (POSS-SFX?CLT-SFX-F?)|
#
# N-SG-PTV (V-front; -t�):
  ((((�iti|etel�|etu|l�nsi|loppu|miehen|pohjois|riita|sis�)?puol)|
  huol|kannel|nuol|taival|tul|((it�)?tuul))ta)(POSS-SFX?CLT-SFX-B?)|
#
# illative and genitive forms of adjectives and nouns
  (aasia|aasian|��ni|��neen|uusi|uuteen|��ne)|
# ��nen|
#
# N, SG-GEN (V-back, -n):
  ((vaskialtaa|telta)n)(CLT-SFX-B?)|
#
# Verbs (stem: -ta, -t�):
  ((v�lt�|malta|polta|(valta(si)?))(n|t|mme|tte))(CLT-SFX-B?)|
  ((puhalta|suojelta|vaelta|tulta)(ko|en))|((kielt�)k�)|
  (malta|polta|v�lt�|
  uskoa|uskon|luottaa|luotan|osata|osaan)(CLT-SFX-B?)|
#  
# Verbs (INFII, Instructive (INST): -s-tan):
  (((edus|haas|julis|lois|omis|paljas|puhdis|raas|ratsas|ripus|
  tarkas|tunnus|vahvis)ta)en)|
#
# Verbs (INFII, Instructive (INST): -st�-en):
  (((ry�s|s��s|s�es|v�is|ylis)t�)en)|
#
# Particles:
  (kauttaaltaan|lopulta)(CLT-SFX-B?)|
#
# Adpositions:
# DE-ON-PRP|POP-C:
  (((a|huipu|huipui|kupee|lae|partaa|pohja|reuna)lta)|
  ((juure|kohda|kupee|noka|pohja|reuna|varre|varsi)sta)|
  ((p��|per�)lt�)|((h�nn�|nen�)st�))(POSS-SFX?CLT-SFX-B?)|
#
# DE-ON-PRP|POP-D:
  (((edusta|juure|juuri|kannoi|kohda|lae|pinna|sivu|suu)lta)|
  ((��re|ede|viere)(lt�|st�))|
  ((h�nni|j�lji|kinterei|like|l�he|p��|viere|y)lt�)|
  ((ohe|niska|poske|sivu)sta)|
  ((j�lje|per�|piele|syrj�)st�)|
  (takaa))(POSS-SFX?CLT-SFX?)|
#
# NEG-MOD-INF
#
# Adpositions containing the strings -lta/-lt�, but which do not belong to the groups C and D:
#  (((puo(le)?)|suunna|taho|varre|varsi)lta)(POSS-SFX?CLT-SFX-B?)|
#  ((keske|peri|sis�|v�li|ymp�ri)lt�)(POSS-SFX?CLT-SFX-F?))
#
  (edustalle|lopussa)|
#
# Kommentteja ensin:
#  1) tama on vasta kokeilu, jolla testataan INCLUDE:n toimintaa fin.spec:ssa
#  2) pitkat saannot voidaan jakaa useille riveille...
#  3) isot kirjaimet eivat ole sallittuja
#
# ILL-EXCL-PRP: aanan|aanemin|aaner|aanerin|aanerille|aanim|aanub|
#  aasiaa|ahinoamista|ahinoamin|israelissa)(POSS-SFX?CLT-SFX?)|
# The occurrences of the words which do not belogn to the group
# the disambiguation concerns are deleted manually from that database.
# 
# The list of word forms which are ambiguous in the way that they
# represent several lexical or morphological classes. In the list,
# the number of homonymous partitive vs. illative forms are numerous.
#
  (aasia|��ni|abihun|baani|ben-haanan|daan|ester|geehasi|guuni|
  haanan|herodes|keenan|kristus|leivinuuni|miikael|mooses|noon|nuun|paratiisi|
  pelikaani|publikaani|rabbuuni|rubiini|saaruhen|siin|siion|soon|topaasi|
  ase|hiuskarva|into|is�|j��nn�s|kanaan|kaikkeinpyhin|kastelija|
  kenaan|koira|kruunu|kuu|l�hettil��|lahja|munaskuu|muusi|
  nuoruusik�|((kanta|olka)?p��)|parta|poika|rakkaus|rauta|ruumis|suku|
  suu|vahinko|vaimo|((seko)?viini)|villiaasi|vuotee)
  (POSS-SFX-V?CLT-SFX?)|
#
# 1 N-PRP: SG-GEN (-n):
  ((aahaa|aarahi|aasaa|adar-kuu|afiahi|aihi|ahimaa|akii|andreaa|aretaa|
  artemii|askenaa|aspenaa|ateena|baal-haana|baana|baani|barnabaa|
  barabbaa|barakiaa|berea|bilha|booaa|diina|doodavahu|eliaa|elifaa|
  elihu|elifelehu|elifa|elul-kuu|esaiaa|esteri|faaree|giiho|guuni|heena|
  herodiaa|herodekse|hiskia|jaaroahi|jaanoahi|jaasia|jaahaa|jeehu|jeremiaa|
  jisbahi|jooaa|jooahaa|joohana|jooahi|jooahaa|jogbeha|joona|joonaa|
  joosee|joosia|juudaa|kaareahi|kaifaa|keefaa|kloopaa|kelahi|kloopaa|
  kooa|koorahi|kristukse|kyproo|laakii|leea|lehi|luukkaa|maanoahi|magbii|
  mattatiaa|mattiaa|messiaa|metusalahi|miikaeli|mikmaa|moosekse|naahaa|
  naahaa|neftoahi|nesiahi|nibhaa|niinivee|nooa|noobahi|paaruahi|
  parmenaa|pekahi|paaseahi|puua|rabbuuni|rubiini|saanoahi|saarue|
  sakariaa|samotrakee|sardee|sebahi|selahi|((timnat-)?serahi)|siia|
  siiaha|siiha|siiho|silaa|skeuaa|sooa|soofahi|soostenee|stefanaa|
  suua|suuahi|suutelahi|taamai|taamahi|((een-)?tappuahi)|tahaa|tarsii|
  tebahi|terahi|tiberiaa|tifsahi|tooahi|toohu)n)(CLT-SFX?)|
#
# 2 N-PRP: SG (words which contain several clitics):
  (((milloin)ka)han)|
  (((olen|pelastuu|voi|voivat|korotetaan)ko)han)|
  (((ei|kest��|menestyy|pysyv�t|viel�)k�)h�n)|
#
# 3 N-COM: PL-NOM (V-back, -t):
  ((hullu|kala|kirjanoppinee|taivaa)t)(CLT-SFX?)|
#
# 4 N-COM: PL-NOM (V-front, -t):
  ((enkeli|t�hde|tiet�j�)t)(CLT-SFX?)|
#
# 5 N-COM: NOM & GEN (V-back, -n): 
  ((aartee|ahdistaja|aihee|((murha-)?aikee)|ala|altaa|aluee|armaa|armahtaja|
  armonantaja|((h�vitys|sota-|tuho)?asee)|asukkaa|
  aseenkantaja|askare|askaree|askelee|asuinsija|asumasija|asukkaa|
  auringonpatsaa|auttaja|ehtoo|(elon(leikkuu|korjuu))|
  ep�jumala|esimie|esinaha|esipiha|hallitsija|hampaa|
  ((sala|turmion)?hankkee)|heilutus-rintaliha|hieho|hikiliina|hoitaja|
  hohtee|((ase|kes�|sivu|talvi|varasto|vieras)?huonee)|houkkiokansa|hurskaa|
  ihmise|((pellava(-)?)?ihokkaa)|ikee|ismaelilaismatkuee|j�lkikorjuu|
  johtomie|juhta|julistaja|juomanlaskija|jyv�rouhee|kaikkivaltiaa|
  kahlee|kankaa|kanssapalvelija|kantaja|kantelee|((puu|vaate)?kappalee)|
  kastee|katsee|kauhu|kaulakoristee|kauppiaa|((syntiuhri)*kaurii)|kavaltaja|
  k�skynhaltija|hohtee|kaarnee|kahina|kantelee|kastee|katsee|kauppia|
  kielimurtee|kiitosuhriteuraa|kinsteripensaa|kirjanoppinee|kirjee|kohina|
  kivijumala|kivipatsaa|koittee|((otsa|ristikko)?koristee)|
  ((viinin)?korjuu)|korokkee|(kulta(-aartee|jumala|renkaa))|kuninkaa|
  kuohu|kupee|kurittaja|((kutsu)?vieraa)|kuu|kuukautistila|kuvapatsaa|lahja|
  laiho|((p��si�is|yhteysuhri)?lampaa)|lantee|((ohran)?leikkuu)|
  liepee|liha|lippaa|loistee|lunastaja|lonkka|lonkkaluu|
  (((aasin)?leuka)?luu)|lumpee|
  ((alanko|aru|anti|arte|egyptin|er�|etel�|hasse|kallioer�|laidun|
  manner|pelto|perint�|siidonin-|synnyin|trakonitiin-)?maa)|
  mainee|manner|((ryp�le)?mehu)|
  mietelausee|mirha|murhee|murtaja|muusi|naaraa|naha|nauha|nen�renkaa|
  niska|niskurikansa|nisunleikkuu|ohdakkee|ohjee|ohranleikkuu|oinaa|
  omistaja|osa|((profeetan)?oppilaa)|orjantappurapensaa|osasto|ostaja|pada|
  paisee|pakanakansa|pakokauhu|paluumatka|((maa|pelto)?palsta)|
  palvelija|patsaa|p��mie|p��si�islampaa|pauhina|((teltta)?peittee)|
  pelastaja|pensaa|per�mie|perhee|pikkukarja|pilvenpatsaa|polttaja|
  polttouhrioinaa|polttouhriteuraa|profeettaoppilaa|puhee|
  ((kehoitus|puolustus|v�li)?puhee)|puimatanteree|
  ((keula)?purjee)|((hedelm�|hirsi|�ljy|manteli|mets��ljy|
  ((granaatti)?omena)|palmu|setri|tamariski|viini|((mets�)?viikuna))?puu)|
  puuasee|puuttee|raaa|raakalee|raavaa|raavaskarja|((henkil�|vilja)?raha)|
  rahvaa|((ranne)?renkaa)|rangaistukse|rantamaa|ratsumie|rauha|rauta-asee|
  rautapatsaa|rehuvilja|riettaa|rikkomukse|rintaliha|ruoho|
  ((enkeli|suku)?ruhtinaa)|((herkku|mieli)?ruua)|ruumii|ruostee|
  ((kalan|voitto)?saalii)|sadanp��mie|sairaa|
  ((kev�t|rae|rankka|syys)?satee)|sein�patsaa|seurakuntakokoukse|
  seuruee|sortajakansa|sotamie|suitsukkee|sukulunastaja|
  suu|suurkuninkaa|synnytystuska|syntiuhri|syntiuhriteuraa|syntivelka|
  taakka|tahtaa|taitee|taivaa|tarpee|t�ydenkuu|(teltta(kankaa|maja))|
  takaa-ajaja|telinee|((yhteysuhri)?teuraa)|tila|(todis(taja|tee))|tuha|tuho|
  tulki|tuomitsija|tyyssija|ty�asee|ty�mie|uhma|(uhri(teuraa|lahja))|
  ulkomaa|uudenkuu|uuhe|((lesken|liina|p��llys)?vaattee)|vaihtee|valhee|
  vakaa|valaa|valhee|valhejumala|valitukse|valtiaa|vangitsija|vanhurskaa|
  vantaa|varustee|varjelija|varkaa|(vaski(altaa|raavaa))|v�limie|varustuksee|
  vastustaja|velka|venhee|verivelka|viha|vihki�isoinaa|
  ((jalo)?viini)|viisaa|(vikauhri(-)?oinaa)|vilja|voitee|vuohe|
  vuorenharjantee|((sairas)vuotee)|ylenkatsee|yl�snousemukse|
  aasia|aasi|aasie|��nie|iho|ihana|uuni)
  (n|(POSS-SFX-V)))(CLT-SFX?)|
# 
# 6 N-COM: GEN (V-front, -n): 
  ((edelt�j�|enkeli|elinnestee|esinee|harmaap��|hedelm�|henkil�|
  hedelm�|heltee|ihmee|ikee|imett�j�|((niska|reisi)*j�ntee)|
  juhlap��hinee|((kyy|lohi|vaski)?k��rmee)|k�skij�|k�ytt�j�|keih��|keng�|
  keritsij�|((k�sky)?kirjee)|kirvee|kyynelee|((puurim-k�sky)?kirjee)|kyy|
  kyyn�r�|l�hett�j�|l�hettil��|l�htee|leiv�|liepee|((heilutus)?lyhtee)|
  loppum��r�|maksanlis�kkee|melskee|mielipitee|((arvo|avio|avionrikkoja|
  apu|esi|hallitus|johto|mahti|matka|meri|murha|p��|p��llys|p�iv�|pelto|
  per�|perhekunta-p��|puolus|ratsu|sadanp��|sota|ty�|valio|v�li|
  viidenkymmenenp��|viha|virka)*miehe)|
  n�l�|nestee|((alku|kanta|loppu|pylv��n|tuulis)?p��)|
  ((ilta|syd�n|tuho)?p�iv�)|
  peittee|perhee|perkelee|pylv��|rikkee|((sireeninnahka)?peittee)|
  ((perhekunta-|sadan|viidenkymmenen)?p��miehe)|perij�|((korkeasti-)?pyh�)|
  r�mee|((viini)?ryp�lee)|seppelee|silm�nr�p�ykse|
  sinapinsiemene|sitee|suitsukkee|synnytt�j�|sy�ttil��|syy|syyhy|
  syytt�j�|syyttee|t�hde|tekelee|tekij�|tiet�j�|vaskik��rmee|
  ((p��llys)?vaattee)|velje|((seko)viini)|viine|villitsij�|
  vuorisel�ntee|��ne)(n|(POSS-SFX-V)))(CLT-SFX?)|
#
# 7 N-COM: PL-GEN (V-back, -ten): 
  (((suku)?ruhtinas)ten)(POSS-SFX?CLT-SFX?)|
#
# 8 N-COM: PL-GEN (V-back, -ten): 
  ((leevil�is)ten)(POSS-SFX?CLT-SFX?)|
#
# 9 N-COM: PL-GEN (V-back, -i-n): 
  (((pakana)i)n)(POSS-SFX?CLT-SFX?)|
#
# 10 N-COM: PL-GEN (V-back, -i-en): 
  (((libertiin|matkamieh|publikaan|tamaan|villiaas)i)en)(POSS-SFX?CLT-SFX?)|
#
# 11 N-COM: SG-PTV (V-back, -a): 
  ((((elin)?aika)|alku|anoppi|asia|ep�usko|haavaa|halu|harjoittaja|hiuskarva|
  huoneenhaltija|juhta|kansa|kanssapalveluja|karja|kartano|kastelija|
  keng�npaula|kohottaja|koira|korva|kulta|kunnia|((seura|suku)?kunta)|
  lahja|laki|latva|lauma|leip�kakku|lupausuhri|manna|matka|napina|
  neuvonantaja|nostaja|omaatunto|
  onne|opettaja|palvelija|parta|pilkka|poika|puoli|raha|rata|ruoka|sana|
  seura|sorkka|tahto|teko|tukka|turva|vaarna|((sivu)?vaimo)|vainaja|vaippa|
  vaiva|valta-asema|vanki|vohla|yhteenmeno)a)(POSS-SFX?CLT-SFX?)|
#
# 12 N-COM: SG-PTV (V-front, -�): 
  ((��ri|em�nt�|henke|((kanta)?is�)|is�nt�|j�lke|jylin�|jyv�|kive|
  kyyn�r�|l�hett�j�|leip�|leiri|mini�|n�ky|nime|((tuho)?p�iv�)|p�yt�|
  pyynt�|silm�ter�|synty|syntyper�|tie|((perhe|talon)*v�ke)|velje|
  ymp�rist�|yst�v�)�)(POSS-SFX?CLT-SFX?)|
#
# 13 N-COM: SG-PTV (V-back, -ta): 
  ((ahdistus|�itipuol|aivoitus|aluet|arvoitus|�itipuol|hautaami|haureut|
  hautaus|ihokas|julkeut|((jumalan)?palvelus)|kaivos|kansalais|
  katset|kauneut|kerskaus|kiitos|kiusaamis|
  laupeut|luopumus|maa|morsian|orjatar|pakenemis|pakenemisaiet|
  orjatar|palaamis|palvelijatar|((perint�|perhe)?omaisuut)|
  pesuet|pitalis|pituut|puhdistus|puhet|puhkeamis|((riita)?puol)|rikkomus|
  rikos|rohkeut|rukous|ruumis|saaliis|saamis|salaisuut|seuralais|
  sisar|suu|tuul|un|uskallus|vaellus|vanhurskaut|vanhuut|vastaus|
  ver|viisaut)ta)(POSS-SFX?CLT-SFX?)|
#
# 14 N-COM: SG-PTV (V-front, -t�): 
  ((��n|h�v�istys|h�vi�mis|hy�tymis|ilmestymis|jalanleveyt|j��nn�s|k�t|
  keih�s|kiel|kiert�mis|kypsyyt|leveyt|levi�mis|menestys|miel|mies|p��|
  perhet|siirtymis|tie|ty�|tyt�r|ver|vilpitt�myyt|ylistys|yltymis)t�)
  (POSS-SFX?CLT-SFX?)|
#
# 15 N: N-COM: PL-PTV (V-back, -i-a):
  (((ahdistaj|irstauks|juur|kaltais|kirjoituks|koristuks|
  neuvonantaj|((opetus)?laps)|osuuks|perint�os|puol|rikkomuks|saalistaj|
  sisar|valittajais)i)a)(POSS-SFX?CLT-SFX?)|
#
# 16 N: N-COM: PL-PTV (V-front, -i-�):
  (((��ri|j�lkel�is|k�s|kenk|((viha)?mieh)|mietelm|p�iv|ry�st�j|silm|
  syytt�j|teht�v|tytt�r|velj|virs|yst�v)i)�)(POSS-SFX?CLT-SFX?)|
#
# 17 N: N-COM: PL-PTV (V-back, -j-a):
  (((aiko|alku|armolahjo|asunto|herkkupalo|jalko|kanso|kasvo|kaupunke|
  lahjo|laulu|meno|orpo|palatse|palo|pelastusteko|pelto|
  pentu|pilkko|polku|polttouhre|profeetto|rinto|sano|sielu|sisar|
  ((sivu)?vaimo)|surmattu|taiko|tapo|((tunnus)?teko)|((teuras|yhteys)?uhre)|
  vaivo|vanke|varo|vaunu|verkko|yl�sale)j)a)
  (POSS-SFX?CLT-SFX?)|
#
# 18 N: N-COM: PL-PTV (V-front, -j-�):
  (((k�sky|kynt�j�|synte|synty|v�vy)j)�)(POSS-SFX?CLT-SFX?)|
#
# 19 N: N-COM: PL-PTV (V-back, -i-ta):
  (((asio|ennustelijo|hampa|kanssapalvelijo|kantele|katse|
  lampa|lu|nilkkarenka|palvelijo|puhe|p�yt�viera|ruhtina|
  salamo|sukuluettelo|taloustavaro|tuomare|uusiaku|
  vaatte)i)ta)(POSS-SFX?CLT-SFX?)|
#
# 20 N: N-COM: PL-PTV (V-front, -i-t�):
  (((h�pe|mini�|pyyte|te|t�)i)t�)(POSS-SFX?CLT-SFX?)|
#  
# 21 N-COM: SG-TRL (V-back, -kse-|-ksi(-)): 
  ((aluee|apulaise|aseenkantaja|elinaja|esikoise|ilo|kadotukse|
  kirkkaude|kompastuks|kuninkaa|kunnia|lai|maalitaulu|m��r�tarkoitu|
  omaisuuskansa|onnettomuude|osa|palka|palvelija|parhaa|
  perint�hauda|perint�osa|puolustukse|ruua|saalii|
  ((seurakunnan)?kokou)|silm�nherku|sotapalvelu|surmattava|
  turmio|ty�orja|vahingo|vaimo|vartija|vedenpaisumu)(kse|ksi))
  (POSS-SFX?CLT-SFX?)|
#
# 22 N-COM: SG-TRL (V-front, -kse): 
  ((h�vi�|h�vitt�mise|hetke|j�lkel�ise|nime|p��llik�|p��miehe|perinn�|
  pyh�k�|silm�nrap�y|silm�nr�p�ykse|teht�v�|tytt�re|v�ijyty|v�symy|velje)
  (kse|ksi))(POSS-SFX?CLT-SFX?)|
#
# 23 N-COM: PL-TRL (V-back, i-kse):
  (((alamais|ep�jumal|laps|orjattar|orj|palvelijo|vaimo)i)kse)
  (POSS-SFX?CLT-SFX?)|
#
# 24 N-COM: PL-TRL (V-front, i-kse):
  (((hengenpite|mieh|miel|ratsumieh|vaunumieh)i)kse)(POSS-SFX?CLT-SFX?)|
#
# 25 N-COM: SG-ESS (V-back, -na): 
  ((apu|herkku|hallitusvuote|hinta|hoitajattare|huole|juhla|k�sivarte|
  k�skynhaltija|kerskaukse|koto|kuninkaa|kunnia|kuukaute|
  ((elin|kuukautis|m��r�)?aika)|lunastushinta|nautinto|oma|pilkka|
  oma|poutavuon|puku|raja|ruoka|saalii|suoja|tuomittava|uhrilahja|
  varustama|verho|viikkojuhla|virta|vuote|vuotee)na)
  (POSS-SFX?CLT-SFX?)|
#
# 26 N-COM: SG-ESS (V-front, -n�): 
  ((hyv�|hyvitykse|is�|leip�|((esi|p��llys)?miehe)|((paasto|puhdistus|
  syntym�)?p�iv�)|teht�v�|viini)n�)(POSS-SFX?CLT-SFX?)|
#
# 27 N-COM: PL-ESS (V-back, -i-na): 
  (((nuol|palvelijo|sapatte|soture|ty�tovere|tuomis|valto|vaunusoture|
  viera|viinitarhure)i)na)(POSS-SFX?CLT-SFX?)|
#
# 28 N-COM: PL-ESS (V-front, -i-n�): 
  (((((ilo)?p�iv)|p��llikk�|peltomieh)i)n�)(POSS-SFX?CLT-SFX?)|
#
# 29 N-PRP: SG-INE (V-back -ssa): 
  ((israeli)ssa)(POSS-SFX?CLT-SFX?)|
#
# 30 N-COM: SG-INE (V-back, -ssa): 
  ((ahdistukse|ahneude|armo|asekarkelo|asuinsija|
  hallitsema|hallu|hampai|harhaille|harrastukse|
  haudate|haureude|heimo|hekuma|helma|himo|hirmuisuude|hoido|
  hulluude|huonee|hurmoksi|idu|ihanuude|iho|jala|
  johdattae|johdo|joukkio|jumala|jumalanpalvelukse|jumalattomuude|
  juode|juoksu|juoste|kanna|kansa|k�sivarre|kauhistavaisuude|kaula|
  ((turva)?kaupungi)|kehoittamise|kertomukse|kiivastukse|kiivaude|kirkkaude|
  kodi|kodittomuude|kohdu|kokonaisuude|korkeude|kotikaupungi|koura|
  kuninkuude|kurjuude|la|lai|leiri|liito|kuukautise|kuukautistila|lauma|
  liha|linna|luottamustoime|maa|makuuhuonee|makuukammio|
  mielisuosio|murhee|neuvo|neuvottelu|nouste|nuoruude|
  ohimo|oksarunsaude|omassatunno|olo|omavaltaisuude|opettamise|
  osasto|otsa|pahuude|palatsi|palvelija|palvelukse|perint�maa|
  perint�osa|petollisuude|pove|rakkaude|riita-asia|rikkaude|
  rintahaarniska|rinna|rukoushuonee|ruumii|sana|sankaruude|sielu|
  sija|suru|suu|suuruude|suuttumukse|synagooga|taistelu|talo|
  taudi|telta|((ep�)?toivo)|une|tulemukse|tupe|tuntemise|
  uppiniskaisuude|usko|uskottomuude|vaipa|valitsema|valla|
  valtakunna|vanhurskaude|vanhuude|varjo|virkatoime|
  vuokra-asunno|vuorilinna|vuoristo|viha|viinitarha|viisaude|
  vimma|vuotee|yl�sali)ssa)(POSS-SFX?CLT-SFX?)|
#
# 31 N-COM: SG-INE (V-front, -ss�): 
  ((el�m�|etunen�|h�d�|hempeyde|henge|hyvyyde|ik�v�ide|is�|
  jala|j�lje|j�rjestykse|jouko|k�de|k�rsiv�llisyyde|k�tk�|
  k�yt�kse|kirjee|kutsumukse|k�yhyyde|leiri|loppum��r�|miele|n�y|nime|
  p��|p��t�kse|per�|p�yd�|pyh�k�|pyhyyde|pyydykse|s��liv�isyyde|
  s�ki|sel�|selitykse|sis�|sisimm�|syd�me|syli|synni|taistelle|
  tekemise|temppeli|ty�|v��ryyde|vaellukse|vere|vilpillisyyde|
  ylpeyde|ylv�stely|
  ymm�rrykse)ss�)(POSS-SFX?CLT-SFX?)|
#
# 32 N-COM: PL-INE (V-back, i-ssa):
  (((aarrekammio|aike|askele|aito|ajatuks|alo|esikartanoi|himo|
  huone|ihastuks|ilo|jalkapohj|jalo|jano|kahle|kauhu|kaupunge|
  k�sivars|kiusauks|kiimo|kiuku|korkeuks|korv|kuukautis|
  kuvittelu|linnoituks|lu|meno|mielimurte|murhe|rukouks|
  omissatunno|p��npohj|pelo|perhekunn|petoks|porte|rukouks|
  sieraim|synagoog|synnytyskivu|telto|toim|vaunu|virkapuvu|
  seurakunnankokouks|sukukunn|synagoog|tarpe|teo|un|vaino|vastustaj|
  vihastuks|viho)i)ssa)(POSS-SFX?CLT-SFX?)|
#
# 33 N-COM: PL-INE (V-front, i-ss�):
  (((enkele|h�d|h�mm�styks|h�pe|itkuvirs|j�sen|juhl|k�mmen|k�s|
  kirje|kyl|n�l|pelj�styks|pyh|s��r|siiv|syd�m|silm|synne|teht�v|
  te|ver)i)ss�)(POSS-SFX?CLT-SFX?)|

# 34 N-COM: SG-ADE (V-back, -lla): 
  ((aasintamma|aja|ala|aluee|asioimise|ennustamise|haureude|houkuttelu|
  itku|kavaluude|k�sivarre|kerra|kiima|kirjoitukse|kirkkaude|koura|kupee|
  kustannukse|loistee|matka|murehtimise|niskoittelu|ola|otsa|paika|
  perint�osa|piha|polvi|((etu)?sorme)|sotajouko|suu|tarpee|
  tavara|vaipa|viisaude|voima|vuore|vuoro|
  ehtoo|halu|istuime|johdo|jouko|kerskumise|levo|maakansa|m��r�aja|mieka|
  mielisuosio|omaisuude|pahuude|poja|polu|puolip�iv�levo|raha|renkai|sana|
  sauva|sija|suvu|taido|valo|valtakunna|vaellukse|valtaistuime|valtika|
  varjo|vatsa|valtika|vanhurskaude|vuotee)lla)(POSS-SFX?CLT-SFX?)|
#
# 35 N-COM: SG-ADE (V-front, -ll�): 
  ((henge|hyvyyde|i�|k�de|keih��|kiele|l�himm�ise|liepee|miele|myrsky|nime|
  puimajyr�|p�yhkeilemise|sineti|syd�me|t�ydellisyyde|v�e|v�litykse|viskime|
  hedelm�|is�|keih��|leiki|p�yd�|((selko)?sel�)|synni|tie|ty�|
  vaivann��|vy�|y�|vere)ll�)(POSS-SFX?CLT-SFX?)|
#
# 36 N-COM: PL-ADE (V-back, -i-lla): 
  (((aarte|alttare|hevos|hiuks|houkutuks|houkuttelu|huul|jalo|
  ((kivi)?jumal)|jumalankuv|juon|kamele|kasvo|katse|korv|lahjo|mieko|
  mielisuosio|noituuks|paiko|((pelto|perint�)?ma)|polv|puhe|renka|
  rikkomuks|rinno|sarano|soittim|teo|tulo|un|valtaistuim|vaunu|
  asuinpaiko|huhu|kahle|kauhistuks|koru|kukkulo|laitum|matko|nuol|oks|
  poj|posk|rauta-ase|sano|rinno|sauvo|sija|sormi|sotajouko|sul|taio|
  tulv|uhrikukkulo|vaatte|valhe|varo|varuvelhouks|vuote)i)lla)
  (POSS-SFX?CLT-SFX?)|
#
# 37 N-COM: PL-ADE (V-front, -i-ll�):
  (((ammattivelj|iljetyks|j�lkel�is|kaulak��dy|k�s|keih�|kyynel|
  olkap�|p�iv|retk|silm|te|t�|tytt�r|siiv|synne|velj|viimeis|vy�t�is)
  i)ll�)(POSS-SFX?CLT-SFX?)|
#
# 38 N-COM: SG-ELA (V-back, -sta): 
  ((alhaisuude|alttiude|armo|asuinsija|asumukse|asunno|haava|
  halu|hartia|haureude|heikkoude|herra|hinna|huokaamise|hurskaude|
  inno|jala|jouko|jumala|jumalattomuude|((aarre)?kammio)|kansa|karja|
  kasvami|kaupungi|
  keskuude|kida|kiivaude|kirja|kirkkaude|kohdu|kohtalo|kompastukse|
  korkeude|kulma|kuolema|kuritukse|kuvaaja|((uhri)?lahja)|laitume|
  (lammasten(-)?kaitsenna)|lauma|liha|lihavuude|((perint�)?maa)|maja|matka|
  mielipaha|mustelma|nuhtelu|nuoruude|ohjaukse|oma|omaisuude|
  onne|onnettomuude|opetu|opi|ove|pahuude|palvelukse|paranemise|
  pensaiko|perint�osa|poja|polvikunna|puhee|
  puhtaaksi-tulemise|puuttee|puvu|raatelija|rakkaude|rikkaude|
  rikkomukse|rikokse|rukoukse|ruumii|saalii|saastaisuude|sado|sana|seura|
  sielu|sukukunna|suosio|suu|suvu|synnyinmaa|tahdo|taido|talo|
  tila|toime|tulo|tuomari|tupe|uhma|uhri|une|usko|uskollisuude|
  uskottomuude|vaikerrukse|vaimo|vanhurskaude|vaellukse|vaiva|
  valittelu|valitukse|vallanalaisuude|valtakunna|vankeude|
  vapahtaja|vatsa|veriheimolaise|viha|vihollise|((viikuna|viini)?puu)|
  viinitarha|vilja|vira|vitsaukse|voima|vuodo|yhteysuhri)sta)
  (POSS-SFX?CLT-SFX?)|
#
# 39 N-COM: SG-ELA (V-front, -st�):   
  ((h�lin�|elime|hedelm�|henge|henk�ykse|ik�v�imise|is�|
  itsemiele|j�lkel�ise|k�rsiv�llisyyde|k�de|k�yhyyde|kylv�|leiv�|miehe|
  miele|nime|p��|pes�|p�yd�|pyhyyde|pyh�k�|sel�|sisimm�|syd�me|
  syli|synni|syntym�|syntymise|t�yteyde|tekij�|temppeli|ty�|
  tytt�re|((palvelus)?v�e)|vere|villiintymise|yhteyde|ylh�isyyde|ylpeyde|
  ymm�rrykse)st�)(POSS-SFX?CLT-SFX?)|
#
# 40 N-COM: PL-ELA (V-back, -i-sta): 
  (((aarte|ahdingo|ahdistuks|ajoks|armo|askele|asuinpaiko|esivanhemm|
  hankke|haudo|heimolais|herjauks|himo|jalo|jyv�rouhe|
  kahle|kaupunge|kauhistuks|k�sivars|((kivi)?jumal)|
  kylkilu|lampa|((opetus)?laps)|lu|murh|naapure|nuorukais|oikeuks|olo|omais|
  onnettomuuks|p��npohj|((kanssa)?palvelijo)|perhekuntalais|pilkkaaj|
  poikas|poj|porte|puhe|raunio|renka|rikoks|ruhtina|ruhtinattar|runoilijo|
  saastaisuuks|sano|sapate|sarv|sieraim|sod|sotajouko|sukulais|
  synnytystusk|talo|tavaro|te|telto|teo|todistuks|tulo|tuntem|
  uhre|uhrilahjo|un|uskonasio|vaatte|vaihe|vainooj|varkauks|
  vaunu|velhouks|vesioj|vihollis|viinitarho|yhteysuhre|
  yhteysuhriteura)i)sta)(POSS-SFX?CLT-SFX?)|
#
# 41 N-COM: PL-ELA (V-front, -i-st�):
  (((hedelm|hiir|j�lkel�is|k�s|k�sky|l�himm�|leire|leiv|mieh|n�y|p�|
  pelj�tyks|riitelemis|s�ke|silm|synne|te|tytt�r|urot�|vaivann��|
  velj|((viha)?mieh)|yst�v)i)st�)(POSS-SFX?CLT-SFX?)|
# 
# 42 N-COM: SG-ABL (V-back, -lta): 
  ((ahmailu|alttari|arvo|aluee|ammati|avunhuudo|haltija|herral|
  ((valta)?istuime)|kansa|lapsi|luvu|muodo|naapuri|olenna|orja|
  orjattare|osa|paika|pohja|puole|rakentee|ruumii|sielu|suvu|teo|
  toise|tuomari|tuttava|varre|vartalo|voima)lta)
  (POSS-SFX?CLT-SFX?)|
# 
# 43 N-COM: SG-ABL (V-front, -lt�): 
  ((�idi|i�|is�|kiele|l�himm�ise|miehe|miele|n��|nime|p��|
  sotap��llik�|syd�me|tie|v�kevyyde|velje|ymm�rrykse)lt�)
  (POSS-SFX?CLT-SFX?)|
#
# 44 N-COM: PL-ABL (V-back, -i-lta):
  (((alue|apostole|huul|kansalais|kasvo|kotipaiko|opetuslaps|
  palvelijo|paiko|rado|sapate|tuttav|valtaistuim|vihollis|voittaj|vuos)i)lta)
  (POSS-SFX?CLT-SFX?)|
#
# 45 N-COM: PL-ABL (front, -i-lt�):
  (((elinp�iv|is|j�rj|j�sen|kotiv�e|mieh|riist�j|silm|te|velj)i)lt�)
  (POSS-SFX?CLT-SFX?)|
#
# 46 N-COM: SG-ALL (V-back, -lle): 
  ((ala|alttari|ape|aseenkantaja|asettaja|asunno|edusta|esikoise|
  ((ep�)?jumala)|hauda|heimolaise|herjaaja|herra|hiuskarva|hovi|
  huoneenhaltija|huuli|iho|istuime|johtaji|jouko|kallio|kansa|
  karja|kukkuloi|kupee|kuukaude|
  laitume|leposija|maa|maatila|maja|matka|muinaise|niska|oksennukse|
  ola|omistaja|opettaja|opetuslapse|((perint�)?osa)|p��lae|paika|
  palvelija|pello|poja|pove|puole|puoliso|rakkaa|rinna|ruumii|seurakunna|
  sielu|sisare|sulhaspoja|suu|suvu|taido|teurasuhri|todistaja|toveri|
  ((sivu)?vaimo)|valtaistuime|uude|viinitarha|voidellu|vuode|vuotee|
  vuore)lle)(POSS-SFX?CLT-SFX?)|
#
# 47 N-COM: SG-ALL (V-front, -lle): 
  ((�idi|h�d�|is�|is�nn�|k�de|k�mmene|kiele|l�hett�j�|l�himm�ise|miehe|
  nime|p�iv�|pyydykse|siemene|silm�|syd�me|sy�nn�kse|tekij�|temppeli|
  tie|ty�|velje|vy�)lle)(POSS-SFX?CLT-SFX?)|
#
# 48 N-COM: PL-ALL (V-back, -i-lle): 
  (((aase|aarte|apostole|askele|halveksijo|hartio|heimolais|herro|jalo|
  kansalais|kasvo|((kivi)?jumal)|kamele|kaupo|kupe|lampa|lante|
  ((opetus)?laps)|ma|majo|naapure|oksennuks|om|opettaj|palvelijo|
  paiko|perhekunn|piio|poikas|poj|polu|polv|portonpalko|profeeto|
  ruhtina|sano|seuralais|sielu|silm�luom|sotajouko|sukukunn|suvu|
  tiluks|((virka)?tovere)|tuttav|ty�kumppane|vaatte|vaimo|vainooj|
  valitu|vanhemm|vankeustovere|vastustaj|vihollis|vuor)i)lle)
  (POSS-SFX?CLT-SFX?)|
#
# 49 N-COM: PL-ALL (V-front, -i-lle): 
  (((enkele|hallitusmieh|is�nn|is|j�lkel�is|kyynele|l�himm�is|silm|tytt�r|
  te|velj|((viha)?mieh)|vihkiytyne|ylimyks|yst�v)i)lle)
  (POSS-SFX?CLT-SFX?)|
#
# 50 N-COM: SG-ABES (V-back, -tta):
  (((huomaa|tunte)ma)tta)(POSS-SFX?CLT-SFX?)|
#
# 51 N-COM: SG-ABES (V-front, -tt�):
  (((tiet�)m�)tt�)(POSS-SFX?CLT-SFX?)|
#
# 52N-COM: PL-COMT (V-back, -i-ne-PX):
  (((ajaj|alue|((�ljy)?ast)|asukka|hakas|halu|harppu|heimokunt|hevos|
  himo|hoviherro|ihokka|jalko|((vaski)?jalusto)|((sota)?joukko)|jous|
  jumal|juomauhre|juur|kalo|kalu|kalusto|((pikku|raavas)?karjo)|
  kaupunke|kantele|karstakuppe|kilp|korento|korko|koukku|kukkaleht|
  ((uhri)?kukkulo)|kuninka|kymbaal|laidunma|lamppu|lamppusaks|
  ((opetus|pikku)?laps)|laumo|lauto|lampa|lamppu|linnoituks|lu|
  luol|ma|miekko|omaisuuks|�ljyastio|palkkalais|palvelijattar|palvelijo|
  pikkulaps|poik|poikkitanko|raavaskarjo|rajo|rapo|rasvo|ruumi|salpo|
  seuralais|sot|talo|takke|tavaro|teltto|torv|tuhk|tuomare|
  vaarno|vaatte|vaimo|vaippo|vanhimp|vars|varso|vaskiristikko|
  ((sota)?vaunu)|vuote)i)ne)(POSS-SFX?CLT-SFX?)|
#
# 53 N-COM: PL-COMT (V-front, -i-ne-PX):
  (((�it|h�rk|helte|imett�j|p�|keih�|k�ys|kyl|kymbaale|kyp�re|
  ((meri|p��llys|ratsu)?mieh)|mini�|p��hine|p��llikk�|perhe|pylv�|peitte|
  p�|palvelusteht�v|peitte|perhe|pylv�|ristikkokehyks|
  s��d�ks|sato|sis�lmyks|teli|tytt�r|((sota)?v�k)|velj|yst�v�tt�r)i)ne)
  (POSS-SFX?CLT-SFX?)|
#
# 54 A: SG-NOM (V-back, positive):
  (nopea|viisaa|uusi)(POSS-SFX-V?CLT-SFX?)|
#
# 55 A: SG-NOM (V-front, positive):
  (pimeys|tyyni|tyyne|ylv��)(POSS-SFX?CLT-SFX?)|
#
# 56 A: SG-NOM (V-back, superlative; -in):
  ((mahtav)in)(CLT-SFX?)|
#
# 57 A: SG-NOM (V-front, superlative):
  ((l�h|pien|v�h)in)(CLT-SFX?)|
#
# 58 A: PL-NOM (V-back, superlative; -imma-t):
  (((mahtav)imma)t)(CLT-SFX?)|
#
# 59 A: SG-GEN (V-back, -n: positive):
  ((anteliaa|armaa|autuaa|hartaa|((van)?hurskaa)|kallii|kiivaa|laiha|kookkaa|
  hopearaha|karvaa|kaunii|paha|paljaa|parhaa|pelokkaa|raaa|puhtaa|
  raikkaa|rakkaa|raskaa|rikkaa|runsaa|tuoree|vakaa|vapaa|varma|viisaa|
  voimakkaa)(n|POSS-SFX-V?))(CLT-SFX?)|
#
# 60 A: SG-GEN (V-front, -n: positive):
  ((k�rkk��|ep�pyh�|korkeastipyh�|k�yh�|siivekk��|tyyne|ylv��)
  (n|POSS-SFX-V?))(CLT-SFX?)|
#
# 61 A: SG-GEN (V-front, -n: positive):
  (((k�yh)i)en)(POSS-SFX?CLT-SFX?)|
#
# 62 A: PL-PTV (V-back, -i-a):
  (((kaltais)i)a)(POSS-SFX?CLT-SFX?)|
#
# 63 A: SG-PTV (V-back, superlative; -immais-ta):
  ((paras)ta)(POSS-SFX?CLT-SFX?)|
#
# 64 A: SG-PTV (V-front, superlative; -imm�is-t�):
  (((p��ll)imm�is)t�)(POSS-SFX?CLT-SFX?)|
#
# 65 A: SG, ESS (V-back,-na):
  ((vanha)na)(POSS-SFX?CLT-SFX?)|
#
# 66 A: SG, ESS (V-front,-n�):
  ((pitk�)n�)(POSS-SFX?CLT-SFX?)|
#
# 67 A: SG, TRL (V-front & V-back, -ksi-/-kse-):
  ((hyv�|paha)kse)(POSS-SFX?CLT-SFX?)|
#
# 68 A: SG, ADE (V-back,-lla):
  ((ikivanha|liia)lla)(POSS-SFX?CLT-SFX?)|
#
# 69 A & PCPL-PRES: PL-ADE (V-back, superlative; -immi-i-lla):
  ((((kov|make|palav|polttav)imm)i)lla)(POSS-SFX?CLT-SFX?)|
#
# 70 A: PL-ADE (V-front, superlative; -imm-i-ll�):
  ((((kiihke|kipe|v�kev)imm)i)ll�)(POSS-SFX?CLT-SFX?)|
#
# 71 A: SG, ELA (V-back, positive; -sta):
  ((ikivanha|liia)sta)(POSS-SFX?CLT-SFX?)|
#
# 72 A: SG, ELA (V-front, positive; -st�):
  ((tyhm�)st�)(POSS-SFX?CLT-SFX?)|
#
# 73 A: SG, ELA (V-front, comparative; -st�):
  (((v�kev�)mm�)st�)(POSS-SFX?CLT-SFX?)|
#
# 74 A: SG, ABL (V-back, comparative; -lta):
  (((pare)mma)lta)(POSS-SFX?CLT-SFX?)|
#
# 75 PRON:
#  (ainoa|ainoan|ainoata|
#  er��n|
#  itse|itse��n|itselt�|itsess�|itsest�|itsell�|itselle|itsekseen|
#  jostakin|
#  kaikki|kaikkineen|
#  kuka|ken|ket�|keit�|kell�|kelt�|kelle|kehen|ketk��n|
#  kenell�|kenelt�|kenelle|keness�|kenest�|
#  kokonaan|
#  kumpi|koska|kuinka|
#  mik�|mit�|mink�|milt�|mitenk�|mitk�|miksi|min�|mille|
#  monta|
#  min�|minun|sinua|h�n|me|meit�|meille|meid�n|
#  te|teit�|teille|teid�n|he|heill�|heille|heit�|
#  mit��n|miss��n|mist��n|mill��n|milloin|milloinkaan|
#  muuan|muun|muiden|muusta|muuta|muutoin|
#  ne|n�it�|niit�|noita|niiden|niin�|n�in|
#  omaa|omalla|omissa|omista|
#  se|sen|sin�|sit�|siksi|siit�|siell�|silloin|sitten|sent�hden|
#  t�m�|t�m�n|t�n�|t�st�|t�t�|t�h�n|t��ll�|
#  toista|toisessa|toisella|toisesta|toiselta|toiselle|
#  toisia|toisissa|toisilla|toisista|toisilta|toisille|
#  yhden|yhdell�|yhdelt�|yhdelle|yhdess�|yhdest�|yht�|yksi)
#  (POSS-SFX?CLT-SFX?)|
#
# 76 NUM, NOM:
  ((nelj�kymment�|kolmekymment�|kaksikymment�|seitsem�nkymment�|
  kahdeksankymment�|tuhat)?(viisi|kuusi))(CLT-SFX?)|
#
# 77 NUM, PTV:
  ((yh)t�)(CLT-SFX?)|
#
# 78 NUM, PL-GEN:
  ((((kymmen)*tuhans)i)en)|
#
# 79 NUM, PL-COM, i+ne+PX:
  (((tuhans)i)ne)(POSS-SFX-V?CLT-SFX?)|
#
# 80 V: INF-I, NOM (V-back, -a, -ta, -da, -la, -na, -n-, -ra):  
  ((ol)la)(CLT-SFX?)|
#
# 81 V: INF-I, NOM (V-front, -�, -t�, -d�, -l�, -n�, -n-, -r�):  
  (n�hd�|p��st�|sy�d�)(POSS-SFX-V?CLT-SFX?)|
#
# 82 V: INF-I, TRL (V-back, -kse):
  ((ajaa|anastaa|antaa|asettaa|asua|auttaa|hajottaa|hakea|hankkia|
  herjata|herjattava|joutua|juottaa|kaapia|kaataa|karata|
  katsoa|kavaltaa|kirjoittaa|koetella|koota|korjata|kukistaa|kuolla|
  kuulla|laajentaa|laittaa|laskea|lunastaa|luoda|maata|
  mitata|muistaa|murskata|murtautua|nostaa|noudattaa|ojentua|olla|
  opettaa|orjuuttaa|osoittaa|ottaa|palata|palauttaa|paljastaa|
  palkata|palvella|panna|parantua|pelastaa|pelastua|peloitella|
  pilkata|poimittavi|poistaa|polttaa|puhdistaa|puhua|puhutella|
  rakastaa|rakentaa|rakentua|ristiinnaulita|rukoilla|saada|saattaa|
  seuloa|seurata|siunata|sotia|sovittaa|sovittamise|suoda|suoja|
  surmata|suudella|taistella|tappaa|tarpee|teurastaa|toimittaa|
  tuhota|tulla|tuntea|tuoda|tuomita|tuottaa|turvautua|uhrata|valaista|
  valhetella|valmistaa|vapahtaa|varjella|voida)kse)
  (POSS-SFX?CLT-SFX?)|
#
# 83 V: INF-I, TRL (V-front, -kse):  
  ((eksytt��|est��|etsi�|h�v�ist�|h�vitt��|hy�k�t�|ilmesty�|itke�|
  k��nt��|k�rsi�|k�yd�|keksi�|kevent��|l�hesty�|l�hett��|l�hte�|
  l�mmitell�|menn�|n�hd�|n�ytt��|niell�|p��st�|peitt��|pit��|
  pyhitt��|pystytt��|pyydyst��|pyyt��|s��st��|s�ilytt��|siirt��|
  sy�st�|sy�tt��|t�ytt��|tehd�|ty�nt��|tyydytt��|v�ltt��|vet��|
  vied�|viihdytell�|ymm�rt��|y�py�)kse)(POSS-SFX?CLT-SFX?)|
#
# 84 V: INF-II, INE (V-back, -e-ssa):
  (((aiko|ajae|alenta|alotta|aja|ano|anta|asetta|astu|asu|hallit|hukku|
  huomat|istu|joutu|julista|kanta|katsell|katsahta|kehu|kemuill|
  keskustell|kiivaill|kirjoitta|kiroill|kolkutta|kulki|kuoll|kuull|
  kuunnell|((l�sn�)?oll)|luki|mata|matkusta|muista|odotta|opetta|otta|paastot|
  paet|paimenta|painiskell|palat|palvell|pelasta|puhalta|puhdista|
  puhu|puhutell|puolusta|puolustautu|purjehti|rakenta|ratsasta|
  riemuit|rukoill|ruvet|saatta|salli|sano|seiso|sisusta|siunat|
  souta|suistu|surmat|taistell|tarkasta|tarkat|tavat|todista|toimi|
  toimitta|tuhot|tull|tunti|tuomit|tutkistell|tuod|uhrat|vaelta|
  vahvista|valitta|vitkastell)e)ssa)(POSS-SFX?CLT-SFX?)|
#
# 85 V: INF-II, INE (V-front, -e-ss�):
  (((el�|etsi|h�vitt�|her�t|ilmesty|k��ntelehti|k��nty|k�rsi|k�ski|k�vell|
  k�yd|k�ytt�|kierrell|kiert�|koot|kylv�|l�hesty|l�hett�|l�hti|
  l�sn�oll|menn|menetell|n�hd|odotta|p��st�|pelj�t|piiritt�|pit�|pyrki|
  pyyt�|rient�|riidell|saapu|siunat|synnytt�|sy�d|t�ytt�|tehd|tull|
  uhrat|usko|vaelta|vied|yritt�)e)ss�)(POSS-SFX?CLT-SFX?)|
#
# 86 V: INF-III, SG-PTV (V-back, -ma-a):  
  (((huo|juo|karkoitta|kuule|perusta|raatele|saa|sekoitta|
  tahto)ma)a)(POSS-SFX?CLT-SFX?)|
#
# 87 V: INF-III, SG-PTV (V-front, -m�-�):  
  (((sy�|teke|tiet�)m�)�)(POSS-SFX?CLT-SFX?)|
#
# 88 V: INF-III, PL-PTV (V-back, -ma-i-a):  
  ((((kaata)m)i)a)(POSS-SFX?CLT-SFX?)|
#
#! 89 V: INF-III, PL-PTV (V-front, -m�-i-�):  
#
# 90 V: INF-III, SG-ADE (V-back, -ma-lla): 
  (((hake|karkoitta|kuule|lupaa|raatele|saa|sekoitta)ma)lla)
  (POSS-SFX?CLT-SFX?)|
#
# 91 V: INF-III, PL-ABL (V-back, -m-i-lta): 
  ((((kukista)m)i)lta)(POSS-SFX-V?CLT-SFX?)|

# 92 V: INF-III, PL-GEN (V-front, -m�-n):  
  (((sy�)m�)(n|(POSS-SFX?)))(CLT-SFX?)|
#
# 93 V: INF-III, SG-ELA (V-front, -m�-st�):
  (((k�ytt�|teke)m�)st�)(POSS-SFX?CLT-SFX?)|
#
# 94 V: INF-III, ABE (V-back, -ma-tta):
  (((huomaa|tahto)ma)tta)(POSS-SFX?CLT-SFX?)|
#
# 95 V: INF-III, ABE (V-front, -m�-tt�):
  (((tiet�)m�)tt�)(POSS-SFX?CLT-SFX?)|
#
# 96 V: INF-III, INES (V-front, -ma-ssa):
  (((ole)ma)ssa)(CLT-SFX?)|
# 
# 97 V: INF-IV, SG-PTV (V-back, -minen: -mista-ta): 
  (((halveksu|heikontu|kaatu|kiehu|kirkastu|kovene|kukistu|
  nouse|omista|poisotta|puhkeamis|tule|vahvistu)mis)ta)
  (POSS-SFX?CLT-SFX?)|
#
# 98 V: INF-IV, SG-PTV (V-front, -minen: -mista-t�): 
  (((h�vi�|hy�ty|ilmesty|iske|kiert�|levi�|levi�|siirty|teke|
  v�hene|v�isty|vihkiyty)mis)t�)
  (POSS-SFX?CLT-SFX?)|
#
# 99 V, INF-V. ADE (V-back, -maisilla):
  (((alka|kuole|laske|pakahtu|sano|tule|uppoa)maisi)lla)
  (POSS-SFX?CLT-SFX?)|
#
# 100 V, INF-V. ADE (V-front, -m�isill�):
  (((k�ske|l�hte|s�rky|synnytt�)m�isi)ll�)
  (POSS-SFX?CLT-SFX?)|
#
# 101 V-PCPL-I, PRES: SG-TRL (V-back, -ksi-/-kse-):
  (((kastetta|maksetta)va)kse)
  (POSS-SFX?CLT-SFX?)|
#
# 102 V-PCPL-I, PRES: SG-PTV (V-back, -a):
  (((hoidetta|kannetta)va)a)
  (POSS-SFX?CLT-SFX?)|
#
# 103 V-PCPL-I, PRES: SG-ESS (V-back,-va-na):
  (((hoidetta)va)na)
  (POSS-SFX?CLT-SFX?)|
#
# 104 V-PCPL-I, PRES: PL-ADE, Superlative, (V-back,-v-i-mmi-lle):
  (((((pala)v)i)mmi)lle)
  (POSS-SFX?CLT-SFX?)|
#
# 105 V-PCPL-I, PRES: PL-ESS (V-back,-v-i-na):
  ((((aiko|hoidetta|joutu|ole|seiso)v)i)na)
  (POSS-SFX?CLT-SFX?)|
#
# 106 V-PCPL-I, PRES: PL-ESS (V-front,-v-i-n�):
  ((((tiet�)v)i)n�)
  (POSS-SFX?CLT-SFX?)|
#
# 107 V-PCL-I, PRES: PL-INE (V-back, -v-i-ssa):
  ((((annetta)v)i)ssa)
  (POSS-SFX?CLT-SFX?)|
#  
# 108 V-PCL-I, PRES: PL-INE (V-front, -v-i-st�):
  ((((n�ky)v)i)st�)
  (POSS-SFX?CLT-SFX?)|
#
# 109 V-ACT, PCPL-II, PAST-SG-NOM (V-back, -(l|n|r|s)ut, -(l|n|r|s)ee-):
  ((ajatel|kuol|ol|tul)lut)(POSS-SFX?CLT-SFX?)|
  ((ano|joutu|katso|puhdistu|saa)nut)(POSS-SFX?CLT-SFX?)|
  (((kohdel|kuol|kuul|ol|tul)lee)(n|(POSS-SFX)))(CLT-SFX?)|
  (((aja|ansain|joutu|karan|lakan|liittoutu|masentu|matkusta|sano|
  paen|pudon|puhdistu|puhjen|saa|saavutta|sairasta|sano|vastan|voitta)nee)
  (n|(POSS-SFX)))(CLT-SFX?)|
#  
# 110 V-ACT, PCPL-II, PAST-SG-NOM (V-front, -(l|n|r|s)ut, -(l|n|r|s)ee-):
  (((eksy|((j�ljelle)?j��)|k�y|kokoontu|l�hett�|l�hte|levin|
  liitty|men|n�h|pit�|pysy|siirty|teh)nee)(n|(POSS-SFX)))(CLT-SFX?)|
  (((jylis|p��s)see)(n|(POSS-SFX)))(CLT-SFX?)|
#
# 111 V-ACT, PCPL-II, PAST-PL-NOM (V-back, -(l|n|r|s)ut, -(l|n|r|s)ee-):
  (((joutu|julista)nee)t)(POSS-SFX?CLT-SFX?)|
#  
# 112 V-ACT, PCPL-II, PAST-SG-NOM (V-front, -(l|n|r|s)yt, -(l|n|r|s)ee-):
  ((hylj�n|men)nyt)(CLT-SFX?)|
#  
# 113 V-ACT, PCPL-II, PAST-PL-NOM (V-front, -(l|n|r|s)yt, -(l|n|r|s)ee-):
  (((synty)nee)t)(CLT-SFX?)|
# 
# 114 V-PASS, PCPL-II, PAST-SG-PTV (V-back, -ttu-, -a):
  (((anne|ava|ero|halo|halu|huoma|juliste|kaive|kukiste|kulje|kuljete|
  kutsu|laka|laske|lue|luoda|maiste|odote|ote|pae|pala|pue|puete|
  puhdiste|puhu|rakenne|ruoski|saate|saavu|sano|siuna|suostute|surma|tape|
  tarkaste|teuraste|toimite|tunne|uhra|vede|veisa|voite)ttu)a)
  (POSS-SFX?CLT-SFX?)|
#
# 115 V-PASS, PCPL-II, PAST-SG-PTV (V-front, -tty-, -�):
  (((her�|k��ri|k�ske|l�hde|levite|l�yde|mieti|p��te|t�yte|vede|viivy)tty)�)
  (POSS-SFX?CLT-SFX?)|
#
# 116 V-PASS, PCPL-II, PAST-SG-PTV (V-back, -tu-, -a):
  (((katsel|kuol|kuul|neuvotel|nous|pan|rohkais|saa|tul)tu)a)
  (POSS-SFX?CLT-SFX?)|
#
# 117 V-ACT, PCPL-II, PAST-SG-GEN (V-back, -nee-n):
  (((juopu|kaatu|kuivettu|muuttu|tapahtu|parantu|pelastu|
  puhu|sortu)nee)n)(POSS-SFX?CLT-SFX?)|
#
# 118 V-ACT, PCPL-II, PAST-SG-GEN (V-front, -nee-n):
  (((ilmesty|k�rsi|mielisty|synty|v�sy|t�ytty)nee)n)
  (POSS-SFX?CLT-SFX?)|
#
# 119 V-PASS, PCPL-II, PAST-SG-PTV (V-front, -ty-, -�):
  (((k�y|n�h|men|p��s|pes|syn|teh)ty)�)(POSS-SFX?CLT-SFX?)|
#
# 120 V-ACT, IND, ACT-PRES (V-back):
  ((ano|aseta|avaa|hakkaa|hukkaa|huokaa|istu|jaa|joutu|karkaa|katso|
  kerskaa|kehu|kihlaa|korjaa|kuule|lakkaa|leikkaa|luule|lupaa|makaa|muista|
  murskaa|ohjaa|ole|ota|ova|palaa|pelastu|pilkkaa|puhu|rakasta|riemuitse|
  saa|saarnaa|salaa|sano|seiso|seuraa|siunaa|surmaa|tallaa|tapaa|tee|
  tehoa|tempaa|todista|tule|turvaa|uhkaa|uhraa|vainoa|veisaa|
# vastaa|
  vertaa|vihaa|vihi|viskaa)
  (n|t|mme|tte|vat))(CLT-SFX?)|
#
# 121 V-ACT, IND, ACT-PRES (V-back), 3SG:
  (anoo|asettaa|avaa|hakee|hakkaa|hautaa|hukkaa|huokaa|istuu|joutuu|
  karkaa|katsoo|kerskaa|kihlaa|kirjoittaa|korjaa|kuulee|lakkaa|leikkaa|luulee|
  makaa|muistaa|murskaa|muuraa|on|onpa|ohjaa|ottaa|palaa|pelastuu|pilkkaa|
  puhuu|rakastaa|riemuitsee|saa|saarnaa|salaa|sanoo|seisoo|seuraa|
  siunaa|surmaa|tallaa|tapaa|tehoaa|tempaa|todistaa|tulee|turvaa|
  uhkaa|uhraa|vainoaa|vastaa|veisaa|vertaa|vihaa|viskaa)
  (CLT-SFX?)|
#
# 122 V-ACT, IND, ACT-PRES (V-front), 3SG:
  (j��|hy�kk��|kest��|lep��|n�kee|menestyy|pelk��|riitt��|rynt��|
  tiet��|ymm�rt��)(CLT-SFX?)|
#
# 123 V, IND, ACT-PRES (V-front):
  ((her��|hylk��|hy�kk��|j��|kest�|lep��|menesty|myy|n�e|pelk��|
  pysy|pyyhi|riit��|rynt��|sy�|tied�|tiet�|vihi|ymm�rr�|ymm�rt�)
  (n|t|mme|tte|v�t))(CLT-SFX?)|
#
# 124 V-ACT, IND, ACT-PAST (V-back), 3SG:
  (piti)(CLT-SFX?)|
#
# 125 V, IND, ACT-PAST (V-back, -i-): 
  (((huus|kaas|kasto|kohos|kuohus|ol|ott|puuhas|rouhens|sano|(so(d|t))|
  te|tuhos|tul|vaan|vihas)i)
  (n|t|mme|tte|vat)?)(CLT-SFX?)|
#
# 126 V, IND, ACT-PAST (V-front, -i-): 
  (((k��ns|k��nty|l�hd|l�ys|p��s|pyys|s��s|synny|ties|v�hen)i)
  ((|t|mme|tte|v�t)|(CLT-SFX?)))(CLT-SFX?)|
#	
# 127 V, ACT-IND, COND (V-back, -isi-): 
  (((anta|maka|ol|pelasta|sano|tahto|tul|ulottu|usko)isi)
  ((n|t|mme|tte|vat)|(CLT-SFX?)))(CLT-SFX?)|
#
# 128 V, ACT-IND, COND (V-front, -isi-): 
  (((keskeyty|p��s|s�)isi)((n|t|mme|tte|v�t)|(CLT-SFX?)))
  (CLT-SFX?)|
#
# 130 V, ACT-IND, POT (V-back, -le-, -ne-, -re-, -se-): 
  ((((saa)ne)e)|
  (((tul)le)e))(CLT-SFX?)|
#
# 131 V, ACT-IND, POT (V-front, -le-, -ne-, -re-, -se-): 
  (((lie)ne)v�t)(CLT-SFX?)|
#
# 132 V-EXT:
  ((ole(n|t|mme|tte))|
  (olla|on|ovat)|
  (ol(i|isi))((n|t|mme|tte|vat)|(CLT-SFX?)))(CLT-SFX?)|
#
# 133 V-NEG:
  (en|et|ei|emme|ette|eiv�t)(CLT-SFX?)|
#
# 134 V-CONNEG (ACT, POT):
  (tulle)(CLT-SFX?)|
#
# 135 V-CONNEG (ACT, PRES):
  (luule|ole)(CLT-SFX?)|
#
# 136 V-CONNEG (PASS, PRES):
  (olla)(CLT-SFX?)|
#
# 137 V-MOD:
  ((pit��|piti|t�ytyy|t�ytyi|mahtaa|mahtoi)|
  ((voi|voisi)(n|t|mme|tte|vat|(CLT-SFX?))))(CLT-SFX?)|
#
# 138 V, ACT-IMP, 2SG:
  (katso|kirjoita|laista|laske|malta|nouse|ota|tee|tule|vie)
  (POSS-SFX-V?CLT-SFX?)|
#
# 139 V, ACT-IMP, 1PL (-kaa):
  (((anasta|anta|antautu|asetta|astu|hukku|ahkeroi|ilmianta|iloit|julista|juo|
  juos|juotta|katkais|katso|kehoitta|koetel|koetta|kohdat|kohotta|
  kukista|kumartu|kutsu|langet|linnoitta|lunasta|luopu|maat|muurautta|
  nautti|neuvotel|nielais|nous|ol|otel|otta|paet|palat|palvel|pan|poiket|
  poltta|polvistu|puhdistautu|pukeutu|rakasta|rakenta|riemuit|sano|sekoitta|
  soitta|soti|sulke|suostu|taistel|tappa|tavoitel|tuhot|tunte|tuo|
  tutki|uhrat|vaani|valit|vallat|vaelta|valvo|varo|veisat)kaa)mme)
  (CLT-SFX?)|
#
# 140 V, ACT-IMP, 1PL (-k��):
  (((�l|erist�|etsi|h�vitt�|heitt�|j�tt�|k�y|kielt�|kiitt�|kysy|l�hett�|
  l�hte|ly�|menetel|men|myy|pelj�t|pit�|pyrki|pysy|ry�st�|ryyp�t|rient�|siirt�|
  siirty|sy�|t�ytt�|teh|tyyty|uudista|v�ijy|viett�|ymp�r�i|y�py)k��)mme)
  (CLT-SFX?)|
#
# 141 V-ACT, IMP-3SG (V-back, -koon):
  ((aja|ajatel|alka|anasta|ano|anta|arvioi|asetta|asettu|astu|
  asu|autta|avautu|erot|hakat|hallit|hankki|hoita|huoju|huuhto|
  hukutta|huuta|ilmoitta|ilahutta|iloit|irroitta|irtautu|istu|
  jaka|jauha|johta|johdatta|joutu|julista|juo|juotta|kaata|kadot|
  kanta|karat|kasat|kasta|kastu|kasva|katso|kehu|kelvat|kerskat|
  kerto|kirjoitta|kirjoitutta|kiroil|koetel|kohdat|kohot|kokoontu|
  koot|korjat|korvat|koske|kosta|kosketta|kuihdutta|kuivettu|
  kukista|kuljetetta|kulke|kulu|kulutta|kumarta|kunnioitta|kuohu|
  kuol|kuritta|kutsu|kuul|kuulu|kuunnel|laajenta|langet|laske|
  laskeutu|lausu|leikat|lohdutta|loista|loppu|luke|lunasta|
  luopu|luotta|maat|maksa|muista|muovat|murtu|muserta|muuttu|nai|
  nosta|noudatta|nous|nuhdel|odotta|ohjat|ojenta|ol|omista|opetta|
  oppi|osoitta|osoittautu|osta|otta|paet|paina|painu|paisutta|pala|
  palat|palautta|palautu|palkit|palvel|pan|panta|pauhat|pelasta|
  pirskoitta|pisaroi|poiket|poista|polke|poltta|pudista|puhdista|
  puhdistautu|puhu|puke|pukeutu|punnit|rakasta|rangais|ratkais|
  rauet|riemuit|riippu|riisu|rot|rukoil|rukoilta|saa|saastu|saata|
  salli|sano|sattu|seiso|seurat|sito|siunat|sopi|sulke|suojat|
  suojel|soet|solmitta|sovitta|suo|suoritta|suota|surmat|suudel|
  tapahtu|tarkasta|tarkat|tarttu|teurasta|toimitta|totel|toteutu|
  tuke|tul|tunnusta|tuo|tuomit|tuotta|turvautu|tutki|uhrat|
  unhotta|vaelta|vahvista|vaiet|vaikutta|vainot|vala|valista|
  valit|vallit|valmista|valu|vanno|vapahta|varjel|varo|vartioi|
  vastat|vavista|veisat|verhot|verso|vihmo|virrat|viskat|vuodatta|
  ymp�rileikatta)koon)(POSS-SFX-V?CLT-SFX?)|
#
# 142 V-ACT, IMP-3SG (V-front, -k��n): 
  ((�l|el�|elpy|etsi|h�vit|heitt�|her�tt�|hylj�t|hyv�ksy|j��|
  j�nnitt�|j�tt�|kasva|k��nt�|k��nty|k�ske|k�y|k�ytt�|kest�|kielt�|
  kiitt�|kivitt�|kysy|l�hesty|l�hett�|l�hte|l�vist�|leikel|
  leiriyty|levit|liitty|lis��nty|lis�t|ly�|menetel|men|miehitt�|
  myy|n�h|n�ytt�yty|nylke|p��s|p��st�|p��tty|peitt�|pelj�t|peseyty|pes|
  pid�tty|pyhitty|pyrki|pys�hty|pysy|rev�is|ry�st�|s�ily|s�ilytt�|
  selitt�|siirty|sivel|sylke|sy�|sy�s|sy�t�|sytytt�|t�ytt�|t�ytty|
  teh|v�isty|vet�|vie|vihkiyty|vilis|vy�tt�|yhty|ylist�|yll�tt�)k��n)
  (POSS-SFX?CLT-SFX?)|
#
# 143 V-IMP: PASS (V-back, -ta-koon): 
  (((julkais|koetel|rangais|ratkais|tuo)ta)koon)(CLT-SFX?)|
#
# 144 V-IMP: PASS (V-back, -tta-koon): 
  (((aja|alenne|ammu|anna|anne|asete|asu|ava|ero|haka|hanga|huude|
  huuhdo|jae|juliste|kaade|kaavi|kasva|koo|kasa|katso|kirjoite|
  korote|kutsu|laske|leikkau|lue|luovute|maini|makse|nauli|
  nostate|ote|peruste|peruute|polte|pue|puhalle|puhdiste|puserre|
  rakenne|riemui|riko|ripuste|ristiinnauli|saastute|sakote|
  salli|sano|save|siuna|sulje|suorite|surma|tallete|tarkaste|
  teuraste|toimite|tuho|tuomi|tutki|uhra|vali|valjaste|valmiste|
  vanno|varuste|vihmo|vuodate|ymp�rileikkau)tta)koon)(CLT-SFX?)|
#
# 145 V-IMP: PASS (V-front, -t�-k��n): 
  (((menetel|menet|myy|pes|pi|pyhit|riit|teh|tie|v��n|vie|ymp�r�i)t�)k��n)
  (CLT-SFX?)|
#
# 146 V-IMP: PASS (V-front, -tt�-k��n): 
  (((etsi|h�vite|h�vi|heite|k�yte|kehyste|kiinnite|kiite|kivite|
  l�hete|levenne|m��r�|my�nne|nimite|p��ste|pelj�|pide|piste|pyhite|
  pyyhi|revi|ry�ste|s�ilyte|t�yte|v�henne|vie|vihi|yhdiste)tt�)k��n)
  (CLT-SFX?)|
#
# 147 V: PASS-PRES (V-back, -ta-an): 
  (((ahdiste|aje|alenne|aliste|anne|asete|askarei|asu|asute|
  ava|erote|hajote|haka|halkais|halveksi|hanki|harjoite|hauda|havai|herja|
  huoma|huude|huuhdo|ilmoite|iloi|irroite|istu|jae|juliste|juote|kaade|
  kaiva|kaiverre|kanne|kara|karkoite|kaste|kate|katso|kaupi|kavalle|
  kerro|kiedo|kirjoite|kirkaste|kokoonnu|koo|koriste|korja|korote|
  koste|kukiste|kulute|kumo|kuoki|kurite|kutsu|lahjoite|laina|laite|
  lakais|laske|laule|leika|liittoudu|louhi|lue|luki|lunaste|luovute|maini|
  makse|mita|mulliste|murehdi|murha|murre|murska|muserre|muute|neuvo|
  noste|noudate|nous|odote|ohja|opete|osoite|oste|ote|paiste|paljaste|
  panna|parja|paukute|pelaste|pelastu|peruste|pilka|poimi|poiste|
  polje|polte|pudiste|pue|puhalle|puhdiste|puhu|punni|pure|raaha|
  raaste|raiska|rakenne|rangais|ravi|riemui|riko|ripuste|ruhjo|
  rusenne|ruumii|ruve|saarna|saate|sakote|sano|seulo|sido|sirote|
  siuna|soite|solva|sorre|sovite|suiste|sulate|sulje|surma|suunna|
  taite|taivute|talla|tallete|tape|tarjo|tarka|tarvi|tava|temma|
  teuraste|todiste|toimite|toivo|toverei|tuho|tuki|tulki|tunne|tuomi|
  tutki|uhra|unhote|vaadi|vaali|vahviste|vaienne|vaino|vaiva|vali|
  valite|valla|valloite|valmiste|vangi|vanhurskaute|vanno|vannote|
  varaste|varuste|vasote|vasta|vavis|veisa|verho|viska|vuodate|
  ylenkatso|ymp�rileika)ta)an)(CLT-SFX?)|
#
# 148 V: PASS-PRES (V-front, -t�-�n): 
  (((el�te|esite|este|etsi|h�lyte|h�v�is|h�vite|heite|her�te|hylji|hy�k�|
  hyvite|itke|j�nnite|j�te|k��nne|k��ri|k�yte|keite|ke|kielle|kiinnite|
  kiiste|kiite|kylve|kynne|kysy|kytke|l�hete|l�viste|levite|liite|lis�|
  l�yde|m��r�|lyhenne|niite|p��ste|p��|pelj�|peri|pes|pete|pide|pies|
  piirite|pyhite|pysyte|pyydyste|pyyhk�is|rev�is|revi|riiste|ry�ste|s��ste|
  s�ik�hyte|s�lyte|s�rje|siirre|sylje|synnyte|sy�s|sys�|t�yte|tervehdi|tiede|
  tyhjenne|ty�nne|v��nne|v��riste|v�lte|vede|viete|vihelle|virite|
  ylenne|yliste)t�)�n)(CLT-SFX?)|
#
# 149 V: PASS-PRES (V-back, -da-an): 
  (((juo|luo|saa|suo|tuo|voi)da)an)(CLT-SFX?)|
#
# 150 V: PASS-PRES (V-front, -d�-�n): 
  (((k�y|ly�|myy|n�h|sinet�i|sy�|teh|vie)d�)�n)(CLT-SFX?)|
#
# 151 V, PASS-PRES (V-back, -la-an): 
  (((ennustel|huhuil|huokail|koetel|kuul|kuulustel|lankeil|luul|
  nuhdel|palvel|pudistel|raadel|tavoitel|tul|valhetel|
  varjel|voidel)la)an)(CLT-SFX?)|
#
# 152 V: PASS-PRES (V-front, -l�-�n): 
  (((etsiskel|hyv�il|riidel|viljel|t�hyil|viskel)l�)�n)(CLT-SFX?)|
#
# 153 V, PASS-PRES (V-back, -na-an): 
  (((pan)na)an)(CLT-SFX?)|
#  
# 154 V: PASS-PRES (V-front, -n�-�n): 
  (((men)n�)�n)(CLT-SFX?)|
#
# 155 V, PASS-PRES (V-back, -ra-an): 
  (((sur)ra)an)(CLT-SFX?)|
#
# 156 V, PASS-PRES (V-back, -ta-an): 
  (((hio|kaadu|korote|laske|murtaudu|vastaanote)ta)an)(CLT-SFX?)|
#
# 157 V: PASS-PAST (V-back, -t-i-in):
  ((((balsamoi|kannel|kuul|luo|luul|nous|ol|pan|puristel|rukoil|
  sirotel|saa|tul|tuo|vartioi|voidel)t)i)in)(CLT-SFX?)|
#
# 158 V: PASS-PAST (V-front, -t-i-in):
  ((((h�v�is|k�y|likistel|ly�|men|myy|p��s|pies|rev�is|sinet�i|
  sy�s|teh|viet|ymp�r�i)t)i)in)(CLT-SFX?)|
#
# 159 V: PASS-PAST (V-back, -tt-i-in):
  ((((ahdiste|aje|ammu|anne|asete|ava|erote|hae|hajaannu|hajote|
  hanki|hauda|havai|hukute|huoma|huude|huuhdo|ilmoite|jae|
  juliste|juote|kanne|karkoite|kaste|kasvate|katsaste|kavalle|
  kerro|kiedo|kirjoite|kohote|koo|kokoonnu|koriste|kukiste|kulje|
  kuljete|kuolete|kutsu|kuulute|laka|lanniste|laske|lausu|
  ((ymp�ri)?leika)|lue|luovute|maini|muonite|murre|murska|muute|
  naure|neuvo|noste|noude|ojenne|odote|oste|ote|paasto|palaute|
  paranne|piina|pilka|polje|polte|puhdiste|puhalle|puhu|punni|
  puno|rakenne|rasite|riisu|ripuste|ristiinnauli|ruve|saarre|
  saate|saavu|salli|sano|sido|siuna|solmi|sulje|suorite|surma|
  tahdo|taite|talla|tava|tao|tape|tarjo|temma|teuraste|toimite|tuho|
  tuomi|tutki|uhra|upote|usko|vaani|vaiva|vale|vali|valite|valloite|
  valmiste|vangi|vasta|veisa|vieroite|viska|voite|vuodate)tt)i)in)
  (CLT-SFX?)|
#
# 160 V: PASS-PAST (V-front, -tt-i-in):
  ((((el�te|eriste|etsi|h�vite|heite|her�te|hirte|hylji|hylj�|itke|
  j�rjeste|j�te|k�ske|k�yte|ker�|kiinnite|kivite|kylve|kynne|kysy|
  l�hesty|l�hete|levite|liite|lis�|l�yde|m��r�|merki|n�yte|nimite|
  n�yryyte|p��llyste|p��ste|p��te|peite|pete|pide|piirite|piirre|
  pyhite|pystyte|pyyde|pyydyste|revi|ry�ste|s��de|s��ste|s�ilyte|
  siirre|syrj�yte|syyte|t�yte|teete|vede|vierite|viete|vihi|virite|
  yhdiste|yliste|ymm�rre)tt)i)in)(CLT-SFX?)|
#
# 161 V: PASS-COND (V-back, -isi-in): 
  (((annetta|asetetta|hakatta|halveksutta|havaitta|ilmoitetta|
  johdatetta|julistetta|katsotta|kerrotta|kirjoitetta|kirkastetta|
  koetelta|kootta|kostetta|kukistetta|kuulta|lietsotta|luetta|
  muistetta|noudatetta|oksastetta|otetta|panta|poistetta|poltetta|
  puetta|puhdistetta|punnitta|rakennetta|rikotta|ripustetta|saata|
  saatetta|sanotta|seulotta|sovitetta|sulatetta|surmatta|tapetta|
  toimitetta|tukitta|tunnetta|tuomitta|tuota|tutkitta|uhratta|
  upotetta|vaaditta|vahvistetta|vihatta|voidelta|voita|
  voitetta)isi)in)(CLT-SFX?)|
# 
# 162 V: PASS-COND (V-front, -isi-in): 
  (((el�tett�|h�vitett�|heitett�|j�tett�|ly�t�|n�ht�|n�ytett�|
  p��stett�|pelj�tt�|pidett�|piirrett�|pyhitett�|pyyhitt�|riistett�|
  t�ytett�|teht�|tiedett�|vihitt�)isi)in)(CLT-SFX?)|
#  
# VERB: Verbs homonymous with illative/partitive forms of nouns:
# haudata: hautaan, m��r�t�: m��r��n.
#
# VERB-NOUNS: 
#  ((min� (teille) (m��r��n|hautaan)|
# 
# Verbs occurring with homonymous partitive/illative forms:
# The homonymous illative/partitive nouns are found with the verb olla, 
# the negative verbs ei, �l�, and with the inflected forms of the verbs 
# in the list VERB-CLSD. With those verbs, the clause/sentence which is 
# separated from the text with the strong punctuation marks
#  (.|!|?) is [-CLSD] and the nominal argument is in the partitive form.
# 
# OBS: onko t�m�n s��nn�n yhteyteen liitett�v� tietoa toisen argumentin
# morfologiasta?
# 163 VERB-CLSD: 
  (antaa|armahtaa|asettaa|astua|etsi�|haluta|h�vitt��|heiluttaa|
  her�t�|herjata|huutaa|hyl�t�|jatkaa|j�tt��|julmistua|juosta|k��nt��|
  kaatua|kallistaa|kalvaa|kantaa|karvastella|k�tke�|katsoa|k�ytt��|kielt��|
  kiinnitt��|kiitt��|kiroilla|kiusata|kohdata|korjata|korvata|kumartaa|
  kunnioittaa|kuulla|kyll�sty�|kylv��|kynt��|l�hesty�|lepytt��|lis�t�|
  loukata|lujittaa|luottaa|moittia|muistella|muuttaa|n�hd�|niskoitella|
  notkistaa|odottaa|onnitella|ontua|ottaa|p��st��|paljastaa|palvella|panna|
  parantaa|pelj�t�|pit��|polkea|pukeutua|rakastaa|rasittaa|rikkoa|rukoilla|
  satuttaa|seurata|siunata|sortaa|suorittaa|surmata|sy�d�|tarkastaa|
  tarttua|tehd�|teroituttaa|todistaa|toimittaa|tuhota|tulla|tuntea|tyydytt��|
  ulottaa|unohtaa|uskoa|vahvistaa|varjella|vartioida|vihastua|vihata|ylist��|
  luottaa|osata|uskoa)|
#
# Particles:
# Adpositions listed in the file fin.spec which belong to the groups A and B:
# 164 DIR-IN-POP-A: 
  (kohtaan|silmiin|sis��n|sis�lle|syd�mee)(POSS-SFX-V?CLT-SFX?)|
#
# 165 DIR-IN-POP-B:   
  (v�liin|v�lille|per�lle|sekaan|sekaa)(POSS-SFX-V?CLT-SFX?)|
#
#   (juureen|��reen|eteen|mukaan|
#
# 166 Adpositions which produce ambiguous structures:
#  (alla|alta|alle|edell�|edelt�|edelle|edess�|edest�|eteen|
#  avuksi|avukse|
#  hallussa|hallusta|
#  huomassa|huomasta|huostassa|huostasta|
#  hyv�kse|
#  j�lkeen|
#  joukossa|joukosta|
#  kaltainen|kaltaisia|kaltaista|kaltaiselle|
#  kaltaisekse|kaltaisikse|kaltaisista|kaltaisille|
#  kanssa|kautta|
#  keskell�|keskelt�|keskelle|keskess�|keskest�|keskuudessa|keskuudesta|
#  kimpussa|kimpusta|kintereill�|kintereilt�|
#  kohdalla|kohdalta|kohdalle|kohdassa|kohdasta|
#  kupeella|kupeelta|
#  l�heisyydess�|l�heisyydest�|l�hell�|l�helle|
#  laista|laiselle|
#  luona|luota|luotaan|luokse|
#  muassa|mukana|mukaan|
#  ((alku|loppu)?p��ll�|p��lt�|p��lle)|
#  ((ala|yl�)?puolella)|((ala|yl�)?puolelta)|puolesta|puolestaan|puolelle|
#  rinnalla|rinnalta|rinnalle|
#  seassa|seasta|seastaan|
#  seurassa|seurasta|sijalla|t�hte|
#  silmi�|silmiss�|silmist�|sis�ss�|sis�st�|
#  sivulla|sivulta|sivussa|sivusta|
#  takana|takaa|
#  toimesta|toimestaan|
#  tyk�n�|tyk��|
#  vallassa|vallasta|
#  v�lill�|v�lilt�|
#  vertaista|vertaisesta|seasta|sijasta|
#  vierell�|vierelle|vieress�|vierest�|
#  yll�|ylt�|ylle|
#  ymp�rill�|ymp�rilt�|ymp�rille)
#  (POSS-SFX?CLT-SFX?)|
#
# Ambiguities with the following postpositions and illative/partitive
# forms: (asti|ennen|kesken|kohtaan|likell�|mukaan|vaille|vastaan)
#
#POP-AMB: 
#  ((ennen(kuolemaansa))|
#  (((herraa(ni|nsa))|(jumalaa(mme|ni|nne))|kunigasta|teit�)
#  vastaan)|
#  (kesken(ik��ni))|
#  (palkkaansa(vaille))|
#  (valtaansa
#  (niit�)kohtaan)|
#  ((sen) mukaan)|
#  (likell�(Herraa meid�n)Jumalaamme)|
#  (mukaani(en)miekkaani))|
#
# 167 Adverbs, conjunctions:
#  (((entis|hallitus)aikaan)|aikoinaan|ainiaan|ainoastaan|alkuaan|
#  alunpit�en|(ammoll(aan|een))|
#  edelleen|ehyelt��n|
#  ensin|ensink��n|puoleen|
#  enint��n|ennest��n|entisell��n|entiselleen|entisaikaan|entuudestaan|
#  erikseen|erill��n|erill�|erilleen|
#  hajallaan|hajalleen|hamaan|hetkelleen|hiljalleen|
#  istualleen|j�ljest�p�in|
#  (j�ljest�p�in(k��n|kin))|j�lleen|j�rjest��n|johan|kaikkiaan|
#  kauttaaltaan|kesken��n|kiinni|(kuiten(kaan|kin))|kun|kunhan|kyll�|kyll��|
#  kyllikseen|l�heisyydess�|lain|lainkaan|l�peens�|leikill�|lev�ll��n|
#  liian|luonnostaan|
#  my�h��n|my�s|niin|niini|nimenomaan|nyt|ollenkaan|omakse|omikse|
#  parhaimmillaan|(parhaimmillaan(kin|kaan))|pitk�n��n|
#  selkosel�ll��n|sel�lleen|
#  senj�lkeen|sikseen|sis��n|(suin(kaan|kin))|suunniltaan|
#  tahansa|taakseen|takaa|t�n��n|t�nne|tarkalleen|
#  t�st�l�hin|t�ydelleen|tarkkaan|toistamiseen|
#  (tieten(kin|k��n))|toisekseen|tosiaan|tosiaan|tosiaankaan|tosiaankin|
#  turhaan|tyynni|umpim�hk��n|uudestaan|vaan|valloilleen|varuillaan|
#  vastaan|vastaamme|vastaammekin|vastaatte|vastaattekin|
#  v�h��|vaiti|vaitikaan|valtoinaan|v�h�n|(varmaan(kaan|kin))|
#  varsin|(varsin(kaan|kin))|vastaan|viel�|(viel�(k��n|kin))|vuorostaan|
#  yhteens�|yhten��n|yksikseen|yksin��n|yksist��n|yleens�|
#  yltyleens�|ylleen|jos|sela)(POSS-SFX?CLT-SFX?)|
#
# Ambiguities with homonymous interjections and verbs:
# INTRJ: (voi)
# INTRJ-HOM: 
#  (voi(herraamme|(minun)rintaani))
#
# 168 ILL-MINT: 
  (ja kun tarkastat asuinsijaasi)|
#2 asuins[ija<a>si]
  (sinun asuinsijaasi)|
#1 el[�m��ns<�>]
#2 el[�m��ns<�>]
  (eik� kukaan synnill�ns� vahvista el�m��ns�)|
  (joka el�m��ns� rakastaa)|
  (mutta joka vihaa el�m��ns�)|
#1 el[�m��ns<�>kin]
  (viel�p� omaa el�m��ns�kin)|
#1 etsikk[oaika<a>si]
  (ettet etsikkoaikaasi tuntenut)|
#1 h[aava<a>si]
  (sinun haavaasi ei paranneta)|
#1 h[auta<an>]
  (ett� min� hautaan)|
  (tiet��n h�nen hautaansa)|
#1 h[�rk�<�>]ns�
  (sapattina p��st� h�rk��ns�)|
#5 h[erra<a>mme]
#3 h[erra<a>mme]
# (voi herraamme)|
  (onnittelemaan meid�n herraamme)|
  (meid�n kirkastettuun herraamme)|
  (voi herraamme)|
# 8 h[erra<a>ni]
  (siunannut minun herraani)|
  (jotka seuraavat herraani)|
  (satuta k�tt�ni herraani)|
  (kiroilla herraani)|
  (nostivat k�tens� herraani)|
  (heimosta tullut t�nne herraani)|
  (salaliiton herraan vastaan)|
  (kohdannut minun herraani)|
#2 h[erra<a>si]
  (vartioinut herraasi)|
  (sinun herraasi)|
#3 h[erraans<a>]
#3 h[erraans<a>]
  (leipoja rikkoivat herraansa)|
  (kapinoitsi herraansa vastaan)|
  (ja palvelija herraansa suurempi)|
  (jotka herraansa odottavat)|
  (ei ole palvelija herraansa)|
#1 hovih[erraans<a>]
  (n�ihin kahteen hoviherraansa)|
#1 i[k�<�>ni]
  (kesken ik��ni)|
#2 i[k��ns<�>]
  (lis�t� ik��ns� kyyn�r�nk��n)|
#2 j[alka<a>si]
#5 j[alka<a>si]
  (jalkaasi kiveen loukkaisi)|
  (etk� loukkaa jalkaasi)|
  (h�n varjelee sinun jalkaasi)|
  (juokse jalkaasi)|
  (polje jalkaasi ja sano)|
  (ettet jalkaasi kiveen loukkaisi)|
#2 jum[ala<a>mme]
#1 jum[ala<a>mme]
  (rukoilimme jumalaamme)|
  (pois jumalaamme)|
  ((meid��n) jumalaamme)|
#10 jum[ala<a>ni]
#4 jum[ala<a>ni]
  (minun jumalaani)|
  (jumalaani min�)|
  (avuksi jumalaani)|
  (odottaessani jumalaani)|
  (kiit�n jumalaani)|
  (jumalaani)|
#31 jum[ala<a>nne]
  (teid�n jumalaanne)|
  (kielt�isi jumalaanne)|
  (jumalaanne)|
#  (rukoilkaa herraa, jumalaanne)|(palvelkaa herraa, jumalaanne)|
#  (jumalaanne, vastaan)|
#  (jumalaanne, sek� te ett� kuningas)|
#(etsim��n herraa, jumalaanne)|
#  (kiitt�k�� herraa, jumalaanne)|(herraa, jumalaanne, vastaan)|
#  (palvelkaa nyt herraa, jumalaanne)|
#  (kiitt�k�� herraa, jumalaanne)|
  (t�htijumalaanne)|
#7 jum[ala<a>si]
  (sinun jumalaasi)|
#  (�l� kiusaa herraa, sinun jumalaasi)|
# kansansa
  (kansaansa)|
#1 kanssapalvel[ija<a>si]
  (armahtaa kanssapalvelijaasi)|
# kaulaanne
  (saa kaulaanne)|
#1 k[aulaans<a>]
  (kaulaansa baabelin)|
#1 k�rs[im�<�>ns�]
  (muistele k�rsim��ns�)|
#1 kuokka[<a>nsa]
  (kuokksa)|
  (kirvest�ns�)|
#4 kuol[emaans<a>]
  (ennen kuolemaansa)|
  (h�nen kuolemaansa)|
#1 lepos[ijaans<a>]
  (�l� h�vit� h�nen leposijaansa)|
# l�hett�j��ns�
  (l�hett�j��ns� suurempi)|
#1 l[iha<a>mme]
  (meid�n omaa lihaamme)|
#4 l[iha<a>ni]
  (luutani ja lihaani)|
  (sy�m��n minun lihaani)|
#1 l[iha<a>nne]
  (luutanne ja lihaanne)|
#2 l[ihaans<a>
  ((kalvaa|vihannut|sy�m��n) omaa lihaansa)|
#3 l[iha<a>si]
  (sinun luutasi ja lihaasi)|
  (on omaa lihaasi)|
#1 l[onkka<a>nsa]
  (ontui lonkkaansa)|
#2 l[uoja<a>nsa]
  (herjaa h�nen luojaansa)|
#1 m[atkaans<a>
  (jatkoi matkaansa iloiten)|
#3 m[��r�<�n>], verbs;
#1 m[��r�<�>nne]
  (niin min� m��r��n)|
  (mit� min� teille m��r��n)|
  (min� m��r��n miekan omiksi)|
  (t�h�nastista m��r��nne)|
#1 m[aja<a>si]
  (l�hesty sinun majaasi)|
#2 m[atka<a>nne]
  (jatkatte matkaanne)|
  (voitte jatkaa matkaanne)|
#4 m[atkaans<a>]
  (ja meniv�t matkaansa)|
  (jatkoivat matkaansa)|
  (k��ntyiv�t jatkamaan matkaansa)|
#2 m[iekka<a>ni]
  (en miekkaani enk�)|
  (heilutan miekkaani)|
#1 m[iekka<a>nsa]
  (ei paljastanut miekkaansa)|
#2 n[�lk��ns<�>]
  (taivaasta heid�n n�lk��ns�)|
  (tyydytt��kseen n�lk��ns�)|
  (n�lk��ns� tyydyt�)|
#1 n[iskaans<a>]
  (eiv�t notkistaneet niskaansa)|
#1 p[aikka<a>si]
  (�l� j�t� paikkaasi)|
#2 p[alkka<a>ni]
  (katsomaan minun palkkaani)|
  (muuttanut palkkaani)|
#1 palvelusteht[�v�<�>ns�]
  (tekem��n palvelusteht�v��ns�)|
#2 p[alkka<a>nsa]
  (ei j�� palkkaansa vaille)|
#1 perhek[unta<a>sa]
  (hoitamaan omaa perhekuntaans)|
#4 perint[�osaans<a>]
  (palasivat perint�osaansa)|
  ((julmistui|kyll�styi) perint�osaansa)|
#  (ja israelia, perint�osaansa)|
  (eik� perint�osaansa heit�)|
  (h�nen perint�osaansa)|
#3 perint[�osa<a>si]
  (kansaasi ja perint�osaasi)|
  (perint�osaasi h�v�ist�v�ksi)|
  (perint�osaasi he rasittavat)|
#1 p[es�<�>si]
  (pid�t pes��si setripuissa)|
#2 r[inta<a>ni]
  (voi minun rintaani)|
#1 s[elk�<�>ni]
  (ovat minun selk��ni kynt�neet)|
#1 s[elk�<�>si]
  (�l�k� k��nn� selk��si sille)|
#1 s[ilm�<�>ni]
  (kiinnit� silm��ni siihen)|
#1 t�htijum[ala<a>nne]
#1 tek[em��ns<�>]
  (kanssa tekem��ns� liittoa)|
#2 v[altaans<a>]
#3 v[altaans<a>]
  ((lujittamaan|ulottamaan) valtaansa)|
  (k�yt� totuuteen valtaansa maassa)|
  (k�ytt�v�t valtaansa niit� kohtaan)|
#1 valtank[unta<a>ni]
  (hallitsemaan valtakuntaani)|
#1 vastust[aja<a>nsa]
  (tarttuivat kukin vastustajaansa)|
#1 v[atsa<a>ni]
  (minun vatsaani karvasteli)|
#1 v[atsaans<a>]
  (vaan omaa vatsaansa)|
#1 ves[iastia<a>si]
  (vesiastiaasi juodakseni)|
#2 viinit[arha<a>ni]
  (anna sinulle viinitarhaani)|
  (viinitarhaani en vartioinut)|
#2 viinit[arha<a>si]
  (korjaa tyhj�ksi viinitarhaasi)|
  (�l�k� leikkaa viinitarhaasi)|
#  v[irka<a>mme>]
#  (ettei virkaamme moitittaisi)|
#11 v[irkaans<a>]
  (toimittaessaan virkaansa)|
  (ilmestysmajaan toimittamaan virkaansa)|
  (astua toimittamaan virkaansa)|
  (he toimittivat virkaansa)|
  (k�yv�t toimittamaan virkaansa)|
  (toimittamaan virkaansa)|
  (toimittavat virkaansa meid�n)|
  (virkaansa toimittavat papit)|
  (joissa toimittavat virkaansa)|
  (toimittaessaan virkaansa)|
#1 v[oima<a>si.
  (�l� anna voimaasi naisille)|
#1 v[irka<a>ni>]
  (min� virkaani kunniassa)|
#
# Nouns:
  (helle)|
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
# conditional conjunctions):
  (elle(n|t|i|mme|tte|iv�t))|
  (jolle(n|t|i|mme|tte|ivat))|
#
# DIR-ON-POP-C: 
  (h�nt��n|juureen|kohtaan|kupeeseen|nen��n|nokkaan|per��n|
  pieleen|pohjaan|p��h�n|suuhun|syrj��n|varteen|vasten)|
  (alle|p��lle|huipulle|huipuille|partaalle|per�lle|pohjalle|reunalle|
  h�nt��|juuree|kupeesee|nen��|nokkaa|pohjaa|reunaa)(POSS-SFX?CLT-SFX?)|
#
# DIR-ON-POP-D: 
  (eteen|j�lkeen|kohdalle|liki|luo|oheen|pieleen|poskeen|sivuun|
  niskaan|per��n|p��h�n|viereen|suuhun|syrj��n|
  ��relle|edelle|edustalle|h�nnille|j�ljille|juurelle|juurille|
  kannoille|kintereille|kupeelle|likelle|l�helle|luokse|rinnalle|
  sivulle|sivuille|suulle|taakse|tyk�|vierelle|
  yl�puolelle|etee|niskaa|p��h�|syrj��|vieree)(POSS-SFX?CLT-SFX?)|
#
  (edelleen|toisiin|toisiinsa|uuni|��nens�|��nen|��neni|��nesi|
  ��neens�|��ni|��ne|��nesih�n|��nenkin|��nikin|��nenh�n))
# "��ne" poistettu useasta ryhm�st�. Ks. alkuper�inen EXCL-tiedosto.
#
