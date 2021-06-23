
import time
from pythonping import ping

while(1):
    time.sleep(1)
    resp = ping("8.8.8.8",count=1,timeout=1)
    resp1 = ping("192.168.0.1",count=1,timeout=1)
    if(resp.packets_lost != 0.0):
        now = time.localtime()
        now = time.strftime("%y/%m/%d-%H.%M.%S",now)
        print(now+" - "+"8.8.8.8 packet loss")
        with open("pingtest.txt","a") as file:
            file.write(now+" - "+"8.8.8.8 packet loss\n")
    if (resp1.packets_lost != 0.0):
        now = time.localtime()
        now = time.strftime("%y/%m/%d-%H.%M.%S",now)
        print(now+" - "+"192.168.0.1 packet loss")
        with open("pingtest.txt","a") as file:
            file.write(now+" - "+"192.168.0.1 packet loss\n")

    print("p")