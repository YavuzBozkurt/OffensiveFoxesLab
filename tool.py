from arpPoison import *

print("Welcome to the tool, this tool is a console style tool.")
print("For the list of commands use the command 'help'")
print("For more info on a command use the command 'help [command]'")
print("to close or reset the tool, use the input 'ctrl+c'")
print(">>>", end = " ")

runner = True

while runner:
    user_in = input()
    
    if(user_in == "help"):
        print("Here is a list of commands you can use:")
        print("help\nhelp [command]\nmimattack\nonewaypoisoning")
        print(">>>", end = " ")
    
    elif(user_in == "help help"):
        print("'help' command is used to list all the commands available to user.")
        print("it can also be used in the format 'help [command]' to get more info on the specified command.")
        print(">>>", end = " ")
        
    elif(user_in == "mimattack"):
        mimAttack()
        
    elif(user_in == "onewaypoisoning"):
        oneWayPoisoning()
        
    else:
        print("Command not found")
        print("For the list of commands use the command 'help'")
        print(">>>", end = " ")