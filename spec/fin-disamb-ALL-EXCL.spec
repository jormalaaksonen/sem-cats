#Pirkko Suihkonen, 2016 and 2017
#Copyright: Pirkko Suihkonen
#
#INE (-ssa/-ssä)
#
# Agreement in NPs: 
# only one case marking is accepted in the NP:s which contain specifiers 
# and modifiers preceeding the lexical head which is a noun:
# tä+ssä piene+ssä poja+ssa. 
#
# The words inside the parentheses contain the combinations <ssa> and <ssä> 
# which are homonymouos with the indices of the inesseive case 
# (fin.spec, Rule 1.1, INE-C and adpositions) in Finnish. 
#
# Sanat "sydämessä, sydämissä, sisässä, silmissä, välissä", ovat sekä substantiiveja että adpositioita. Sanaluokkien jakauma on tarkastettava tekstistä, 
#
# N-PRP, SG-NOM:
ALL-EXCL: ^((gassa|hadassa|massa|missa|rissaan|ussa)|
#
# PRP-N, foreign words, illative (-an):
  ((gassa|hadassa|massa|missa|rissaan|ussa)an)|
#
# Adpositions mentioned in the file fin.spec: 
# IN-POP-A: 
  ((silmi|sisä|sydäme)ssä)(POSS-SFX?CLT-SFX?)|
  (tulen liekissä keskellä)|
#
# IN-POP-B: 
  ((välissä|perällä|seassa)(POSS-SFX?CLT-SFX?))|
#
#
# ADE (-lla/-llä)
#
# Agreement in NPs: 
# only one case marking is accepted in the NP:s which contain specifiers and 
# modifiers preceeding the lexical head which is a noun: 
# tä+llä piene+llä poja+lla. 
#
# The words inside the parentheses contain the combinations <lla> and <llä> 
# which are homonymous with the indices of the adessive case 
# (fin.spec, Rule 1.2, ADE-C and adpositions) in Finnish. 
#
# Ambiguous structures:
# sillä = CONJ (62), 
# sillä = the adessive form of the demonstrative prnouns se.
#
# Nouns:
# Proper nouns, GEN (-n):
  ((drusilla|priskilla|silla|ulla)|
  ((drusilla|priskilla|silla|ulla)n))(POSS-SFX?CLT-SFX?)|
#
# Common nouns, GEN (-n):
  ((((esi|ilma|kaikki|tuomio|väki|yli)?valla)|
  kulla|mulla|villa)n)(POSS-SFX?CLT-SFX?)|
# 
# Nouns, SG-NOM:
  (helle)(POSS-SFX?CLT-SFX?)|
#
# Adjectives
  (hellä)(POSS-SFX?CLT-SFX?)|
#
# Verbs:
# Infinitives (V-back, -lla):
  ((ajatel|arvostel|astel|ennustel|harhail|iloitel|katsel|kiroil|
  koetel|kohdel|kuol|kuul|luetel|luul|majail|nuhdel|ol|oleskel|ommel|
  palvel|puhel|puhutel|rakennel|remahdel|rukoil|seurustel|sommitel|
  suositel|suudel|taistel|tavoitel|totel|tul|turmel|tutkistel|uhitel|
  vaellel|valhetel|varjel|viekoitel|voidel|voivotel)la)(CLT-SFX?)|
#
# Infinitives (V-back, -llä):
  ((heitel|hypel|käyskennel|kierrel|kysel|kävel|lämmitel|niel|nyökytel|
  oleskel|pidel|piileskel|riidel|syleil|vietel|viljel|
  vääristel|ylvästel)lä)(CLT-SFX?)|
#
# Imperatives and connegatives:
  (kiellä|sivalla|vaella)(CLT-SFX?)|
#
# Ambiguous (homonyms: infinitive and the adessive form of the 
# demonstrative adjective "sama": samoilla.
#
# Inflected forms:
# V-PRES. 1SG, 1PL:x1:
  ((puhalla|tallaa|uskalla|vaella)(n|mme))(CLT-SFX?)|
  (elle|kiellä(n|mme))(CLT-SFX?)|
#
# Pass. Pres. (V-back (la-an))
  ((ennustel|huhuil|koetel|kuul|kuulustel|lankeil|nuhdel|ommel|palvel|pudistel|
  raadel|tavoitel|tul|valhetel|varjel|voidel)laan)(POSS-SFX?CLT-SFX?)|
#
# Pass. Pres. (V-front (lä-än))
  ((hyväil|viljel|viskel)lään)
  (POSS-SFX?CLT-SFX?)|
#
# Particles:
# (kyllä|kyllähän|kylläänsä|kylläänne|kyllääsi|kylläsi|kylläänsähän|
#  todella|todellakin|
#  vähälläpä|tahallamme|tahallanne)|
#
# Adpositions taken into account in the file fin.spec:
# ON-POP|PRP-C: 
#  (vasten|alla|päällä|partaalla|partailla|pinnalla|
#  pohjalla|pohjilla|reunassa|reunoissa|reunalla|reunoilla)
#  (POSS-SFX?CLT-SFX?)|
#
#  ON-PRP|POP-D:
#  ON-POP-D: (edessä|edustalla|ohessa|ääressä)|
#  (hännillä|jäljessä|juurella|juurilla|kannoilla|kintereillä|kohdalla|
#  keskikohdalla|likellä|lähellä|luona|niskassa|paikalla|
#  perässä|rinnalla|sivussa|sivuissa|sivulla|sivuilla|suulla|syrjässä|
#  takana|välillä|vastapäätä|vieressä|yllä)(POSS-SFX?CLT-SFX?)|
#
#Conjunction "sillä", OT and NT:
#SILLA-CONJ: ((, |. |; |: |! |? |' |\" |- )sillä))
#1. demonstrative "sillä" in NPs marked with the adessive case:
#  (sillä (^@a?b?c?d?e?f?g?h?i?j?k?l?m?n?o?p?q?r?s?t?u?v?w?x?y?z?)ADE)|
#2. except habeo constructions and idioms:
#  (sillä (ole|oli|on|tavoin))|
#3. "sillä" in restrictive relative clauses:
#  (sillä, (joka|jolla|jonka|minkä))|
#4. except demonstrative "sillä" referring to objects mentioned in 
# before in the utteraces or in previous expressions:
#  ((sydämemme|teot|makaat|maan) sillä)|
# Lisäksi kaikki tapaukset, joissa "sillä"-sanan ympärillä on sanaväli.
#  ( sillä )
#
#
# ELA (-sta/-stä)
# Agreement in NPs: 
# and modifiers preceeding the lexical head which is a noun:
# tä+stä piene+stä poja+sta. 
###
# The words inside the parentheses contain the combinations <sta> and <stä> 
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
# CN: PTV (V-back, -ta; kun sija määritellään siten, että se liittyy
# heikkoon vokaalivartaloon, voidaan kaikki konsonanttiloppuiset 
# partitiivit poistaa):
  ((ahdistus|ajatus|allas|anteeksiantamis|anteeksiantamus|arvoitus|
  asukas|asumus|aviorikos|avustus|elatus|enkeliruhtinas|esaias|filippus|
  epäjumalanpalvelus|erotus|esikois|hajaannus|hallitus|hapatus|
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
  parantamis|parjaus|päänalais|pääsiäislammas|pelastus|pellavakangas|
  pensas|perustamis|perustus|petos|pilkkaamis|pitalis|pohjois|
  poistamis|polttamis|porras|profetoimis|puhdistus|puhkeamis|
  pukeutumis|punonnais|puolustautumis|pyhäkköpalvelus|pöytäpalvelus|
  raavas|rakennus|rakentumis|raastosaalis|rangaistus|rannerengas|
  rasitus|ratsuhevos|rengas|reunus|riistosaalis|rikkomus|rikos|
  ripustamis|ruhtinas|rukous|ruoskimis|ruumis|ryöstösaalis|saalis|
  saamis|saas|sanomis|sekoitus|seos|sortumis|sinettisormus|sitomis|
  siunaus|skyyttalais|sotapalvelus|sovitus|suitsutus|sukurutsaus|
  suorittamis|suosionosoitus|suositus|suunemilais|suuttumus|
  syntiuhrikauris|syöttöraavas|taikomis|taivas|tallaamis|tapaus|
  tarkoitus|tarsolais|tavoittelemis|teos|teuras|todistus|toimittamis|
  toteutumis|tulemis|tulemus|tuntemis|tuntemus|tuomis|uhraamis|
  uskallus|vaellus|vaeltamis|vahvistus|vahvistumis|vaikerrus|
  vainoamis|valittamis|valivaliolammas|valkenemis|valmistamis|
  vanhus|vannomis|vapautus|varas|varis|varvas|varoitus|
  (vaski(allas|hakas|jous|rengas))|veronhuojennus|vastaus|vastustus|
  vaunuhevos|vavistus|väentungos|vedenpaisumus|velallis|verenvuodatus|
  veronhuojennus|vertaus|vieras|vihaamis|vihollis|virvoitus|vitsaus|
  ylösnousemus|ympärileikkaus)ta)(POSS-SFX?CLT-SFX?)|
#
# CN: PTV (V-front, -tä):
  ((häviämis|ammonilais-iljetys|eteis|eväs|henkäys|hillitsemis|
  hylkäämis|hyväksymis|hyväntekemis|hämmästys|häpäisemis|häväistys|
  häämötys|hävitys|ies|ihmis|ihmisymmärrys|ikävöimis|ilmestymis|
  ilmestys|ilvehtimis|itsensähillitsemis|jalkamies|jälkeläis|jänis|
  järjestys|jäännös|keihäs|kestämis|kärsimys|käyttämis|kääntymys|
  kiertämis|lähimmäis|leviämis|lisäämis|maanjäristys|määräys|
  menemis|menestys|merkitys|metsäkyyhkys|
  ((murha|pää|päällys|päätös|perä|ratsu|sadanpää|valio|viha|
  viidenkymmenenpää)?mies)|pääsiäis|pelkäämis|pesemis|peseytymis|
  poisviemis|pylväs|pyydys|pyytämis|sääs|säätämys|selitys|
  sikiämis|sotamies|synnyttämis|syytös|syömis|teettämis|tekemis|
  täyteläis|täyttymis|täyttämis|teräs|vähentämis|vähennys|väijytys|
  vasenkätis|veis|veljes|viemis|vihkimis|vihkiytymis|
  ylistys|ylistämis|yltymis|ymmärrys)tä)(POSS-SFX?CLT-SFX?)|
#
# A: PTV (V-back, -ta): 
  ((aamuis|ahdas|aikais|ainokais|aineellis|anakilais|anatotilais|
  aramilais|daanilais|edomilais|egyptin-aikais|arvois|arvokas|
  arvollis|aviollis|erikois|erinomais|esikuvallis|etumais|etiopialais|
  filistealais|halpasukuis|halkeamis|harhaoppis|harras|haureellis|
  hebrealais|heikkouskois|helakanpunais|herkullis|hiljais|hurskas|
  hyvänhajuis|ihotautis|iankaikkis|iänikuis|ikuis|ilmais|jalosukuis|
  jaspis|jokavuotis|juutalais|kaikenkaltais|kaikkinais|kaikkivaltias|kallis|
  kallisarvois|kaltais|kaikenkaltais|kapinallis|karvais|karvas|
  kastei|katoavais|kaukais|kaunis|keskinäis|kirkas|keskinäis|
  kohtuullis|kolmitahkois|kompastuvais|kookas|korkuis|kreikkalais|
  kultais|kuninkaallis|kunniallis|kuolevais|kuvannollis|kuvapatsas|
  liukas|luonnollis|luvallis|lyhytaikais|maallis|mahdollis|makedonialais|
  miehenpuolis|mieluis|minkäkaltais|monilukuis|mooabilais|muinais|
  mukais|muotois|omais|nasaretilais|onnellis|otollis|pahanlaatuis|
  paljas|pallonmuotois|paras|patsas|pellavais|pellavapukuis|pitalitautis|
  petollis|pitalis|pohjoispuolis|puolis|puhdas|purppuranpunais|
  puutteenalais|raikas|rakas|rakentavais|raskas|rauhallis|rikas|
  rikollis|ruhtinaallis|runsas|rupis|ruumiillis|saastais|
  sairas|salais|samankaltais|seitsenhaarais|senkaltais|senpuoleis|
  seurakunnankokous|sielullis|sotakelpois|sotakuntois|sovelias|
  suitsevais|sulois|suolais|taidollis|taivaallis|taivais|
  tapais|tarpeellis|tasais|tavallis|tämänkaltais|totis|tulevais|
  tulis|turmiollis|tähänastis|ulkonais|uppiniskais|urhoollis|
  vaarallis|vahingollis|vaikeatajuis|vaivais|vajavais|vakallis|
  vakituis|valheellis|valkois|vanhurskas|vasullis|velallis|
  vertais|vihollis|viisas|villais|virsta|väkivaltais|voimallis|
  yhtämittais|ylenpalttis|ylimmäispapillis)ta)(POSS-SFX?CLT-SFX?)|
#
# A: PTV (V-front, -tä): 
  ((egyptiläis|edellis|eksyttäväis|ensimmäis|entis|eräs|hengellis|
  häpeällis|hyödyllis|hyötymistä|ihmeellis|ilmeis|imeväis|itäis|jisreeliläis|
  jokapäiväis|keskinäis|leeviläis|nurjasydämis|näköis|nöyrtyväis|
  nykyis|oikeamielis|päällimmäis|perillis|pettäväis|päivällis|
  pysyväis|rehellis|runsasvetis|samanmielis|siivekäs|synnyttäväis|
  syntis|syyllis|terveellis|täydellis|täyteläis|vähäis|veljellis|
  veljes|viimeis|vilpillis|yhteis|yhtäläis|yksinäis|ylhäis|ylimmäis|
  ymmärtäväis)tä)(POSS-SFX?CLT-SFX?)|

# ELA-EXCL-PRN:
  ((((jol|kahden|kaiken|minkä|minkään|sel|tuol|täl)lais)|
  ((minkä|saman|sen|tämän)kaltais)|
  jokais|mois|semmois)ta)(POSS-SFX?CLT-SFX?)|
#
# NUM, -toista: 
  (((yhdellä|yhdelle|yhden|yhdennen|yhtentenä|yhtenä|yhdennessä|yhdenteen|
  yhdes|yksi|kahdet|kahden|kahtena|kahdella|kahdelle|kahdesta|kahteen|
  kahta|kahdeksi|kahdessa|kahdes|kahtena|kahden|kahdennen|kahdentena|
  kahdennella|kahdennelle|kahdennesta|kahdenteenteen|kahdennetta|
  kahdenneksi|kahdennessa|kahdenteen|kahdes|kahdetta|kaksi|
  kolme|kolmannesta|kolmantena|kolmas|kolmen|kolmesta|kolme|
  neljä|neljän|neljännen|neljänteen|neljäntenä|neljästä|neljättä|
  neljäs|neljättä|
  viisi|viiteen|viideksi|viiden|viidennen|viidentenä|viidennellä|
  viidettä|viides|viidellä|viiteen|
  kuusi|kuuden|kuudentena|kuudes|kuusi|
  seitsemän|seitsemäs|seitsemästä|seitsemäntenä|
  kahdeksas|kahdeksan|kahdeksantena|kahdeksan|
  yhdeksän|yhdeksäntenä|yhdeksännes|yhdeksäs)toista)|
  (kymmentuhantista)|
  (puolen|puolta|puoltatoista))(CLT-SFX?)|
#
# V-INF-I (V-back, -ta):
  ((ilmais|katkais|nous|puhkais|rohkais|sokais|valkais|vapis)ta)|
#
# V-INF-I (V-front, -tä):
  ((jylis)tä)|
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
  (äänestä|äestä|edistä|eristä|estä|häväistä|järjestä|jylistä|keihästä|
  kestä|kiristä|päästä|pestä|piestä|pistä|pyydystä|reväistä|riistä|
  rynnistä|ryöstä|säästä|säestä|syöstä|tähystä|vääristä|väistä|virkistä|
  yhdistä|ylistä)(CLT-SFX?)|
#
# V-IMP (V-front, -kää, -köön, -kö):
  ((äänestä|äestä|edistä|eristä|estä|häväistä|järjestä|jylistä|keihästä|
  kestä|kiristä|päästä|pestä|piestä|pistä|pyydystä|reväistä|riistä|
  rynnistä|ryöstä|säästä|säestä|syöstä|tähystä|vääristä|väistä|virkistä|
  yhdistä|ylistä)(kää|köön|kö))(CLT-SFX?)|
#
# INF-I, (V-back, -ta)
#
# INF-I, (V-front, -tä)
  ((häväis|jylis|reväis|syös)tä)(CLT-SFX?)|
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
  ((äänestä|äestä|edistä|eristä|estä|häväistä|järjestä|jylistä|keihästä|
  kestä|kiristä|päästä|pestä|piestä|pistä|pyydystä|reväistä|riistä|
  rynnistä|ryöstä|säästä|säestä|syöstä|tähystä|vääristä|väistä|virkistä|
  yhdistä|ylistä)en)(CLT-SFX?)|
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
  ((äänestä|äestä|edistä|eristä|estä|järjestä|keihästä|kestä|kiristä|
  päästä|pistä|pyydystä|riistä|rynnistä|ryöstä|säästä|säestä|tähystä|
  vääristä|väistä|virkistä|yhdistä|ylistä)(n|mme))(CLT-SFX?)|
#
# V-PASS, PRES (V-back, -taan):
  (((halkais|nous|rangais)ta)an)(CLT-SFX?)|
#
# V-PASS, PRES (V-back, -taan):
  (((häväis|pääs|syös)tä)än)(CLT-SFX?)|
#
# Adpositions which are included in the adposition rules:
  (sisästä|välistä)(POSS-SFX?CLT-SFX?)|
#  seasta, silmistä, sydämestä
# Adpositions:
  (huostaan|laista)(CLT-SFX?)|
#
# Adverbs (V-back): 
#  (vasta|vastaan|ainoastaan|nousemistaan|uudestaan)(CLT-SFX?)|
#
# Adverbs (V-front):
#  (ennestään|järjestään|siirtymistään|vähenemistään|väistymistään|
#  yksistään)(CLT-SFX?)|
#
#  (VERBS-SOM (aasi|aasisi|aasinsa|aasien|ääni|äänen|ihon|ihanan|uusi|
#  osata|uskoa)))
#
# ABL (-lta/-ltä)
#
# Agreement in NPs: 
# only one case marking is accepted in the NP:s which contain specifiers 
# and modifiers preceeding the lexical head which is a noun: 
# tä+ltä piene+ltä poja+lta. 
#
# The words inside the parentheses contain the combinations <lta> and <ltä> 
# which are homonymous with the indices of the ablative case 
# (fin.spec, Rule 2.2, ABL-C and adpositions) in Finnish. 
#
# The ambiguous word forms contain the combinations -lta-/-ltä in the stems, 
# or inflected word forms: the partitive forms of nouns and adjectives,
# or verbs containing the derivative suffixes -lta-/-ltä- which participate 
# in the consonant gradation: viheltää, polttaa, etc. 
# 
# Nouns and adjectives:
# N, SG-NOM:
  (ilta|kulta|multa|((kuningas|tuomio|väki)?valta))
  (POSS-SFX?CLT-SFX-B?)|
#
# N, SG-ILL (V-back, -an): 
  (ilta|kulta|multa|((kuningas|tuomio|väki)valta)an)
  (POSS-SFX?CLT-SFX-B?)|
#
# N-SG-PTV (V-back; -ta):
  ((((juudan|asdodin|aramin)?kiel)|kyynel|miel|((pihti)?piel)|syl|tiil)tä)
  (POSS-SFX?CLT-SFX-F?)|
#
# N-SG-PTV (V-front; -tä):
  ((((äiti|etelä|etu|länsi|loppu|miehen|pohjois|riita|sisä)?puol)|
  huol|kannel|nuol|taival|tul|((itä)?tuul))ta)(POSS-SFX?CLT-SFX-B?)|
#
# illative and genitive forms of adjectives and nouns
  (aasia|aasian|ääni|ääneen|uusi|uuteen|ääne)|
# äänen|
#
# N, SG-GEN (V-back, -n):
  ((vaskialtaa|telta)n)(CLT-SFX-B?)|
#
# Verbs (stem: -ta, -tä):
  ((vältä|malta|polta|(valta(si)?))(n|t|mme|tte))(CLT-SFX-B?)|
  ((puhalta|suojelta|vaelta|tulta)(ko|en))|((kieltä)kö)|
  (malta|polta|vältä|
  uskoa|uskon|luottaa|luotan|osata|osaan)(CLT-SFX-B?)|
#  
# Verbs (INFII, Instructive (INST): -s-tan):
  (((edus|haas|julis|lois|omis|paljas|puhdis|raas|ratsas|ripus|
  tarkas|tunnus|vahvis)ta)en)|
#
# Verbs (INFII, Instructive (INST): -stä-en):
  (((ryös|sääs|säes|väis|ylis)tä)en)|
#
# Particles:
  (kauttaaltaan|lopulta)(CLT-SFX-B?)|
#
# Adpositions:
# DE-ON-PRP|POP-C:
  (((a|huipu|huipui|kupee|lae|partaa|pohja|reuna)lta)|
  ((juure|kohda|kupee|noka|pohja|reuna|varre|varsi)sta)|
  ((pää|perä)ltä)|((hännä|nenä)stä))(POSS-SFX?CLT-SFX-B?)|
#
# DE-ON-PRP|POP-D:
  (((edusta|juure|juuri|kannoi|kohda|lae|pinna|sivu|suu)lta)|
  ((ääre|ede|viere)(ltä|stä))|
  ((hänni|jälji|kinterei|like|lähe|pää|viere|y)ltä)|
  ((ohe|niska|poske|sivu)sta)|
  ((jälje|perä|piele|syrjä)stä)|
  (takaa))(POSS-SFX?CLT-SFX?)|
#
# NEG-MOD-INF
#
# Adpositions containing the strings -lta/-ltä, but which do not belong to the groups C and D:
#  (((puo(le)?)|suunna|taho|varre|varsi)lta)(POSS-SFX?CLT-SFX-B?)|
#  ((keske|peri|sisä|väli|ympäri)ltä)(POSS-SFX?CLT-SFX-F?))
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
  (aasia|ääni|abihun|baani|ben-haanan|daan|ester|geehasi|guuni|
  haanan|herodes|keenan|kristus|leivinuuni|miikael|mooses|noon|nuun|paratiisi|
  pelikaani|publikaani|rabbuuni|rubiini|saaruhen|siin|siion|soon|topaasi|
  ase|hiuskarva|into|isä|jäännös|kanaan|kaikkeinpyhin|kastelija|
  kenaan|koira|kruunu|kuu|lähettilää|lahja|munaskuu|muusi|
  nuoruusikä|((kanta|olka)?pää)|parta|poika|rakkaus|rauta|ruumis|suku|
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
  (((ei|kestää|menestyy|pysyvät|vielä)kö)hän)|
#
# 3 N-COM: PL-NOM (V-back, -t):
  ((hullu|kala|kirjanoppinee|taivaa)t)(CLT-SFX?)|
#
# 4 N-COM: PL-NOM (V-front, -t):
  ((enkeli|tähde|tietäjä)t)(CLT-SFX?)|
#
# 5 N-COM: NOM & GEN (V-back, -n): 
  ((aartee|ahdistaja|aihee|((murha-)?aikee)|ala|altaa|aluee|armaa|armahtaja|
  armonantaja|((hävitys|sota-|tuho)?asee)|asukkaa|
  aseenkantaja|askare|askaree|askelee|asuinsija|asumasija|asukkaa|
  auringonpatsaa|auttaja|ehtoo|(elon(leikkuu|korjuu))|
  epäjumala|esimie|esinaha|esipiha|hallitsija|hampaa|
  ((sala|turmion)?hankkee)|heilutus-rintaliha|hieho|hikiliina|hoitaja|
  hohtee|((ase|kesä|sivu|talvi|varasto|vieras)?huonee)|houkkiokansa|hurskaa|
  ihmise|((pellava(-)?)?ihokkaa)|ikee|ismaelilaismatkuee|jälkikorjuu|
  johtomie|juhta|julistaja|juomanlaskija|jyvärouhee|kaikkivaltiaa|
  kahlee|kankaa|kanssapalvelija|kantaja|kantelee|((puu|vaate)?kappalee)|
  kastee|katsee|kauhu|kaulakoristee|kauppiaa|((syntiuhri)*kaurii)|kavaltaja|
  käskynhaltija|hohtee|kaarnee|kahina|kantelee|kastee|katsee|kauppia|
  kielimurtee|kiitosuhriteuraa|kinsteripensaa|kirjanoppinee|kirjee|kohina|
  kivijumala|kivipatsaa|koittee|((otsa|ristikko)?koristee)|
  ((viinin)?korjuu)|korokkee|(kulta(-aartee|jumala|renkaa))|kuninkaa|
  kuohu|kupee|kurittaja|((kutsu)?vieraa)|kuu|kuukautistila|kuvapatsaa|lahja|
  laiho|((pääsiäis|yhteysuhri)?lampaa)|lantee|((ohran)?leikkuu)|
  liepee|liha|lippaa|loistee|lunastaja|lonkka|lonkkaluu|
  (((aasin)?leuka)?luu)|lumpee|
  ((alanko|aru|anti|arte|egyptin|erä|etelä|hasse|kallioerä|laidun|
  manner|pelto|perintö|siidonin-|synnyin|trakonitiin-)?maa)|
  mainee|manner|((rypäle)?mehu)|
  mietelausee|mirha|murhee|murtaja|muusi|naaraa|naha|nauha|nenärenkaa|
  niska|niskurikansa|nisunleikkuu|ohdakkee|ohjee|ohranleikkuu|oinaa|
  omistaja|osa|((profeetan)?oppilaa)|orjantappurapensaa|osasto|ostaja|pada|
  paisee|pakanakansa|pakokauhu|paluumatka|((maa|pelto)?palsta)|
  palvelija|patsaa|päämie|pääsiäislampaa|pauhina|((teltta)?peittee)|
  pelastaja|pensaa|perämie|perhee|pikkukarja|pilvenpatsaa|polttaja|
  polttouhrioinaa|polttouhriteuraa|profeettaoppilaa|puhee|
  ((kehoitus|puolustus|väli)?puhee)|puimatanteree|
  ((keula)?purjee)|((hedelmä|hirsi|öljy|manteli|metsäöljy|
  ((granaatti)?omena)|palmu|setri|tamariski|viini|((metsä)?viikuna))?puu)|
  puuasee|puuttee|raaa|raakalee|raavaa|raavaskarja|((henkilö|vilja)?raha)|
  rahvaa|((ranne)?renkaa)|rangaistukse|rantamaa|ratsumie|rauha|rauta-asee|
  rautapatsaa|rehuvilja|riettaa|rikkomukse|rintaliha|ruoho|
  ((enkeli|suku)?ruhtinaa)|((herkku|mieli)?ruua)|ruumii|ruostee|
  ((kalan|voitto)?saalii)|sadanpäämie|sairaa|
  ((kevät|rae|rankka|syys)?satee)|seinäpatsaa|seurakuntakokoukse|
  seuruee|sortajakansa|sotamie|suitsukkee|sukulunastaja|
  suu|suurkuninkaa|synnytystuska|syntiuhri|syntiuhriteuraa|syntivelka|
  taakka|tahtaa|taitee|taivaa|tarpee|täydenkuu|(teltta(kankaa|maja))|
  takaa-ajaja|telinee|((yhteysuhri)?teuraa)|tila|(todis(taja|tee))|tuha|tuho|
  tulki|tuomitsija|tyyssija|työasee|työmie|uhma|(uhri(teuraa|lahja))|
  ulkomaa|uudenkuu|uuhe|((lesken|liina|päällys)?vaattee)|vaihtee|valhee|
  vakaa|valaa|valhee|valhejumala|valitukse|valtiaa|vangitsija|vanhurskaa|
  vantaa|varustee|varjelija|varkaa|(vaski(altaa|raavaa))|välimie|varustuksee|
  vastustaja|velka|venhee|verivelka|viha|vihkiäisoinaa|
  ((jalo)?viini)|viisaa|(vikauhri(-)?oinaa)|vilja|voitee|vuohe|
  vuorenharjantee|((sairas)vuotee)|ylenkatsee|ylösnousemukse|
  aasia|aasi|aasie|äänie|iho|ihana|uuni)
  (n|(POSS-SFX-V)))(CLT-SFX?)|
# 
# 6 N-COM: GEN (V-front, -n): 
  ((edeltäjä|enkeli|elinnestee|esinee|harmaapää|hedelmä|henkilö|
  hedelmä|heltee|ihmee|ikee|imettäjä|((niska|reisi)*jäntee)|
  juhlapäähinee|((kyy|lohi|vaski)?käärmee)|käskijä|käyttäjä|keihää|kengä|
  keritsijä|((käsky)?kirjee)|kirvee|kyynelee|((puurim-käsky)?kirjee)|kyy|
  kyynärä|lähettäjä|lähettilää|lähtee|leivä|liepee|((heilutus)?lyhtee)|
  loppumäärä|maksanlisäkkee|melskee|mielipitee|((arvo|avio|avionrikkoja|
  apu|esi|hallitus|johto|mahti|matka|meri|murha|pää|päällys|päivä|pelto|
  perä|perhekunta-pää|puolus|ratsu|sadanpää|sota|työ|valio|väli|
  viidenkymmenenpää|viha|virka)*miehe)|
  nälä|nestee|((alku|kanta|loppu|pylvään|tuulis)?pää)|
  ((ilta|sydän|tuho)?päivä)|
  peittee|perhee|perkelee|pylvää|rikkee|((sireeninnahka)?peittee)|
  ((perhekunta-|sadan|viidenkymmenen)?päämiehe)|perijä|((korkeasti-)?pyhä)|
  rämee|((viini)?rypälee)|seppelee|silmänräpäykse|
  sinapinsiemene|sitee|suitsukkee|synnyttäjä|syöttilää|syy|syyhy|
  syyttäjä|syyttee|tähde|tekelee|tekijä|tietäjä|vaskikäärmee|
  ((päällys)?vaattee)|velje|((seko)viini)|viine|villitsijä|
  vuoriseläntee|ääne)(n|(POSS-SFX-V)))(CLT-SFX?)|
#
# 7 N-COM: PL-GEN (V-back, -ten): 
  (((suku)?ruhtinas)ten)(POSS-SFX?CLT-SFX?)|
#
# 8 N-COM: PL-GEN (V-back, -ten): 
  ((leeviläis)ten)(POSS-SFX?CLT-SFX?)|
#
# 9 N-COM: PL-GEN (V-back, -i-n): 
  (((pakana)i)n)(POSS-SFX?CLT-SFX?)|
#
# 10 N-COM: PL-GEN (V-back, -i-en): 
  (((libertiin|matkamieh|publikaan|tamaan|villiaas)i)en)(POSS-SFX?CLT-SFX?)|
#
# 11 N-COM: SG-PTV (V-back, -a): 
  ((((elin)?aika)|alku|anoppi|asia|epäusko|haavaa|halu|harjoittaja|hiuskarva|
  huoneenhaltija|juhta|kansa|kanssapalveluja|karja|kartano|kastelija|
  kengänpaula|kohottaja|koira|korva|kulta|kunnia|((seura|suku)?kunta)|
  lahja|laki|latva|lauma|leipäkakku|lupausuhri|manna|matka|napina|
  neuvonantaja|nostaja|omaatunto|
  onne|opettaja|palvelija|parta|pilkka|poika|puoli|raha|rata|ruoka|sana|
  seura|sorkka|tahto|teko|tukka|turva|vaarna|((sivu)?vaimo)|vainaja|vaippa|
  vaiva|valta-asema|vanki|vohla|yhteenmeno)a)(POSS-SFX?CLT-SFX?)|
#
# 12 N-COM: SG-PTV (V-front, -ä): 
  ((ääri|emäntä|henke|((kanta)?isä)|isäntä|jälke|jylinä|jyvä|kive|
  kyynärä|lähettäjä|leipä|leiri|miniä|näky|nime|((tuho)?päivä)|pöytä|
  pyyntö|silmäterä|synty|syntyperä|tie|((perhe|talon)*väke)|velje|
  ympäristö|ystävä)ä)(POSS-SFX?CLT-SFX?)|
#
# 13 N-COM: SG-PTV (V-back, -ta): 
  ((ahdistus|äitipuol|aivoitus|aluet|arvoitus|äitipuol|hautaami|haureut|
  hautaus|ihokas|julkeut|((jumalan)?palvelus)|kaivos|kansalais|
  katset|kauneut|kerskaus|kiitos|kiusaamis|
  laupeut|luopumus|maa|morsian|orjatar|pakenemis|pakenemisaiet|
  orjatar|palaamis|palvelijatar|((perintö|perhe)?omaisuut)|
  pesuet|pitalis|pituut|puhdistus|puhet|puhkeamis|((riita)?puol)|rikkomus|
  rikos|rohkeut|rukous|ruumis|saaliis|saamis|salaisuut|seuralais|
  sisar|suu|tuul|un|uskallus|vaellus|vanhurskaut|vanhuut|vastaus|
  ver|viisaut)ta)(POSS-SFX?CLT-SFX?)|
#
# 14 N-COM: SG-PTV (V-front, -tä): 
  ((ään|häväistys|häviämis|hyötymis|ilmestymis|jalanleveyt|jäännös|kät|
  keihäs|kiel|kiertämis|kypsyyt|leveyt|leviämis|menestys|miel|mies|pää|
  perhet|siirtymis|tie|työ|tytär|ver|vilpittömyyt|ylistys|yltymis)tä)
  (POSS-SFX?CLT-SFX?)|
#
# 15 N: N-COM: PL-PTV (V-back, -i-a):
  (((ahdistaj|irstauks|juur|kaltais|kirjoituks|koristuks|
  neuvonantaj|((opetus)?laps)|osuuks|perintöos|puol|rikkomuks|saalistaj|
  sisar|valittajais)i)a)(POSS-SFX?CLT-SFX?)|
#
# 16 N: N-COM: PL-PTV (V-front, -i-ä):
  (((ääri|jälkeläis|käs|kenk|((viha)?mieh)|mietelm|päiv|ryöstäj|silm|
  syyttäj|tehtäv|tyttär|velj|virs|ystäv)i)ä)(POSS-SFX?CLT-SFX?)|
#
# 17 N: N-COM: PL-PTV (V-back, -j-a):
  (((aiko|alku|armolahjo|asunto|herkkupalo|jalko|kanso|kasvo|kaupunke|
  lahjo|laulu|meno|orpo|palatse|palo|pelastusteko|pelto|
  pentu|pilkko|polku|polttouhre|profeetto|rinto|sano|sielu|sisar|
  ((sivu)?vaimo)|surmattu|taiko|tapo|((tunnus)?teko)|((teuras|yhteys)?uhre)|
  vaivo|vanke|varo|vaunu|verkko|yläsale)j)a)
  (POSS-SFX?CLT-SFX?)|
#
# 18 N: N-COM: PL-PTV (V-front, -j-ä):
  (((käsky|kyntöjä|synte|synty|vävy)j)ä)(POSS-SFX?CLT-SFX?)|
#
# 19 N: N-COM: PL-PTV (V-back, -i-ta):
  (((asio|ennustelijo|hampa|kanssapalvelijo|kantele|katse|
  lampa|lu|nilkkarenka|palvelijo|puhe|pöytäviera|ruhtina|
  salamo|sukuluettelo|taloustavaro|tuomare|uusiaku|
  vaatte)i)ta)(POSS-SFX?CLT-SFX?)|
#
# 20 N: N-COM: PL-PTV (V-front, -i-tä):
  (((häpe|miniö|pyyte|te|tö)i)tä)(POSS-SFX?CLT-SFX?)|
#  
# 21 N-COM: SG-TRL (V-back, -kse-|-ksi(-)): 
  ((aluee|apulaise|aseenkantaja|elinaja|esikoise|ilo|kadotukse|
  kirkkaude|kompastuks|kuninkaa|kunnia|lai|maalitaulu|määrätarkoitu|
  omaisuuskansa|onnettomuude|osa|palka|palvelija|parhaa|
  perintöhauda|perintöosa|puolustukse|ruua|saalii|
  ((seurakunnan)?kokou)|silmänherku|sotapalvelu|surmattava|
  turmio|työorja|vahingo|vaimo|vartija|vedenpaisumu)(kse|ksi))
  (POSS-SFX?CLT-SFX?)|
#
# 22 N-COM: SG-TRL (V-front, -kse): 
  ((häviö|hävittämise|hetke|jälkeläise|nime|päällikö|päämiehe|perinnö|
  pyhäkö|silmänrapäy|silmänräpäykse|tehtävä|tyttäre|väijyty|väsymy|velje)
  (kse|ksi))(POSS-SFX?CLT-SFX?)|
#
# 23 N-COM: PL-TRL (V-back, i-kse):
  (((alamais|epäjumal|laps|orjattar|orj|palvelijo|vaimo)i)kse)
  (POSS-SFX?CLT-SFX?)|
#
# 24 N-COM: PL-TRL (V-front, i-kse):
  (((hengenpite|mieh|miel|ratsumieh|vaunumieh)i)kse)(POSS-SFX?CLT-SFX?)|
#
# 25 N-COM: SG-ESS (V-back, -na): 
  ((apu|herkku|hallitusvuote|hinta|hoitajattare|huole|juhla|käsivarte|
  käskynhaltija|kerskaukse|koto|kuninkaa|kunnia|kuukaute|
  ((elin|kuukautis|määrä)?aika)|lunastushinta|nautinto|oma|pilkka|
  oma|poutavuon|puku|raja|ruoka|saalii|suoja|tuomittava|uhrilahja|
  varustama|verho|viikkojuhla|virta|vuote|vuotee)na)
  (POSS-SFX?CLT-SFX?)|
#
# 26 N-COM: SG-ESS (V-front, -nä): 
  ((hyvä|hyvitykse|isä|leipä|((esi|päällys)?miehe)|((paasto|puhdistus|
  syntymä)?päivä)|tehtävä|viini)nä)(POSS-SFX?CLT-SFX?)|
#
# 27 N-COM: PL-ESS (V-back, -i-na): 
  (((nuol|palvelijo|sapatte|soture|työtovere|tuomis|valto|vaunusoture|
  viera|viinitarhure)i)na)(POSS-SFX?CLT-SFX?)|
#
# 28 N-COM: PL-ESS (V-front, -i-nä): 
  (((((ilo)?päiv)|päällikkö|peltomieh)i)nä)(POSS-SFX?CLT-SFX?)|
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
  juode|juoksu|juoste|kanna|kansa|käsivarre|kauhistavaisuude|kaula|
  ((turva)?kaupungi)|kehoittamise|kertomukse|kiivastukse|kiivaude|kirkkaude|
  kodi|kodittomuude|kohdu|kokonaisuude|korkeude|kotikaupungi|koura|
  kuninkuude|kurjuude|la|lai|leiri|liito|kuukautise|kuukautistila|lauma|
  liha|linna|luottamustoime|maa|makuuhuonee|makuukammio|
  mielisuosio|murhee|neuvo|neuvottelu|nouste|nuoruude|
  ohimo|oksarunsaude|omassatunno|olo|omavaltaisuude|opettamise|
  osasto|otsa|pahuude|palatsi|palvelija|palvelukse|perintömaa|
  perintöosa|petollisuude|pove|rakkaude|riita-asia|rikkaude|
  rintahaarniska|rinna|rukoushuonee|ruumii|sana|sankaruude|sielu|
  sija|suru|suu|suuruude|suuttumukse|synagooga|taistelu|talo|
  taudi|telta|((epä)?toivo)|une|tulemukse|tupe|tuntemise|
  uppiniskaisuude|usko|uskottomuude|vaipa|valitsema|valla|
  valtakunna|vanhurskaude|vanhuude|varjo|virkatoime|
  vuokra-asunno|vuorilinna|vuoristo|viha|viinitarha|viisaude|
  vimma|vuotee|yläsali)ssa)(POSS-SFX?CLT-SFX?)|
