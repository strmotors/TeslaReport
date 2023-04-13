import urllib.request
import csv
import os
import hashlib

print()
print("  ______          __      ____                        __ ")
print(" /_  __/__  _____/ /___ _/ __ \___  ____  ____  _____/ /_")
print("  / / / _ \/ ___/ / __ `/ /_/ / _ \/ __ \/ __ \/ ___/ __/")
print(" / / /  __(__  ) / /_/ / _, _/  __/ /_/ / /_/ / /  / /_  ")
print("/_/  \___/____/_/\__,_/_/ |_|\___/ .___/\____/_/   \__/  ")
print("                                /_/                      ")
print("By ST-R Motors")
print()

try:
    urllib.request.urlretrieve("http://192.168.90.100:4035/get_data_values?format=csv", "dataValues.csv")
except:
    print("[ERROR] Grabbing data values from vehicle failed. Please ensure the SecEth is unlocked and cable is plugged.")
    print()
    quit()

with open('dataValues.csv', encoding="utf8") as file:
    content = file.readlines()
header = content[:1]
rows = content[1:]

capacity = 0
carType = ""

def generalInfo():
    print()
    print("soon.")

def batterySoH(capacity):
    print()
    for row in rows:
        row = row.split(",")
        if row[0]=="BMS_nominalFullPackEnergyRemaining":
            nominalFullPack = row[1]
            nominalFullPack = float(nominalFullPack[:len(nominalFullPack)-1])
            sohPercentage = (nominalFullPack/capacity)*100
            soh = str('%.2f' %sohPercentage)
            print(" Battery SoH: %"+soh)
    print()
    
def recentAlerts():
    print()
    for row in rows:
        row = row.split(",")
        if row[0]=="carserver/recentAlerts":
            print(" 1 - Show Active Alerts Only")
            print(" 2 - Last 5 alerts")
            print(" 3 - Last 10 alerts")
            print(" 4 - Last 50 alerts")
            print(" 5 - Last 100 alerts")
            print(" 0 - Main Menu")
            print()
            alertsSelectionString = input("Select a number: ")
            alertNumber = 0
            activeOnly = False
            try:
                alertsSelection = int(alertsSelectionString)
                if alertsSelection == 1:
                    alertNumber = 100
                    activeOnly  = True
                elif alertsSelection == 2:
                    alertNumber = 5
                elif alertsSelection == 3:
                    alertNumber = 10
                elif alertsSelection == 4:
                    alertNumber = 50
                elif alertsSelection == 5:
                    alertNumber = 100
                elif alertsSelection == 0:
                    mainMenu()
                else:
                    print()
                    print("Invalid operation. Please enter a number between 0-5")
                    recentAlerts()
            except ValueError:
                print()
                print("Invalid operation. Please enter a number between 0-5")
                recentAlerts()

            if alertNumber != 0:
                if os.path.isfile(vin+"_alerts.txt"):
                    os.remove(vin+"_alerts.txt")
                text_file = open(vin+"_alerts.txt", "a")
                text_file.write("TeslaReport - Service Alerts")
                
                for i in range(alertNumber):
                    i = i+1
                    alertString = row[i]
                    alertString = alertString.split("@")
                    alertCode = alertString[0]
                    alertTime = alertString[1]
                    alertDesc = alertString[2]
                    alertEnd = alertString[3]
                    
                    alertTime = alertTime.split("T")
                    if alertEnd != "":
                        alertEnd = alertEnd.split("T")
                    
                    alertLogs = []
                    
                    if activeOnly == False:
                        print()
                        alertLogs.append("\n")
                        print("[Alert "+str(i)+"]")
                        alertLogs.append("[Alert "+str(i)+"]")
                        alertLogs.append("\n")
                        print()
                        alertLogs.append("\n")
                        print(" Alert Code: " + alertCode)
                        alertLogs.append(" Alert Code: " + alertCode)
                        alertLogs.append("\n")
                        print(" Alert Description: " + alertDesc)
                        alertLogs.append(" Alert Description: " + alertDesc)
                        alertLogs.append("\n")
                        print(" Alert Date: " + alertTime[0])
                        alertLogs.append(" Alert Date: " + alertTime[0])
                        alertLogs.append("\n")
                        print(" Alert Time: " + alertTime[1])
                        alertLogs.append(" Alert Time: " + alertTime[1])
                        alertLogs.append("\n")
                        if alertEnd != "":
                            print(" Alert End Date: " + alertEnd[0])
                            alertLogs.append(" Alert Date: " + alertTime[0])
                            alertLogs.append("\n")
                            print(" Alert End Time: " + alertEnd[1])
                            alertLogs.append(" Alert Time: " + alertTime[1])
                            alertLogs.append("\n")
                        else:
                            print(" [!] Alert is active!")
                            alertLogs.append(" [!] Alert is active!")
                            alertLogs.append("\n")
                        
                        for alert in alertLogs:
                                       text_file.write(alert)
                    else:
                        if alertEnd == "":
                            print()
                            alertLogs.append("\n")
                            print(" Alert Code: " + alertCode)
                            alertLogs.append(" Alert Code: " + alertCode)
                            alertLogs.append("\n")
                            print(" Alert Description: " + alertDesc)
                            alertLogs.append(" Alert Description: " + alertDesc)
                            alertLogs.append("\n")
                            print(" Alert Date: " + alertTime[0])
                            alertLogs.append(" Alert Date: " + alertTime[0])
                            alertLogs.append("\n")
                            print(" Alert Time: " + alertTime[1])
                            alertLogs.append(" Alert Time: " + alertTime[1])
                            alertLogs.append("\n")
                            print(" [!] Alert is active!")
                            alertLogs.append(" [!] Alert is active!")
                            alertLogs.append("\n")
                            for alert in alertLogs:
                                           text_file.write(alert)
                
                print()
                print(" Output file saved as "+vin+"_alerts.txt")
                text_file.close()
    print()

