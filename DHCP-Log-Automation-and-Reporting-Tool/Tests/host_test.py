"""
host_test.py
By: Konrad Jeziorski
Date: 12/11/2022
****************
Lists the host information for each row of logs in the dhcpd.log file"""
import os

def host():

    # Open the logfile for read
    my_host_list = []
    logfile_name = os.path.join(os.path.dirname(__file__), "dhcpd.log")
    logfile = open(logfile_name, "r")
    #interate through every line in the log file
    for line in logfile:
        # Parse the line type
        interesting_bit = line[34:]
        list_of_values = interesting_bit.split(" ")
        # Handle each line type
        if list_of_values[0] == "DHCPACK" and list_of_values[1]== "on":
            host_name = (list_of_values[5]).upper()
           
            # Check to see if this host was priviously identified
            if host_name in my_host_list:
                pass
            else: 
                # Add this new host to the my host list
                my_host_list.append(host_name)
                
                # Some sentences do not have a host name
            if host_name == "VIA":
                host_name = " Not present "

            # Lists all hosts for each row of DHCPACK, if the hostname does not exist, it shows the appropriate message;
            # To get rid of the brackets, remove the first and last characters
            print(f"{host_name[1:-1]}")
        else:
            #the message refers to rows that do not contain DHCPACK
            print("Not applicable")
                    
host()

print("Finished test for host"  "\nIf the test is run from a batch file in windows, press [ctrl][z] and then [Enter] to exit")