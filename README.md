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
* SDS011 Sensor
* DHT22 Sensor
* Raspberry Pi

### Software Design

### Data Design

## Data Type: 
* Time: the date is saved in the following format month/date/year
* Temperature: the temperature is measured in Celsius 
* Humidity: the humidity levels are measured in percentage 
## Frequency of the Data: 
* the data is collected every 30 seconds

![image](https://user-images.githubusercontent.com/97661971/226230326-53a2b3df-9595-466c-8ff9-7202d12c663a.png)
### Diagram Images

![DHT22 Sensor](https://github.com/CSC300-Embedded-Systems/p02-project-2-silas-madina-garrett/blob/299e4b322f7ee57cb1add314cebee5af348ec9cc/images/DHT22.jpg)
![SD011 Sensor](https://github.com/CSC300-Embedded-Systems/p02-project-2-silas-madina-garrett/blob/299e4b322f7ee57cb1add314cebee5af348ec9cc/images/sds011.jpg)
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

## Data Analysis

## Errors and Constraints

## References
* https://www.tomshardware.com/how-to/raspberry-pi-air-quality-monitor
Shows how to set up an air quality monitor and graph over time
* https://www.piedmont.org/living-better/health-benefits-of-indoor-plants : we used this source to learn more about the benefits of keeping plants indoors as part of our planning stage. 
* https://iotdesignpro.com/projects/iot-based-soil-moisture-monitoring-system-using-esp32 : example of how someone else created their soil moisture monitor that includes instructions on how to make our own with circuit diagram, video instructions, etc. 
* https://quartzcomponents.com/blogs/electronics-projects/lpg-gas-leakage-detector-using-mq2-sensor-and-controller-using-sg90-servo-and-arduino : we used this to learn more about how we can create a gas leak detector. 
* https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/ : This is a base template for the humidity sensor.

## Summary and Reflection

## Final Self-Evaluations

### Ideation, Brainstorming, Design:

### Code creation: 

### Documentation creation:

### Teamwork & Participation:


