#
#Pirkko Suihkonen , 2016 and 2017
#Copyright: Pirkko Suihkonen
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
ELA-EXCL: ^((artahsastan|bistan|nehustan|parmastan)|
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
  jokais|mois|semmois|tois)ta)(POSS-SFX?CLT-SFX?)|
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
  yksistään)(CLT-SFX?))
#
