from devices import Firewall, Load_Balancer

from devices import Switch


# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()
# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")

switch3 = Switch("Switch3")
switch3.configure_switch()
trunk = Switch("Trunk")
trunk.port_mode("dummy data")
VLAN10 = Switch("VLAN 10") 
VLAN10.conf_vlan("dummy data")

LoadBalancer01 = Load_Balancer("Load Balancer 01")
LoadBalancer01.conf_load_balancer()
server3studentexamplepageie = Load_Balancer(" Server 3: student-examplepage.ie")
server3studentexamplepageie.set_nodes
westeurope = Load_Balancer("West Europe")
westeurope.availability_zone