#
# 31 N-COM: SG-INE (V-front, -ssä): 
  ((elämä|etunenä|hädä|hempeyde|henge|hyvyyde|ikävöide|isä|
  jala|jälje|järjestykse|jouko|käde|kärsivällisyyde|kätkö|
  käytökse|kirjee|kutsumukse|köyhyyde|leiri|loppumäärä|miele|näy|nime|
  pää|päätökse|perä|pöydä|pyhäkö|pyhyyde|pyydykse|sääliväisyyde|
  säki|selä|selitykse|sisä|sisimmä|sydäme|syli|synni|taistelle|
  tekemise|temppeli|työ|vääryyde|vaellukse|vere|vilpillisyyde|
  ylpeyde|ylvästely|
  ymmärrykse)ssä)(POSS-SFX?CLT-SFX?)|
#
# 32 N-COM: PL-INE (V-back, i-ssa):
  (((aarrekammio|aike|askele|aito|ajatuks|alo|esikartanoi|himo|
  huone|ihastuks|ilo|jalkapohj|jalo|jano|kahle|kauhu|kaupunge|
  käsivars|kiusauks|kiimo|kiuku|korkeuks|korv|kuukautis|
  kuvittelu|linnoituks|lu|meno|mielimurte|murhe|rukouks|
  omissatunno|päänpohj|pelo|perhekunn|petoks|porte|rukouks|
  sieraim|synagoog|synnytyskivu|telto|toim|vaunu|virkapuvu|
  seurakunnankokouks|sukukunn|synagoog|tarpe|teo|un|vaino|vastustaj|
  vihastuks|viho)i)ssa)(POSS-SFX?CLT-SFX?)|
