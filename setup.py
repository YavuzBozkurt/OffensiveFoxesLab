def getInterface(interface):
    
    print("")
    user_in = raw_input("use interface " + str(interface) + "? (y/n): ")

    if user_in in ["y","Y"]:
        return interface
 
    elif user_in in ["n","N"]:
        print("")
        return raw_input("enter interface: ")

    else:
        print("")
        print("bad input \"" + user_in + "\"")
        return getInterface(interface)

    return

def showUrlsToSpoof(urlsToSpoof):

    print("\nURLs to spoof:")
    
    for url in urlsToSpoof.keys():
        print(url)

    return

def inputUrlsToSpoof(urlsToSpoof):

    print("\ninput URLs to spoof")
    print("after entering last URL, enter c to continue\n")    

    def addUrls(urlsToSpoof):
	
        urlsToSpoof[user_in + "."] = user_in_2
        urlsToSpoof["*." + user_in + "."] = user_in_2
        urlsToSpoof["www." + user_in + "."] = user_in_2

        return urlsToSpoof
    
    while(True):
        user_in = raw_input("URL to spoof: ")
        user_in_split = user_in.split(".")
    
        if user_in == "c":
            return urlsToSpoof
    
        elif len(user_in_split) == 2:
            user_in_2 = raw_input("IP to use: ")
            print("")
            urlsToSpoof = addUrls(urlsToSpoof)

        elif len(user_in_split) == 3:
            user_in_2 = raw_input("IP to use: ")
            print("")

            if user_in_split[0] in ("*.", "www"):
                del user_in_split[0]
                user_in = ".".join(user_in_split)
                urlsToSpoof = addUrls(urlsToSpoof)
	
            else:
                urlsToSpoof[user_in + "."] = user_in_2
        
        else:
            print("Error: bad input \"" + str(user_in) + "\"")

def showAddrs(addrs):

    print("")    

    for k in addrs.keys():
        print(k + ": " + addrs[k])

    return

def addAddrs(addrs):

    print("")
    
    for k in addrs.keys():
        addrs[k] = raw_input(k + ": ")

    return addrs
