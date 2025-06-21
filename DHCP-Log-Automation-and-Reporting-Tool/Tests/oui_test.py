"""
ipv4_test.py
By: Konrad Jeziorski
    Inspired by John O'Row's code
Date: 12/11/2022
*****************
Lists oui and OEM
"""

def manufacturer():

    oui_id = {
            "c8:4b:d6": "Dell",
            "c0:25:a5": "Dell",
            "a4:4c:c8": "Dell",
            "b8:27:eb": "Raspberry Pi",
            "bc:5f:f4": "ASRock/Assus",
            "18:68:cb": "Hikvision CCTV"
    }
    for oui, oem in oui_id.items(): 
        print (oui, oem)

manufacturer()

print("Finished test for oui"  "\nIf the test is run from a batch file in windows, press [ctrl][z] and then [Enter] to exit")