import os
import time
import csv
import Adafruit_DHT

class MoldSensor:
    def __init__(self):
        print("Initializing Mold Sensor Rig")
        self.DHT_SENSOR = Adafruit_DHT.DHT22
        self.DHT_PIN = 13
        self.filename = "data.csv"

    def start(self):
        while True:
            humidity, temperature = Adafruit_DHT.read_retry(self.DHT_SENSOR, self.DHT_PIN)
            current_time = time.strftime("%m-%d %H:%M", time.localtime())

            with open(self.filename, mode='a+', newline='') as data_file:
                data_writer = csv.writer(data_file)
                if os.stat(self.filename).st_size == 0:
                    data_writer.writerow(["Time", "Temperature", "Humidity", "Air Quality"])
        
                data_writer.writerow([current_time, "Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity)])
            time.sleep(30)