#
# 33 N-COM: PL-INE (V-front, i-ssä):
  (((enkele|häd|hämmästyks|häpe|itkuvirs|jäsen|juhl|kämmen|käs|
  kirje|kyl|näl|peljästyks|pyh|säär|siiv|sydäm|silm|synne|tehtäv|
  te|ver)i)ssä)(POSS-SFX?CLT-SFX?)|

# 34 N-COM: SG-ADE (V-back, -lla): 
  ((aasintamma|aja|ala|aluee|asioimise|ennustamise|haureude|houkuttelu|
  itku|kavaluude|käsivarre|kerra|kiima|kirjoitukse|kirkkaude|koura|kupee|
  kustannukse|loistee|matka|murehtimise|niskoittelu|ola|otsa|paika|
  perintöosa|piha|polvi|((etu)?sorme)|sotajouko|suu|tarpee|
  tavara|vaipa|viisaude|voima|vuore|vuoro|
  ehtoo|halu|istuime|johdo|jouko|kerskumise|levo|maakansa|määräaja|mieka|
  mielisuosio|omaisuude|pahuude|poja|polu|puolipäivälevo|raha|renkai|sana|
  sauva|sija|suvu|taido|valo|valtakunna|vaellukse|valtaistuime|valtika|
  varjo|vatsa|valtika|vanhurskaude|vuotee)lla)(POSS-SFX?CLT-SFX?)|
