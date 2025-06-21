from file_utilities import path_name, log_file_name
from os_utilities import detect_os
# Check the OS in use, and figure out a log file name and path
this_os = detect_os()
log_path = path_name()
filename = log_file_name(".log")
print(log_path + filename )
