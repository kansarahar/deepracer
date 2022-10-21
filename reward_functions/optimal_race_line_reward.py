import numpy as np

# --------------------- Optimization Results --------------------- #

track_name = 'jochem-turnpike'
race_line = np.array([[-6.983025861430506, 0.7956637534290296], [-7.031893849757385, 0.5412577230635391], [-7.06662090015778, 0.28078515286723604], [-7.087363763664056, 0.015035679296541527], [-7.0941596222994425, -0.25490300629030416], [-7.086996184329555, -0.5276368198722104], [-7.065946495053509, -0.8015740319966189], [-7.031175360303472, -1.0751094501118466], [-6.982684040286685, -1.3467206897674355], [-6.920207018876006, -1.6149223938248063], [-6.843171676298908, -1.8781635699416501], [-6.74910341291854, -2.133900757352696], [-6.635827586285117, -2.379165961546696], [-6.500501628753203, -2.610055440887309], [-6.339233277749578, -2.820800541960412], [-6.147183783115494, -3.001315431289096], [-5.932937064535219, -3.15346843602236], [-5.702912539635657, -3.280498583236296], [-5.461155288944336, -3.3848019397964717], [-5.210659180755474, -3.4687238576916575], [-4.953412520034468, -3.533757048786083], [-4.690987313664065, -3.581331741281117], [-4.424278848673898, -3.6110821278894294], [-4.153464390316276, -3.6151829175835344], [-3.8809862911126958, -3.5975291486064616], [-3.6081565260348207, -3.5615620271206474], [-3.33569838618485, -3.510192655206041], [-3.0640034815786565, -3.445730009209975], [-2.7932658360455713, -3.3701453908568366], [-2.5235620804429084, -3.285100717974758], [-2.2548993691109986, -3.19198707539906], [-1.9872399791890851, -3.092000138127739], [-1.7204892074648033, -2.9863432308494824], [-1.4545616506278873, -2.8759039111434923], [-1.189352206112242, -2.7615248221421766], [-0.9247634711720705, -2.6438963534626936], [-0.6606439616775432, -2.5238996129075453], [-0.3968764431636991, -2.402171902660197], [-0.13335314767418183, -2.279265621194692], [0.12716723411197117, -2.156997222814282], [0.38751104068900044, -2.035898433745924], [0.6475967231723226, -1.9164089040193653], [0.9073582114377475, -1.7988075655434523], [1.1667071107237814, -1.6834441262157736], [1.4255587211073717, -1.5705898306555102], [1.683828704939298, -1.4604742106496569], [1.9414392756214718, -1.3532700996794054], [2.1983290940168354, -1.2490666958490357], [2.4544643645616375, -1.1478423670657478], [2.709847921872523, -1.0494483499148308], [2.9645182421360055, -0.9536272986830137], [3.2185173644828335, -0.8601325575207377], [3.471864823306693, -0.768809607611664], [3.7245201136565598, -0.6796889336507586], [3.9763960082613816, -0.5928346614136317], [4.2270773643957185, -0.5085447963491192], [4.474687129525638, -0.42757422767462916], [4.721074231765318, -0.34415806354263917], [4.966291171739166, -0.255616421926811], [5.209279844808659, -0.15967319244935751], [5.448028251988914, -0.05289935733707478], [5.679733216212833, 0.06805905110500876], [5.9002286088471765, 0.20708029068781275], [6.103900063071003, 0.36771667766945515], [6.283550021601684, 0.5522235984494219], [6.4397794868700196, 0.7547240568691975], [6.573740525572806, 0.9709380109690846], [6.685554475958437, 1.1981401921064028], [6.775320755248783, 1.4339676257693044], [6.84295135548364, 1.6763007245311168], [6.887627499460411, 1.9231555315904685], [6.908519868764589, 2.172321515048332], [6.90417713209534, 2.4213518325332046], [6.87146325403434, 2.667050418425038], [6.806360843058126, 2.9047309960902625], [6.704927930945599, 3.127897953664002], [6.5639158840134915, 3.328325256218422], [6.375805086700144, 3.4893940536471666], [6.156542242457566, 3.6139240142360736], [5.9151001960879235, 3.7050655460222957], [5.657959981812557, 3.766251445559808], [5.390156453547158, 3.800916513189375], [5.115645536258125, 3.8122445452906595], [4.83748522214471, 3.803003950989986], [4.557972409796751, 3.7760764488088703], [4.278675993730001, 3.7333614116468987], [4.000727032441299, 3.676546261636979], [3.7249075772500895, 3.6071093541155888], [3.451721008427051, 3.5263542734470823], [3.181431073172305, 3.4355118057758727], [2.914152394349546, 3.3356355266000914], [2.649897096637427, 3.2276383649785525], [2.388800893455666, 3.1118807719516983], [2.1310750294932967, 2.988473099068959], [1.8769365715523652, 2.857466921674594], [1.6273080481184596, 2.7175370453860355], [1.3832737407372133, 2.5673130345619892], [1.1465409105683113, 2.404670564712965], [0.9147473311241805, 2.2340840479809896], [0.6869039261863994, 2.057293690508062], [0.4622390529258401, 1.8755799674367934], [0.2400728181905872, 1.6900293734838518], [0.019806513476605336, 1.5015769249329756], [-0.1991575698870045, 1.311141905649184], [-0.41741373578309005, 1.1196310202771609], [-0.6349850619543485, 0.9283281187096861], [-0.8539621735170297, 0.7399447812182145], [-1.07569216645859, 0.5575269907443774], [-1.3013548720069146, 0.3843415567073892], [-1.5318619502769226, 0.2241249266837716], [-1.7676360284468524, 0.08125316223153292], [-2.0082562529335117, -0.03928774678410586], [-2.2521011702424567, -0.13187829511766047], [-2.4959711258973245, -0.19043132231978388], [-2.7347712753732427, -0.20886090599162402], [-2.9611961312165658, -0.18145458058806604], [-3.1650700423714238, -0.10356960140056998], [-3.3300583142903406, 0.02919134928663455], [-3.4621956930306257, 0.19532935898294956], [-3.563142597706195, 0.38762199830331334], [-3.634923840289848, 0.6005596107230909], [-3.6785256715477073, 0.830351960803995], [-3.6947846056893345, 1.0736399136647088], [-3.6850637794797114, 1.3265678909939096], [-3.6499580839665775, 1.5788402852087124], [-3.6383808670017785, 1.822834099010659], [-3.6555790944961766, 2.056469609193421], [-3.7068661744605644, 2.2759248730195187], [-3.7989156081930133, 2.4752919275846574], [-3.9437986544502057, 2.6410663231522813], [-4.130113975946353, 2.7704642766435956], [-4.347551989102646, 2.8606983091567684], [-4.58530833139308, 2.910080396731514], [-4.832856254648279, 2.919136906771068], [-5.081554551992777, 2.8916113242673394], [-5.3253950904188905, 2.831176844289595], [-5.5604266214369105, 2.7420698328426596], [-5.784211046201056, 2.6281098709553503], [-5.99471568062987, 2.4917844644734846], [-6.1886740511489995, 2.333503867904337], [-6.359247979572636, 2.1515475313021493], [-6.50792303575435, 1.9522665611709136], [-6.636676538224876, 1.7396386415521423], [-6.747261801713706, 1.516223177260822], [-6.8413014863073425, 1.2838042229992066], [-6.919665380435516, 1.0433779746737524]])
velocities = [2.851495779296184, 2.9551646701034917, 3.0459753183918052, 3.1220608978590687, 3.0709228663850454, 2.779760156294315, 2.5460034323793486, 2.2990623968815926, 2.0374824432450933, 1.7629183278026375, 1.7629183278026375, 1.7629183278026375, 1.7629183278026375, 1.7629183278026375, 1.7629183278026375, 1.9194437814265914, 2.1114220970700064, 2.276469128465595, 2.3203783253640964, 2.3203783253640964, 2.3203783253640964, 2.3203783253640964, 2.3203783253640964, 2.5545483756401275, 2.8127691372516974, 3.0938918188610836, 3.3819281728556976, 3.69554557640899, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.354858361607017, 2.8754102121417167, 2.478315910073245, 2.1755896392146363, 1.9452375680795457, 1.9452375680795457, 1.9452375680795457, 1.9452375680795457, 1.9452375680795457, 1.9452375680795457, 2.0685773156895637, 2.184349737779593, 2.1749325569568696, 2.035454363674706, 1.8734140590353991, 1.7202440021159506, 1.5876872708636816, 1.3767837431661378, 1.3767837431661378, 1.3767837431661378, 1.3767837431661378, 1.3767837431661378, 1.3767837431661378, 1.5818215434396148, 1.7731782376733773, 1.9827194928943783, 2.209458303776141, 2.4424641391638042, 2.66754019881714, 2.919484931821114, 3.1118460403141617, 3.297756858258759, 3.477623007844769, 3.6558283078925893, 3.75, 3.75, 3.6625607853955064, 3.3097758713042853, 3.3097758713042853, 3.3097758713042853, 3.3097758713042853, 3.3097758713042853, 3.3097758713042853, 3.75, 3.75, 3.75, 3.75, 3.75, 3.75, 3.387456184841754, 2.9176218951998214, 2.5480699262297755, 2.236390589636351, 1.9629017917222888, 1.721476910622896, 1.5070860735654756, 1.3239475525472986, 1.15, 1.15, 1.15, 1.15, 1.15, 1.15, 1.3559818699258617, 1.4782990113994863, 1.635978328605495, 1.7871377064312404, 1.680094252392452, 1.450213314312512, 1.2161809068154272, 1.2161809068154272, 1.2161809068154272, 1.2161809068154272, 1.2161809068154272, 1.2161809068154272, 1.3221341883879394, 1.4407631360683422, 1.5596325297195952, 1.6721177095032107, 1.8031387711696745, 1.8961043188060456, 1.8961043188060456, 1.8961043188060456, 1.8961043188060456, 1.8961043188060456, 1.8961043188060456, 2.062806642000884, 2.2218312498618684, 2.370721349540163, 2.5246699931745256, 2.636485676061513, 2.7445899325461935]
steerings = [2.227521120007225, 2.0739073665284655, 1.9520419554299928, 1.8580237829662052, 1.7913911045719024, 1.7414698942255633, 1.7088184698717817, 1.7217637825688337, 1.79024826227861, 1.9204428731832663, 2.344036613792104, 2.7945515367315448, 3.4277999881942733, 4.366068325328969, 5.836397015330769, 4.920861459301729, 4.065108908175543, 3.496261545936812, 3.0129767940857746, 2.7017259955423305, 2.42662931981227, 2.412120471982968, 3.3650381087351047, 2.775872635154224, 2.289313529524986, 1.8920236994772723, 1.5833772778407857, 1.3259878059800678, 1.1135538292353728, 0.9391292419922856, 0.792089527541615, 0.6478872961277685, 0.5425325359067201, 0.44424785275655765, 0.36461707729533216, 0.26475907975832497, 0.19298829790608446, 0.13115665646764227, 0.07848988333006769, -0.11268140431999576, -0.15557357222037, -0.18341816452700918, -0.21874974036697173, -0.24719970388476278, -0.2724158065381362, -0.2928986846695203, -0.3057432463587734, -0.30771421228681833, -0.2964223292131467, -0.27303629912413363, -0.24981463823558198, -0.23573778518867117, -0.24133622500892857, -0.249429647102802, -0.2740248102547254, -0.2996244981246543, 0.37758400780808954, 0.7283016005793698, 1.07042562326246, 1.6090390900747944, 2.1906050194041202, 2.9494183635358526, 3.8284867648688476, 4.7909186426454236, 4.235551822833191, 3.797795731494435, 3.6275230881434557, 3.502437922389727, 3.435976390888887, 3.5047805642515475, 3.6016767593996946, 3.8308038623724303, 4.3747900974465335, 5.166292560489296, 6.130654014128189, 7.202318426201162, 9.597526405017843, 7.256119754557123, 5.768821805357756, 4.611096865134042, 3.711847251730364, 3.0367206498384567, 2.545533534852673, 2.1249316944748537, 1.8702463231644781, 1.6652589195101353, 1.4974155095979225, 1.3549609707611083, 1.2211098462345067, 1.1063349403455816, 1.0056561066568963, 0.9714521027141119, 0.9682747049317939, 0.9721591467962128, 1.1549537319242082, 1.3499832785972437, 1.6531831806977344, 1.0678475082127994, 0.8350709547516642, 0.6617488010848531, 0.5143668809283605, 0.3878803638874543, 0.2643031326181786, 0.14316006924124033, 0.033229383829400404, -0.3530785483944176, -0.722357273195079, -1.1198808853531392, -1.5782123385501532, -2.1276475430481323, -2.7900170045623867, -3.622863817775477, -4.704884088174108, -6.121842121938275, -7.99821722537874, -10.387185256160949, -13.825633238945597, -9.897193610467246, -8.314934049806972, -6.781366742178578, -5.67875489982252, -4.783127740376075, -4.001931534971096, -3.718995862443947, 3.4437332687063846, 4.779238988866129, 6.428388752658495, 8.642557583214366, 12.337376448495627, 10.416015601592916, 8.757193162430251, 7.4652231105511655, 6.490129054016075, 5.578094364585013, 5.007123487046454, 4.495305456844757, 4.088906589128799, 3.9070448996104292, 4.142669209997243, 5.043062341359569, 4.259326456899324, 3.670564440902832, 3.223487555807374, 2.842017555596305, 2.6058942823165574, 2.404531357324601]
lookahead_points = 5
min_speed = 1.15
max_speed = 3.75
print(track_name, len(race_line), len(velocities), len(steerings))