#
# 35 N-COM: SG-ADE (V-front, -llä): 
  ((henge|hyvyyde|iä|käde|keihää|kiele|lähimmäise|liepee|miele|myrsky|nime|
  puimajyrä|pöyhkeilemise|sineti|sydäme|täydellisyyde|väe|välitykse|viskime|
  hedelmä|isä|keihää|leiki|pöydä|((selko)?selä)|synni|tie|työ|
  vaivannäö|vyö|yö|vere)llä)(POSS-SFX?CLT-SFX?)|
#
# 36 N-COM: PL-ADE (V-back, -i-lla): 
  (((aarte|alttare|hevos|hiuks|houkutuks|houkuttelu|huul|jalo|
  ((kivi)?jumal)|jumalankuv|juon|kamele|kasvo|katse|korv|lahjo|mieko|
  mielisuosio|noituuks|paiko|((pelto|perintö)?ma)|polv|puhe|renka|
  rikkomuks|rinno|sarano|soittim|teo|tulo|un|valtaistuim|vaunu|
  asuinpaiko|huhu|kahle|kauhistuks|koru|kukkulo|laitum|matko|nuol|oks|
  poj|posk|rauta-ase|sano|rinno|sauvo|sija|sormi|sotajouko|sul|taio|
  tulv|uhrikukkulo|vaatte|valhe|varo|varuvelhouks|vuote)i)lla)
  (POSS-SFX?CLT-SFX?)|
#
# 37 N-COM: PL-ADE (V-front, -i-llä):
  (((ammattivelj|iljetyks|jälkeläis|kaulakäädy|käs|keihä|kyynel|
  olkapä|päiv|retk|silm|te|tö|tyttär|siiv|synne|velj|viimeis|vyötäis)
  i)llä)(POSS-SFX?CLT-SFX?)|
