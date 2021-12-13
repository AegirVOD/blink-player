import curses
import datetime
import time
from time import strftime
from time import gmtime
from curses import wrapper


class PlayerUI(object):

    # The player looks like something like this:
    #
    #         Now playing : Psychosocial - Slipknot
    # 00:30 |========>------------------------------| 4:00
    #
    #

    def __init__(self, begin_y, begin_x, end_y, end_x):
        # Set basic parameters
        self.begin_y = begin_y
        self.begin_x = begin_x
        self.end_y = end_y
        self.end_x = end_x
        self.height = end_y - begin_y
        self.width = end_x - begin_x
        self.current_time = 0  # Length that has already been played, in second
        self.total_time = 42  # Length of the song, in second
        self.title = "Title"
        self.artist = "Artist"
        # Create new panel for player
        self.panel = curses.newwin(self.height, self.width, self.begin_y, self.begin_x)
        # self.panel = curses.initscr()
        # self.panel.keypad(True)
        # Start to draw player

        # Draw player border
        for i in range(0, self.width - 1):
            self.panel.addch(0, i, '-')
        for i in range(1, self.height - 1):
            self.panel.addch(i, 0, '|')
            self.panel.addch(i, self.width - 2, '|')
        for i in range(0, self.width - 1):
            self.panel.addch(self.height - 1, i, '-')

        # Add player title
        self.update_full_title()
        # TODO: Handle oversize title (or too small windows size)

        # Add and initialize progress bar
        self.update_progress_bar()

        # Refresh Panel
        self.panel.refresh()

    @staticmethod
    def sec_to_str(sec):
        return strftime("%M:%S", gmtime(sec))

    def update_progress_bar(self):
        self.panel.addstr(3, 2, self.sec_to_str(self.current_time))
        self.panel.addch(3, 7, '|')
        # Calculate cursor position
        # Cursor position = (end - start) * (current_time / total_time) + start
        cursor_position = int((self.width - 10 - 8) * (self.current_time / self.total_time) + 8)
        for i in range(8, cursor_position):
            self.panel.addch(3, i, '=')
        self.panel.addch(3, cursor_position, '>')
        for i in range(cursor_position + 1, self.width - 9):
            self.panel.addch(3, i, '-')
        self.panel.addch(3, self.width - 9, '|')
        self.panel.addstr(3, self.width - 8, self.sec_to_str(self.total_time))
        self.panel.refresh()

    def update_current_time(self, current_time):
        self.current_time = current_time
        self.update_progress_bar()

    def set_total_time(self, total_time):
        self.total_time = total_time
        self.update_progress_bar()

    def set_title(self, title):
        self.title = title

    def set_artist(self, artist):
        self.artist = artist

    def update_full_title(self):
        full_title = self.title + " - " + self.artist
        self.panel.addstr(1, int((self.width - len(full_title)) / 2), full_title)

class MenuUI(object):
    def __init__(self, begin_y, begin_x, end_y, end_x):
        #Set basic parameters