import sys
from arpPoison import *
from dnsPoison import *

def inputline():
    sys.stdout.write(">>> ")
    return 

print("Welcome to the tool, this tool is a console style tool.")
print("For the list of commands use the command 'help'")
print("For more info on a command use the command 'help [command]'")
print("to close or reset the tool, use the input 'ctrl+c'")
inputline()

runner = True

while runner:
    user_in = raw_input()
        
    if(user_in == "help"):
        print("Here is a list of commands you can use:")
        print("help\nhelp [command]\nmimattack\nonewaypoisoning")
        inputline()
    
    elif(user_in == "help help"):
        print("'help' command is used to list all the commands available to user.")
        print("it can also be used in the format 'help [command]' to get more info on the specified command.")
        inputline()
        
    elif(user_in == "mimattack"):
        mimAttack()
        
    elif(user_in == "onewaypoisoning"):
        oneWayPoisoning()
        
    else:
        print("Command not found")
        print("For the list of commands use the command 'help'")
        inputline()