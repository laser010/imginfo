class printer:
    def info(string):
            print("\033[32m[+] {}\033[0".format(string))
    def error(string):
            print("\033[1m\033[31m[-] {}\033[0".format(string))
    def  title(string):
            print("\033[1m\033[32m>---<{}>---<\033[0".format(string))
