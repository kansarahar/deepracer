import numpy as np

# --------------------- Optimization Results --------------------- #

track_name = 'cumulo'
race_line = np.array([[-2.3074580170214176, -5.338676273822784], [-2.3801075220108032, -5.3720526695251465], [-2.5168585777282715, -5.434880495071411], [-2.6536084413528442, -5.497710466384888], [-2.7903579473495483, -5.560542583465576], [-2.927107095718384, -5.62337589263916], [-3.0638540983200073, -5.686211824417114], [-3.200601100921631, -5.749051094055176], [-3.3373450040817256, -5.811892986297607], [-3.474087953567505, -5.874738931655884], [-3.610828995704651, -5.937588453292847], [-3.7475684881210327, -6.0004425048828125], [-3.884305953979492, -6.063300132751465], [-4.021041393280029, -6.126162528991699], [-4.1577736139297485, -6.189031600952148], [-4.29450249671936, -6.251907587051392], [-4.431227922439575, -6.314790487289429], [-4.567950963973999, -6.377681016921997], [-4.704670429229736, -6.440577983856201], [-4.841385126113892, -6.503485441207886], [-4.978002757303123, -6.566148605899162], [-5.11427550481023, -6.627815059002638], [-5.249980550510279, -6.687762513237398], [-5.384905201978735, -6.7452723127918635], [-5.518857034776682, -6.7996639551282385], [-5.651668739468615, -6.850319761228411], [-5.783219986752509, -6.896768919164228], [-5.913375777908456, -6.938490109034212], [-6.042010892027785, -6.974996140436501], [-6.169018351002261, -7.005868963939731], [-6.294333706591838, -7.0308495435801674], [-6.417997127982229, -7.050058302689546], [-6.539930388957325, -7.063215207306881], [-6.660052400335395, -7.0700432634121135], [-6.778153712444935, -7.069835476609265], [-6.89390669509487, -7.06150889463221], [-7.006858359878763, -7.043621163091298], [-7.116512982722817, -7.014716441145659], [-7.221658897200882, -6.971373906954651], [-7.32305325458167, -6.9166810941170525], [-7.4211069525170235, -6.852356527473263], [-7.516094805693735, -6.7795736462674725], [-7.608179572060834, -6.699126805451115], [-7.697538159951984, -6.611804525569032], [-7.784228717153664, -6.518079335334212], [-7.868293442506583, -6.418405633878349], [-7.949770397644171, -6.3132598303663094], [-8.028697005667144, -6.203157166557696], [-8.105006251836599, -6.088494604379013], [-8.178732556363016, -5.9699137372303115], [-8.249810816286695, -5.847936819823575], [-8.318131767885166, -5.723075829169221], [-8.383526719346156, -5.595806391785727], [-8.445763254523523, -5.466559962232967], [-8.50454707966399, -5.33572287216397], [-8.559528069836542, -5.203638039833321], [-8.61030979612644, -5.070608055041734], [-8.65646249594807, -4.936899104246153], [-8.697540638755735, -4.802745270330096], [-8.733106819306226, -4.668352639356128], [-8.76275855688029, -4.533902714625039], [-8.786146572581629, -4.399555051961009], [-8.802962857936823, -4.265450657763173], [-8.81283007572387, -4.131721645351728], [-8.81548566301974, -3.9984867755189653], [-8.810793567456738, -3.8658490451724283], [-8.798736470018355, -3.7338937676388664], [-8.779417425901201, -3.6026862956254573], [-8.753062822474973, -3.472269571041003], [-8.720022012987796, -3.3426618957317524], [-8.680761714857438, -3.2138554036745304], [-8.635854627804942, -3.0858156240562664], [-8.585967278777495, -2.958481666546573], [-8.531830274012702, -2.831769711776717], [-8.473980930299813, -2.7056110156460758], [-8.412776918490664, -2.57994750093145], [-8.348202613462355, -2.4547297585665895], [-8.280064775100053, -2.329683634033058], [-8.215322167341338, -2.2034933443584013], [-8.154206680348826, -2.076447349182561], [-8.097043031540933, -1.9485490912829648], [-8.044298498645572, -1.8197651939164783], [-7.996464147991736, -1.6900640931969986], [-7.953817342721525, -1.5594598101765924], [-7.916752945803793, -1.4279508877108527], [-7.885656467123454, -1.295545710390178], [-7.861011138650828, -1.1622498734406692], [-7.843086810878234, -1.0281105798493821], [-7.8320066576870815, -0.8932001458098796], [-7.827763839064389, -0.7576076994158727], [-7.830224367446528, -0.6214330931136605], [-7.839130418287029, -0.4847809723397769], [-7.85410501579204, -0.34775505576350707], [-7.874656174695858, -0.21045298324648706], [-7.900183063584531, -0.07296201065997215], [-7.9300281633112135, 0.0646446361791625], [-7.963560449160948, 0.20231017948661928], [-8.000479412681628, 0.3399925306265391], [-8.040571835819412, 0.47765119288427943], [-8.083461537693157, 0.6152512932356005], [-8.128632317131565, 0.7511892837638419], [-8.170302999440477, 0.8868853407761322], [-8.207890989642982, 1.0222718645818705], [-8.240857533776893, 1.1572586410282866], [-8.268646092763099, 1.2917258338115611], [-8.290770954623486, 1.4255320273349033], [-8.306752129691468, 1.5585084353167713], [-8.316101526901583, 1.690455921753512], [-8.318326329384114, 1.8211434319633388], [-8.312949111839542, 1.950309907803558], [-8.299544103717182, 2.0776713188411406], [-8.277775410536456, 2.2029311506934164], [-8.247420480444713, 2.3257907666300106], [-8.208376993659304, 2.4459581200297773], [-8.160660154634531, 2.5631550803831056], [-8.104395668661049, 2.6771236656676773], [-8.039810031039142, 2.787630999644496], [-7.967218287678559, 2.894472633826376], [-7.8870095315776005, 2.9974739798237393], [-7.799630829042338, 3.0964898003263865], [-7.705570508013954, 3.191401904392266], [-7.605341755594999, 3.2821153549231816], [-7.499467351711347, 3.368553616312132], [-7.3884661839300545, 3.450653144891913], [-7.272841985746336, 3.5283579518827253], [-7.153074538861933, 3.6016146487910214], [-7.0296133923360635, 3.6703684232234832], [-6.902873987583995, 3.734560296925943], [-6.7732359452365145, 3.79412589807435], [-6.641043172627718, 3.8489958481216044], [-6.5066053912075485, 3.899097731421553], [-6.3702006607487185, 3.9443594938544875], [-6.232078488522053, 3.984714013346378], [-6.092463151211783, 4.0201045067945635], [-5.951556918295902, 4.050490388295556], [-5.809542940202739, 4.07585317401478], [-5.6665876449726875, 4.096202038366716], [-5.522842566168359, 4.111578660835747], [-5.378445596246197, 4.122061057137467], [-5.233521718874312, 4.1277661555898515], [-5.088183317853467, 4.128850952961717], [-4.942530188364401, 4.125512160011899], [-4.796649389103253, 4.11798432782518], [-4.650615073911837, 4.10653654395851], [-4.504488431729596, 4.091467930111914], [-4.3583178453262175, 4.073102423184356], [-4.212139347756592, 4.051783844307864], [-4.065977398615608, 4.027873349299574], [-3.9198459548949236, 4.001751402452587], [-3.7737500955925656, 3.9738130260170768], [-3.6276890580782775, 3.9444200457038203], [-3.4816584965674027, 3.9138704752298032], [-3.3356440447175446, 3.8823858060227128], [-3.189573975394349, 3.850175555496822], [-3.0430749093116307, 3.817283475769667], [-2.8963595260254147, 3.7848232970146327], [-2.7495474606412174, 3.7528383809972237], [-2.6026288102625124, 3.7213790204726114], [-2.4555932580272297, 3.690497929912455], [-2.3084294243393186, 3.660253546221336], [-2.161125350472992, 3.63070772334824], [-2.0136727341958567, 3.601904621000296], [-1.8660681365149876, 3.5738644106341195], [-1.7183166624230335, 3.5465643450437034], [-1.5704314610186478, 3.5199406861643023], [-1.4224296193076411, 3.4939091078893467], [-1.2743228427965123, 3.4684120334377626], [-1.1261244554920362, 3.4433831109757556], [-0.9778405323505288, 3.418792646669174], [-0.8297240724482038, 3.394650760530297], [-0.682382243251474, 3.369840883548729], [-0.5356575903002377, 3.3440526511964705], [-0.38961901117426834, 3.3169566354749547], [-0.2444032564590733, 3.288243766358611], [-0.10017767561769338, 3.2575903296645388], [0.04287203323179195, 3.224655026954163], [0.18454313149350757, 3.1890800061147497], [0.32461633108477217, 3.1504943969355734], [0.46285871950813595, 3.1085222398331562], [0.599030889922395, 3.0627969274320335], [0.7328969652334667, 3.012979168134902], [0.8642331021854386, 2.958770312445679], [0.992834332898539, 2.8999211382869756], [1.1185214141581028, 2.8362394781418567], [1.241148176181322, 2.7675977671503142], [1.360608841048096, 2.6939397149963087], [1.4768446224397782, 2.61528510529799], [1.5898491259657024, 2.531732201688734], [1.6996722880277098, 2.443457703296114], [1.8064227175988221, 2.350714460517696], [1.9102683611852398, 2.2538272747109955], [2.0114357785496257, 2.153187584997645], [2.110209961798888, 2.0492499719625106], [2.206927036750276, 1.9425204117187045], [2.301887857253165, 1.8334404229935122], [2.395311718915556, 1.7223304247729447], [2.4873244744153915, 1.6093804225802808], [2.577908422422326, 1.4945927810778417], [2.6695213242685023, 1.382243188534526], [2.7626149333525545, 1.2723140765543217], [2.8573671260355455, 1.1652731581952656], [2.95398404110871, 1.0617233376176842], [3.052687146062008, 0.9624421631646856], [3.153490711263098, 0.8679211933991346], [3.256433050767133, 0.7788342772711838], [3.3614249761605697, 0.6956811117451609], [3.4683724308973605, 0.6191140019768383], [3.5771073577917534, 0.5497577048771422], [3.6873733770795996, 0.488081907578224], [3.798852613947005, 0.43437372194240814], [3.9111944874098405, 0.3887096432165193], [4.0240376248410605, 0.3507444493117108], [4.137064566868718, 0.3204230138088028], [4.249947377677012, 0.2979077053926723], [4.362309128371461, 0.2836815743968927], [4.47372276702, 0.2781736168592488], [4.583448974907604, 0.283138528687887], [4.690463703270117, 0.30019277099170716], [4.793195049481115, 0.331556069605247], [4.8890358566461405, 0.38040322474030586], [4.973292836122571, 0.4509886383705513], [5.049316397362615, 0.5340335034251593], [5.117887187115225, 0.6273208226127955], [5.180124999404329, 0.728784035323923], [5.237566456548636, 0.8362200305160687], [5.2916289831533785, 0.9477843023216339], [5.34393347016654, 1.0614762995109395], [5.398154544608285, 1.1789908330613557], [5.453867641866481, 1.2957999789942238], [5.51211970368679, 1.4110746547970783], [5.57358987954307, 1.5239277804820646], [5.638678954200708, 1.6336199048504794], [5.707511834223126, 1.7397297139225194], [5.78011776714186, 1.8420216813246197], [5.857050054101554, 1.9397544677349352], [5.938845262317658, 2.0321741295434466], [6.026404092414704, 2.118053211463192], [6.120800018486349, 2.1958011659617194], [6.223539769092401, 2.2629385154601946], [6.332942057109715, 2.3209891306914474], [6.44784375263317, 2.3711349136325572], [6.567485182386047, 2.4141582655493194], [6.691269586556334, 2.450693341271144], [6.818702697396234, 2.4812787547295403], [6.949378322226103, 2.5063532936170727], [7.082950360113755, 2.526280299446081], [7.219183323300312, 2.541221194675927], [7.357816656371595, 2.5513442488548446], [7.49848754338888, 2.5569750507545788], [7.640799876637963, 2.5584699003539053], [7.784354349214254, 2.556149512403885], [7.928756435854008, 2.550269766202183], [8.073616492038227, 2.5410085049360718], [8.21854796301244, 2.528460267166248], [8.363165917965823, 2.512636249169624], [8.50708659985089, 2.4934684600758374], [8.649928025949178, 2.4708173668466484], [8.791311369681061, 2.44448234448478], [8.930862765939182, 2.414214247573322], [9.068215252798248, 2.3797294614909603], [9.203010717089377, 2.3407248663689715], [9.334901861710673, 2.296893225679729], [9.463554286630998, 2.2479385643656267], [9.588648741701718, 2.1935911092486107], [9.70988348275886, 2.133621326922652], [9.82697649378363, 2.0678525327524264], [9.939667191939993, 1.996171495831486], [10.047717165669283, 1.918536468442986], [10.150909540642626, 1.8349821525593022], [10.249046724936013, 1.7456212856890194], [10.34194652552074, 1.6506427646557702], [10.429436906419358, 1.5503064908893267], [10.511349921739075, 1.444935369966297], [10.587515556839179, 1.3349050924857868], [10.657756314620377, 1.2206324382918476], [10.721883375747867, 1.1025628744832923], [10.779695043741992, 0.9811581680829978], [10.830977975315522, 0.8568846256610656], [10.875511420521079, 0.7302024281993362], [10.913074389292056, 0.601556373229746], [10.943455355306217, 0.4713681872412877], [10.96646383711228, 0.3400304436296898], [10.981942987550994, 0.20790202340091635], [10.98978219609363, 0.07530499040443031], [10.9899286767934, -0.05747728151194683], [10.982397079784121, -0.19020090042155816], [10.967276319796982, -0.32266132799642544], [10.944733044915345, -0.4546924707904628], [10.915011448292482, -0.5861651072452849], [10.878429423205201, -0.7169847455955944], [10.835371340522109, -0.8470889922804383], [10.786277948117426, -0.976444499199381], [10.731634019896847, -1.1050435472379596], [10.671954403762598, -1.2329003087349113], [10.607769058390875, -1.3600468124152103], [10.539607602701633, -1.4865286155962183], [10.467983927722923, -1.6124001752853587], [10.393381590162644, -1.7377198963880371], [10.31624095259394, -1.8625448030795004], [10.236949172583017, -1.9869247263267285], [10.155833980802399, -2.1108958950267818], [10.073161654808132, -2.234474010681497], [9.98913878337899, -2.3576473884265567], [9.903916569860584, -2.480371409385504], [9.817595922608385, -2.602565841535281], [9.730231810677234, -2.7241160033531915], [9.641836359890734, -2.8448773161009684], [9.552381368699647, -2.964681408404881], [9.461801510613615, -3.0833416376712814], [9.369999099954107, -3.200656815313896], [9.276850342704273, -3.3164131980509213], [9.182212220514305, -3.4303855302708395], [9.085929021709498, -3.5423379495417735], [8.987837982295044, -3.652025337881703], [8.887774148959686, -3.759195590830388], [8.785575034351954, -3.863593293450399], [8.68108570514624, -3.9649652278757945], [8.574164632979576, -4.063067812415717], [8.464690110755893, -4.157676008382653], [8.352566563046421, -4.248592680959563], [8.237729901844435, -4.335657166532082], [8.120151242577785, -4.418751968643038], [7.999838642999231, -4.497806908291713], [7.876836861942587, -4.572800456626011], [7.751225355201606, -4.643758256069921], [7.623114836971774, -4.710748996435062], [7.49264278409292, -4.773877914321204], [7.359968282636352, -4.833278271466698], [7.225266623816237, -4.889101252946401], [7.088724045562692, -4.94150480110002], [6.950532981445844, -4.990641952811185], [6.810888117870853, -5.036649267195724], [6.669983476647524, -5.079635915215944], [6.5280106402761096, -5.119673955145142], [6.38515813084264, -5.156790244972436], [6.241611849915024, -5.190960353643657], [6.097556394845406, -5.222104736779889], [5.953176992938453, -5.2500873474795755], [5.8086617430392025, -5.274716765112941], [5.664203825729531, -5.295749847917927], [5.520003337951689, -5.312897848959153], [5.37626842360894, -5.325834877338943], [5.23321540604851, -5.334208533670402], [5.091067678858335, -5.33765249681012], [4.9500531760331095, -5.335800784973097], [4.810400319659685, -5.328303358015289], [4.6723324314916415, -5.314842670618814], [4.536060692727508, -5.295150731927129], [4.401775841955024, -5.269026180457729], [4.269638910296796, -5.236350850876571], [4.139771391193067, -5.197105316331907], [4.0122452807452955, -5.15138303681203], [3.8870733265959254, -5.099403185716843], [3.7641999959639594, -5.041521978873252], [3.6434965005472533, -4.978235818462399], [3.524769463180472, -4.910155199401245], [3.4077912881795305, -4.837932600101592], [3.292370463113777, -4.762103626610446], [3.178374206690716, -4.683049153385843], [3.06580876536497, -4.600841653113741], [2.956338041603492, -4.516969329154717], [2.8470639874023185, -4.4375850728643496], [2.737205424369993, -4.362296478530318], [2.6263462353880205, -4.291141199844501], [2.514297914939384, -4.224184169898725], [2.4009017078242842, -4.161795868697455], [2.286054765764357, -4.10433643098563], [2.169509426641194, -4.052768905944476], [2.0509370983869513, -4.008471090025666], [1.9299867183196684, -3.973111100345515], [1.8061593798652293, -3.949398061498309], [1.6800980564608041, -3.9355587340046547], [1.5522801314442325, -3.930066840547152], [1.4229688975634653, -3.9321498079191475], [1.2923541055222236, -3.9412918509070245], [1.1605948686051746, -3.957065202744815], [1.0278406871380463, -3.9790296133564373], [0.8941999333617153, -4.006962560323911], [0.7598295381890152, -4.040243787374974], [0.6248347638788987, -4.078549030267439], [0.48934387380470495, -4.121300703587245], [0.35347137490737407, -4.167907753273242], [0.2173135882311465, -4.217804483506986], [0.08094864125011283, -4.270466395545167], [-0.05556209784321679, -4.325419077699078], [-0.19217200978325144, -4.382244291536193], [-0.3288468702472513, -4.440581214465677], [-0.46556227151255386, -4.500120097533552], [-0.6023013784822915, -4.5605979470505105], [-0.7390531035341341, -4.621792186664198], [-0.875810655434627, -4.683539338975244], [-1.0125694341743054, -4.745560927567682], [-1.1493282066473474, -4.807757225875386], [-1.2860863129935176, -4.870092897608848], [-1.422842980915611, -4.9325662997564725], [-1.5595975624601377, -4.995175107795985], [-1.6963495016098022, -5.057917833328247], [-1.8330999612808228, -5.120747089385986], [-1.9698514938354492, -5.183574676513672], [-2.106602966785431, -5.24640154838562], [-2.2433555126190186, -5.3092265129089355]])
velocities = [3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.0787523851172, 2.817389681345486, 2.596868585451407, 2.41526657152128, 2.2819654825411257, 2.231447315234055, 2.113025132598805, 2.006136215761953, 1.849559279330641, 1.6756599548010818, 1.5068320709341447, 1.3787044836620084, 1.1968863337184243, 1.1968863337184243, 1.1968863337184243, 1.1968863337184243, 1.1968863337184243, 1.1968863337184243, 1.1968863337184243, 1.1968863337184243, 1.1968863337184243, 1.1968863337184243, 1.1968863337184243, 1.3620572720760586, 1.5076912395710507, 1.6487360554423722, 1.7786904771693763, 1.9286015703105455, 2.049826975608732, 2.1759736880999956, 2.3115496203491386, 2.458714120096713, 2.570021366724203, 2.4709451887942526, 2.3622678290527754, 2.26901905123361, 2.188572148026867, 2.1038357987384537, 2.044506760499827, 2.010159957792249, 1.9988323992180652, 1.9988323992180652, 1.9988323992180652, 1.9988323992180652, 1.9988323992180652, 1.9988323992180652, 1.9988323992180652, 1.9988323992180652, 1.9988323992180652, 1.9988323992180652, 1.9988323992180652, 2.0109137735196083, 2.047973136637631, 2.1124621252772564, 2.2079853167765555, 2.340004532930869, 2.51833519468039, 2.4777311618573523, 2.3720038872645395, 2.280383814843055, 2.1832860649366532, 2.133414897362407, 2.1136726471835825, 2.1136726471835825, 2.1136726471835825, 2.1136726471835825, 2.1136726471835825, 2.1136726471835825, 2.1136726471835825, 2.1136726471835825, 2.1136726471835825, 2.1136726471835825, 2.1136726471835825, 2.119682249985177, 2.151076553410052, 2.208999241224873, 2.2962721565176376, 2.4186175970876973, 2.547830743428231, 2.39629647421851, 2.2616872260579575, 2.139046715728199, 2.0278487988971365, 1.9299658315107495, 1.848535730382341, 1.7860080605676951, 1.7429439946562746, 1.718567713300409, 1.7116891529558322, 1.7116891529558322, 1.7116891529558322, 1.7116891529558322, 1.7116891529558322, 1.7116891529558322, 1.7116891529558322, 1.7116891529558322, 1.7116891529558322, 1.7116891529558322, 1.7116891529558322, 1.7211094477740096, 1.7456158820273324, 1.7838660762949132, 1.834300590142296, 1.895100300566854, 1.9641712022418483, 2.039146276442268, 2.117408753271258, 2.1961518235492035, 2.272492665074673, 2.3436509692182708, 2.407183389065537, 2.4612399601569774, 2.504787440414687, 2.537740911126967, 2.5609655988167757, 2.576148938014113, 2.585580674509836, 2.5918992151684024, 2.597859759654575, 2.6061608725163152, 2.6193432230423364, 2.63975662576311, 2.66958265062201, 2.710898719395717, 2.7657729258550825, 2.8363846824147956, 2.925174591125349, 3.0350409321198937, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.0613565330557484, 2.8790984189860604, 2.729054225766866, 2.608016921838101, 2.5126608801769095, 2.440760528572503, 2.3912309870177872, 2.3637759832164336, 2.3586666815492494, 2.3586666815492494, 2.3586666815492494, 2.3586666815492494, 2.3586666815492494, 2.3586666815492494, 2.3586666815492494, 2.3586666815492494, 2.3586666815492494, 2.3586666815492494, 2.3586666815492494, 2.3767322893008695, 2.419527102935735, 2.489673682613506, 2.591464894323195, 2.7321093080526997, 2.7314669856479092, 2.580980878834456, 2.4038099785822666, 2.2827791696227715, 2.1440704375741237, 2.0213102839158763, 1.9261745910035346, 1.8554188617803031, 1.8090087321403316, 1.8090087321403316, 1.7819665166101486, 1.729034065326356, 1.6444933303262714, 1.5707397234317781, 1.4020980601625688, 1.2748425903026643, 1.1452664898399307, 1.016250930777596, 0.8999999999999999, 0.8999999999999999, 0.8999999999999999, 0.8999999999999999, 0.8999999999999999, 0.8999999999999999, 0.8999999999999999, 0.8999999999999999, 0.8999999999999999, 0.8999999999999999, 0.8999999999999999, 1.1894548224350254, 1.3365026007399157, 1.535647455439324, 1.848185068612282, 1.9005890098955314, 1.7111250553924717, 1.5403553242547146, 1.3669881393475272, 1.3669881393475272, 1.3669881393475272, 1.3669881393475272, 1.3669881393475272, 1.3669881393475272, 1.3669881393475272, 1.3669881393475272, 1.3669881393475272, 1.3669881393475272, 1.3669881393475272, 1.5090383494400545, 1.6560885251688384, 1.7885900804124826, 1.9228974060971666, 2.060764656633884, 2.196564029297816, 2.3297962488578436, 2.4251309954854405, 2.525740322778012, 2.6731767707239777, 2.715410844337723, 2.5760058764121205, 2.446908327353839, 2.3312804941943144, 2.2308855291553344, 2.146581458544599, 2.0786291655373774, 2.0268502566886006, 1.9906799803370323, 1.9691553254602896, 1.9608711132251637, 1.9608711132251637, 1.9608711132251637, 1.9608711132251637, 1.9608711132251637, 1.9608711132251637, 1.9608711132251637, 1.9608711132251637, 1.9608711132251637, 1.9608711132251637, 1.9608711132251637, 1.9639322713967093, 1.9759300305418899, 1.984616581803245, 1.9695232511917957, 1.9621395386824407, 1.9621395386824407, 1.9621395386824407, 1.9621395386824407, 1.9621395386824407, 1.9621395386824407, 1.9621395386824407, 1.9621395386824407, 1.9621395386824407, 1.9621395386824407, 1.9621395386824407, 1.9652513927019932, 1.9812313794983125, 2.0120702405691375, 2.0594595676426835, 2.1249084814300785, 2.2098834087114096, 2.315962764148983, 2.4449954527703275, 2.59924096729645, 2.7814462705896363, 2.994778117424625, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.0823633740627576, 2.961135555947412, 2.8612256860097385, 2.7825788126664857, 2.7250162958661823, 2.6881773019035506, 2.671548637794417, 2.671548637794417, 2.671548637794417, 2.671548637794417, 2.671548637794417, 2.671548637794417, 2.671548637794417, 2.671548637794417, 2.671548637794417, 2.671548637794417, 2.671548637794417, 2.6745145439439435, 2.6963729503835983, 2.736291703929073, 2.7931953985511946, 2.865578677922497, 2.9512443007720757, 3.0469760099330956, 3.05396525047347, 2.916010814729067, 2.7782401723966084, 2.6460723946332396, 2.523490558513731, 2.413373520740519, 2.3178553835645284, 2.2386418307898013, 2.1772681341097564, 2.135316701948791, 2.114636025162349, 2.114636025162349, 2.114636025162349, 2.114636025162349, 2.114636025162349, 2.114636025162349, 2.114636025162349, 2.114636025162349, 2.114636025162349, 2.114636025162349, 2.114636025162349, 2.1176407180585146, 2.147846716805311, 2.210754688577994, 2.314214865059871, 2.46551740982148, 2.3539452200870303, 2.130949090497687, 1.9011125965907847, 1.7035726851962905, 1.4914420358620155, 1.4914420358620155, 1.4914420358620155, 1.4914420358620155, 1.4914420358620155, 1.4914420358620155, 1.4914420358620155, 1.4914420358620155, 1.4914420358620155, 1.4914420358620155, 1.4914420358620155, 1.6309756472877412, 1.7951482181518281, 1.913024653138069, 2.016291329429798, 2.1200140735354034, 2.2379321264276113, 2.326048083913435, 2.506856133159526, 2.6361668704068433, 2.852037833080044, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1, 3.1]
lookahead_points = 10
min_speed = 0.9
max_speed = 3.1
# print(track_name, len(race_line), len(velocities))

