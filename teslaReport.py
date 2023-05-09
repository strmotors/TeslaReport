import urllib.request
import csv
import os
import hashlib

print()
print("   ______          __      ____                        __ ")
print("  /_  __/__  _____/ /___ _/ __ \___  ____  ____  _____/ /_")
print("   / / / _ \/ ___/ / __ `/ /_/ / _ \/ __ \/ __ \/ ___/ __/")
print("  / / /  __(__  ) / /_/ / _, _/  __/ /_/ / /_/ / /  / /_  ")
print(" /_/  \___/____/_/\__,_/_/ |_|\___/ .___/\____/_/   \__/  ")
print("                                 /_/                      ")
print(" By ST-R Motors")
print()

try:
    urllib.request.urlretrieve("http://192.168.90.100:4035/get_data_values?format=csv", "dataValues.csv")
except:
    print("[ERROR] Grabbing data values from vehicle failed. Please ensure that the SecEth is unlocked and cable is plugged.")
    print()
    quit()

with open('dataValues.csv', encoding="utf8") as file:
    content = file.readlines()
header = content[:1]
rows = content[1:]

effectiveCapacity = 0
usableCapacity = 0
brickMax = 0
brickMin = 0
acChargeCount = 0
dcChargeCount = 0
kwDischargeCount = 0
carType = ""

def generalInfo():
    print()
    for row in rows:
        row = row.split(",")
        if row[0]=="VAPI_chargerType":
            print(" AC Charger Type: "+row[1])
        if row[0]=="VAPI_airSuspension":
            print(" Air Suspension: "+row[1])
        if row[0]=="VAPI_frontFogLights":
            print(" Front Fog Lights: "+row[1])
        if row[0]=="VAPI_rearFogLights":
            print(" Rear Fog Lights: "+row[1])
        if row[0]=="VAPI_hasHomelink":
            print(" Homelink: "+row[1])
        if row[0]=="VAPI_hasSunroof":
            print(" Sunroof: "+row[1])
        if row[0]=="VAPI_hasPowerLiftgate":
            print(" Power Liftgate: "+row[1])
        if row[0]=="FEATURE_blindspotWarningEnabled":
            print(" Blindspot Warning: "+row[1])
        if row[0]=="VAPI_hasMemorySeats":
            print(" Memory Seats: "+row[1])
        if row[0]=="VAPI_hasMemoryMirrors":
            print(" Memory Mirrors: "+row[1])
        if row[0]=="SYS_IC_cpuHardware":
            print(" CPU Hardware: "+row[1])
        if row[0]=="VAPI_hasSeatHeaters":
            print(" Front Seat Heater: "+row[1])
        if row[0]=="VAPI_rearSeatHeaters":
            print(" Rear Seat Heater: "+row[1])
        if row[0]=="VAPI_steeringWheelHeater":
            print(" Steering Wheel Heater: "+row[1])
        if row[0]=="VAPI_fourWheelDrive":
            print(" Four Wheel Drive: "+row[1])
        if row[0]=="VAPI_wheelType":
            print(" Wheel Type: "+row[1])
        if row[0]=="FEATURE_parkAssistEnabled":
            print(" Park Assist: "+row[1])
        if row[0]=="VAPI_hasFoldingMirrors":
            print(" Folding Mirrors: "+row[1])
        if row[0]=="VAPI_noKeylessEntry":
            if row[1]=="true":
                print(" Keyless Entry: false")
                print()
            else:
                print(" Keyless Entry: true")
                print()
        if row[0]=="VAPI_tpmsType":
            print(" TPMS Type: "+row[1])
        if row[0]=="VAPI_autopilot":
            print(" Autopilot: "+row[1])
        if row[0]=="CONN_cellIMEI":
            print(" IMEI Number: "+row[1])
        if row[0]=="CONN_cellConnected":
            print(" Cell Connection: "+row[1])
        if row[0]=="CONN_connectedToInternet":
            print(" Internet Connection: "+row[1])
        if row[0]=="CONN_vpnConnected":
            print(" Tesla Connection: "+row[1])
        if row[0]=="VAPI_performanceAddOn":
            print(" Performance AddOn: "+row[1])
    print()

