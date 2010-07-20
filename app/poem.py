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


"""
Works thank you for your collaboration, but they can also create themselves on their own; thus:
Come to free the words 
To free the words come 
Free the words to come 
The words come to free 
Words come to free thee!
The possible permutations are 5x4x3x2x1=120 lines. Therefore a 120-line poem without an author. Where is the poet Brion Gysin?

-Brion Gysin
"""

import itertools
import math

class Poem:
    def __init__(self, s, title=True):
        self.sequence = s.split()
        self.text = []
        self.is_reading = False
        self.max_line_length = len(s)
        if title == True:
            self.title = s
                
        def make_perms(sequence):
            """
            Create a list of all possible permutations of a
            given sequence.
            """
            for p in itertools.permutations(sequence):
                p = list(p)
                p.reverse()
                line = " ".join(p)
                self.text.append(line)
            self.text.reverse()
            
        make_perms(self.sequence)
        self.line_length = len(s)
        self.lines = len(self.text)
        self.chars = len("".join(self.text))
        
    def read_line(self):
        """
        Read a permutation from the text list. If all lines
        have been read return None.
        """
        if self.is_reading == False:
            #if finished reading or first call "reset" iterator
            self.poem = iter(self.text)
            self.is_reading = True
        try:  
            return self.poem.next()
        except StopIteration:
            #finished reading
            self.is_reading = False
            return None
class Book:
    def __init__(self, poems):
        self.poems = poems
        self.poem_count = len(poems)
        
    def get_poem_titles(self):
        titles = [poem.title for poem in self.poems]
        return titles
