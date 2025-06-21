"""
main.py
By: Konrad Jeziorski
Date: 12/11/2022

!!! Initialization code provided by lecturer John O'Raw (ATU); 
reused and modified to meet all the requirements of the assignment specification !!!
"""
# Imports for text processing
from Sources import remove_brackets as util

# Imports for check OUI
from Sources import manufacturer

# Import for processing folders and files from different places in the system
import os.path

# Declar a list as opposed to any variables, and invoke specific methods (etc. append)
my_host = []


# Run blocks of code only if program is the main program executed (be executable by itself)
if (__name__ == '__main__'):
    print(f"This module is called {__name__} and executes as a standalone script")

    # Open the logfile for read (path in root directory)
    logfile_name = os.path.join(os.path.dirname(__file__), "dhcpd.log")
   
    # Open file for read
    logfile = open(logfile_name, "r")
    #interate through every line in the log file
    for line in logfile:
        # Parse the line type        
        payload = line[34:]
        # creates a space between values
        list_of_values = payload.split(" ")
        # Handle each line type
        if list_of_values[0] == "DHCPACK":
        # Any other value will be ignored.
            # There are two different formats for the DHCPACK line ("on" and "to")
            if list_of_values[1] == "on":
                ipv4 = list_of_values[2]
                # Assigns the value, in uppercase; and removes unnecessary brackets; 
                mac_address = util.remove_brackets(list_of_values[4]).upper()                              
                oui_id = manufacturer.oui_id
                # OUI formula, first 8 characters from MAC value
                oui = mac_address[:8].lower()

                # Looks up oui in the dictionaries list and assigns a value
                if oui in oui_id:
                    node_type = oui_id[oui]
                else:
                    node_type = "Unknown Manufacturer: {oui}"
                    # print(node_type)
                                       
                # Check to see if this host was previously identified
                if mac_address in my_host:
                    pass
                else:
                    # Add this new host to the my_hosts list
                    my_host.append(mac_address)
                    host_name = util.remove_brackets(list_of_values[5]).upper()
                    # Some sentences do not have a host name
                    if host_name == "VIA":
                        host_name = "Not present"                       
                    print(f"ON IP {ipv4} and MAC {mac_address} and my hostname is {host_name}, {node_type}")

                    # Opens or, in its absence, creates a directory and a file in it (root directory / Results/nodes.csv)
                    directory = './Results/'
                    filename = "nodes.csv"
                    file_path = os.path.join(directory, filename)
                    if not os.path.isdir(directory):
                        os.mkdir(directory)
                    f = open(file_path, 'a')                      
                    print(f"ON IP {ipv4} and MAC {mac_address} and my hostname is {host_name}, {node_type}", file=f)
                    f.close()
                        
            elif list_of_values[1] == "to":
                
                mac_address = util.remove_brackets(list_of_values[3]).upper()
                if oui in oui_id:
                    node_type = oui_id[oui]
                else:
                    node_type = "Unknown Manufacturer: {oui}"
                    #print(node_type)

                    # Check to see if this host was priviously identified
                if mac_address in my_host:
                    pass
                else:
                    # Add this new host to the my_host_list
                    my_host.append(mac_address)

                    print(f"TO IP {ipv4} and MAC {mac_address}, {node_type}")

                    # Opens or, in its absence, creates a directory and a file in it (root directory / Results/nodes.csv)
                    directory = './Results/'
                    filename = "nodes.csv"
                    file_path = os.path.join(directory, filename)
                    if not os.path.isdir(directory):
                        os.mkdir(directory)
                    f = open(file_path, 'a')
                    print(f"TO IP {ipv4} and MAC {mac_address}, {node_type}", file=f)
                    f.close()
else:
    print(f"This module is called {__name__} and is being called by another script")
    
# Added at the end as it checks and modifies (removes duplicates) the output (nodes.csv file) after executing the program
from Sources import remove_duplicates