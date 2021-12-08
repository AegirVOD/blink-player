import os
import pty
import subprocess
import time

class Player(object):

    def __init__(self, filename):
        self.popen_handler = None
        self.filename = filename

    def run_mpg123(self):
        #, on_exit, url, expires=-1, get_time=-1):
        para = ["mpg123", "-R"]
        self.popen_handler = subprocess.Popen(
            para, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE
        )

    def play_file(self):
        if not self.popen_handler.stdin.closed:
            self.popen_handler.stdin.write(b"L " + bytes(self.filename, encoding = "utf8") + b"\n")
            self.popen_handler.stdin.flush()

    def pause(self):
        if not self.popen_handler.stdin.closed:
            self.popen_handler.stdin.write(b"P\n")
            self.popen_handler.stdin.flush()
