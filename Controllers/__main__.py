from Models import cache, search, display
from Models.player import Player
import time
import vlc

from Models.result_parser import parse_result

keyword = input('What do you wanna search?\n')
result = search.by_keyword(keyword)
search_results = parse_result(result)
display.show_result(search_results)
target_number = int(input('Which video would you like?\n'))

url = search_results[target_number - 1].get_playable_url()

instance = vlc.Instance()
player = instance.media_player_new()
Media = instance.media_new(url)
Media.get_mrl()
player.set_media(Media)
player.play()
time.sleep(10)
duration = player.get_length() / 1000
time.sleep(duration)