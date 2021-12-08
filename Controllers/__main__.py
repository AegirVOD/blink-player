from Models import cache, search, display
from Models.player import Player
import time


keyword = input('What do you wanna search?\n')
result = search.by_keyword(keyword)
display.show_result(result)
target_number = int(input('Which video would you like?\n'))
target_videoId = result['result'][target_number - 1]['id']
cache.download(target_videoId)

filename = target_videoId + '.mp3'

#filename = '1.mp3'

player = Player(filename)
player.run_mpg123()
player.play_file()
time.sleep(3)
player.pause()