def revealPins():
    print()
    for row in rows:
        row = row.split(",")
        if row[0]=="GUI_PINToDrivePassword":
            ptd = row[1]
            print(" PIN to Drive Password: " + ptd)
    for row in rows:
        row = row.split(",")
        if row[0]=="GUI_gloveboxPassword":
            gb = row[1]
            print(" Glovebox Password: " + gb)
    for row in rows:
        row = row.split(",")
        if row[0]=="GUI_speedLimitModePassword":
            sl = row[1]
            print(" Speed Limit Password: " + sl)
    for row in rows:
        row = row.split(",")
        if row[0]=="GUI_valetModePassword":
            vm = row[1]
            print(" Valet Mode Password: " + vm)

def revealSpotify():
    print()
    for row in rows:
        row = row.split(",")
        if row[0]=="MEDIA_spotifyUsername":
            username = row[1]
            print(" Spotify Username: " + username)
    for row in rows:
        row = row.split(",")
        if row[0]=="MEDIA_spotifyPassword":
            password = row[1]
            print(" Spotify Password: " + password)

def revealWifi():
    print()
    for row in rows:
        if "LINK_wifiKnownNetworks," in row:
            row = row.split(",[ { ")
            row = row[1]
            row = row.split("}, {")
            for network in row:
                ssid = ""
                spass = ""
                network = network.split(",")
                for netData in network:
                    if "ssid" in netData:
                        netData = netData.split(":")
                        netData = netData[1].split("\"")
                        ssid = netData[1]
                
                for netData in network:
                    if "key" in netData:
                        netData = netData.split(":")
                        netData = netData[1].split("\"")
                        spass = netData[1]
                
                print("SSID: "+ssid)
                print("Password: "+spass)
                print()

for row in rows:
    row = row.split(",")
    if row[0]=="VAPI_carType":
        carType = row[1]
        print(" Vehicle Model: " + carType)

for row in rows:
    row = row.split(",")
    if row[0]=="VAPI_trim":
        trimName = row[1]
        print(" Vehicle Trim: " + trimName)
        if trimName == "100D\n" or trimName == "P100D\n":
            capacity = 98.4
        elif trimName == "90D\n" or trimName == "P90D\n":
            capacity = 81.8
        elif trimName == "85D\n" or trimName == "P85D\n" or trimName == "85\n" or trimName == "P85\n":
            capacity = 77.5
        elif trimName == "75D\n" or trimName == "75\n":
            capacity = 72.6
        elif trimName == "70D\n" or trimName == "70\n":
            capacity = 65.9
        elif trimName == "60D\n" or trimName == "60\n":
            capacity = 62.4
        else:
            print("Corrupted data!")
            quit()

vin = ""

for row in rows:
    row = row.split(",")
    if row[0]=="GUI_remoteFileHashes":
        try:
            vinArray = row[17]
            vinArray = vinArray.split("/")
            vin = vinArray[1]
            print(" VIN Number: " + vin)
        except:
            vin = "UNKNOWNVIN"

def mainMenu():
    developerMode = False
    while True:
        print()
        print(" 1 - General Information")
        print(" 2 - Battery State of Health")
        print(" 3 - Service Alerts")
        if developerMode:
            print(" 4 - [DEV] Reveal PINs")
            print(" 5 - [DEV] Reveal Spotify")
            print(" 6 - [DEV] Reveal Wifi")
        print(" 0 - Exit")
        print()
        selectionString = input("Select a number: ")
        try:
            selection = int(selectionString)
            if selection == 1:
                print()
                print(" GENERAL INFORMATION")
                print()
                generalInfo()
            elif selection == 2:
                print()
                print(" BATTERY STATE OF HEALTH")
                print()
                batterySoH(capacity)
            elif selection == 3:
                print()
                print(" SERVICE ALERTS")
                print()
                recentAlerts()
            elif selection == 4:
                if developerMode:
                    print()
                    print(" REVEAL PINS")
                    print()
                    revealPins()
                else:
                    print()
                    print("Invalid operation. Please enter a number from list.")
            elif selection == 5:
                if developerMode:
                    print()
                    print(" REVEAL SPOTIFY")
                    print()
                    revealSpotify()
                else:
                    print()
                    print("Invalid operation. Please enter a number from list.")
            elif selection == 6:
                if developerMode:
                    print()
                    print(" REVEAL WIFI")
                    print()
                    revealWifi()
                else:
                    print()
                    print("Invalid operation. Please enter a number from list.")
            elif selection == 0:
                quit()
            else:
                print()
                print("Invalid operation. Please enter a number from list.")
        except ValueError:
            print()
            result = hashlib.md5(selectionString.encode())
            if result.hexdigest() == "91f52cef031577ee94bc4fd738b06a06":
                if developerMode:
                    developerMode = False
                    print(" Developer Mode deactivated.")
                else:
                    developerMode = True
                    print(" Developer Mode activated.")
            else:
                print("Invalid operation. Please enter a number from list.")
mainMenu()