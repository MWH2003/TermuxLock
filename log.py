from getpass import getpass
import os
import time

def menu():
      while True:
           print("")
           os.system("clear")
           print('\033[1;36;40m<─────────────── WORLD OF HACKING ───────────────>')
           print('')
           os.system('date | lolcat')
           print("\033[1;93m")
           print(" \033[1;92m  E.H. => WELCOME HACKER')")
           print("\033[1;93m")
           print("  <───────[ MASK WALA HACKER ]───────>")
           print("")
           try:
                x = str(input('\033[1;92mUsername \033[1;93m: '))
                print("")
                e = getpass('\033[1;92mPassword \033[1;93m: ')
                print ("")
                if x=="MWH" and e=="HACKER":
                   print('CHECKING PASSWORD...')
                   time.sleep(1)
                   os.system('clear')
                   print('')
                   os.system('figlet ' + x + ' | lolcat')
                   print('\033[1;92m ────────────────────────────────────── ')
                   print("")
                   break
                else:
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m   ACCESS DENIED WRONG PASSWORD")
                      time.sleep(2)
                      print("")
           except Exception:
                      
                      print("")
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m    ACCESS DENIED WRONG PASSWORD")
                      time.sleep(2)
           except KeyboardInterrupt:
                      print("")
                      os.system('killall -9 com.termux')
                      print("")
                      print("")
                      print("")
                      print("")
                      print("\033[1;91m   ACCESS DENIED WRONG PASSWORD")
                      time.sleep(2)
menu()
