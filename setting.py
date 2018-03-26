VERSION = "demo"
IG_LINK = "instagram.com/laser01/"
BANNER = ("""\033[32m

  _                 _        __      
 (_)               (_)      / _|    
  _ _ __ ___   __ _ _ _ __ | |_ ___  
 | | '_ ` _ \ / _` | | '_ \|  _/ _ \ 
 | | | | | | | (_| | | | | | || (_) |
 |_|_| |_| |_|\__, |_|_| |_|_| \___/ 
               __/ |                 
              |___/                 

	dev {0}
	Version {1}

\033[0m""".format(IG_LINK, VERSION))
def logo():
    print(BANNER)
