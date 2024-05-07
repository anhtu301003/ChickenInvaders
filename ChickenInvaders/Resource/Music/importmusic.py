import os

filepath = os.path.abspath(__file__)
filedir = os.path.dirname(filepath)
musicchicken = os.path.join(filedir, "chickendie.wav")
musicgameover = os.path.join(filedir, "gameover.wav")
musicwinner = os.path.join(filedir, "winner.wav")