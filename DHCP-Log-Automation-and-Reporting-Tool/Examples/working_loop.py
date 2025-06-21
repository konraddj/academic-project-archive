import csv
import os

"""
working_loop.py
By: Konrad Jeziorski
Date: 12/11/2022

!!! Sample code provided by Lecturer John O'Raw (ATU), reused for this work!!!

This script works as a loop, and does not import functions or packages.
All code is written in this file.
This is an example of a working script, written in a slightly sloppy manner. 

!!!After its execution, output appears in the root directory!!!
"""

my_host = []
#oui_id = {
#    "c8:4b:d6": "Dell laptop",
#    "c0:25:a5": "Dell laptop",
#    "a4:4c:c8": "Dell laptop",
#    "b8:27:eb": "Raspberry Pi",
#    "bc:5f:f4": "ASRock/Assus PC",
#    "18:68:cb": "Hikvision CCTV"
#}
#for k, v in oui_id.items(): 
#    pass


def remove_brackets(string_with_brackets):
    string_without_brackets = str(string_with_brackets.strip('('))
    string_without_brackets = str(string_without_brackets.strip(')'))
    return string_without_brackets


if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")
    # Open the logfile for read
    logfile_name = os.path.join(os.path.dirname(__file__), "dhcpd.log")
    logfile = open(logfile_name, "r")
    #interate through every line in the log file
    for line in logfile:
        # Parse the line type
        interesting_bit = line[34:]
        list_of_values = interesting_bit.split(" ")
        # Handle each line type
        if list_of_values[0] == "DHCPACK":
            # There are two different formats for the DHCPACK line
            if list_of_values[1] == "on":
                ipv4 = list_of_values[2]
                mac_address = remove_brackets(list_of_values[4]).upper()
                
                
                oui = mac_address[:8].lower()
                if oui == "c8:4b:d6":
                    oui = "Dell laptop"
                    pass
                if oui == "c0:25:a5":
                    oui = "Dell laptop"
                    pass
                if oui == "a4:4c:c8":
                    oui =  "Dell laptop"
                    pass
                if oui == "b8:27:eb": 
                    oui = "Raspberry Pi"
                    pass
                if oui == "bc:5f:f4": 
                    oui = "ASRock/Assus PC"
                    pass
                if oui ==  "18:68:cb": 
                    oui = "Hikvision CCTV"
                    pass
                
                # Check to see if this host was previously identified
                if mac_address in my_host:
                    pass
                else:
                    # Add this new host to the my_hosts list
                    my_host.append(mac_address)
                    host_name = remove_brackets(list_of_values[5]).upper()
                    # Some sentences do not have a host name
                    if host_name == "VIA":
                        host_name = "Not present"
                    
                    print(f"ON IP {ipv4} and MAC {mac_address} and my hostname is {host_name}, {oui}")

                    f = open('nodes.csv', 'a')
                    
                    print(f"ON IP {ipv4} and MAC {mac_address} and my hostname is {host_name}, {oui}", file=f)
                    f.close()
                    
            elif list_of_values[1] == "to":
                ipv4 = list_of_values[2]
                mac_address = remove_brackets(list_of_values[3]).upper()

                oui = mac_address[:8].lower()
                if oui == "c8:4b:d6":
                    oui = "Dell laptop"
                    pass
                if oui == "c0:25:a5":
                    oui = "Dell laptop"
                    pass
                if oui == "a4:4c:c8":
                    oui =  "Dell laptop"
                    pass
                if oui == "b8:27:eb": 
                    oui = "Raspberry Pi"
                    pass
                if oui == "bc:5f:f4": 
                    oui = "ASRock/Assus PC"
                    pass
                if oui ==  "18:68:cb": 
                    oui = "Hikvision CCTV"
                    pass

                # Check to see if this host was priviously identified
                if mac_address in my_host:
                    pass
                else:
                    # Add this new host to the my_host_list
                    my_host.append(mac_address)

                    print(f"TO IP {ipv4} and MAC {mac_address}, {oui}")

                    g = open('nodes.csv', 'a')
                    print(f"TO IP {ipv4} and MAC {mac_address}, {oui}", file=g)
                    g.close()

else:
    print(f"This module is called {__name__} and is being called by another script")

remove_brackets(string_with_brackets=str)

#Below are two functions for removing duplicates from the list in CSV

#with open('nodes.csv', 'w', newline='') as f:
 #   writer=csv.writer(f)
  #  A = ({ipv4},{mac_address}, {host_name}, {oui})
   # writer.writerow(A)

def remove_duplicates_from_CVS():
    rows = open('nodes.csv').read().split('\n')
    newrows = []
    for row in rows:
        if row not in newrows:
            newrows.append(row)

    f = open('nodes.csv', 'w')
    f.write('\n'.join(newrows))
    f.close()


remove_duplicates_from_CVS()