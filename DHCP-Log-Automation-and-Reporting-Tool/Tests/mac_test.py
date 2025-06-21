"""
ipv4_test.py
By: Konrad Jeziorski
    Inspired by John O'Row's code
Date: 12/11/2022
****************
List MAC addresses from dhcpd.log
"""
import os

def mac():

    # Open the logfile for read
    my_mac_list = []
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
                
                mac_address =(list_of_values[4]).upper()
                
                if mac_address in my_mac_list:
                    pass
                else:
                    # Add this new mac to the my mac list
                    my_mac_list.append(mac_address)
                    
                    
                    print(f"MAC {mac_address}")
                    
            elif list_of_values[1] == "to":
                
                # Set position of mac with slice the string 
                # to exclude the first and last character witch are brackets
                mac_address = (list_of_values[3])[1:][:17].upper()

                # Check to see if this mac was priviously identified
                if mac_address in my_mac_list:
                    pass
                else:
                    # Add this new mac to the mac list
                    my_mac_list.append(mac_address)
                    print(f"MAC {mac_address}")
        else:
            pass

mac()

print("Finished test for mac"  "\nIf the test is run from a batch file in windows, press [ctrl][z] and then [Enter] to exit")