#
# 38 N-COM: SG-ELA (V-back, -sta): 
  ((alhaisuude|alttiude|armo|asuinsija|asumukse|asunno|haava|
  halu|hartia|haureude|heikkoude|herra|hinna|huokaamise|hurskaude|
  inno|jala|jouko|jumala|jumalattomuude|((aarre)?kammio)|kansa|karja|
  kasvami|kaupungi|
  keskuude|kida|kiivaude|kirja|kirkkaude|kohdu|kohtalo|kompastukse|
  korkeude|kulma|kuolema|kuritukse|kuvaaja|((uhri)?lahja)|laitume|
  (lammasten(-)?kaitsenna)|lauma|liha|lihavuude|((perintö)?maa)|maja|matka|
  mielipaha|mustelma|nuhtelu|nuoruude|ohjaukse|oma|omaisuude|
  onne|onnettomuude|opetu|opi|ove|pahuude|palvelukse|paranemise|
  pensaiko|perintöosa|poja|polvikunna|puhee|
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
# 39 N-COM: SG-ELA (V-front, -stä):   
  ((hälinä|elime|hedelmä|henge|henkäykse|ikävöimise|isä|
  itsemiele|jälkeläise|kärsivällisyyde|käde|köyhyyde|kylvö|leivä|miehe|
  miele|nime|pää|pesä|pöydä|pyhyyde|pyhäkö|selä|sisimmä|sydäme|
  syli|synni|syntymä|syntymise|täyteyde|tekijä|temppeli|työ|
  tyttäre|((palvelus)?väe)|vere|villiintymise|yhteyde|ylhäisyyde|ylpeyde|
  ymmärrykse)stä)(POSS-SFX?CLT-SFX?)|
#
# 40 N-COM: PL-ELA (V-back, -i-sta): 
  (((aarte|ahdingo|ahdistuks|ajoks|armo|askele|asuinpaiko|esivanhemm|
  hankke|haudo|heimolais|herjauks|himo|jalo|jyvärouhe|
  kahle|kaupunge|kauhistuks|käsivars|((kivi)?jumal)|
  kylkilu|lampa|((opetus)?laps)|lu|murh|naapure|nuorukais|oikeuks|olo|omais|
  onnettomuuks|päänpohj|((kanssa)?palvelijo)|perhekuntalais|pilkkaaj|
  poikas|poj|porte|puhe|raunio|renka|rikoks|ruhtina|ruhtinattar|runoilijo|
  saastaisuuks|sano|sapate|sarv|sieraim|sod|sotajouko|sukulais|
  synnytystusk|talo|tavaro|te|telto|teo|todistuks|tulo|tuntem|
  uhre|uhrilahjo|un|uskonasio|vaatte|vaihe|vainooj|varkauks|
  vaunu|velhouks|vesioj|vihollis|viinitarho|yhteysuhre|
  yhteysuhriteura)i)sta)(POSS-SFX?CLT-SFX?)|
#
# 41 N-COM: PL-ELA (V-front, -i-stä):
  (((hedelm|hiir|jälkeläis|käs|käsky|lähimmä|leire|leiv|mieh|näy|pä|
  peljätyks|riitelemis|säke|silm|synne|te|tyttär|urotö|vaivannäö|
  velj|((viha)?mieh)|ystäv)i)stä)(POSS-SFX?CLT-SFX?)|
# 
# 42 N-COM: SG-ABL (V-back, -lta): 
  ((ahmailu|alttari|arvo|aluee|ammati|avunhuudo|haltija|herral|
  ((valta)?istuime)|kansa|lapsi|luvu|muodo|naapuri|olenna|orja|
  orjattare|osa|paika|pohja|puole|rakentee|ruumii|sielu|suvu|teo|
  toise|tuomari|tuttava|varre|vartalo|voima)lta)
  (POSS-SFX?CLT-SFX?)|
# 
# 43 N-COM: SG-ABL (V-front, -ltä): 
  ((äidi|iä|isä|kiele|lähimmäise|miehe|miele|näö|nime|pää|
  sotapäällikö|sydäme|tie|väkevyyde|velje|ymmärrykse)ltä)
  (POSS-SFX?CLT-SFX?)|
#
# 44 N-COM: PL-ABL (V-back, -i-lta):
  (((alue|apostole|huul|kansalais|kasvo|kotipaiko|opetuslaps|
  palvelijo|paiko|rado|sapate|tuttav|valtaistuim|vihollis|voittaj|vuos)i)lta)
  (POSS-SFX?CLT-SFX?)|
#
# 45 N-COM: PL-ABL (front, -i-ltä):
  (((elinpäiv|is|järj|jäsen|kotiväe|mieh|riistäj|silm|te|velj)i)ltä)
  (POSS-SFX?CLT-SFX?)|
#
# 46 N-COM: SG-ALL (V-back, -lle): 
  ((ala|alttari|ape|aseenkantaja|asettaja|asunno|edusta|esikoise|
  ((epä)?jumala)|hauda|heimolaise|herjaaja|herra|hiuskarva|hovi|
  huoneenhaltija|huuli|iho|istuime|johtaji|jouko|kallio|kansa|
  karja|kukkuloi|kupee|kuukaude|
  laitume|leposija|maa|maatila|maja|matka|muinaise|niska|oksennukse|
  ola|omistaja|opettaja|opetuslapse|((perintö)?osa)|päälae|paika|
  palvelija|pello|poja|pove|puole|puoliso|rakkaa|rinna|ruumii|seurakunna|
  sielu|sisare|sulhaspoja|suu|suvu|taido|teurasuhri|todistaja|toveri|
  ((sivu)?vaimo)|valtaistuime|uude|viinitarha|voidellu|vuode|vuotee|
  vuore)lle)(POSS-SFX?CLT-SFX?)|
#
# 47 N-COM: SG-ALL (V-front, -lle): 
  ((äidi|hädä|isä|isännä|käde|kämmene|kiele|lähettäjä|lähimmäise|miehe|
  nime|päivä|pyydykse|siemene|silmä|sydäme|syönnökse|tekijä|temppeli|
  tie|työ|velje|vyö)lle)(POSS-SFX?CLT-SFX?)|
#
# 48 N-COM: PL-ALL (V-back, -i-lle): 
  (((aase|aarte|apostole|askele|halveksijo|hartio|heimolais|herro|jalo|
  kansalais|kasvo|((kivi)?jumal)|kamele|kaupo|kupe|lampa|lante|
  ((opetus)?laps)|ma|majo|naapure|oksennuks|om|opettaj|palvelijo|
  paiko|perhekunn|piio|poikas|poj|polu|polv|portonpalko|profeeto|
  ruhtina|sano|seuralais|sielu|silmäluom|sotajouko|sukukunn|suvu|
  tiluks|((virka)?tovere)|tuttav|työkumppane|vaatte|vaimo|vainooj|
  valitu|vanhemm|vankeustovere|vastustaj|vihollis|vuor)i)lle)
  (POSS-SFX?CLT-SFX?)|
#
# 49 N-COM: PL-ALL (V-front, -i-lle): 
  (((enkele|hallitusmieh|isänn|is|jälkeläis|kyynele|lähimmäis|silm|tyttär|
  te|velj|((viha)?mieh)|vihkiytyne|ylimyks|ystäv)i)lle)
  (POSS-SFX?CLT-SFX?)|
#
# 50 N-COM: SG-ABES (V-back, -tta):
  (((huomaa|tunte)ma)tta)(POSS-SFX?CLT-SFX?)|
#
# 51 N-COM: SG-ABES (V-front, -ttä):
  (((tietä)mä)ttä)(POSS-SFX?CLT-SFX?)|
#
# 52N-COM: PL-COMT (V-back, -i-ne-PX):
  (((ajaj|alue|((öljy)?ast)|asukka|hakas|halu|harppu|heimokunt|hevos|
  himo|hoviherro|ihokka|jalko|((vaski)?jalusto)|((sota)?joukko)|jous|
  jumal|juomauhre|juur|kalo|kalu|kalusto|((pikku|raavas)?karjo)|
  kaupunke|kantele|karstakuppe|kilp|korento|korko|koukku|kukkaleht|
  ((uhri)?kukkulo)|kuninka|kymbaal|laidunma|lamppu|lamppusaks|
  ((opetus|pikku)?laps)|laumo|lauto|lampa|lamppu|linnoituks|lu|
  luol|ma|miekko|omaisuuks|öljyastio|palkkalais|palvelijattar|palvelijo|
  pikkulaps|poik|poikkitanko|raavaskarjo|rajo|rapo|rasvo|ruumi|salpo|
  seuralais|sot|talo|takke|tavaro|teltto|torv|tuhk|tuomare|
  vaarno|vaatte|vaimo|vaippo|vanhimp|vars|varso|vaskiristikko|
  ((sota)?vaunu)|vuote)i)ne)(POSS-SFX?CLT-SFX?)|
#
# 53 N-COM: PL-COMT (V-front, -i-ne-PX):
  (((äit|härk|helte|imettäj|pä|keihä|köys|kyl|kymbaale|kypäre|
  ((meri|päällys|ratsu)?mieh)|miniö|päähine|päällikkö|perhe|pylvä|peitte|
  pä|palvelustehtäv|peitte|perhe|pylvä|ristikkokehyks|
  säädöks|sato|sisälmyks|teli|tyttär|((sota)?väk)|velj|ystävättär)i)ne)
  (POSS-SFX?CLT-SFX?)|
#
# 54 A: SG-NOM (V-back, positive):
  (nopea|viisaa|uusi)(POSS-SFX-V?CLT-SFX?)|
#
# 55 A: SG-NOM (V-front, positive):
  (pimeys|tyyni|tyyne|ylvää)(POSS-SFX?CLT-SFX?)|
#
# 56 A: SG-NOM (V-back, superlative; -in):
  ((mahtav)in)(CLT-SFX?)|
#
# 57 A: SG-NOM (V-front, superlative):
  ((läh|pien|väh)in)(CLT-SFX?)|
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
  ((kärkkää|epäpyhä|korkeastipyhä|köyhä|siivekkää|tyyne|ylvää)
  (n|POSS-SFX-V?))(CLT-SFX?)|
#
# 61 A: SG-GEN (V-front, -n: positive):
  (((köyh)i)en)(POSS-SFX?CLT-SFX?)|
#
# 62 A: PL-PTV (V-back, -i-a):
  (((kaltais)i)a)(POSS-SFX?CLT-SFX?)|
#
# 63 A: SG-PTV (V-back, superlative; -immais-ta):
  ((paras)ta)(POSS-SFX?CLT-SFX?)|
#
# 64 A: SG-PTV (V-front, superlative; -immäis-tä):
  (((pääll)immäis)tä)(POSS-SFX?CLT-SFX?)|
#
# 65 A: SG, ESS (V-back,-na):
  ((vanha)na)(POSS-SFX?CLT-SFX?)|
#
# 66 A: SG, ESS (V-front,-nä):
  ((pitkä)nä)(POSS-SFX?CLT-SFX?)|
#
# 67 A: SG, TRL (V-front & V-back, -ksi-/-kse-):
  ((hyvä|paha)kse)(POSS-SFX?CLT-SFX?)|
#
# 68 A: SG, ADE (V-back,-lla):
  ((ikivanha|liia)lla)(POSS-SFX?CLT-SFX?)|
#
# 69 A & PCPL-PRES: PL-ADE (V-back, superlative; -immi-i-lla):
  ((((kov|make|palav|polttav)imm)i)lla)(POSS-SFX?CLT-SFX?)|
#
# 70 A: PL-ADE (V-front, superlative; -imm-i-llä):
  ((((kiihke|kipe|väkev)imm)i)llä)(POSS-SFX?CLT-SFX?)|
#
# 71 A: SG, ELA (V-back, positive; -sta):
  ((ikivanha|liia)sta)(POSS-SFX?CLT-SFX?)|
#
# 72 A: SG, ELA (V-front, positive; -stä):
  ((tyhmä)stä)(POSS-SFX?CLT-SFX?)|
#
# 73 A: SG, ELA (V-front, comparative; -stä):
  (((väkevä)mmä)stä)(POSS-SFX?CLT-SFX?)|
#
# 74 A: SG, ABL (V-back, comparative; -lta):
  (((pare)mma)lta)(POSS-SFX?CLT-SFX?)|
#
# 75 PRON:
#  (ainoa|ainoan|ainoata|
#  erään|
#  itse|itseään|itseltä|itsessä|itsestä|itsellä|itselle|itsekseen|
#  jostakin|
#  kaikki|kaikkineen|
#  kuka|ken|ketä|keitä|kellä|keltä|kelle|kehen|ketkään|
#  kenellä|keneltä|kenelle|kenessä|kenestä|
#  kokonaan|
#  kumpi|koska|kuinka|
#  mikä|mitä|minkä|miltä|mitenkä|mitkä|miksi|minä|mille|
#  monta|
#  minä|minun|sinua|hän|me|meitä|meille|meidän|
#  te|teitä|teille|teidän|he|heillä|heille|heitä|
#  mitään|missään|mistään|millään|milloin|milloinkaan|
#  muuan|muun|muiden|muusta|muuta|muutoin|
#  ne|näitä|niitä|noita|niiden|niinä|näin|
#  omaa|omalla|omissa|omista|
#  se|sen|sinä|sitä|siksi|siitä|siellä|silloin|sitten|sentähden|
#  tämä|tämän|tänä|tästä|tätä|tähän|täällä|
#  toista|toisessa|toisella|toisesta|toiselta|toiselle|
#  toisia|toisissa|toisilla|toisista|toisilta|toisille|
#  yhden|yhdellä|yhdeltä|yhdelle|yhdessä|yhdestä|yhtä|yksi)
#  (POSS-SFX?CLT-SFX?)|
#
# 76 NUM, NOM:
  ((neljäkymmentä|kolmekymmentä|kaksikymmentä|seitsemänkymmentä|
  kahdeksankymmentä|tuhat)?(viisi|kuusi))(CLT-SFX?)|
#
# 77 NUM, PTV:
  ((yh)tä)(CLT-SFX?)|
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
# 81 V: INF-I, NOM (V-front, -ä, -tä, -dä, -lä, -nä, -n-, -rä):  
  (nähdä|päästä|syödä)(POSS-SFX-V?CLT-SFX?)|
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
  ((eksyttää|estää|etsiä|häväistä|hävittää|hyökätä|ilmestyä|itkeä|
  kääntää|kärsiä|käydä|keksiä|keventää|lähestyä|lähettää|lähteä|
  lämmitellä|mennä|nähdä|näyttää|niellä|päästä|peittää|pitää|
  pyhittää|pystyttää|pyydystää|pyytää|säästää|säilyttää|siirtää|
  syöstä|syöttää|täyttää|tehdä|työntää|tyydyttää|välttää|vetää|
  viedä|viihdytellä|ymmärtää|yöpyä)kse)(POSS-SFX?CLT-SFX?)|
#
# 84 V: INF-II, INE (V-back, -e-ssa):
  (((aiko|ajae|alenta|alotta|aja|ano|anta|asetta|astu|asu|hallit|hukku|
  huomat|istu|joutu|julista|kanta|katsell|katsahta|kehu|kemuill|
  keskustell|kiivaill|kirjoitta|kiroill|kolkutta|kulki|kuoll|kuull|
  kuunnell|((läsnä)?oll)|luki|mata|matkusta|muista|odotta|opetta|otta|paastot|
  paet|paimenta|painiskell|palat|palvell|pelasta|puhalta|puhdista|
  puhu|puhutell|puolusta|puolustautu|purjehti|rakenta|ratsasta|
  riemuit|rukoill|ruvet|saatta|salli|sano|seiso|sisusta|siunat|
  souta|suistu|surmat|taistell|tarkasta|tarkat|tavat|todista|toimi|
  toimitta|tuhot|tull|tunti|tuomit|tutkistell|tuod|uhrat|vaelta|
  vahvista|valitta|vitkastell)e)ssa)(POSS-SFX?CLT-SFX?)|
#
# 85 V: INF-II, INE (V-front, -e-ssä):
  (((elä|etsi|hävittä|herät|ilmesty|kääntelehti|käänty|kärsi|käski|kävell|
  käyd|käyttä|kierrell|kiertä|koot|kylvä|lähesty|lähettä|lähti|
  läsnäoll|menn|menetell|nähd|odotta|päästä|peljät|piirittä|pitä|pyrki|
  pyytä|rientä|riidell|saapu|siunat|synnyttä|syöd|täyttä|tehd|tull|
  uhrat|usko|vaelta|vied|yrittä)e)ssä)(POSS-SFX?CLT-SFX?)|
#
# 86 V: INF-III, SG-PTV (V-back, -ma-a):  
  (((huo|juo|karkoitta|kuule|perusta|raatele|saa|sekoitta|
  tahto)ma)a)(POSS-SFX?CLT-SFX?)|
#
# 87 V: INF-III, SG-PTV (V-front, -mä-ä):  
  (((syö|teke|tietä)mä)ä)(POSS-SFX?CLT-SFX?)|
#
# 88 V: INF-III, PL-PTV (V-back, -ma-i-a):  
  ((((kaata)m)i)a)(POSS-SFX?CLT-SFX?)|
#
#! 89 V: INF-III, PL-PTV (V-front, -mä-i-ä):  
#
# 90 V: INF-III, SG-ADE (V-back, -ma-lla): 
  (((hake|karkoitta|kuule|lupaa|raatele|saa|sekoitta)ma)lla)
  (POSS-SFX?CLT-SFX?)|
#
# 91 V: INF-III, PL-ABL (V-back, -m-i-lta): 
  ((((kukista)m)i)lta)(POSS-SFX-V?CLT-SFX?)|

# 92 V: INF-III, PL-GEN (V-front, -mä-n):  
  (((syö)mä)(n|(POSS-SFX?)))(CLT-SFX?)|
#
# 93 V: INF-III, SG-ELA (V-front, -mä-stä):
  (((käyttä|teke)mä)stä)(POSS-SFX?CLT-SFX?)|
#
# 94 V: INF-III, ABE (V-back, -ma-tta):
  (((huomaa|tahto)ma)tta)(POSS-SFX?CLT-SFX?)|
#
# 95 V: INF-III, ABE (V-front, -mä-ttä):
  (((tietä)mä)ttä)(POSS-SFX?CLT-SFX?)|
#
# 96 V: INF-III, INES (V-front, -ma-ssa):
  (((ole)ma)ssa)(CLT-SFX?)|
# 
# 97 V: INF-IV, SG-PTV (V-back, -minen: -mista-ta): 
  (((halveksu|heikontu|kaatu|kiehu|kirkastu|kovene|kukistu|
  nouse|omista|poisotta|puhkeamis|tule|vahvistu)mis)ta)
  (POSS-SFX?CLT-SFX?)|
#
# 98 V: INF-IV, SG-PTV (V-front, -minen: -mista-tä): 
  (((häviä|hyöty|ilmesty|iske|kiertä|leviä|leviä|siirty|teke|
  vähene|väisty|vihkiyty)mis)tä)
  (POSS-SFX?CLT-SFX?)|
#
# 99 V, INF-V. ADE (V-back, -maisilla):
  (((alka|kuole|laske|pakahtu|sano|tule|uppoa)maisi)lla)
  (POSS-SFX?CLT-SFX?)|
#
# 100 V, INF-V. ADE (V-front, -mäisillä):
  (((käske|lähte|särky|synnyttä)mäisi)llä)
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
# 106 V-PCPL-I, PRES: PL-ESS (V-front,-v-i-nä):
  ((((tietä)v)i)nä)
  (POSS-SFX?CLT-SFX?)|
#
# 107 V-PCL-I, PRES: PL-INE (V-back, -v-i-ssa):
  ((((annetta)v)i)ssa)
  (POSS-SFX?CLT-SFX?)|
#  
# 108 V-PCL-I, PRES: PL-INE (V-front, -v-i-stä):
  ((((näky)v)i)stä)
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
  (((eksy|((jäljelle)?jää)|käy|kokoontu|lähettä|lähte|levin|
  liitty|men|näh|pitä|pysy|siirty|teh)nee)(n|(POSS-SFX)))(CLT-SFX?)|
  (((jylis|pääs)see)(n|(POSS-SFX)))(CLT-SFX?)|
#
# 111 V-ACT, PCPL-II, PAST-PL-NOM (V-back, -(l|n|r|s)ut, -(l|n|r|s)ee-):
  (((joutu|julista)nee)t)(POSS-SFX?CLT-SFX?)|
#  
# 112 V-ACT, PCPL-II, PAST-SG-NOM (V-front, -(l|n|r|s)yt, -(l|n|r|s)ee-):
  ((hyljän|men)nyt)(CLT-SFX?)|
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
# 115 V-PASS, PCPL-II, PAST-SG-PTV (V-front, -tty-, -ä):
  (((herä|kääri|käske|lähde|levite|löyde|mieti|pääte|täyte|vede|viivy)tty)ä)
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
  (((ilmesty|kärsi|mielisty|synty|väsy|täytty)nee)n)
  (POSS-SFX?CLT-SFX?)|
#
# 119 V-PASS, PCPL-II, PAST-SG-PTV (V-front, -ty-, -ä):
  (((käy|näh|men|pääs|pes|syn|teh)ty)ä)(POSS-SFX?CLT-SFX?)|
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
  (jää|hyökkää|kestää|lepää|näkee|menestyy|pelkää|riittää|ryntää|
  tietää|ymmärtää)(CLT-SFX?)|
#
# 123 V, IND, ACT-PRES (V-front):
  ((herää|hylkää|hyökkää|jää|kestä|lepää|menesty|myy|näe|pelkää|
  pysy|pyyhi|riitää|ryntää|syö|tiedä|tietä|vihi|ymmärrä|ymmärtä)
  (n|t|mme|tte|vät))(CLT-SFX?)|
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
  (((kääns|käänty|lähd|löys|pääs|pyys|sääs|synny|ties|vähen)i)
  ((|t|mme|tte|vät)|(CLT-SFX?)))(CLT-SFX?)|
#	
# 127 V, ACT-IND, COND (V-back, -isi-): 
  (((anta|maka|ol|pelasta|sano|tahto|tul|ulottu|usko)isi)
  ((n|t|mme|tte|vat)|(CLT-SFX?)))(CLT-SFX?)|
#
# 128 V, ACT-IND, COND (V-front, -isi-): 
  (((keskeyty|pääs|sö)isi)((n|t|mme|tte|vät)|(CLT-SFX?)))
  (CLT-SFX?)|
#
# 130 V, ACT-IND, POT (V-back, -le-, -ne-, -re-, -se-): 
  ((((saa)ne)e)|
  (((tul)le)e))(CLT-SFX?)|
#
# 131 V, ACT-IND, POT (V-front, -le-, -ne-, -re-, -se-): 
  (((lie)ne)vät)(CLT-SFX?)|
#
# 132 V-EXT:
  ((ole(n|t|mme|tte))|
  (olla|on|ovat)|
  (ol(i|isi))((n|t|mme|tte|vat)|(CLT-SFX?)))(CLT-SFX?)|
#
# 133 V-NEG:
  (en|et|ei|emme|ette|eivät)(CLT-SFX?)|
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
  ((pitää|piti|täytyy|täytyi|mahtaa|mahtoi)|
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
# 140 V, ACT-IMP, 1PL (-kää):
  (((äl|eristä|etsi|hävittä|heittä|jättä|käy|kieltä|kiittä|kysy|lähettä|
  lähte|lyö|menetel|men|myy|peljät|pitä|pyrki|pysy|ryöstä|ryypät|rientä|siirtä|
  siirty|syö|täyttä|teh|tyyty|uudista|väijy|viettä|ympäröi|yöpy)kää)mme)
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
  ympärileikatta)koon)(POSS-SFX-V?CLT-SFX?)|
#
# 142 V-ACT, IMP-3SG (V-front, -köön): 
  ((äl|elä|elpy|etsi|hävit|heittä|herättä|hyljät|hyväksy|jää|
  jännittä|jättä|kasva|kääntä|käänty|käske|käy|käyttä|kestä|kieltä|
  kiittä|kivittä|kysy|lähesty|lähettä|lähte|lävistä|leikel|
  leiriyty|levit|liitty|lisäänty|lisät|lyö|menetel|men|miehittä|
  myy|näh|näyttäyty|nylke|pääs|päästä|päätty|peittä|peljät|peseyty|pes|
  pidätty|pyhitty|pyrki|pysähty|pysy|reväis|ryöstä|säily|säilyttä|
  selittä|siirty|sivel|sylke|syö|syös|syötä|sytyttä|täyttä|täytty|
  teh|väisty|vetä|vie|vihkiyty|vilis|vyöttä|yhty|ylistä|yllättä)köön)
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
  vanno|varuste|vihmo|vuodate|ympärileikkau)tta)koon)(CLT-SFX?)|
