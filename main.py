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
        self.ADC_PIN = 3
        self.GAIN = 1  # Set the gain to 1 for reading voltages up to 4.096V
        self.filename = "data.csv"

        # Create an ADS1115 ADC instance
        self.adc = Adafruit_ADS1x15.ADS1115()

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.DHT_PIN, GPIO.IN)

    def start(self):
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(self.DHT_SENSOR, self.DHT_PIN)
            
            # Read the analog voltage from the ADS1115 on A3
            voltage = self.adc.read_adc(self.ADC_PIN, gain=self.GAIN) / 32767.0 * 4.096  # Convert the raw ADC reading to voltage
            airQuality = voltage  # Assign the voltage reading to airQuality

            current_time = time.strftime("%m-%d %H:%M", time.localtime())

            with open(self.filename, mode='a+', newline='') as data_file:
                data_writer = csv.writer(data_file)
                if os.stat(self.filename).st_size == 0:
                    data_writer.writerow(["Time", "Temperature", "Humidity", "Air Quality"])
                print(['{0}'.format(current_time), 'Temp={0:0.1f}*C'.format(temperature), 'Humidity={0:0.1f}%'.format(humidity*3), 'Air Quality= {0:0.1f}V'.format(airQuality)])
                data_writer.writerow(['{0}'.format(current_time), 'Temp={0:0.1f}*C'.format(temperature), 'Humidity={0:0.1f}%'.format(humidity*3), 'Air Quality= {0:0.1f}V'.format(airQuality)])
            time.sleep(30)
            

if __name__ == "__main__":
    ms = MoldSensor()
    ms.start()
