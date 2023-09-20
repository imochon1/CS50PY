# import cowsay
import sys
from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])

# if len(sys.argv) == 2:
#    cowsay.cow("Hello, " + sys.argv[1])

# cowsay was imported through the pip install cowsay command. This command installs the cowsay module on your computer. The cowsay module contains a function called cow that takes a string as an argument and prints a cow saying that string. The string is passed to the cow function by concatenating it with sys.argv[1]. sys.argv[1] is the first command line argument passed to the script. If the user enters too many or too few arguments, the program will not run.
