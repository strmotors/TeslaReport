import urllib.request
import csv

print()
print("  ______          __      ____                        __ ")
print(" /_  __/__  _____/ /___ _/ __ \___  ____  ____  _____/ /_")
print("  / / / _ \/ ___/ / __ `/ /_/ / _ \/ __ \/ __ \/ ___/ __/")
print(" / / /  __(__  ) / /_/ / _, _/  __/ /_/ / /_/ / /  / /_  ")
print("/_/  \___/____/_/\__,_/_/ |_|\___/ .___/\____/_/   \__/  ")
print("                                /_/                      ")
print("By ST-R Motors")
print()

urllib.request.urlretrieve("http://192.168.90.100:4035/get_data_values?format=csv", "dataValues.csv")

with open('dataValues.csv', encoding="utf8") as file:
    content = file.readlines()
header = content[:1]
rows = content[1:]

capacity = 0
carType = ""

for row in rows:
    row = row.split(",")
    if row[0]=="VAPI_carType":
        carType = row[1]
        print("Vehicle Model: " + carType)

for row in rows:
    row = row.split(",")
    if row[0]=="VAPI_trim":
        trimName = row[1]
        print("Vehicle Trim: " + trimName)
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
            
for row in rows:
    row = row.split(",")
    if row[0]=="BMS_nominalFullPackEnergyRemaining":
        nominalFullPack = row[1]
        nominalFullPack = float(nominalFullPack[:len(nominalFullPack)-1])
        sohPercentage = (nominalFullPack/capacity)*100
        soh = str('%.2f' %sohPercentage)
        print("Battery SoH: %"+soh)