#
# 145 V-IMP: PASS (V-front, -tä-köön): 
  (((menetel|menet|myy|pes|pi|pyhit|riit|teh|tie|vään|vie|ympäröi)tä)köön)
  (CLT-SFX?)|
#
# 146 V-IMP: PASS (V-front, -ttä-köön): 
  (((etsi|hävite|hävi|heite|käyte|kehyste|kiinnite|kiite|kivite|
  lähete|levenne|määrä|myönne|nimite|pääste|peljä|pide|piste|pyhite|
  pyyhi|revi|ryöste|säilyte|täyte|vähenne|vie|vihi|yhdiste)ttä)köön)
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
  ylenkatso|ympärileika)ta)an)(CLT-SFX?)|
#
# 148 V: PASS-PRES (V-front, -tä-än): 
  (((eläte|esite|este|etsi|hälyte|häväis|hävite|heite|heräte|hylji|hyökä|
  hyvite|itke|jännite|jäte|käänne|kääri|käyte|keite|ke|kielle|kiinnite|
  kiiste|kiite|kylve|kynne|kysy|kytke|lähete|läviste|levite|liite|lisä|
  löyde|määrä|lyhenne|niite|pääste|pää|peljä|peri|pes|pete|pide|pies|
  piirite|pyhite|pysyte|pyydyste|pyyhkäis|reväis|revi|riiste|ryöste|sääste|
  säikähyte|sälyte|särje|siirre|sylje|synnyte|syös|sysä|täyte|tervehdi|tiede|
  tyhjenne|työnne|väänne|vääriste|välte|vede|viete|vihelle|virite|
  ylenne|yliste)tä)än)(CLT-SFX?)|
