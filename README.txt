Requirements & Recommendations:

* Python 2.6 or greater
* ncurses
* iTerm http://iterm.sourceforge.net/ (recommendation for OSX)

Recommended Terminal Settings:
Font: Monaco
Text color: white
Background color: black
Cursor: white

To run on OSX
################
If you are running OSX 10.6 Snow Leopard or later, the only thing you will need to run the software in the recommended environment is iTerm. Snow Leopard comes with python 2.6 installed. ncurses will be most likely available in any OSX version.

In OSX turn on "Enable access for assistive devices" in Universal Access in your system preferences. Start script by clicking on "start_permutations_osx.app" in the app directory. Note that this assumes you have installed iTerm. 

If you don't want to install iTerm then open the default terminal application. The terminal application is in your Utilities directory which is in your Applications directory. Make the window your preferred size and type:

python /path/to/permutations/permutations_main.py

and hit "enter". If you don't know how to get the path to the permutations_main.py file, just type "python" and a space in the terminal and then drag and drop the permutations_main.py file into the terminal window. This will cause the path to be written into the terminal window, you can then hit enter.

To kill (stop) Permutations hit the "control" button and the letter "c" at the same time.

On Linux
###############
I've run the program on Ubuntu in the Gnome terminal without a problem.

On Windows
###############
I haven't had the opportunity to test on Windows. One issue you will run into on that platform is the lack of ncurses. Apparently there are a number of ncurses ports though it seems that most of them are difficult to get working.

Enjoy!

Joseph Moore 2010
moore.joseph@gmail.com
http://joseph-moore.com
