Vim�UnDo� !�XR�-hL�g�w��C��Z���8�$Җ�N   �   =        while prior[pos[1], pos[0]] == 0 and num_traj < 1000:   �   <      $       $   $   $    Z *    _�                    P       ����                                                                                                                                                                                                                                                                                                                            f          f          V       Z�n     �   O   Q   �          model(map, s1, s2, label)5�_�                    P       ����                                                                                                                                                                                                                                                                                                                            f          f          V       Z�o     �   O   Q   �            = model(map, s1, s2, label)5�_�                    P   "    ����                                                                                                                                                                                                                                                                                                                            f          f          V       Z�q    �   O   R   �      "     _ = model(map, s1, s2, label)5�_�                   P       ����                                                                                                                                                                                                                                                                                                                            g          g          V       Zƌ     �   M   Q   �      D    label = chainer.Variable(np.reshape(np.array(label_data), (1,)))   _ = model(map, s1, s2, label)�   N   P   �          _ = model(map, s1, s2, label)�   O   Q   �      "     _ = model(map, s1, s2, label)5�_�                    Q       ����                                                                                                                                                                                                                                                                                                                            g          g          V       ZƏ    �   P   R   �           print _5�_�      	              {       ����                                                                                                                                                                                                                                                                                                                            g          g          V       Z�:    �   z   |                  print pos5�_�      
           	   Q   
    ����                                                                                                                                                                                                                                                                                                                            g          g          V       Z�    �   P   R              print _5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                            g          g          V       Z�o     �          �      (#  from __future__ import print_function5�_�   
                         ����                                                                                                                                                                                                                                                                                                                            h          h          V       Z�p    �          �       5�_�                    F       ����                                                                                                                                                                                                                                                                                                                            i          i          V       Z��     �   E   G              print map_data.shape5�_�                    G       ����                                                                                                                                                                                                                                                                                                                            i          i          V       Z��    �   F   H              print map_data5�_�                    _        ����                                                                                                                                                                                                                                                                                                                            ^           _           V        Z��     �   _   a   �    5�_�                   _        ����                                                                                                                                                                                                                                                                                                                            ^           _           V        Z��     �   _   b   �    �   _   `   �    5�_�                    ^        ����                                                                                                                                                                                                                                                                                                                            ^          _          V       Z��     �   ^   `              size_2 = 16�   ]   _              size_1 = 165�_�                    `       ����                                                                                                                                                                                                                                                                                                                            ^          _          V       Z��     �   _   a   �          size_1 = 165�_�                    a       ����                                                                                                                                                                                                                                                                                                                            ^          _          V       Z��     �   `   b   �          size_2 = 165�_�                    d        ����                                                                                                                                                                                                                                                                                                                            d          d          V       Z��     �   d   f   �    �   d   e   �    5�_�                    d       ����                                                                                                                                                                                                                                                                                                                            d          d          V       Z��     �   c   e              max_obs = 405�_�                    e       ����                                                                                                                                                                                                                                                                                                                            d          d          V       Z��    �   d   f   �          max_obs = 405�_�                            ����                                                                                                                                                                                                                                                                                                                               	          	       V   	    Z}�     �      !   �    �          �    5�_�                           ����                                                                                                                                                                                                                                                                                                                               	          	       V   	    Z}�     �                     pos = [10, 10]5�_�                            ����                                                                                                                                                                                                                                                                                                                               	          	       V   	    Z}�     �      !   �          pos = [10, 10]5�_�                            ����                                                                                                                                                                                                                                                                                                                               	          	       V   	    Z}�   	 �      !   �          pos = [20, 10]5�_�                    �   9    ����                                                                                                                                                                                                                                                                                                                               	          	       V   	    Z}�   
 �   �   �   �      <        while prior[pos[1], pos[0]] == 0 and num_traj < 100:5�_�                    �   <    ����                                                                                                                                                                                                                                                                                                                               	          	       V   	    Z��    �   �   �   �      =        while prior[pos[1], pos[0]] == 0 and num_traj < 1000:5�_�                    b       ����                                                                                                                                                                                                                                                                                                                               	          	       V   	    Z )�     �   a   c              size_2 = 325�_�                    a       ����                                                                                                                                                                                                                                                                                                                               	          	       V   	    Z )�     �   `   b              size_1 = 325�_�                     `       ����                                                                                                                                                                                                                                                                                                                               	          	       V   	    Z )�     �   _   a              #  size_2 = 165�_�      !               _       ����                                                                                                                                                                                                                                                                                                                               	          	       V   	    Z )�     �   ^   `              #  size_1 = 165�_�       "           !   f       ����                                                                                                                                                                                                                                                                                                                               	          	       V   	    Z *      �   e   g              max_obs = 605�_�   !   #           "   e       ����                                                                                                                                                                                                                                                                                                                               	          	       V   	    Z *     �   d   f              #  max_obs = 405�_�   "   $           #           ����                                                                                                                                                                                                                                                                                                                               	          	       V   	    Z *     �      !              pos = [20, 20]5�_�   #               $          ����                                                                                                                                                                                                                                                                                                                               	          	       V   	    Z *    �                     #  pos = [10, 10]5�_�                    `        ����                                                                                                                                                                                                                                                                                                                            ^           _           V        Z��     �   `   a   �    �   `   a   �          size_1 = 16       size_2 = 165�_�                    Q       ����                                                                                                                                                                                                                                                                                                                            g          g          V       Z�x     �   Q   R   �    �   P   R   �      ?     print _https://qiita.com/mitmul/items/eccf4e0a84cb784ba84a5�_�                     j       ����                                                                                                                                                                                                                                                                                                                                                             Z��     �   i   k   �          a   print "========="5��