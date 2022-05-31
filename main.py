
'''
Write A Program to Find the Wifi Password : 

First import needed modules
command --- netsh wlan show profiles <profileName> key=clear

create a variable wifiName and
 search whether that wifi exists or not in the system
 if exists then invoke showPassword()
 else not found and exit the programm
 
 showPassword(wifiName)
 pass the wifiName
 execute the command 
 then convert whole output into the list on the basis of "\n"
 Then search for the word keycontent on the list and 
 display that'''

 #importing necessary modules
import subprocess
commandUtility = "netsh wlan show profiles"

 #defining the showPassword()

def showPassword(wifiName) :

    #printing some informations

     print("\n"*2 + "\t"*4 + "We have found {} network on our system .".format(wifiName))
     
     #executing the command and getting output

     data = (subprocess.getoutput(commandUtility + " \"{}\" ".format(wifiName) + " key=clear")).split("\n")

     #converting the output into list and comparing

     for i in range(len(data)) :

         if (str(data[i]).find("Key Content")!= -1) :
             
             key = str(data[i]).split(":") 
             password = key[1]
             
             print("\n"*3 + "\t"*5 + "SSID Name      : {}".format(wifiName))
             print("\n"*2 + "\t"*5 + "Password (Key) : {}".format(password))
             break

     exit(0)
     

if __name__ == "__main__" :

     while True :
     #creating a variable and asking for the wifi Name
        wifiName = input("\n"*3 + "\t"*5 + "Enter your wifi name (Case Sensitive So please be careful ) : ")

        #checkning if the wifiName exists or not :
        
        data = subprocess.getoutput(commandUtility).split("\n")

        for i in range(len(data)) :

            if (str(data[i]).find(wifiName)!= -1) :
        
              showPassword(wifiName)

        print("\n\n\t\t\t\tWe didn't found any {} network in our system....".format(wifiName))

        #asking if they again want to reneter the name or exit the program

        choice = input("\n\n\t\t\t Do you want to reenter the wifi name (Y or N) :")

        if choice == "Y" or choice == "y" :
            continue
        else :
            exit(0)
            


