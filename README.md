# P02: Air Quality/Humidity Sensor for Mold

**Author(s)**: __*Garrett Clark, Silas Fair, Madinabonu Solijonova*__

**Google Document**: __*https://docs.google.com/document/d/1vEkP05DatnfGtrbYecCQdyYocopVIO_u0U4QBJyAbHo/edit?usp=sharing*__

---
## Purpose
**Air Quality/Humidity Sensor for Mold**: 
This class project aims to develop an air quality monitoring system using a Raspberry Pi and two sensors, a dust sensor, and a humidity/temperature sensor. The Raspberry Pi will collect and analyze real-time data from the sensors, and the data will be displayed on a unit for users to monitor air quality. The dust sensor will detect particulate matter in the air, while the humidity/temperature sensor will measure the relative humidity and temperature of the air. This project has potential applications in various settings, such as dorms, workspaces, and other public spaces, where air quality monitoring is important for maintaining a healthy and comfortable environment.

**Environmental Sustainability**: 
The use of the humidity and temperature sensors helps to promote environmental sustainability by preventing mold growth without the use of harsh chemicals. This method reduces the negative impact on the environment that is usually associated with mold remediation processes. Additionally, by detecting and monitoring conditions that lead to mold growth, the sensor helps to reduce the overall need for remediation and maintenance, which minimizes waste and energy consumption.

**Social Sustainability**: 
The Air Quality/Humidity Sensor for Mold project promotes social sustainability by improving the health and well-being of the campus community. Mold growth is a common health hazard that can cause respiratory problems and allergic reactions. By detecting and preventing mold growth, the sensor helps to maintain a safe and healthy environment for the community. This promotes social sustainability by ensuring the health and well-being of individuals and the community as a whole.

**Economic Sustainability**: 
The project promotes economic sustainability by reducing the cost associated with mold remediation and maintenance. The use of the humidity and temperature sensors helps to prevent the need for expensive remediation methods, which reduces the overall cost of maintenance. Additionally, by detecting and preventing mold growth, the project helps to minimize the potential financial and legal liabilities associated with mold-related health issues.

---

## Initial Design Plan

### Hardware Design
**Air Quality/Humidity Sensor for Mold**:
* KS0196 Sensor
* DHT22 Sensor
* Raspberry Pi
* T-Cobbler
* ADS1115

### Software Design
#### Class Name: **MoldSensor**
#### **Methods**:
- init(self): Initializes the Mold Sensor Rig by setting the settings for the DHT sensor, dust sensor, ADC, and the files. 
- start(self): Starts the Mold Sensor, continuously reading temperature and humidity values from the DHT sensor and saving them to the data file every 10 seconds.

### Data Design
- Data Type: 
  - Time: the date is saved in the following format month/date/year
  - Temperature: the temperature is measured in Celsius 
  - Humidity: the humidity levels are measured in percentage 
- Frequency of the Data: 
   - the data is collected every 10 seconds

