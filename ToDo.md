
Network Monitoring Tool

Primary Tasks:

1) Monitor traffic on host
2) Run checks on each IP in communication with host

  2.1) Is the IP a private or public network address?
  2.2) Does DNS resolve a hostname? Is this hostname known? Is it secure?
  2.3) How much data is being traded? Is the amount unexpected for the traffic type?
  

Breakdown:

0) Learn how to most effectively read IO from network card

1) ~~Create general modules to hold: main, classes, helper_funcs, arguments, footers, headers, citations~~

2) Create a class "snoopie" to actively copy networking requests into a hidden file

3) Create a class "sniffie" to parse snoopie's hidden file

 3.1) sniffie will have some methods, one for each primary task ( 2.1, 2.2, 2.3 )
 
 3.2) sniffie will generate a multi-dimensional dict object with any suspicious traffics
 
4) Create a class "screedie" to receive sniffies multi-dict object

  4.1) screedie will basically just pull the multi-dict apart and report it to the user ( will need flatdict library for this )
  
  4.2) could maybe get creative with different data transforms screedie can do to the data, but let's just get it talking and test the code for efficacy before we get too fancy
  
5) Write main logic loop
  
6) Test runs

  6.1) Test on Windows and Linux
  
  6.2) Set up a virtual network with known safe traffic and test, expecting no output
  
  6.3) Run a reverse shell on the virtual network, see if it reports
  
  6.4) Run small data exfiltration on the virt net, see if it reports
  
  6.5) Run large data exfil on the virt net, see if it reports
  
  6.6) Run small data infiltration 
  
  6.7) Run large data infiltration