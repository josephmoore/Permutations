"""
Copyright 2010 Joseph Moore

This file is part of Permutations.

Permutations is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Permutations is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Permutations.  If not, see <http://www.gnu.org/licenses/>.
"""

import curses
import time
from poem import Poem, Book
import os
import json

class Window:
    def __init__(self):
        self.linepause = 0.5
        self.charpause = 0.1
        self.poempause = 8.0
        self.gutter = 6
        self.poems = []
        
        try:
            self.screen = curses.initscr()
            curses.noecho()
            curses.cbreak()
        except:
            self._restore()
            
        s_size = self.screen.getmaxyx()
        self.length = s_size[0] * s_size[1]
        self.cols = s_size[1]
        self.rows = s_size[0]
        
    def _restore(self):
      curses.nocbreak()
      curses.echo()
      curses.endwin()

    def add_poems(self, poem_strings):
        for p in poem_strings:
            self.poems.append(Poem(p))

    def add_poem(self, poem):
        self.poems.append(poem)
    
    def draw(self):
        p = 0
        book = Book(self.poems)
        padding = 1
        y = 0
        x = padding
        
        def col_count(poem):
            count = (self.width - (padding * 2)) / (poem.line_length + self.gutter)
            return count

        try:
            while True:
                if(y >= self.rows):
                    y = 0
                    col_width = book.poems[p].max_line_length + self.gutter
                    x = x + col_width
                    if x + col_width > self.cols:
                        self.screen.clear()
                        x = 0

                line = book.poems[p].read_line()

                if line == None:
                    curses.flash()
                    time.sleep(self.poempause)
                    curses.flash()
                    self.screen.clear()
                    if p == book.poem_count - 1:
                        p = 0
                    else:
                        p = p +  1
                    
                    y = 0
                    x = 1
                    line = book.poems[p].read_line()
                    
                step = 0
                for char in line:
                    self.screen.addstr(y,x + step, char)
                    self.screen.refresh()
                    time.sleep(self.charpause)
                    step = step + 1
                step = 0
                self.screen.refresh()
                time.sleep(self.linepause)
                y = y + 1
        except:
            self._restore()

        self._restore()


if __name__ == '__main__':
    
    wd = os.path.dirname(__file__)
    f = open(wd + "/data.json","r")
    json = json.load(f)
    f.close()
    poems = json["poems"]
             
    win = Window()
    win.add_poems(poems)
    win.poempause = 3.0 #pause in seconds between poems
    win.linepause = 0.1 #pause in seconds between lines
    win.charpause = 0.01 #pause in seconds between characters
    win.draw()
