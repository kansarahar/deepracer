import numpy as np

# import os
# track_name = 'ace-speedway'
# dir_name = os.path.dirname(os.path.abspath(__file__))
# race_line = np.load('%s/../tracks/optimal_track_points/%s.npy' % (dir_name, track_name)).tolist()
# velocities = np.load('%s/../action_space/velocities/%s.npy' % (dir_name, track_name)).tolist()
# steering_angles = np.load('%s/../action_space/steering_angles/%s.npy' % (dir_name, track_name)).tolist()
# print(velocities)
# print(len(race_line), len(velocities))

race_line = np.array([[0.12689816547208466, -3.4209022149443626], [0.26724113058298826, -3.4979465007781982], [0.5314155369997025, -3.6429725885391235], [0.7955881655216217, -3.7880018949508667], [1.0597597062587738, -3.9330344200134277], [1.3239295482635498, -4.0780699253082275], [1.588104486465454, -4.223094463348389], [1.8522890210151703, -4.3680999279022235], [2.1164824962616, -4.51308584213257], [2.380680561065674, -4.6580634117126465], [2.6448378550973266, -4.803103960486831], [2.909048757447338, -4.947408896528296], [3.173431047874324, -5.090230890589229], [3.4380723491340763, -5.230710592656108], [3.703054327338247, -5.367953218790003], [3.968448507025923, -5.501008518258342], [4.234311315200571, -5.62884540612859], [4.500678373259689, -5.750319767049772], [4.76755412863038, -5.864174744945943], [5.034910346025399, -5.968816862904529], [5.302650452118881, -6.0624806184859], [5.57058546978371, -6.143055646221676], [5.838364303522649, -6.207510958240514], [6.105367753074983, -6.252666858594858], [6.370568340419135, -6.274553480815069], [6.63223998461123, -6.268082917451933], [6.88724840417013, -6.2262627339853776], [7.128884690034742, -6.138960079718887], [7.355203241353056, -6.015645859364903], [7.56538782624799, -5.862963766146395], [7.759009633092937, -5.686114939232846], [7.936321634348552, -5.489872687980415], [8.097216850538596, -5.277586863816326], [8.241795326617055, -5.05221559386948], [8.37033843647107, -4.816336659484184], [8.483159922720553, -4.572097611634165], [8.580624631628538, -4.321306109939103], [8.663094444414083, -4.065484069212381], [8.730884073254, -3.8059300547867156], [8.783922650614246, -3.5437416368587513], [8.821990660564893, -3.279958820337737], [8.84381994424658, -3.0156121094411383], [8.847636881320572, -2.7519934418740766], [8.831558143330518, -2.490707233004681], [8.791712208443107, -2.2341790256202048], [8.724110266288427, -1.9858286028525258], [8.62227391858065, -1.751517979781713], [8.47969062483713, -1.5403666075779063], [8.299361475975918, -1.3583808470690593], [8.09107559026679, -1.2039530336533382], [7.861762426129866, -1.0742062946539968], [7.616343784731604, -0.9661408506105494], [7.358561320997049, -0.8767083910044691], [7.091335184836953, -0.8028819853058192], [6.8170828115864985, -0.7415304293916005], [6.53799956314535, -0.6892040891865281], [6.2557638219259974, -0.6429646080434905], [5.971977833061682, -0.5997751414810809], [5.683936997693676, -0.5540495520484958], [5.396529856381665, -0.5058010105898676], [5.110010225851489, -0.45433290969478246], [4.824693865200558, -0.39884961759886906], [4.541010099125459, -0.338344641036722], [4.259334702922766, -0.27211738462246615], [3.98004252858093, -0.19954970010049333], [3.703632430773091, -0.11980082476998186], [3.4306579458013893, -0.032037092098495035], [3.161651065287315, 0.06438650669086109], [2.8971360473445698, 0.16997737641461136], [2.6376249513985153, 0.2851161342073052], [2.3835906128319175, 0.41003293114857714], [2.1354109572609445, 0.5447527765071083], [1.893276427593155, 0.6890031187702981], [1.6571132080541804, 0.8421577562442586], [1.4268146610439554, 1.003613026819277], [1.2023236111834326, 1.1728959086540418], [0.9844295217720417, 1.3506308493267456], [0.7742941788081763, 1.5377362267695198], [0.5736045086922917, 1.7354733897327037], [0.3856413878137326, 1.9461736371510865], [0.2095208159307938, 2.167544300205166], [0.04312718563883471, 2.3966489301307448], [-0.11499248681278751, 2.631504801982968], [-0.2661470207986866, 2.8704200746905615], [-0.41133992007243975, 3.111877132245152], [-0.5512603986197147, 3.3544314047245765], [-0.6865965065243274, 3.596831881222066], [-0.8181580716340974, 3.838330657930663], [-0.9469912049849145, 4.078778936442272], [-1.0741138716313108, 4.3184033519452045], [-1.1908554943223912, 4.539515501498285], [-1.3101430457020684, 4.758420508898411], [-1.4345783122469014, 4.9729078142757395], [-1.5667940889601315, 5.1808428783653], [-1.7100651744532547, 5.3797237821883055], [-1.868371852831765, 5.5666323187593605], [-2.046608900218188, 5.737469587104233], [-2.2417827391556977, 5.893567962643906], [-2.454028280769043, 6.033210874156791], [-2.6838491644599083, 6.153526727892614], [-2.927603297067672, 6.25619427160086], [-3.182708922196836, 6.34250640992364], [-3.446927870564095, 6.4139033738301485], [-3.718732244876717, 6.471013992641204], [-3.9966262938917945, 6.514468711832477], [-4.279140155579764, 6.544832566777158], [-4.5648635906611705, 6.562389962667046], [-4.852342648694765, 6.567582417153211], [-5.140223584821835, 6.561029762624443], [-5.4273271856210314, 6.543041516337494], [-5.712654699962801, 6.514029829160282], [-5.995172661740137, 6.473621252935411], [-6.27379717088594, 6.4212482822447585], [-6.5472815395560495, 6.3558945356197505], [-6.8140208256418955, 6.275870981182002], [-7.072047212543163, 6.179031065818831], [-7.319258785452023, 6.06325232273115], [-7.551298124290529, 5.923372004493887], [-7.762425485569121, 5.7544245877277636], [-7.955579406530725, 5.564011819372114], [-8.131439285717246, 5.35567878089496], [-8.290225523841947, 5.132223285226675], [-8.432404881319428, 4.896419343089692], [-8.557462271126411, 4.650182033088984], [-8.66484795170275, 4.3954536100308665], [-8.754126736927326, 4.13418228277984], [-8.825040163381972, 3.8682360537252274], [-8.877346312781246, 3.5993383795228455], [-8.910517799829545, 3.3291164057952045], [-8.923961931982014, 3.059193494891357], [-8.916743167014989, 2.7911729077578467], [-8.8858116339137, 2.5271132116278445], [-8.82733465147125, 2.269822087746882], [-8.735805043804849, 2.023496496380738], [-8.60373586637163, 1.794931251851935], [-8.445470949832028, 1.5802481442919654], [-8.264962583861312, 1.3786028488873718], [-8.065427574548082, 1.1890579304342155], [-7.8500284819647215, 1.0103245908540612], [-7.621151973731521, 0.8413473545488428], [-7.381149480268986, 0.680880435497759], [-7.132390178725382, 0.5274416376238398], [-6.877009697793701, 0.3795043514189964], [-6.616812987786393, 0.23559677389218175], [-6.353216191443867, 0.09427585792326412], [-6.087399982683882, -0.0459395357733003], [-5.821348492386335, -0.18724898980038573], [-5.555485224808901, -0.3289311800897694], [-5.28974936716256, -0.4708656773557811], [-5.0241322203225, -0.6130352531050527], [-4.758644514308756, -0.7554611531263282], [-4.4932892195862575, -0.8981492567244789], [-4.228051257118642, -1.041069701047076], [-3.9629277733818244, -1.1842168325756863], [-3.6979188735610378, -1.3275908561953242], [-3.4330260255807357, -1.4711946741847064], [-3.168250228873397, -1.615030258465501], [-2.903592072168319, -1.7590987615400602], [-2.639051918389508, -1.9034008747520126], [-2.374630074171421, -2.0479371468225187], [-2.1103270649909973, -2.1927084922790527], [-1.8461494445800781, -2.337728500366211], [-1.5819770097732544, -2.4827585220336914], [-1.317804992198944, -2.6277894973754883], [-1.0536318719387054, -2.772818446159363], [-0.7894578874111176, -2.9178454875946045], [-0.525283545255661, -3.0628714561462402], [-0.26110872998833656, -3.2078969478607178], [0.003066137433052063, -3.352921962738037]])
velocities = [4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 3.809012347965144, 3.4090890135765175, 3.034698637755151, 2.684390856107079, 2.349018518301849, 2.0233414406813464, 2.2237233497771207, 2.4185471268238716, 2.6110622379107284, 2.833491554697632, 2.9996294957551735, 3.1599739843686545, 3.3126106298786953, 3.444124499340132, 3.559171943401785, 3.655421038529742, 3.730537876782836, 3.743031937112695, 3.723634988362124, 3.57081714589884, 3.373312006469539, 3.1797196003203325, 2.8679604694825676, 2.6013415318009665, 2.2802251705095875, 2.014535160450092, 2.0, 2.227054420778258, 2.4916328170917903, 2.785859846258342, 3.1270825313591994, 3.5330529442300636, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 3.5779923536615055, 3.8273009456377873, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 3.521458644808042, 3.021127169362349, 2.6308235479092725, 2.846734769410863, 2.8189859876485106, 2.7442975566350536, 3.02537099956261, 3.2824547617858433, 3.5676953187806606, 3.7658644768456577, 3.9635935885769977, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 3.791114396867093, 3.461225154255273, 3.1863274563518797, 2.7581616627391914, 2.4451267811451163, 2.767200377379044, 2.947759962655652, 3.097516977238296, 3.26733920605464, 3.330279475678072, 3.3731943636475923, 3.40365194801297, 3.424718572741662, 3.42360496960897, 3.3771388453658977, 3.3094207980660406, 3.202767800448434, 2.949831851361953, 2.6914976447207772, 2.4124847968720133, 2.1403359314589516, 2.6398167073540537, 2.876881193071219, 3.139526342332706, 3.4769981263863494, 3.8145666171076575, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0, 4.0]