MIN_REWARD = 1e-3
STEPS_PER_SECOND = 15

EXPECTED_SLOW_COMPLETION_TIME = 35
EXPECTED_FASTEST_COMPLETION_TIME = 20
AVG_SPEED = 2.5
AVG_REWARD_PER_STEP = 0.5
AVG_REWARD_PER_LENGTH = AVG_REWARD_PER_STEP * STEPS_PER_SECOND / AVG_SPEED

HEADING_WEIGHT = 55
CENTER_WEIGHT = 30
SPEED_WEIGHT = 15
PROGRESS_WEIGHT = 1

def reward_function(params):

  # ---------------------- Off-track Penalty ---------------------- #

  # Penalize if off track
  if not params['all_wheels_on_track']:
    return MIN_REWARD
  
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
  
  # --------------------------- Direction --------------------------- #

  # calculate track direction angle
  track_vector = race_line[closest_waypoints[1]]-race_line[closest_waypoints[0]]
  track_direction = np.arctan2(track_vector[1], track_vector[0])*180/np.pi


  steering_difference = abs(steering_angle - steerings[closest_waypoints[0]])
  heading_difference = abs(track_direction-heading)
  heading_difference = heading_difference if heading_difference < 180 else 360-heading_difference

  # punish hard if heading direction is way off
  if heading_difference > 30 or steering_difference > 30:
    return MIN_REWARD

  # when direction difference is 20, the reward is 1/e^2 ~ 0.1
  heading_reward = np.exp(-2 * (heading_difference / 20)**2) if heading_difference < 20 else 0.1
  steering_reward = np.exp(-2 * (steering_difference / 20)**2) if steering_difference < 20 else 0.1

  # --------------------------- Center --------------------------- #

  # fraction of the distance to the center line
  cx, cy = (race_line[closest_waypoints[0]] + race_line[closest_waypoints[1]]) / 2
  distance_from_race_line = np.sqrt((cx - x)**2 + (cy - y)**2)
  track_fraction = 2 * distance_from_race_line / track_width
  
  # punish hard if too far from center line
  if 2 * distance_from_center > track_width:
    return MIN_REWARD

  # when beyond 2/3 of the track width, the reward is 1/e^2 ~ 0.1
  center_reward = np.exp(-2 * (track_fraction / 0.67)**2) if track_fraction > 0.67 else 0.1

  # --------------------------- Speed --------------------------- #

  # difference in expected speed vs actual speed
  ideal_speed = velocities[closest_waypoints[0]]
  speed_difference = abs(ideal_speed - speed)
  
  # punish hard if too slow or speed is far from ideal
  if speed < 0.5 or speed_difference > 1:
    return MIN_REWARD
  
  # when speed deviates from ideal_speed by 0.67, 1/e^2 ~ 0.1
  speed_reward = np.exp(-2 * (speed_difference / 0.67)**2) if speed_difference > 0.67 else 0.1
  
  # --------------------------- Progress --------------------------- #

  progress_reward = 0
  if (progress == 100):
    time = steps / STEPS_PER_SECOND
    expected_total_reward = AVG_REWARD_PER_LENGTH * track_length
    
    # interpolate between slow and fast steps
    normalized_time = (time - EXPECTED_SLOW_COMPLETION_TIME) / (EXPECTED_FASTEST_COMPLETION_TIME - EXPECTED_SLOW_COMPLETION_TIME)
    progress_reward = expected_total_reward * normalized_time
    progress_reward = progress_reward if progress_reward > 0 else 0

  # --------------------------- Total --------------------------- #

  reward = HEADING_WEIGHT*heading_reward + CENTER_WEIGHT*center_reward + SPEED_WEIGHT*speed_reward + PROGRESS_WEIGHT*progress_reward
  reward = reward if reward > MIN_REWARD else MIN_REWARD
  print('=============== <REWARDS> ===============')
  print('steering_reward:', steering_reward)
  print('heading_reward:', heading_reward)
  print('center_reward:', center_reward)
  print('speed_reward:', speed_reward)
  print('progress_reward:', progress_reward)
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
  print('min_speed', min_speed)
  print('max_speed', max_speed)
  print('track_direction:', track_direction)
  print('steering_difference:', steering_difference)
  print('heading_difference:', heading_difference)
  print('distance_from_race_line:', distance_from_race_line)
  print('track_fraction:', track_fraction)
  print('speed_difference:', speed_difference)
  print('lookahead_points:', lookahead_points)
  print('=============== </MISC> ===============')

  return float(reward)