#
# 149 V: PASS-PRES (V-back, -da-an): 
  (((juo|luo|saa|suo|tuo|voi)da)an)(CLT-SFX?)|
#
# 150 V: PASS-PRES (V-front, -dä-än): 
  (((käy|lyö|myy|näh|sinetöi|syö|teh|vie)dä)än)(CLT-SFX?)|
#
# 151 V, PASS-PRES (V-back, -la-an): 
  (((ennustel|huhuil|huokail|koetel|kuul|kuulustel|lankeil|luul|
  nuhdel|palvel|pudistel|raadel|tavoitel|tul|valhetel|
  varjel|voidel)la)an)(CLT-SFX?)|
#
# 152 V: PASS-PRES (V-front, -lä-än): 
  (((etsiskel|hyväil|riidel|viljel|tähyil|viskel)lä)än)(CLT-SFX?)|
#
# 153 V, PASS-PRES (V-back, -na-an): 
  (((pan)na)an)(CLT-SFX?)|
#  
# 154 V: PASS-PRES (V-front, -nä-än): 
  (((men)nä)än)(CLT-SFX?)|
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
  ((((häväis|käy|likistel|lyö|men|myy|pääs|pies|reväis|sinetöi|
  syös|teh|viet|ympäröi)t)i)in)(CLT-SFX?)|
