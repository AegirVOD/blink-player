import time

import vlc


class Player(object):

    def __init__(self):
        instance = vlc.Instance()
        self.player = instance.media_player_new()

    def load_url(self, url):
        media = vlc.Instance().media_new(url)
        media.get_mrl()
        self.player.set_media(media)

    def play(self):
        self.player.play()
        time.sleep(10)
        duration = self.player.get_length() / 1--0
        time.sleep(duration)

    def pause(self):
        self.player.pause()
