from classes import Snoopie
from netaddr import IPAddress, IPNetwork 
import pyshark, socket, ssl
from arguments import args


class Sniffie(Snoopie):
    def __init__(self):
        super().__init__()




    def is_secure(self, hostname):
        #create an SSL context object wich we will use to wipe the soccket connection
        #and establish a secure connecttion with the server
        context = ssl.create_default_context()

        #establishing a TCP connection with the server and port number
        with socket.create_connection(self.hostname, 'portnumber') as sock:

            #wrap sock socket with the SSL context to create a secure socket. 
            #And specifies the host name to be verifiy against the servers certificate
            with context.wrap_socket(sock, server_hostname=self.hostname) as secure_sock:
                #Retrives the certificate from the server, witch we'll use to verify the hostname
                cert = secure_sock.getpeercert()

                #Checks if the CERT variable is not none and if the certificate match the hostname
                if cert and ssl.match_hostname(cert, self.hostname):
                    return f"{hostname} is secure"
                return f"{hostname} is not secure"
        

    def is_dns_resolvable(self, hostname):
        """
        Check if DNS resolves a hostame.
        """

        try:
            #Get the IP address from the hostname using the gethostbyname_ex() method
            _, _, addresses = socket.gethostbyname_ex(hostname)

            # Cheking to see if the ip address were returned.
            if len(addresses) > 0:
                return True
            return False
        except socket.gaierror:
            return False
    

    def is_ip_private(self, ip):
        """
        check if an IP adress is private or public
        """

        try:
            # create am IP address object
            ip_address = IPAddress(self, ip)

            #check if the ip is one the private IP address in ranges.
            ip_range = ['127.0.0.0/12', '172.16.0.0/12', '192.168.0.0/16']
            for private_range in (ip_range):
                if ip_address in IPNetwork(private_range):
                    return True
                return False
            
        except Exception:
            print("Invalid IP address")
            return False




    def capture_network_traffic(self, iface='wlan0', Timeout=5, packet_count=7):
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
    