#
# 159 V: PASS-PAST (V-back, -tt-i-in):
  ((((ahdiste|aje|ammu|anne|asete|ava|erote|hae|hajaannu|hajote|
  hanki|hauda|havai|hukute|huoma|huude|huuhdo|ilmoite|jae|
  juliste|juote|kanne|karkoite|kaste|kasvate|katsaste|kavalle|
  kerro|kiedo|kirjoite|kohote|koo|kokoonnu|koriste|kukiste|kulje|
  kuljete|kuolete|kutsu|kuulute|laka|lanniste|laske|lausu|
  ((ympäri)?leika)|lue|luovute|maini|muonite|murre|murska|muute|
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
  ((((eläte|eriste|etsi|hävite|heite|heräte|hirte|hylji|hyljä|itke|
  järjeste|jäte|käske|käyte|kerä|kiinnite|kivite|kylve|kynne|kysy|
  lähesty|lähete|levite|liite|lisä|löyde|määrä|merki|näyte|nimite|
  nöyryyte|päällyste|pääste|pääte|peite|pete|pide|piirite|piirre|
  pyhite|pystyte|pyyde|pyydyste|revi|ryöste|sääde|sääste|säilyte|
  siirre|syrjäyte|syyte|täyte|teete|vede|vierite|viete|vihi|virite|
  yhdiste|yliste|ymmärre)tt)i)in)(CLT-SFX?)|
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
  (((elätettä|hävitettä|heitettä|jätettä|lyötä|nähtä|näytettä|
  päästettä|peljättä|pidettä|piirrettä|pyhitettä|pyyhittä|riistettä|
  täytettä|tehtä|tiedettä|vihittä)isi)in)(CLT-SFX?)|
#  
# VERB: Verbs homonymous with illative/partitive forms of nouns:
# haudata: hautaan, määrätä: määrään.
#
# VERB-NOUNS: 
#  ((minä (teille) (määrään|hautaan)|
# 
# Verbs occurring with homonymous partitive/illative forms:
# The homonymous illative/partitive nouns are found with the verb olla, 
# the negative verbs ei, älä, and with the inflected forms of the verbs 
# in the list VERB-CLSD. With those verbs, the clause/sentence which is 
# separated from the text with the strong punctuation marks
#  (.|!|?) is [-CLSD] and the nominal argument is in the partitive form.
# 
# OBS: onko tämän säännön yhteyteen liitettävä tietoa toisen argumentin
# morfologiasta?
# 163 VERB-CLSD: 
  (antaa|armahtaa|asettaa|astua|etsiä|haluta|hävittää|heiluttaa|
  herätä|herjata|huutaa|hylätä|jatkaa|jättää|julmistua|juosta|kääntää|
  kaatua|kallistaa|kalvaa|kantaa|karvastella|kätkeä|katsoa|käyttää|kieltää|
  kiinnittää|kiittää|kiroilla|kiusata|kohdata|korjata|korvata|kumartaa|
  kunnioittaa|kuulla|kyllästyä|kylvää|kyntää|lähestyä|lepyttää|lisätä|
  loukata|lujittaa|luottaa|moittia|muistella|muuttaa|nähdä|niskoitella|
  notkistaa|odottaa|onnitella|ontua|ottaa|päästää|paljastaa|palvella|panna|
  parantaa|peljätä|pitää|polkea|pukeutua|rakastaa|rasittaa|rikkoa|rukoilla|
  satuttaa|seurata|siunata|sortaa|suorittaa|surmata|syödä|tarkastaa|
  tarttua|tehdä|teroituttaa|todistaa|toimittaa|tuhota|tulla|tuntea|tyydyttää|
  ulottaa|unohtaa|uskoa|vahvistaa|varjella|vartioida|vihastua|vihata|ylistää|
  luottaa|osata|uskoa)|
#
# Particles:
# Adpositions listed in the file fin.spec which belong to the groups A and B:
# 164 DIR-IN-POP-A: 
  (kohtaan|silmiin|sisään|sisälle|sydämee)(POSS-SFX-V?CLT-SFX?)|
#
# 165 DIR-IN-POP-B:   
  (väliin|välille|perälle|sekaan|sekaa)(POSS-SFX-V?CLT-SFX?)|
#
#   (juureen|ääreen|eteen|mukaan|
#
# 166 Adpositions which produce ambiguous structures:
#  (alla|alta|alle|edellä|edeltä|edelle|edessä|edestä|eteen|
#  avuksi|avukse|
#  hallussa|hallusta|
#  huomassa|huomasta|huostassa|huostasta|
#  hyväkse|
#  jälkeen|
#  joukossa|joukosta|
#  kaltainen|kaltaisia|kaltaista|kaltaiselle|
#  kaltaisekse|kaltaisikse|kaltaisista|kaltaisille|
#  kanssa|kautta|
#  keskellä|keskeltä|keskelle|keskessä|keskestä|keskuudessa|keskuudesta|
#  kimpussa|kimpusta|kintereillä|kintereiltä|
#  kohdalla|kohdalta|kohdalle|kohdassa|kohdasta|
#  kupeella|kupeelta|
#  läheisyydessä|läheisyydestä|lähellä|lähelle|
#  laista|laiselle|
#  luona|luota|luotaan|luokse|
#  muassa|mukana|mukaan|
#  ((alku|loppu)?päällä|päältä|päälle)|
#  ((ala|ylä)?puolella)|((ala|ylä)?puolelta)|puolesta|puolestaan|puolelle|
#  rinnalla|rinnalta|rinnalle|
#  seassa|seasta|seastaan|
#  seurassa|seurasta|sijalla|tähte|
#  silmiä|silmissä|silmistä|sisässä|sisästä|
#  sivulla|sivulta|sivussa|sivusta|
#  takana|takaa|
#  toimesta|toimestaan|
#  tykönä|tyköä|
#  vallassa|vallasta|
#  välillä|väliltä|
#  vertaista|vertaisesta|seasta|sijasta|
#  vierellä|vierelle|vieressä|vierestä|
#  yllä|yltä|ylle|
#  ympärillä|ympäriltä|ympärille)
#  (POSS-SFX?CLT-SFX?)|
#
# Ambiguities with the following postpositions and illative/partitive
# forms: (asti|ennen|kesken|kohtaan|likellä|mukaan|vaille|vastaan)
#
#POP-AMB: 
#  ((ennen(kuolemaansa))|
#  (((herraa(ni|nsa))|(jumalaa(mme|ni|nne))|kunigasta|teitä)
#  vastaan)|
#  (kesken(ikääni))|
#  (palkkaansa(vaille))|
#  (valtaansa
#  (niitä)kohtaan)|
#  ((sen) mukaan)|
#  (likellä(Herraa meidän)Jumalaamme)|
#  (mukaani(en)miekkaani))|
#
# 167 Adverbs, conjunctions:
#  (((entis|hallitus)aikaan)|aikoinaan|ainiaan|ainoastaan|alkuaan|
#  alunpitäen|(ammoll(aan|een))|
#  edelleen|ehyeltään|
#  ensin|ensinkään|puoleen|
#  enintään|ennestään|entisellään|entiselleen|entisaikaan|entuudestaan|
#  erikseen|erillään|erillä|erilleen|
#  hajallaan|hajalleen|hamaan|hetkelleen|hiljalleen|
#  istualleen|jäljestäpäin|
#  (jäljestäpäin(kään|kin))|jälleen|järjestään|johan|kaikkiaan|
#  kauttaaltaan|keskenään|kiinni|(kuiten(kaan|kin))|kun|kunhan|kyllä|kyllää|
#  kyllikseen|läheisyydessä|lain|lainkaan|läpeensä|leikillä|levällään|
#  liian|luonnostaan|
#  myöhään|myös|niin|niini|nimenomaan|nyt|ollenkaan|omakse|omikse|
#  parhaimmillaan|(parhaimmillaan(kin|kaan))|pitkänään|
#  selkoselällään|selälleen|
#  senjälkeen|sikseen|sisään|(suin(kaan|kin))|suunniltaan|
#  tahansa|taakseen|takaa|tänään|tänne|tarkalleen|
#  tästälähin|täydelleen|tarkkaan|toistamiseen|
#  (tieten(kin|kään))|toisekseen|tosiaan|tosiaan|tosiaankaan|tosiaankin|
#  turhaan|tyynni|umpimähkään|uudestaan|vaan|valloilleen|varuillaan|
#  vastaan|vastaamme|vastaammekin|vastaatte|vastaattekin|
#  vähää|vaiti|vaitikaan|valtoinaan|vähän|(varmaan(kaan|kin))|
#  varsin|(varsin(kaan|kin))|vastaan|vielä|(vielä(kään|kin))|vuorostaan|
#  yhteensä|yhtenään|yksikseen|yksinään|yksistään|yleensä|
#  yltyleensä|ylleen|jos|sela)(POSS-SFX?CLT-SFX?)|
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
#1 el[ämääns<ä>]
#2 el[ämääns<ä>]
  (eikä kukaan synnillänsä vahvista elämäänsä)|
  (joka elämäänsä rakastaa)|
  (mutta joka vihaa elämäänsä)|
#1 el[ämääns<ä>kin]
  (vieläpä omaa elämäänsäkin)|
#1 etsikk[oaika<a>si]
  (ettet etsikkoaikaasi tuntenut)|
#1 h[aava<a>si]
  (sinun haavaasi ei paranneta)|
#1 h[auta<an>]
  (että minä hautaan)|
  (tietään hänen hautaansa)|
#1 h[ärkä<ä>]nsä
  (sapattina päästä härkäänsä)|
#5 h[erra<a>mme]
#3 h[erra<a>mme]
# (voi herraamme)|
  (onnittelemaan meidän herraamme)|
  (meidän kirkastettuun herraamme)|
  (voi herraamme)|
# 8 h[erra<a>ni]
  (siunannut minun herraani)|
  (jotka seuraavat herraani)|
  (satuta kättäni herraani)|
  (kiroilla herraani)|
  (nostivat kätensä herraani)|
  (heimosta tullut tänne herraani)|
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
  (näihin kahteen hoviherraansa)|
#1 i[kä<ä>ni]
  (kesken ikääni)|
#2 i[kääns<ä>]
  (lisätä ikäänsä kyynäränkään)|
#2 j[alka<a>si]
#5 j[alka<a>si]
  (jalkaasi kiveen loukkaisi)|
  (etkä loukkaa jalkaasi)|
  (hän varjelee sinun jalkaasi)|
  (juokse jalkaasi)|
  (polje jalkaasi ja sano)|
  (ettet jalkaasi kiveen loukkaisi)|
#2 jum[ala<a>mme]
#1 jum[ala<a>mme]
  (rukoilimme jumalaamme)|
  (pois jumalaamme)|
  ((meidään) jumalaamme)|
#10 jum[ala<a>ni]
#4 jum[ala<a>ni]
  (minun jumalaani)|
  (jumalaani minä)|
  (avuksi jumalaani)|
  (odottaessani jumalaani)|
  (kiitän jumalaani)|
  (jumalaani)|
#31 jum[ala<a>nne]
  (teidän jumalaanne)|
  (kieltäisi jumalaanne)|
  (jumalaanne)|
#  (rukoilkaa herraa, jumalaanne)|(palvelkaa herraa, jumalaanne)|
#  (jumalaanne, vastaan)|
#  (jumalaanne, sekä te että kuningas)|
#(etsimään herraa, jumalaanne)|
#  (kiittäkää herraa, jumalaanne)|(herraa, jumalaanne, vastaan)|
#  (palvelkaa nyt herraa, jumalaanne)|
#  (kiittäkää herraa, jumalaanne)|
  (tähtijumalaanne)|
#7 jum[ala<a>si]
  (sinun jumalaasi)|
#  (älä kiusaa herraa, sinun jumalaasi)|
# kansansa
  (kansaansa)|
#1 kanssapalvel[ija<a>si]
  (armahtaa kanssapalvelijaasi)|
# kaulaanne
  (saa kaulaanne)|
#1 k[aulaans<a>]
  (kaulaansa baabelin)|
#1 kärs[imä<ä>nsä]
  (muistele kärsimäänsä)|
#1 kuokka[<a>nsa]
  (kuokksa)|
  (kirvestänsä)|
#4 kuol[emaans<a>]
  (ennen kuolemaansa)|
  (hänen kuolemaansa)|
#1 lepos[ijaans<a>]
  (älä hävitä hänen leposijaansa)|
# lähettäjäänsä
  (lähettäjäänsä suurempi)|
#1 l[iha<a>mme]
  (meidän omaa lihaamme)|
#4 l[iha<a>ni]
  (luutani ja lihaani)|
  (syömään minun lihaani)|
#1 l[iha<a>nne]
  (luutanne ja lihaanne)|
#2 l[ihaans<a>
  ((kalvaa|vihannut|syömään) omaa lihaansa)|
#3 l[iha<a>si]
  (sinun luutasi ja lihaasi)|
  (on omaa lihaasi)|
#1 l[onkka<a>nsa]
  (ontui lonkkaansa)|
#2 l[uoja<a>nsa]
  (herjaa hänen luojaansa)|
#1 m[atkaans<a>
  (jatkoi matkaansa iloiten)|
#3 m[äärä<än>], verbs;
#1 m[äärä<ä>nne]
  (niin minä määrään)|
  (mitä minä teille määrään)|
  (minä määrään miekan omiksi)|
  (tähänastista määräänne)|
#1 m[aja<a>si]
  (lähesty sinun majaasi)|
#2 m[atka<a>nne]
  (jatkatte matkaanne)|
  (voitte jatkaa matkaanne)|
#4 m[atkaans<a>]
  (ja menivät matkaansa)|
  (jatkoivat matkaansa)|
  (kääntyivät jatkamaan matkaansa)|
#2 m[iekka<a>ni]
  (en miekkaani enkä)|
  (heilutan miekkaani)|
#1 m[iekka<a>nsa]
  (ei paljastanut miekkaansa)|
#2 n[älkääns<ä>]
  (taivaasta heidän nälkäänsä)|
  (tyydyttääkseen nälkäänsä)|
  (nälkäänsä tyydytä)|
#1 n[iskaans<a>]
  (eivät notkistaneet niskaansa)|
#1 p[aikka<a>si]
  (älä jätä paikkaasi)|
#2 p[alkka<a>ni]
  (katsomaan minun palkkaani)|
  (muuttanut palkkaani)|
#1 palvelusteht[ävä<ä>nsä]
  (tekemään palvelustehtäväänsä)|
#2 p[alkka<a>nsa]
  (ei jää palkkaansa vaille)|
#1 perhek[unta<a>sa]
  (hoitamaan omaa perhekuntaans)|
#4 perint[öosaans<a>]
  (palasivat perintöosaansa)|
  ((julmistui|kyllästyi) perintöosaansa)|
#  (ja israelia, perintöosaansa)|
  (eikä perintöosaansa heitä)|
  (hänen perintöosaansa)|
#3 perint[öosa<a>si]
  (kansaasi ja perintöosaasi)|
  (perintöosaasi häväistäväksi)|
  (perintöosaasi he rasittavat)|
#1 p[esä<ä>si]
  (pidät pesääsi setripuissa)|
#2 r[inta<a>ni]
  (voi minun rintaani)|
#1 s[elkä<ä>ni]
  (ovat minun selkääni kyntäneet)|
#1 s[elkä<ä>si]
  (äläkä käännä selkääsi sille)|
#1 s[ilmä<ä>ni]
  (kiinnitä silmääni siihen)|
#1 tähtijum[ala<a>nne]
#1 tek[emääns<ä>]
  (kanssa tekemäänsä liittoa)|
#2 v[altaans<a>]
#3 v[altaans<a>]
  ((lujittamaan|ulottamaan) valtaansa)|
  (käytä totuuteen valtaansa maassa)|
  (käyttävät valtaansa niitä kohtaan)|
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
  (korjaa tyhjäksi viinitarhaasi)|
  (äläkä leikkaa viinitarhaasi)|
#  v[irka<a>mme>]
#  (ettei virkaamme moitittaisi)|
#11 v[irkaans<a>]
  (toimittaessaan virkaansa)|
  (ilmestysmajaan toimittamaan virkaansa)|
  (astua toimittamaan virkaansa)|
  (he toimittivat virkaansa)|
  (käyvät toimittamaan virkaansa)|
  (toimittamaan virkaansa)|
  (toimittavat virkaansa meidän)|
  (virkaansa toimittavat papit)|
  (joissa toimittavat virkaansa)|
  (toimittaessaan virkaansa)|
#1 v[oima<a>si.
  (älä anna voimaasi naisille)|
#1 v[irka<a>ni>]
  (minä virkaani kunniassa)|
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
  (elle(n|t|i|mme|tte|ivät))|
  (jolle(n|t|i|mme|tte|ivat))|
#
# DIR-ON-POP-C: 
  (häntään|juureen|kohtaan|kupeeseen|nenään|nokkaan|perään|
  pieleen|pohjaan|päähän|suuhun|syrjään|varteen|vasten)|
  (alle|päälle|huipulle|huipuille|partaalle|perälle|pohjalle|reunalle|
  häntää|juuree|kupeesee|nenää|nokkaa|pohjaa|reunaa)(POSS-SFX?CLT-SFX?)|
#
# DIR-ON-POP-D: 
  (eteen|jälkeen|kohdalle|liki|luo|oheen|pieleen|poskeen|sivuun|
  niskaan|perään|päähän|viereen|suuhun|syrjään|
  äärelle|edelle|edustalle|hännille|jäljille|juurelle|juurille|
  kannoille|kintereille|kupeelle|likelle|lähelle|luokse|rinnalle|
  sivulle|sivuille|suulle|taakse|tykö|vierelle|
  yläpuolelle|etee|niskaa|päähä|syrjää|vieree)(POSS-SFX?CLT-SFX?)|
#
  (edelleen|toisiin|toisiinsa|uuni|äänensä|äänen|ääneni|äänesi|
  ääneensä|ääni|ääne|äänesihän|äänenkin|äänikin|äänenhän))
# "ääne" poistettu useasta ryhmästä. Ks. alkuperäinen EXCL-tiedosto.
#
