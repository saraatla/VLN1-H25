import time
from Extra.TermcolorFile.termcolor import colored

def acci():
        x = colored("███╗   ██╗ █████╗ ███╗   ██╗     █████╗ ██╗██████╗ ",'green',attrs=['bold'])
        print(f'\x1bc{x}')
        time.sleep(0.1)
        print(colored("████╗  ██║██╔══██╗████╗  ██║    ██╔══██╗██║██╔══██╗",'blue' ,attrs=['bold']))
        time.sleep(0.12)
        print(colored("██╔██╗ ██║███████║██╔██╗ ██║    ███████║██║██████╔╝",'green' ,attrs=['bold']))
        time.sleep(0.13)
        print(colored("██║╚██╗██║██╔══██║██║╚██╗██║    ██╔══██║██║██╔══██╗", 'blue' ,attrs=['bold']))
        time.sleep(0.14)
        print(colored("██║ ╚████║██║  ██║██║ ╚████║    ██║  ██║██║██║  ██║", 'green' ,attrs=['bold']))
        time.sleep(0.15)
        print(colored("╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝", 'blue' ,attrs=['bold']))
        time.sleep(0.16)

def empAscii():
        print("""\033c ___    ___    ___    ,,,
|"~"|  $`.´$  J>.<L  |-_-| 
-[Y]-  -[:]-  -[U]-  -(Ö)-
_/ \_   | |   _\ |_   | |""")

def locAscii():
        print("""\033c        _,--',   _._.--._____
 .--.--';_'-.', ";_      _.,-'
.'--'.  _.'    {`'-;_ .-.>.'
      '-:_      )  / `' '=.
        ) >     {_/,     /~)
        |/               `^ .'""")

def contAscii():
        print("""     _.---.                            .---.
    '---,  `.________________________.'  _  `.
         )   ________________________   (_)  :
    .---'  .'                        `.     .'
     `----'                            `---' """)

def propAscii():
        print("""\x1bc    _________U ,%%&%,	  _____Y____^
   /\     _   \%&&%%&%	 /	   / \ 
  /  \___/^\___\%&%%&&	/_________/   \ 
  |  | []   [] |%\Y&%'	|  =====  | + |
  |  |   .-.   | ||  	|    _    |   |
~~@._|@@_|||_@@| ||	|<> | | @ |___|""")

def workAscii():
        print("""\x1bc –––––––––––
| ~~~       | 
| ~~~~~~~   |
| ~~~~~~~~~ |
|___________| """)
