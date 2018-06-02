import webbrowser
import getpass
import socket
import platform
import time



def nichtGut():
    time.sleep(.5)
    print("Hmm...")
    time.sleep(1)
    print("Ich glaube.. ich kann dir helfen..")
    time.sleep(2)
    webbrowser.open('https://www.143.ch/')


class getInfo:
    def __init__(self):
        self.ipAdr=socket.gethostbyname(socket.gethostname())
        self.username=getpass.getuser()
        self.cpu=platform.processor()
        self.osystem=platform.system()
    def text(self):
        time.sleep(.5)
        print("Ok, dann wünsche ich dir noch viel spass auf deinem {0} Rechner mit der IP {1} und Cpu {2}. Auf nimmer wiedersehen {3}!".format(self.osystem,self.ipAdr,self.cpu,self.username))
        time.sleep(7)


#######
#Hauptprogramm
#######
info=getInfo()

print("Hallo ", getpass.getuser())
time.sleep(1)
antw=input("Wie geht es dir? ").lower().strip()

if "nicht" in antw:
    if "s" in antw:
        info.text()
    elif "g" in antw:
        nichtGut()
elif "gu" in antw:
    info.text()
elif "sch" in antw:
    nichtGut()
else:
    print("")
    print("Du solltest lernen wie man sich einfacher ausdrückt! ")
    time.sleep(4)
    webbrowser.open('http://www.learn-german-online.net/learning-german-resouces/lehrbuch.htm')

time.sleep(2)

print("TestGithu<Blelluzlelr")

