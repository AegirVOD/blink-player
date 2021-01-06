import os
import pty
import subprocess
import time

player = subprocess.Popen(["mplayer", "5abamRO41fE.mp3"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
time.sleep(10)
player.stdin.write("pause")
player.stdin.flush()
