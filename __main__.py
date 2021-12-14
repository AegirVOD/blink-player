import curses
import time
from curses import wrapper


import UI
import search
from result_parser import parse_result

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
    result = search.by_keyword("No.10 jersey not for")
    search_results = parse_result(result)
    curses.noecho()
    curses.cbreak()
    curses.curs_set(False)
    curses.start_color()

    """
    player_ui = UI.PlayerUI(3, 3, 10, 100)
    player_ui.set_artist("Slipknot")
    player_ui.set_title("Psychosocial")
    player_ui.update_full_title()
    player_ui.set_total_time(500)
    for i in range(0, 500):
        player_ui.update_current_time(i)
        time.sleep(1)
    """

    menu_ui = UI.MenuUI(3, 3, 10, 100)
    menu_ui.update_items_result(search_results)
    menu_ui.highlight_item(3)
    time.sleep(10)


wrapper(main)
