Vim�UnDo� id�oʈ}G|7I۸���VS1ɟ	�O��f��   �   		ofs << "    6Dof: [";   �                          Zv��    _�                     �       ����                                                                                                                                                                                                                                                                                                                                                             Zv�     �   �   �   �      		ofs << diff_y << ", 0.0, ";5�_�                    �        ����                                                                                                                                                                                                                                                                                                                                                             Zv�%     �   �   �   �      ?		ofs << diff_yaw << ", 0.0, 0.0] # x, y, z, yaw, pitch, roll";5�_�                    �   &    ����                                                                                                                                                                                                                                                                                                                                                             Zv�8     �   �   �   �      5		ofs << diff_yaw << "] # x, y, z, yaw, pitch, roll";5�_�                    �   4    ����                                                                                                                                                                                                                                                                                                                                                             Zv�<    �   �   �   �      6		ofs << diff_yaw << "] # x, y, z, roll, pitch, roll";5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             Zv�|    �   �   �   �      		ofs << "    6Dof: [";5�_�                     �        ����                                                                                                                                                                                                                                                                                                                            �          �          V       Zv��    �   �   �          	ofs_args.close();�   �   �           �   �   �          	}�   �   �          #		cerr << "ofs_args ERROR" << endl;�   �   �          	}else{�   �   �          :		ofs_args << diff_yaw << " 0.0 0.0 /world /map 100\" />";�   �   �           		ofs_args << diff_y << " 0.0 ";�   �   �          		ofs_args << diff_x << " ";�   �   �          		ofs_args << fixed;�   �   �          		ofs_args << "args=\"";�   �   �          	if(ofs_args){�   �   �          a	std::ofstream ofs_args("/home/amsl/TFmap2vicon.args"); //launchだと~/.rosがカレントパス5��