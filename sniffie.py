from classes import Snoopie
from netaddr import IPAddress, IPNetwork 
import pyshark, socket, ssl
from arguments import args


class Sniffie(Snoopie):


    def __init__(self):
       super().__init__()

#assign each remote host to an index start at POSITION 1 
    # so that they can easily be track-down
    packet_index = 0

    #looping through each packet
    # in other to retrive each remote ip a and port number
    packets = Snoopie().harvest()
    for packet in packets:
        packet_index += 1
        remoteHost = packet['Remote Host']
        portNumber = packet["Remote Port"]

        #skip each packet that dosen't have a remote ip address and port number
        if remoteHost and portNumber == 'None':
            continue


    def is_secure(self, hostname=remoteHost):
        #create an SSL context object wich we will use to wipe the soccket connection
        #and establish a secure connecttion with the server
        context = ssl.create_default_context()

        #establishing a TCP connection with the server and port number
        with socket.create_connection(hostname, Sniffie.portNumber) as sock:


            #wrap sock socket with the SSL context to create a secure socket. 
            #And specifies the host name to be verifiy against the servers certificate
            with context.wrap_socket(sock, server_hostname=Sniffie.hostname) as secure_sock:
                #Retrives the certificate from the server, witch we'll use to verify the hostname
                cert = secure_sock.getpeercert()

                #Checks if the CERT variable is not none and if the certificate match the hostname
                if cert and ssl.match_hostname(cert, Sniffie.hostname):
                    return f"Remoe Host: {hostname} at position {Sniffie.packet_index} is secure"
                return f"Remoe Host: {hostname} at position {Sniffie.packet_index} is NOT secure"
        

    def is_dns_resolvable(self, hostname=remoteHost):
        """
        Check if DNS resolves a hostame.
        """

        try:
            #Get the IP address from the hostname using the gethostbyname_ex() method
            _, _, addresses = socket.gethostbyname_ex(hostname)

            # Cheking to see if the ip address were returned.
            if len(addresses) > 0:
                return f"DNS at position: {Sniffie.packet_index} is resolveable"
            return f"DNS at position: {Sniffie.packet_index} is NOT resolveable"
        except socket.gaierror:
            return False
    

    def is_ip_private(self, ip=remoteHost):
        """
        check if an IP adress is private or public
        """

        try:
            # create am IP address object
            ip_address = IPAddress(self, ip)

            #check if the ip is one the private IP addresses in ranges.
            ip_range = ['127.0.0.0/12', '172.16.0.0/12', '192.168.0.0/16']
            for private_range in (ip_range):
                if ip_address in IPNetwork(private_range):
                    return f"Ip Address: {Sniffie.remoteHost}, is private"
                return f"Ip Address: {Sniffie.remoteHost}, is NOT private"
            
        except Exception:
            print("Invalid IP address")
            return False




    def capture_network_traffic(self, iface=args.interface, Timeout=args.timeout, packet_count=7):
        """
        Capture and prints out network traffic on specified network interface

        Default interface: 'wlan0'
        
        Default timeout: 5
        
        Default Packet Count: 7
        """
        self.iface = iface
        self.Timeout = Timeout
        self.packet_count = packet_count

        #capturing live packtes from specified interface
        capture = pyshark.LiveCapture(interface=self.iface)
        capture.sniff(timeout=self.Timeout)

        #reading from each packets as they arrived
        for packet in capture.sniff_continuously(packet_count=self.packet_count):
            return packet

        
    def __str__(self) -> str:
        return self.capture_network_traffic()
    