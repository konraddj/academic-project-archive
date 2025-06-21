"""
ipv4_test.py
By: Konrad Jeziorski
    Inspired by John O'Row's code
Date: 12/11/2022
****************
Lists the IP addresses from dhcpd.log
"""
import os

def ipv4():

    my_ip_list =[]
    logfile_name = os.path.join(os.path.dirname(__file__), "dhcpd.log")
    logfile = open(logfile_name, "r")
    #interate through every line in the log file
    for line in logfile:
        # Parse the line type
        interesting_bit = line[34:]
        list_of_values = interesting_bit.split(" ")
        # Handle each line type
        if list_of_values[0] == "DHCPACK":           
            ipv4_ = list_of_values[2]

            # Check to see if this IP was priviously identified
            if ipv4_ in my_ip_list:
                pass
            else:
                # Add this new ipv4 to the my ip list
                my_ip_list.append(ipv4_)
                print(f"IP {ipv4_}")
        else:
            pass
ipv4()


print("Finished test for ipv4"  "\nIf the test is run from a batch file in windows, press [ctrl][z] and then [Enter] to exit")