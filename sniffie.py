from classes import Snoopie
from netaddr import IPAddress #pip install netaddr
import pyshark
from arguments import args

#sudo apt install tshark

'''

There are two different is_private() method, one is from the IPAddress class
Note: I couln't come up with a better name, but feel free to change it.

'''

class Sniffie(Snoopie):
    def __init__(self):
        super().__init__()
        ''' using this right now for testing purposes as of right now as a place holder 
        of the actual IP's comming from the file'''
        #self.ipadress = ipadress
        
        #Applying a time out
        self.Timeout = 5
        # After testing, set to global argument
        #self.Timeout = args.timeout

        #number of packet count
        self.PacketCount = 15

        #
        self.ifaceName = 'wlan0'
        # After testing, set to global argument
        #self.ifaceName = args.interface
        
        self.filter_traffic = 'port 443'
    

    def is_private(self):
        #cheking to see if the ipaddr is private or not
        if IPAddress(self.IP).is_private():
            return True

        return False

    #create method to capture network traffic
    def capture(self):
        #capturing live packet, then assign to cap(capture) variable
        cap = pyshark.LiveCapture(interface=self.ifaceName, bpf_filter=self.filter_traffic)
        cap.sniff(timeout=self.Timeout, packet_count=self.PacketCount)

        if len(cap) >=1:
            for packet in cap:
                return f'Src: {packet.ip.src} \nDst: {packet.ip.dst}'
    

x = Sniffie()

res = x.capture()

print(res)
