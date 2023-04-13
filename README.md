```
  ______          __      ____                        __
 /_  __/__  _____/ /___ _/ __ \___  ____  ____  _____/ /_
  / / / _ \/ ___/ / __ `/ /_/ / _ \/ __ \/ __ \/ ___/ __/
 / / /  __(__  ) / /_/ / _, _/  __/ /_/ / /_/ / /  / /_
/_/  \___/____/_/\__,_/_/ |_|\___/ .___/\____/_/   \__/
                                /_/
```
 Tesla status reporter, written in Python, using CSV vitals.

## Functions

- **General Information:** Grab general information about the vehicle.
- **Battery SoH Percentage:** Compute the state of health of the high-voltage battery.
- **Service Alerts:** See last (up to) 100 service alerts and save as a text document.

More coming up!

## Installation
```
git pull https://github.com/strmotors/teslaReport
cd TeslaReport
python teslaReport.py
```

## Usage
- Connect your computer to the diag port using a Fakra to ethernet cable.
- Set your local IP to ```192.168.90.125```
- Perform a seceth unlock using Toolbox or any other method you wish.
- Run the Python script.
