```
  ______          __      ____                        __
 /_  __/__  _____/ /___ _/ __ \___  ____  ____  _____/ /_
  / / / _ \/ ___/ / __ `/ /_/ / _ \/ __ \/ __ \/ ___/ __/
 / / /  __(__  ) / /_/ / _, _/  __/ /_/ / /_/ / /  / /_
/_/  \___/____/_/\__,_/_/ |_|\___/ .___/\____/_/   \__/
                                /_/
```

This Python script is designed to gather and process diagnostic data from a vehicle's onboard systems and present it in a human-readable format. It retrieves data values and diagnostic alerts from the vehicle, analyzes battery health and charging statistics, and provides general vehicle information.

## Features

- Retrieve data values from the vehicle's systems using the Tesla API.
- Display general information about the vehicle's features.
- Analyze battery state of health (SoH) and potential issues.
- Display recent service alerts and provide export options.
- Export a detailed health report in .docx format.
- Developer mode with additional options to reveal PINs, Spotify credentials, and WiFi network details.

## Usage

1. Clone this repository to your local machine.

   ```
   git clone https://github.com/strmotors/TeslaReport
   cd TeslaReport
   ```
   
2. Install the required Python libraries.

   ```
   pip install -r requirements.txt
   ```

3. Edit your base report file (basereport) using Microsoft Word (Optional)
   
4. Connect your computer to the diag port using a Fakra to ethernet cable.

5. Set your local IP to ```192.168.90.125```

6. Perform a secEth unlock using Toolbox or any other method you wish.

7. Run the script in your terminal.

   ```
   python teslaReport.py
   ```
   
8. Follow the on-screen menu to choose the desired operation.

## Note

- To edit the .docx file layout, just open the file "basereport" with Microsoft Word and edit the file as you wish. You should only keep the placeholders starting with "$" sign and you can put them wherever you want.
- Make sure you have the required permissions and access to the vehicle's data using the provided API endpoints.
- This script is for educational purposes and should be used responsibly and within the bounds of the law.

## Contributing

Contributions to improve and expand the script are welcome. Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.