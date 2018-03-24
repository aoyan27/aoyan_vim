Vim�UnDo� ��8��S\�=�d)�P���)�)T�ʳ�!�ֆ_   �   $	vaa.setPoints(pose1, pose2, pose3);   k   !                       Z��G    _�                     ,        ����                                                                                                                                                                                                                                                                                                                            +           ,           V        Z�sM     �   ,   /   �    �   ,   -   �    5�_�                    -       ����                                                                                                                                                                                                                                                                                                                            +           ,           V        Z�s]     �   ,   .   �      T		sub2 = n.subscribe<geometry_msgs::TransformStamped>("/vicon/person_1/person_1", 1,5�_�                    -   F    ����                                                                                                                                                                                                                                                                                                                            +           ,           V        Z�sb     �   ,   .   �      T		sub3 = n.subscribe<geometry_msgs::TransformStamped>("/vicon/person_1/person_1", 1,5�_�                    -   O    ����                                                                                                                                                                                                                                                                                                                            +           ,           V        Z�sd    �   ,   .   �      T		sub3 = n.subscribe<geometry_msgs::TransformStamped>("/vicon/person_2/person_1", 1,5�_�                    .       ����                                                                                                                                                                                                                                                                                                                            +           ,           V        Z�sh    �   -   /   �      ,				&ArrowsPublisher::Point2Callback, this);5�_�                    >        ����                                                                                                                                                                                                                                                                                                                            9   $       >          V   '    Z�su     �   >   E   �    �   >   ?   �    5�_�                    ?       ����                                                                                                                                                                                                                                                                                                                            9   $       >          V   '    Z�sx     �   >   @   �      K	void Point2Callback(const geometry_msgs::TransformStamped::ConstPtr& msg){5�_�      	              @       ����                                                                                                                                                                                                                                                                                                                            9   $       >          V   '    Z�s     �   ?   A   �      4		pointSubstitution(p2, msg->transform.translation);5�_�      
           	   A       ����                                                                                                                                                                                                                                                                                                                            9   $       >          V   '    Z�s�     �   @   B   �      @		pointSubstitution(pose2.position, msg->transform.translation);5�_�   	              
   B       ����                                                                                                                                                                                                                                                                                                                            9   $       >          V   '    Z�s�     �   A   C   �      ?		quatSubstitution(pose2.orientation, msg->transform.rotation);5�_�   
                 C   
    ����                                                                                                                                                                                                                                                                                                                            9   $       >          V   '    Z�s�    �   B   D   �      		flag_cb2 = true;5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       Z�s�     �         �    �         �    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       Z�s�    �         �      	bool flag_cb2;5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       Z�s�     �         �    �         �    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       Z�s�    �         �      	geometry_msgs::Point p2;5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       Z�s�    �                	geometry_msgs::Pose pose4;5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        Z�s�     �         �    �         �    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        Z�s�    �         �      	ros::Subscriber sub2;5�_�                    +       ����                                                                                                                                                                                                                                                                                                                                                  V        Z�s�     �   *   ,   �      b		sub1 = n.subscribe<geometry_msgs::TransformStamped>("/vicon/infant_velodyne/infant_velodyne", 1,5�_�                    ,       ����                                                                                                                                                                                                                                                                                                                                                  V        Z�s�    �   *   ,   �      b		sub1 = n.subscribe<geometry_msgs::TransformStamped>("/vicon/infant_velodyne/infant_velodyne", 1,   (&ArrowsPublisher::Point1Callback, this);�   +   -   �      ,				&ArrowsPublisher::Point1Callback, this);5�_�                    +   6    ����                                                                                                                                                                                                                                                                                                                                                  V        Z�s�     �   *   -   �      �		sub1 = n.subscribe<geometry_msgs::TransformStamped>("/vicon/infant_velodyne/infant_velodyne", 1, &ArrowsPublisher::Point1Callback, this);5�_�                    ,   1    ����                                                                                                                                                                                                                                                                                                                                                  V        Z�s�   	 �   +   .   �      Y				"/vicon/infant_velodyne/infant_velodyne", 1, &ArrowsPublisher::Point1Callback, this);5�_�                    i        ����                                                                                                                                                                                                                                                                                                                            i          s           V        Z�s�   
 �   h   i          L	pose3.position.x = pose1.position.x + pose1.orientation.x*pose2.position.x;   8	pose3.position.y = pose1.position.y + pose2.position.y;   L	pose3.position.z = pose1.orientation.z*pose1.position.z + pose2.position.z;   8	quatSubstitution(pose3.orientation, pose1.orientation);   A	pose3.orientation.w = pose1.orientation.w + pose2.orientation.w;       8	pose4.position.x = pose1.position.x - pose2.position.x;   L	pose4.position.y = pose1.position.y - pose1.orientation.y*pose2.position.y;   8	pose4.position.z = pose1.position.z - pose2.position.z;   8	quatSubstitution(pose4.orientation, pose2.orientation);   A	pose4.orientation.w = pose1.orientation.w - pose2.orientation.w;5�_�                    i        ����                                                                                                                                                                                                                                                                                                                            i          i           V        Z�s�    �   h   i           5�_�                    b       ����                                                                                                                                                                                                                                                                                                                            i          i           V        Z�s�     �   a   c   �      %	if(rtn) flag_cb1 = flag_cb2 = false;5�_�                    b       ����                                                                                                                                                                                                                                                                                                                            i          i           V        Z�s�    �   a   c   �      0	if(rtn) flag_cb1 = flag_cb2 =flag_cb3 =  false;5�_�                    j       ����                                                                                                                                                                                                                                                                                                                            i          i           V        Z�t     �   i   k   �      	vaa.setPoints(pose1, pose2);5�_�                    j        ����                                                                                                                                                                                                                                                                                                                            j           j           V        Z��=     �   j   l   �    �   j   k   �    5�_�                    j   "    ����                                                                                                                                                                                                                                                                                                                            j           j           V        Z��A     �   i   k          $	vaa.setPoints(pose1, pose2, pose3);5�_�                    k   !    ����                                                                                                                                                                                                                                                                                                                            j           j           V        Z��D     �   j   l   �      $	vaa.setPoints(pose1, pose2, pose3);5�_�                     k       ����                                                                                                                                                                                                                                                                                                                            j           j           V        Z��F    �   j   l   �      !	vaa.setPoints(pose1, pose2, p3);5��