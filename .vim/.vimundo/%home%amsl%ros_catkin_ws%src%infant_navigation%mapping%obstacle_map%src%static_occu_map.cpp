Vim�UnDo� �&�4�0���{|�����;jΞbmiYl6r�t  �   const float RADIUS = 0.3;   U                          ZqA7    _�                    H        ����                                                                                                                                                                                                                                                                                                                           H         H          V       ZF,     �  H  J  �    �  H  I  �    5�_�                   H       ����                                                                                                                                                                                                                                                                                                                           H         H          V       ZF,     �  G  I          Q	ros::Subscriber sub12 = n.subscribe("/ekf_DgaussAndNDT", 1 , ndt_odom_callback);5�_�                   I   7    ����                                                                                                                                                                                                                                                                                                                           H         H          V       ZF,     �  H  J  �      Q	ros::Subscriber sub12 = n.subscribe("/ekf_DgaussAndNDT", 1 , ndt_odom_callback);5�_�                   I   +    ����                                                                                                                                                                                                                                                                                                                           H         H          V       ZF,     �  H  J  �      E	ros::Subscriber sub12 = n.subscribe("/lcl_", 1 , ndt_odom_callback);5�_�                   I   +    ����                                                                                                                                                                                                                                                                                                                           H         H          V       ZF,      �  H  J  �      E	ros::Subscriber sub12 = n.subscribe("/lcl_", 1 , ndt_odom_callback);5�_�                   I   +    ����                                                                                                                                                                                                                                                                                                                           H         H          V       ZF,0    �  H  J  �      F	ros::Subscriber sub12 = n.subscribe("/lcl_2", 1 , ndt_odom_callback);5�_�                   I       ����                                                                                                                                                                                                                                                                                                                           H         H          V       ZG�f     �  H  J          E	ros::Subscriber sub12 = n.subscribe("/lcl2", 1 , ndt_odom_callback);5�_�      	             G       ����                                                                                                                                                                                                                                                                                                                           H         H          V       ZG�h    �  F  H          K	// ros::Subscriber sub12 = n.subscribe("/ekf_ndt", 1 , ndt_odom_callback);5�_�      
           	  �        ����                                                                                                                                                                                                                                                                                                                           �         �          V       ZG��     �  �  �  �    �  �  �  �    5�_�   	              
  �       ����                                                                                                                                                                                                                                                                                                                           �         �          V       ZG��     �  �  �          =			ndt_theta = ndt_odom.pose.pose.orientation.z + theta_init;5�_�   
                �       ����                                                                                                                                                                                                                                                                                                                           �         �          V       ZG��     �  �  �  �      =			ndt_theta = ndt_odom.pose.pose.orientation.z + theta_init;5�_�                   �       ����                                                                                                                                                                                                                                                                                                                           �         �          V       ZG��     �  �  �  �      G			ndt_theta = tf::getYawndt_odom.pose.pose.orientation.z + theta_init;5�_�                   �   :    ����                                                                                                                                                                                                                                                                                                                           �         �          V       ZG��    �  �  �  �      H			ndt_theta = tf::getYaw(ndt_odom.pose.pose.orientation.z + theta_init;5�_�                    K       ����                                                                                                                                                                                                                                                                                                                                                             Zq@�     �   J   L  �      const float R = 0.1;5�_�                    P       ����                                                                                                                                                                                                                                                                                                                                                             Zq@�     �   O   Q  �      const float local_W = 20.0;5�_�                    Q       ����                                                                                                                                                                                                                                                                                                                                                             Zq@�    �   P   R  �      const float local_H = 20.0;5�_�                     U       ����                                                                                                                                                                                                                                                                                                                                                             ZqA6    �   T   V  �      const float RADIUS = 0.3;5��