
Network Monitoring Tool

Primary Tasks:

1) Monitor traffic on host
2) Run checks on each IP in communication with host

  2.1) Is the IP a private or public network address?
  2.2) Does DNS resolve a hostname? Is this hostname known? Is it secure?
  2.3) How much data is being traded? Is the amount unexpected for the traffic type?
  

Left to Do:

0) Fix Sniffie, or absorb Sniffie into Snoopie methods?

1) Assess the need for a Screedie (reporting class) or if Snoopie/Sniffie could absorb that functionality
  
2) Finish main logic loop
  
3) Test runs
 
  3.2) Set up a virtual network with known safe traffic and test, expecting no output
  
  3.3) Run a reverse shell on the virtual network, see if it reports
  
  3.4) Run small data exfiltration on the virt net, see if it reports
  
  3.5) Run large data exfil on the virt net, see if it reports
  
  3.6) Run small data infiltration 
  
  3.7) Run large data infiltration
