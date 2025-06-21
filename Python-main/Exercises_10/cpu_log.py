""""
File utilities, forked from the Comm module of SD-Node, written c. 2017
Tested with Python >=3.6
By: JOR
 v0.1 26AUG21
"""
import os
from file_utilities import path_name, log_file_name
from os_utilities import detect_os, cpu_load
from time import sleep
# Check the OS in use, and figure out a log file name and path
this_os = detect_os()
log_path = path_name()
filename = log_file_name(".csv")
# Loop forever
while True:
 # Sleep for 1 second
 sleep(1)
 # Get a time stamp for this line
 timestamp = log_file_name("")
 # Get some information
 information = cpu_load()
 # Create a line for the logfile, convert the integer values to string
 logline = timestamp + ":" + str(information[0]) + "," + str(information[1]) + "\n"
 # Now write it to the logfile
 try:
  if not os.path.exists(log_path):
    os.makedirs(log_path)
  with open(log_path+filename, "a") as file_handle:
   print(f"logging to {filename}")
   file_handle.write(logline)
 except IOError as err:
  print(f"IOError was {err}")
 except EOFError as err:
  print(f"End of file error was {err}")
 except OSError:
  print("OS Error")
 except:
  print("General Error")