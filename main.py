import os
import time
import csv
import Adafruit_DHT
import RPi.GPIO as GPIO
import Adafruit_ADS1x15

class MoldSensor:
    def __init__(self):
        print("Initializing Mold Sensor Rig")
        self.DHT_SENSOR = Adafruit_DHT.DHT22
        self.DHT_PIN = 13
        self.DUST_PIN = 21
        self.ADC_PIN = 3
        self.GAIN = 1  # Set the gain to 1 for reading voltages up to 4.096V
        self.adc = Adafruit_ADS1x15.ADS1115()
        self.filename = "data.csv"
       
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.DUST_PIN, GPIO.IN)

    def start(self):
        # Create a new "Data" folder if it doesn't exist
        if not os.path.exists("Data"):
            os.makedirs("Data")

        # Generate a unique file name with current time
        current_time = time.strftime("%m-%d-%Y_%H:%M:%S", time.localtime())
        file_name = "Data/data_{}.csv".format(current_time)

        while True:
            humidity, temperature = Adafruit_DHT.read_retry(self.DHT_SENSOR, self.DHT_PIN)

            voltage = self.adc.read_adc(self.ADC_PIN, gain=self.GAIN) / 32767.0 * 4.096  # Convert the raw ADC reading to voltage
            airQuality = 170 * voltage - 0.1   # Convert the voltage to particulate matter concentration in μg/m³ (based on PMS5003 datasheet)

            with open(file_name, mode='a+', newline='') as data_file:
                data_writer = csv.writer(data_file)
                # Write header row only if the file is newly created
                if data_file.tell() == 0:
                    data_writer.writerow(["Time", "Temperature(c)", "Humidity(%)", "Air Quality(μg/m3)"])
                print(['{0}'.format(current_time), 'Temp={0:0.1f}*C'.format(temperature), 'Humidity={0:0.1f}%'.format(humidity*3), 'Air Quality= {0}μg/m3'.format(airQuality)])
                data_writer.writerow(['{0}'.format(current_time), 'Temp={0:0.1f}*C'.format(temperature), 'Humidity={0:0.1f}%'.format(humidity*3), 'Air Quality= {0}μg/m3'.format(airQuality)])
            time.sleep(5)


if __name__ == "__main__":
    ms = MoldSensor()
    ms.start()