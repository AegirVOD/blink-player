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
#target_videoId = result['result'][target_number - 1]['id']
#cache.download(target_videoId)

#filename = target_videoId + '.mp3'

#filename = '1.mp3'

player = vlc.MediaPlayer(search_results[target_number - 1].get_url())

player.play()
#player.run_mpg123()
#player.play_file()
#time.sleep(3)
#player.pause()