MIN_REWARD = 1e-3
STEPS_PER_SECOND = 15.0

EXPECTED_SLOW_COMPLETION_TIME = 35.0
EXPECTED_FASTEST_COMPLETION_TIME = 20.0
AVG_SPEED = 2
AVG_REWARD_PER_STEP = 0.5
AVG_REWARD_PER_LENGTH = AVG_REWARD_PER_STEP * STEPS_PER_SECOND / AVG_SPEED

DEFAULT_REWARD = 0.25
STEERING_WEIGHT = 0
HEADING_WEIGHT = 0.25
CENTER_WEIGHT = 0.25
SPEED_WEIGHT = 0.25
PROGRESS_WEIGHT = 1.0

def reward_function(params):
  
  # --------------------------- Params --------------------------- #

  speed = params['speed']
  steering_angle = params['steering_angle']
  heading = params['heading']
  track_width = params['track_width']
  closest_waypoints = params['closest_waypoints']
  distance_from_center = params['distance_from_center']
  track_length = params['track_length']
  progress = params['progress']
  steps = params['steps']
  x = params['x']
  y = params['y']
  
  # --------------------------- Steering --------------------------- #
  
  # calculate track direction angle
  track_vector = race_line[closest_waypoints[1]]-race_line[closest_waypoints[0]]
  track_direction = np.arctan2(track_vector[1], track_vector[0])*180/np.pi
  
  steering_direction = steering_angle+heading
  steering_difference = abs(track_direction-steering_direction)
  steering_difference = steering_difference if steering_difference < 180 else 360-steering_difference
  
  steering_reward = np.exp(-0.5 * (steering_angle / 10)**2)

  # --------------------------- Heading --------------------------- #


  heading_difference = abs(track_direction-heading)
  heading_difference = heading_difference if heading_difference < 180 else 360-heading_difference

  # when heading difference deviates by 2 stddev, the reward is 1/e^2 ~ 0.1
  heading_reward = np.exp(-0.5 * (heading_difference / 15)**2)

  # --------------------------- Center --------------------------- #

  # fraction of the distance to the center line
  cx, cy = (race_line[closest_waypoints[1]] + race_line[closest_waypoints[1]]) / 2
  distance_from_race_line = np.sqrt((cx - x)**2 + (cy - y)**2)
  track_fraction = 2 * distance_from_race_line / track_width

  # when distance to race line deviates by 2 stddev, the reward is 1/e^2 ~ 0.1
  center_reward = np.exp(-0.5 * (track_fraction / 0.4)**2)

  # --------------------------- Speed --------------------------- #

  # difference in expected speed vs actual speed
  ideal_speed = velocities[closest_waypoints[1]]
  speed_difference = abs(ideal_speed - speed)
  
  # when speed deviates from ideal_speed by 2 stddev, the reward is 1/e^2 ~ 0.1
  speed_reward = np.exp(-0.5 * (speed_difference / 0.8)**2)
  
  # --------------------------- Progress --------------------------- #

  progress_reward = 0.0
  if (progress == 100):
    time = steps / STEPS_PER_SECOND
    expected_total_reward = AVG_REWARD_PER_LENGTH * track_length
    
    # interpolate between slow and fast steps
    normalized_time = (time - EXPECTED_SLOW_COMPLETION_TIME) / (EXPECTED_FASTEST_COMPLETION_TIME - EXPECTED_SLOW_COMPLETION_TIME)
    progress_reward = expected_total_reward * normalized_time
    progress_reward = progress_reward if progress_reward > 0 else 0

  # --------------------------- Total --------------------------- #

  reward = DEFAULT_REWARD + STEERING_WEIGHT*steering_reward + HEADING_WEIGHT*heading_reward + CENTER_WEIGHT*center_reward + SPEED_WEIGHT*speed_reward + PROGRESS_WEIGHT*progress_reward
  reward = reward if reward > MIN_REWARD else MIN_REWARD

  # -------------------------- Bonuses -------------------------- #

  bonus_reward = 0

  # if all within 1.5 stddevs, add a small reward
  if (heading_difference < 22.5 and track_fraction < 0.6 and speed_difference < 1.2):
    bonus_reward = 0.1
  
  # if all within 1 stddev, add a moderate reward
  elif (heading_difference < 15 and track_fraction < 0.4 and speed_difference < 0.8):
    bonus_reward = 0.25

  # if all within 0.5 stddevs, add a large reward
  if (heading_difference < 7.5 and track_fraction < 0.2 and speed_difference < 0.4):
    bonus_reward = 0.75

  reward += bonus_reward

  # ------------------------- Penalties ------------------------- #

  penalty = 'none'

  # punish hard if off track
  if not params['all_wheels_on_track']:
    reward = MIN_REWARD
    penalty = 'off track'

  # punish hard if heading direction is way off
  if heading_difference > 30:
    reward = MIN_REWARD
    penalty = 'off heading'
  
  # punish hard if too far from center line or race line
  if 2 * distance_from_center > track_width or track_fraction > 0.8:
    reward = MIN_REWARD
    penalty = 'off center'
  
  # punish hard if too slow or speed is far from ideal
  if speed < 0.5 or speed_difference > 1.6:
    reward = MIN_REWARD
    penalty = 'off speed'

  # --------------------------- Logs ---------------------------- #

  print('=============== <REWARDS> ===============')
  print('steering_reward:', steering_reward)
  print('heading_reward:', heading_reward)
  print('center_reward:', center_reward)
  print('speed_reward:', speed_reward)
  print('progress_reward:', progress_reward)
  print('bonus_reward:', bonus_reward)
  print('total_reward:', reward)
  print('=============== </REWARDS> ===============')
  print('=============== <PARAMS> ===============')
  print('position:', f'({x}, {y})')
  print('speed:', speed)
  print('steering_angle:', steering_angle)
  print('heading:', heading)
  print('closest_waypoints:', closest_waypoints)
  print('distance_from_center:', distance_from_center)
  print('track_length:', track_length)
  print('steps:', steps)
  print('progress:', progress)
  print('=============== </PARAMS> ===============')
  print('=============== <MISC> ===============')
  print('track_name:', track_name)
  print('min_speed:', min_speed)
  print('max_speed:', max_speed)
  print('track_direction:', track_direction)
  print('steering_difference:', steering_difference)
  print('heading_difference:', heading_difference)
  print('distance_from_race_line:', distance_from_race_line)
  print('track_fraction:', track_fraction)
  print('speed_difference:', speed_difference)
  print('lookahead_points:', lookahead_points)
  print('penalty:', penalty)
  print('=============== </MISC> ===============')

  return float(reward)
