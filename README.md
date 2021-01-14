# ロボットシステム学課題２
ROSを使って入力したアルファベットを大文字と小文字に変換するパッケージです．

# 使い方
１．ワークスペースにパッケージを入れてください．  
２．roscoreを起動してください．  
３．端末を3つ起動し，rosrunを使ってinput.py, lower.py, upper.pyをそれぞれ起動してください．  

＄rosrun mypkg input.py  
＄rosrun mypkg lower.py  
＄rosrun mypkg upper.py  

４．input.pyを起動すると”アルファベットを入力してください”と表示されますので文字を入力してください．入力した文字がlower.py, upper.pyによってそれぞれ小文字，大文字で出力されます．  
５．Ctr+cで停止します．すべての端末で行ってください．  

# 動作環境
Rasberry Pi 3  
Ubuntu 20.04  
ROS noetic  



*このパッケージはRyuichiUeda氏の作成したパッケージを改造して作成されたものです．
