import search
import cache
import player
import display
import playlist

keyword = input('What do you wanna search?\n')
result = search.by_keyword(keyword)
display.show_result(result)
target_number = int(input('Which video would you like?\n'))
target_videoId = result['result'][target_number - 1]['id']
cache.download(target_videoId)
player.play(target_videoId + '.mp3')
