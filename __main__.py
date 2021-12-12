import curses
import time
from curses import wrapper

import PlayerUI

"""
keyword = input('What do you wanna search?\n')
result = search.by_keyword(keyword)
search_results = parse_result(result)
display.show_result(search_results)
target_number = int(input('Which video would you like?\n'))

url = search_results[target_number - 1].get_playable_url()

player = Player()
player.load_url(url)
player.play()
time.sleep(20)
player.pause()
"""
def main(self):
    curses.noecho()
    curses.cbreak()
    curses.curs_set(False)
    player_ui = PlayerUI.PlayerUI(3, 3, 10, 100)
    player_ui.set_artist("Slipknot")
    player_ui.set_title("Psychosocial")
    player_ui.update_full_title()
    player_ui.set_total_time(500)
    for i in range(0, 500):
        player_ui.update_current_time(i)
        time.sleep(1)
wrapper(main)