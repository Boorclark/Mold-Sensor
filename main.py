import os
import time
import csv
import Adafruit_DHT
import RPi.GPIO as GPIO
import Adafruit_ADS1x15

class MoldSensor:
    def __init__(self):
        # DHT sensor settings
        self.DHT_SENSOR = Adafruit_DHT.DHT22
        self.DHT_PIN = 13 
        
        # Dust sensor settings
        self.DUST_PIN = 21 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.DUST_PIN, GPIO.IN)
        
        # ADC settings
        self.ADC_PIN = 3
        self.GAIN = 1 
        self.adc = Adafruit_ADS1x15.ADS1115()   
        self.maxValADC = 32767.0 # Max val obtained from a 16-bit ADC
        self.maxVolRange = 4.096 # Max voltage range from a ADC
        
        # File settings
        self.filename = "data.csv"

    def start(self):
        # Create a new "Data" folder if it doesn't exist
        if not os.path.exists("Data"):
            os.makedirs("Data")

        # Generate a unique file name with current time
        current_time = time.strftime("%m-%d-%Y_%H:%M:%S", time.localtime())
        file_name = "Data/data_{}.csv".format(current_time)

        while True:
            # Read temperature and humidity from DHT sensor
            humidity, temperature = Adafruit_DHT.read_retry(self.DHT_SENSOR, self.DHT_PIN)

            # Convert the raw ADC reading to voltage
            voltage = self.adc.read_adc(self.ADC_PIN, gain=self.GAIN) / self.maxValADC * self.maxVolRange 
            
            # Convert the voltage to particulate matter concentration in μg/m³ 
            airQuality = 170 * voltage - 0.1   

            # Open the CSV file in append mode
            with open(file_name, mode='a+', newline='') as data_file:
                data_writer = csv.writer(data_file)
                # Write header row only if the file is newly created
                if data_file.tell() == 0:
                    data_writer.writerow(["Time", "Temperature(c)", "Humidity(%)", "Air Quality(μg/m3)"])

                # Write data collected to a row in the CSV
                data_writer.writerow(['{0}'.format(current_time), '{0:0.1f}'.format(temperature), '{0:0.1f}'.format(humidity), '{0}'.format(airQuality)])
            time.sleep(10)


if __name__ == "__main__":
    ms = MoldSensor()
    ms.start()