import time
from Extra.TermcolorFile.termcolor import colored
def acci():
        print(f'\x1b{colored("███╗   ██╗ █████╗ ███╗   ██╗     █████╗ ██╗██████╗ ","red")}')
        time.sleep(0.1)
        print(colored("████╗  ██║██╔══██╗████╗  ██║    ██╔══██╗██║██╔══██╗","green"))
        time.sleep(0.12)
        print(colored("██╔██╗ ██║███████║██╔██╗ ██║    ███████║██║██████╔╝", "blue"))
        time.sleep(0.13)
        print(colored("██║╚██╗██║██╔══██║██║╚██╗██║    ██╔══██║██║██╔══██╗", "yellow"))
        time.sleep(0.14)
        print(colored("██║ ╚████║██║  ██║██║ ╚████║    ██║  ██║██║██║  ██║", "magenta"))
        time.sleep(0.15)
        print(colored("╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝", "cyan"))
        time.sleep(0.16)

def empAscii():
        print("""\x1bc ___    ___    ___    ,,,
|"~"|  $`.´$  J>.<L  |-_-| 
-[Y]-  -[:]-  -[U]-  -(Ö)-
_/ \_   | |   _\ |_   | |""")

def locAscii():
        print("""\x1bc        _,--',   _._.--._____
 .--.--';_'-.', ";_      _.,-'
.'--'.  _.'    {`'-;_ .-.>.'
      '-:_      )  / `' '=.
        ) >     {_/,     /~)
        |/               `^ .'""")

def contAscii():
        print("""\x1bc     _.---.                            .---.
    '---,  `.________________________.'  _  `.
         )   ________________________   (_)  :
    .---'  .'                        `.     .'
     `----'                            `---' """)

def propAscii():
        print("""\x1bc    _________U ,%%&%,	   ____Y____
   /\     _   \%&&%%&%	  /	    /\ 
  /  \___/^\___\%&%%&&	 /_________/  \ 
  |  | []   [] |%\Y&%'	|  =====  | + |
  |  |   .-.   | ||  	|    _    |   |
~~@._|@@_|||_@@| ||	|<> | | @ |___|""")