def reward_function(params):

  # --------------------------- Weights --------------------------- #

  steering_weight = 50
  center_weight = 30
  speed_weight = 15
  progress_weight = 5

  # ---------------------- Off-track Penalty ---------------------- #

  # Penalize if off track
  if not params['all_wheels_on_track']:
    return 1e-3
  
  # --------------------------- Params --------------------------- #

  speed = params['speed']
  steering_angle = params['steering_angle']
  heading = params['heading']
  track_width = params['track_width']
  closest_waypoints = params['closest_waypoints']
  progress = params['progress']
  x = params['x']
  y = params['y']
  
  # --------------------------- Heading --------------------------- #

  # I don't think there's really any benefit to rewarding separately for
  # steering and heading, so I will omit the heading reward

  # calculate track direction angle
  track_vector = race_line[closest_waypoints[1]]-race_line[closest_waypoints[0]]
  track_direction = np.arctan2(track_vector[1], track_vector[0])*180/np.pi

  # reward if heading direction is the same as track direction
  # heading_difference = abs(track_direction-heading)
  # heading_difference = heading_difference if heading_difference < 180 else 360-heading_difference

  # # when heading angle difference is 20, the reward is 1/e~0.37
  # heading_reward = np.exp(-0.0025*heading_difference**2) if heading_difference < 45 else 0

  # --------------------------- Steering --------------------------- #

  # reward if steering direction is the same as track direction
  steering_direction = steering_angle+heading
  steering_difference = abs(track_direction-steering_direction)
  steering_difference = steering_difference if steering_difference < 180 else 360-steering_difference

  # when steering difference is 4, the reward is 1/e~0.37
  steering_reward = np.exp(-0.0625*steering_difference**2) if steering_difference < 30 else 0

  # --------------------------- Center --------------------------- #

  # reward if close to center line

  # when at 50% of the track width, the reward is 1/e~0.37
  cx, cy = race_line[closest_waypoints[0]]
  distance_from_race_line = ((cx - x)**2 + (cy - y)**2)**0.5
  center_reward = np.exp(-16*(distance_from_race_line/track_width)**2) if distance_from_race_line < track_width/2 else 0

  # --------------------------- Speed --------------------------- #

  # reward for speed
  ideal_speed = velocities[closest_waypoints[1]]

  # when speed deviates from ideal_speed by 0.5, reward is 1/e~0.37
  speed_reward = np.exp(-4*(ideal_speed-speed)**2) if speed > 0 else 0  
  
  # --------------------------- Progress --------------------------- #

  progress_reward = progress / 100

  # --------------------------- Total --------------------------- #

  reward = steering_weight*steering_reward + center_weight*center_reward + speed_weight*speed_reward + progress_weight*progress_reward
  reward = reward if reward > 1e-3 else 1e-3
  print(f'REWARDS: steering_reward({steering_reward}), center_reward({center_reward}), speed_reward({speed_reward}), progress_reward({progress_reward}), total_reward({reward})')
  print(f'PARAMS: position({x}, {y}), speed({speed}), steering_angle({steering_angle}), heading({heading}), progress({progress})')
  return float(reward)