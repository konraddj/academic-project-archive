# DHCP Log Automation & Reporting Tool #
## Project Scope ##

This project aims to write a simple log file process for DHCP logs from a production server Ubuntu based on client networks including CCTV.

Each sentence of the log is analyzed to extract data fields such as:
- IPv4 address
- MAC address
- hostname
- computed OUI OEM information
#
The assumption of the project is to write the code clearly and cost-effectively and to practice its functionality in separate modules.
#
The generated list with interesting nodes was saved in a CSV file, keeping in mind a readable style, without duplicating data.
#
## Project Composition ##
The project comprises four categories:
1.  Structure
2.  Documentation
3.  Styles
4.  Functionality

The project should fill these categories with the best effort as intended.
#
![img.png](device.png)
#
## The Structure of Project Files ##
A batch file automated the creation of an organized directory structure to efficiently manage the project's files. The main executable file, "main.py", serves as the central script that orchestrates the execution of the project. It imports various functions and packages from the source directory, enabling modularity and reusability of code. The testing suite is designed to focus on the functions and code snippets directly related to the project's objectives, ensuring that each component operates correctly and integrates seamlessly. These tests help validate the functionality and reliability of the implemented solutions.
#
>More detailed information about the project can be found in the Documentation directory.
#
