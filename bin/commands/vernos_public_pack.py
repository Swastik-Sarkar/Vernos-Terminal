import sys
import os
import subprocess

author = "kb_swastik"
license = "None"
rating = "unknown"
pack_id = "c103115a"

#ver token and details

def vernos_public_ver():
     print("vernos version : 0.1")
     print("pack version : 1")
 
def vernos_token_c103115a():
     print("Vernos Token : Bx4asa35g9")
     
def vernos_public_details():
     print("Vernos Public Pack Details")
     print("Author : kb_swastik")
     print("ID : c103115a")
     print("Description : First Pack Of Vernos")
     print("Version Support : 0.1")
     print("Pack Version : 1")

#commands 
#command.router_setup_helper
def vernos_command_rsh():
     print("Configuring a single router on Cisco Packet Tracer. Simplified." + "\n"
      + "Basically answer all the questions and the program will prepare a script you have to type in the router to "
        "get desired configuration." + "\n" +
      "Make sure you are typing the data correctly. There's no error-catching as of yet." + "\n"
                                                                                            "Let's start!")

     hostname = input("What's the name for the router?")
     if hostname == "":
     hostname = "Router"

     numberOfSubnets = int(input("How many local subnetworks are connected to the router?"))

     while numberOfSubnets <= 0:
     numberofSubnets = int(input("Type a correct number of local subnetworks."))
     print("Number of subnets is " + str(numberOfSubnets))

     interfacesDictionary = {}
     for i in range(numberOfSubnets):
       interfaceIP = input("Type IP address of your " + str(i + 1) + " subnet: ")
       interfaceName = input("Type what interface will the subnet be assigned to: ")
       interfacesDictionary[interfaceName] = interfaceIP
       print("The IP address of your " + str(i + 1) + " subnet is: " + interfaceIP)
       print("The assigned interface: " + interfaceName)

     defaultGateway = str(input(
      "Do you want the router to have default ip as .254 in the subnets or you prefer custom ones? Type either "
      "'default' or 'custom'."))

     while defaultGateway != "default" or defaultGateway != "custom":
        defaultGateway = input("Wrong answer! Type either 'default' or 'custom'!")
     print(defaultGateway)
     