def batterySoH(usableCapacity, effectiveCapacity):
    print()
    for row in rows:
        row = row.split(",")
        if row[0]=="BMS_nominalFullPackEnergyRemaining":
            nominalFullPack = row[1]
            nominalFullPack = float(nominalFullPack[:len(nominalFullPack)-1])
            sohEffective = (nominalFullPack/effectiveCapacity)*100
            sohUsable = (nominalFullPack/usableCapacity)*100
            sohE = str('%.2f' %sohEffective)
            sohU = str('%.2f' %sohUsable)
            print(" Effective Battery SoH: %"+sohE)
            print(" Usable Battery SoH: %"+sohU)
    print()
    for row in rows:
        row = row.split(",")
        if row[0]=="VAPI_brickVoltageMax":
            brickMax = row[1]
            brickMax = float(brickMax[:len(brickMax)-1])
            bMax = str('%.2f' %brickMax)
            print(" Maximum Brick Voltage: "+bMax+"V")
        if row[0]=="VAPI_brickVoltageMin":
            brickMin = row[1]
            brickMin = float(brickMin[:len(brickMin)-1])
            bMin = str('%.2f' %brickMin)
            print(" Minimum Brick Voltage: "+bMin+"V")
    
    print()
    
    brickDelta = brickMax - brickMin
    brickError = brickDelta / brickMax
    
    bDelta = str('%.2f' %brickDelta)
    bError = str('%.2f' %brickError)
    
    print(" Maximum Potantial Difference: "+bDelta+"V")
    print(" Maximum Error: %"+bError)
    
    print()
    
    for row in rows:
        row = row.split(",")
        if row[0]=="VAPI_acChargerKwhTotal":
            acChargeCount = row[1]
            acChargeCount = float(acChargeCount[:len(acChargeCount)-1])
            acChargeCount = str('%.2f' %acChargeCount)
            print(" AC Charge Count: "+acChargeCount+" KWh")
        if row[0]=="VAPI_dcChargerKwhTotal":
            dcChargeCount = row[1]
            dcChargeCount = float(dcChargeCount[:len(dcChargeCount)-1])
            dcChargeCount = str('%.2f' %dcChargeCount)
            print(" DC Charge Count: "+dcChargeCount+" KWh")
        if row[0]=="VAPI_kWhDischargeCounter":
            kwDischargeCount = row[1]
            kwDischargeCount = float(kwDischargeCount[:len(kwDischargeCount)-1])
            kwDischargeCount = str('%.2f' %kwDischargeCount)
            print(" KWh Discharge Count: "+kwDischargeCount+" KWh")
    
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
                text_file.write("   ______          __      ____                        __ ")
                text_file.write("\n")
                text_file.write("  /_  __/__  _____/ /___ _/ __ \___  ____  ____  _____/ /_")
                text_file.write("\n")
                text_file.write("   / / / _ \/ ___/ / __ `/ /_/ / _ \/ __ \/ __ \/ ___/ __/")
                text_file.write("\n")
                text_file.write("  / / /  __(__  ) / /_/ / _, _/  __/ /_/ / /_/ / /  / /_  ")
                text_file.write("\n")
                text_file.write(" /_/  \___/____/_/\__,_/_/ |_|\___/ .___/\____/_/   \__/  ")
                text_file.write("\n")
                text_file.write("                                 /_/                      ")
                text_file.write("\n")
                text_file.write(" By ST-R Motors")
                text_file.write("\n")
                text_file.write("Service Alerts")
                text_file.write("\n")
                
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
            effectiveCapacity = 102.4
            usableCapacity = 98.4
        elif trimName == "90D\n" or trimName == "P90D\n":
            effectiveCapacity = 85.8
            usableCapacity = 81.8
        elif trimName == "85D\n" or trimName == "P85D\n" or trimName == "85\n" or trimName == "P85\n":
            effectiveCapacity = 81.5
            usableCapacity = 77.5
        elif trimName == "75D\n" or trimName == "75\n":
            effectiveCapacity = 75
            usableCapacity = 72.6
        elif trimName == "70D\n" or trimName == "70\n":
            effectiveCapacity = 75
            usableCapacity = 65.9
        elif trimName == "60D\n" or trimName == "60\n":
            effectiveCapacity = 75
            usableCapacity = 62.4
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
        print(" 0 - Exit")
        if developerMode:
            print()
            print(" Developer Options")
            print()
            print(" a - [DEV] Reveal PINs")
            print(" b - [DEV] Reveal Spotify")
            print(" c - [DEV] Reveal Wifi")
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
                batterySoH(usableCapacity, effectiveCapacity)
            elif selection == 3:
                print()
                print(" SERVICE ALERTS")
                print()
                recentAlerts()
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
            elif selectionString == "a":
                if developerMode:
                    print()
                    print(" REVEAL PINS")
                    print()
                    revealPins()
                else:
                    print()
                    print("Invalid operation. Please enter a number from list.")
            elif selectionString == "b":
                if developerMode:
                    print()
                    print(" REVEAL SPOTIFY")
                    print()
                    revealSpotify()
                else:
                    print()
                    print("Invalid operation. Please enter a number from list.")
            elif selectionString == "c":
                if developerMode:
                    print()
                    print(" REVEAL WIFI")
                    print()
                    revealWifi()
                else:
                    print()
                    print("Invalid operation. Please enter a number from list.")
            else:
                print("Invalid operation. Please enter a number from list.")
mainMenu()