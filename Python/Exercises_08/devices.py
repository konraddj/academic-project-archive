"""
Parent class Template by JOR
"""
# In any complex application, create a base class which will never be instantiated.
class Device():
 
# Define a class object attribute, it will be the same for any instance of the class
    pi = 3.142
# Constructor, called whenever an instance of the class is created.
    def __init__(self) -> None:
        print("Running constructor for base class")
# Create attributes and set initial values
        self.debug = False
    def run(self):
        raise NotImplementedError("This is an abstract class, do not instantiate")
    def calculate_crc(self, frame:str)->int: 
        print("Checking CRC from base")
# Put real code in here, this is a dummy value for initial setup
        crc = 123456789
        return crc
"""
Child class Template by JOR
"""
# Create child class which can access the methods and properties of the base class
class Firewall(Device):
# Constructor, called whenever an instance of the class is created.
# Use parameter1 as a tag to identify the object
    def __init__(self, parameter1) -> None:
# Call back to the parent class
        Device.__init__(self)
        print(f"Running constructor for {parameter1}") 
# Create attributes and set initial values
        self.parameter1 = parameter1
        self.test_message = ""
 
    def configure_firewall(self):
        print("Configuring Firewall")
    def calculate_crc(self, frame:str)->int: 
        print("Checking CRC from child")
# Put real code in here, this is a dummy value for initial setup
        crc = 123456789
        return crc

class Switch(Device):
    def __init__(self, parameter2) -> None:
        Device.__init__(self)
        print(f"Running constructor for {parameter2}")
        self.parameter2 = parameter2
        self.test_message = ""
    def configure_switch(self):
        print("Configuring switch")
    def port_mode(self, port_mode):
        print("Configuring Switch Port Mode")
        
    def conf_vlan(self, VLAN):
        print("Configuring VLAN")
  

class Load_Balancer(Device):
    def __init__(self, parameter3)-> None:
        Device.__init__(self)
        print(f"Running constructor for {parameter3}")
        self.parameter3 = parameter3
        self.test_message = ""
    def conf_load_balancer(self):
        print("Configuring Load blancer")
    def set_nodes(self, load_balancer_nodes):
        print("Settings Load Balancer Nodes")
    def availability_zone(self, availability_zone):
        print("Settings for Availability Zone") 

