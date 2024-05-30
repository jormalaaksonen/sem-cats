#Pirkko Suihkonen (Copyright), 2016 and 2017
#
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
  (((drusilla|priskilla|silla|ulla)|
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
  (kyllä|kyllähän|kylläänsä|kylläänne|kyllääsi|kylläsi|kylläänsähän|
  todella|todellakin|
  vähälläpä|tahallamme|tahallanne)|
#
# Adpositions taken into account in the file fin.spec:
# ON-POP|PRP-C: 
  (vasten|alla|päällä|partaalla|partailla|pinnalla|
  pohjalla|pohjilla|reunassa|reunoissa|reunalla|reunoilla)
  (POSS-SFX?CLT-SFX?)|
#
#  ON-PRP|POP-D: 
#ON-POP-D: (edessä|edustalla|ohessa|ääressä)|
  (hännillä|jäljessä|juurella|juurilla|kannoilla|kintereillä|kohdalla|
  keskikohdalla|likellä|lähellä|luona|niskassa|paikalla|
  perässä|rinnalla|sivussa|sivuissa|sivulla|sivuilla|suulla|syrjässä|
  takana|välillä|vastapäätä|vieressä|yllä)(POSS-SFX?CLT-SFX?)|
#
#
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
  teurasta|todista|toista|tunnusta|uudista|vahvista|valista|valjasta|
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
  teurasta|todista|toista|tunnusta|uudista|vahvista|valista|valjasta|
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
  teurasta|todista|toista|tunnusta|uudista|vahvista|valista|valjasta|
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
  (vasta|vastaan|ainoastaan|nousemistaan|uudestaan)(CLT-SFX?)|
#
# Adverbs (V-front):
  (ennestään|järjestään|siirtymistään|vähenemistään|väistymistään|
  yksistään)(CLT-SFX?)|
#
#  (VERBS-SOM (aasi|aasisi|aasinsa|aasien|ääni|äänen|ihon|ihanan|uusi|
#  osata|uskoa)))
#
#
DE-ON-EXCL: ^((ilta|kulta|multa|((kuningas|tuomio|väki)?valta))
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
  (aasia|aasian|ääni|äänen|ääneen|uusi|uuteen)|
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
  (takaa))(POSS-SFX?CLT-SFX?))|
#
# NEG-MOD-INF
#
# Adpositions containing the strings -lta/-ltä, but which do not belong to the groups C and D:
#  (((puo(le)?)|suunna|taho|varre|varsi)lta)(POSS-SFX?CLT-SFX-B?)|
#  ((keske|peri|sisä|väli|ympäri)ltä)(POSS-SFX?CLT-SFX-F?))
#
  (edustalle|lopussa)|
#
