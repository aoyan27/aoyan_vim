Vim�UnDo� ��n�$]��=�s�Р��-�R�t��I�>  "                                      Z�I    _�                    .       ����                                                                                                                                                                                                                                                                                                                                                             Z\�    �  -  .          ,    np.save(dirs+'reward_array.npy', reward)5�_�                    �   *    ����                                                                                                                                                                                                                                                                                                                                                             Z]�    �   �   �  A      *                feat_map[i, 0] = 1.0 / 1.05�_�                    �   )    ����                                                                                                                                                                                                                                                                                                                                                             Z^     �   �   �          >            feat_map[:, i] = z_score_normalize(feat_map[:, i])5�_�                    �   )    ����                                                                                                                                                                                                                                                                                                                                                             Z^    �   �   �          9            #  feat_map[:, i] = normalize(feat_map[:, i])5�_�                       (    ����                                                                                                                                                                                                                                                                                                                                                             Z^�     �        B                      �        A    5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Z^�     �        B                      l3 = L.Linear5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Z^�     �        B                      l3 = L.Linear()5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             Z^�     �        B                      l3 = L.Linear()5�_�      
           	      '    ����                                                                                                                                                                                                                                                                                                                                                             Z^�     �        B      '                l3 = L.Linear(512, 256)5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                             Z^�     �         B      ]                l3 = L.Linear(512, n_out, initialW=np.zeros((n_out, 512), dtype=np.float32)),5�_�   
                    !    ����                                                                                                                                                                                                                                                                                                                                                             Z^�     �         B      ]                l4 = L.Linear(512, n_out, initialW=np.zeros((n_out, 512), dtype=np.float32)),5�_�                       G    ����                                                                                                                                                                                                                                                                                                                                                             Z^�    �         B      ]                l4 = L.Linear(256, n_out, initialW=np.zeros((n_out, 512), dtype=np.float32)),5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             Z_     �      C          �      B    5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             Z_    �              2    print reward.reshape([rows, cols]).transpose()5�_�                    $        ����                                                                                                                                                                                                                                                                                                                                                             Z_=     �   $   &  D              �   $   &  C    5�_�                    %       ����                                                                                                                                                                                                                                                                                                                                                             Z_A     �   $   &  D              h = F.relu5�_�                    %       ����                                                                                                                                                                                                                                                                                                                                                             Z_D     �   $   &  D              h = F.relu(self.l3)5�_�                    %       ����                                                                                                                                                                                                                                                                                                                                                             Z_F     �   $   &  D              h = F.relu(self.l3(h))5�_�                    &       ����                                                                                                                                                                                                                                                                                                                                                             Z_H    �   %   '  D              y = self.l3(h)5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Z_^     �                  print reward5�_�                          ����                                                                                                                                                                                                                                                                                                                                                             Z__    �              5    #  print reward.reshape([rows, cols]).transpose()5�_�                           ����                                                                                                                                                                                                                                                                                                                            1                    V       Zb     �                class DeepIRLNetwork(Chain):   $    def __init__(self, n_in, n_out):   -        super(DeepIRLNetwork, self).__init__(   *                l1 = L.Linear(n_in, 1024),   )                l2 = L.Linear(1024, 512),   (                l3 = L.Linear(512, 256),   ]                l4 = L.Linear(256, n_out, initialW=np.zeros((n_out, 256), dtype=np.float32)),                   )           def __call__(self, x):           h = F.relu(self.l1(x))           h = F.relu(self.l2(h))           h = F.relu(self.l3(h))           y = self.l4(h)           return y       "    def get_reward(self, feature):   B        features = Variable(np.asarray(feature, dtype=np.float32))   #        #  print "features.data : "           #  print features.data   (        reward = self.__call__(features)           #  print "reward__ : "           #  print reward   +        #  reward = reward.data.reshape(-1)           return reward5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       Zb     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       Zb     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       Zb     �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       Zb   	 �        (       �        '    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        Zi�    �   
             import chainer    ;from chainer import cuda, Variable, optimizers, serializers   from chainer import Chain   import chainer.functions as F   import chainer.links as L    5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �           �           V        Z�*     �   �   �  #          �   �   �  "    5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �           �           V        Z�<     �   �   �  #          model.load_model5�_�                    �   +    ����                                                                                                                                                                                                                                                                                                                            �           �           V        Z�C     �   �   �  #      ,    model.load_model(dirs+model_namr, model)5�_�                     �   $    ����                                                                                                                                                                                                                                                                                                                            �           �           V        Z�D     �   �   �  #      ,    model.load_model(dirs+model_namr, model)5�_�                      �       ����                                                                                                                                                                                                                                                                                                                            �           �           V        Z�H    �   �   �          0    serializers.load_npz(dirs+model_name, model)5��