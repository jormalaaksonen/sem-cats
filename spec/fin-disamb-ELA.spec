#
#Pirkko Suihkonen , 2016 and 2017
#Copyright: Pirkko Suihkonen
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
  jokais|mois|semmois|tois)ta)(POSS-SFX?CLT-SFX?)|
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
  teurasta|todista|toista|tunnusta|uudista|vahvista|valista|valjasta|
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
  teurasta|todista|toista|tunnusta|uudista|vahvista|valista|valjasta|
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
  teurasta|todista|toista|tunnusta|uudista|vahvista|valista|valjasta|
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
  (vasta|vastaan|ainoastaan|nousemistaan|uudestaan)(CLT-SFX?)|
#
# Adverbs (V-front):
  (ennest��n|j�rjest��n|siirtymist��n|v�henemist��n|v�istymist��n|
  yksist��n)(CLT-SFX?))
#
