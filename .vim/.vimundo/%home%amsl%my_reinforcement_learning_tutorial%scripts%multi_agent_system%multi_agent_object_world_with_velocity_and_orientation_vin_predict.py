Vim�UnDo� �ː��֕�~�~ZPC?$�q�#�Om-2F�  c                                  Zq��    _�                    2        ����                                                                                                                                                                                                                                                                                                                           2          O           V        Zq��    �  1  3          7            #  velocities[0] = env.movement[actions[0]]�  2  4          O            #  orientations[0] = math.atan2(velocities[0][0], velocities[0][1])�  3  5           �  4  6          7            #  actions[1] = get_enemy_agent_action(env)�  5  7          7            #  velocities[1] = env.movement[actions[1]]�  6  8          O            #  orientations[1] = math.atan2(velocities[1][0], velocities[1][1])�  7  9          *            #  print "actions : ", actions�  8  :           �  9  ;                      �  :  <          6            #  #  #  actions = env.get_sample_action()�  ;  =          /            #  #  #  print "action : ", actions�  <  >          I            #  observation, reward, episode_end, info = env.step(actions)�  =  ?          1            #  print "next_state : ", observation�  >  @          5            #  print "next_velocities : ", velocities�  ?  A          9            #  print "next_orientations : ", orientations�  @  B          (            #  print "reward : ", reward�  A  C          2            #  print "episode_end : ", episode_end�  B  D                      #  time.sleep(0.5)�  C  E           �  D  F          =            #  if (episode_end[0]==1 and episode_end[1]==1) \�  E  G          G                    #  or (episode_end[0]==2) or (episode_end[0] == 3):�  F  H          >                #  if episode_end[0]==1 and episode_end[1]==1:�  G  I          )                    #  success_times += 1�  H  J                          #  break�  I  K           �  J  L          5        #  if episode_end[0]!=1 or episode_end[1]!=1:�  K  M                       #  failed_times += 1�  L  N           �  M  O          .    #  print "success_times : ", success_times�  N  P          ,    #  print "failed_times : ", failed_times5�_�                   +        ����                                                                                                                                                                                                                                                                                                                           2          O           V        Zq�     �  *  ,  c                  start = time.time5�_�                   +       ����                                                                                                                                                                                                                                                                                                                           2          O           V        Zq�     �  *  ,  c                  start = time.time()5�_�                   +       ����                                                                                                                                                                                                                                                                                                                           2          O           V        Zq�     �  *  ,  c                  start = time.time()5�_�                   /       ����                                                                                                                                                                                                                                                                                                                           3          P           V        Zq�3     �  /  0  c                  �  /  1  d      $            elapsed_time = time.time5�_�                   0   $    ����                                                                                                                                                                                                                                                                                                                           3          P           V        Zq�5     �  /  1  d      &            elapsed_time = time.time()5�_�                   0   %    ����                                                                                                                                                                                                                                                                                                                           3          P           V        Zq�5     �  /  1  d      .            elapsed_time = time.time() - start5�_�      	             0   -    ����                                                                                                                                                                                                                                                                                                                           4          Q           V        Zq�7     �  0  1  d                  �  0  2  e                   print 5�_�      
           	  1       ����                                                                                                                                                                                                                                                                                                                           4          Q           V        Zq�A     �  0  2  e                   print ()5�_�   	              
  1       ����                                                                                                                                                                                                                                                                                                                           4          Q           V        Zq�A     �  0  2  e      .             print ("elapsed_time:{0}".format)5�_�   
                1   -    ����                                                                                                                                                                                                                                                                                                                           4          Q           V        Zq�A     �  0  2  e      <             print ("elapsed_time:{0}".format(elapsed_time))5�_�                   1   :    ����                                                                                                                                                                                                                                                                                                                           4          Q           V        Zq�A     �  0  2  e      ?             print ("elapsed_time:{0}".format(elapsed_time) + )5�_�                   1   >    ����                                                                                                                                                                                                                                                                                                                           4          Q           V        Zq�A     �  0  2  e      F             print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")5�_�                   1   E    ����                                                                                                                                                                                                                                                                                                                           4          Q           V        Zq�A     �  0  2  e      F             print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")5�_�                    1       ����                                                                                                                                                                                                                                                                                                                           4          Q           V        Zq�E    �  0  2  e      9print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")�  /  2  e      .            elapsed_time = time.time() - start   E            print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")5��