![image](https://user-images.githubusercontent.com/97661971/226230326-53a2b3df-9595-466c-8ff9-7202d12c663a.png)
### Diagram Images

![DHT22 Sensor](https://github.com/CSC300-Embedded-Systems/p02-project-2-silas-madina-garrett/blob/299e4b322f7ee57cb1add314cebee5af348ec9cc/images/DHT22.jpg)
![image](https://user-images.githubusercontent.com/97661971/226479600-67463cc4-c96d-43ab-b868-01494b819b9f.png)
![image](https://user-images.githubusercontent.com/97661971/225777106-18c18982-5ed1-4415-bb9f-da50b6717dad.png)
![image](https://user-images.githubusercontent.com/97661971/225777162-6f7f241d-e624-496d-91cf-e1115a9c1b09.png)

## Files

* Data Folder: empty for now, but this directory will contain the files that contain the data,
* Images Folder: contains an example image, and diagrams for both sensors. 
* License: contains the licensing and copyright rules and regulations
* README.md: contains detailed information on the project, and the milestone regulations,
* example-README.md: this file has the instructions on how the actual README.md should be formatted
* data.csv: Contains data collected overnight for milestone 3.
* main.py: a python file which includes the instructions for collecting the data. 

### Project Files
* main.py: A python file that includes the code to collect the data. 
### Data Files
* data.csv: Contains data collected overnight for milestone 3.
## Instructions
1. Turn on
2. Place the embedded system in the desired location, data will start collecting every 10 seconds as soon as it is turned on
3. Depending how long you would like to collect data, remove the embedded system once enough data been collected
4. To access the data, remove the memory card and insert it in a computer
5. Locate an excel file called 'data.csv' 
6. Now, you have access to the data that the embedded system has collected over the period of time.
7. Interpret data
## Data Analysis
The following data is from 7 hours inside a vent in Anna Smith Residence Hall

* Average Humidity: 71.3% (Mold grows usually at above 70%)
* Average Temperature: 18.2 Celsius (Mold usually requires 25-30°C)
* Average Air Quality: 99.07 μg/m3 (Air quality over 35 μg/m3 can cause some)

![image_720](https://user-images.githubusercontent.com/78548914/227698277-6f2ffdf5-6b34-43bc-9671-e6f454e2b445.png)

**Sources:**
National Ambient Air Standards are established to be protective of public health. The short-term standard (24-hour or daily average) is 35 micrograms per cubic meter of air (µg/m3) and the long-term standard (annual average) is 12 µg/m3.d https://www.indoorairhygiene.org/pm2-5-

"The optimal temperature range for most common indoor mold species is 25-30°C, but some molds can grow at temperatures as low as 0°C and as high as 60°C" (Centers for Disease Control and Prevention, https://www.cdc.gov/mold/faqs.htm)

"Mold grows best in warm, damp, and humid conditions, typically between 68°F and 86°F (20°C and 30°C)" (United States Environmental Protection Agency, https://www.epa.gov/mold/mold-cleanup-your-home)

## Errors and Constraints
* Callibration of sensors usually means that they are not exact measurements 
* Detects the conditions in which mold should grow but does not directly detect the mold 
## References
* https://www.tomshardware.com/how-to/raspberry-pi-air-quality-monitor : Shows how to set up an air quality monitor and graph over time 
* https://www.piedmont.org/living-better/health-benefits-of-indoor-plants : we used this source to learn more about the benefits of keeping plants indoors as part of our planning stage. 
* https://iotdesignpro.com/projects/iot-based-soil-moisture-monitoring-system-using-esp32 : example of how someone else created their soil moisture monitor that includes instructions on how to make our own with circuit diagram, video instructions, etc. 
* https://quartzcomponents.com/blogs/electronics-projects/lpg-gas-leakage-detector-using-mq2-sensor-and-controller-using-sg90-servo-and-arduino : we used this to learn more about how we can create a gas leak detector. 
* https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/ : This is a base template for the humidity sensor.
* ChatGPT
* https://wiki.keyestudio.com/Ks0196_keyestudio_PM2.5_Shield : Code helped us understand the keyestudio sensor.
* https://www.epa.gov/pm-pollution/particulate-matter-pm-basics : Shows the levels of air quality that are unhealthy, for μg/m3 of particulate matter.
* https://www.epa.gov/sites/production/files/2014-05/documents/zones.pdf : Shows the EPA air quality ratings and what they mean.
* https://www.cdc.gov/mold/faqs.html : Showed the conditions at which mold is most likely to form and cause air quality issues.
* https://www.epa.gov/mold/mold-cleanup-your-home : Also shows ideal mold growth conditions.

## Summary and Reflection
The "Air Quality/Humidity Sensor for Mold" project aims to create a sustainable air quality monitoring system using a Raspberry Pi and two sensors, a dust sensor, and a humidity/temperature sensor. The project's objective is to improve the health and well-being of the campus community, prevent mold growth without the use of harsh chemicals, and reduce costs associated with mold remediation and maintenance.

The initial design plan included hardware and software design, with the hardware design comprising of the KS0196 sensor, the DHT22 sensor, and the Raspberry Pi. The software design included a class named MoldSensor that continuously reads temperature and humidity values from the DHT sensor and saves them to the data file every 10 seconds.

However, the team encountered issues getting the Wi-Fi to work on their Pi and had to reinstall drivers since they had no Wi-Fi. For some reason our drivers uninstalled or stopped working, but with the help of Proffessor Wilborne, Garrett was able to resolve the issue and set up the final sensor for sensing dust. The project's final data design includes time, temperature measured in Celsius, and humidity levels measured in percentage.

The project's data analysis revealed that the average humidity was 71.3%, which is above the threshold for mold growth, and the average temperature was 18.2 Celsius, within the range of spores' requirements, however, less than usual temperature required for mold growth. The average air quality was 99.07 μg/m3, indicating poor air quality. Using a graph, you may also observe a clear corelation in the data collected from each sensor. So humidity, air quality, and temperature all go up and down at the same time in the data we collected.

I think, the project has significant potential to improve air quality and promote sustainability by detecting and preventing mold growth in an eco-friendly way. 

## Final Self-Evaluations
### Ideation, Brainstorming, Design:
* *Garrett: 2*
* *Madina: 6*
* *Silas: 2*

### Code creation:
* *Garrett: 6*
* *Madina: 2*
* *Silas: 2*

### Documentation creation:
* *Garrett: 2*
* *Madina: 2*
* *Silas: 6*

### Teamwork & Participation:
* *Garrett: 3.33*
* *Madina: 3.33*
* *Silas: 3.33*
