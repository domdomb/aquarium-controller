from tuya_connector import TuyaOpenAPI, TUYA_LOGGER
import logging
import os


# https://github.com/prometheus/client_python

class AquariumManager:
    def __init__(self):
        self.ACCESS_ID = os.getenv('AQUARIUM_ACCESS_ID')
        self.ACCESS_KEY = os.getenv('AQUARIUM_ACCESS_KEY')
        self.API_ENDPOINT = "https://openapi.tuyaus.com"
        self.DEVICE_ID = os.getenv('AQUARIUM_DEVICE_ID')
        self.logger = logging.getLogger('mytest') #unique identifier from main or prometheus 
        self.current_temp = 0
        

        
    def fan_check(self):
        if self.current_temp >= 81.5:
            self.fan_control("on")
            self.heater_control("off")
            print("current temp: ", self.current_temp, " | Fan: On | Heater: Off")
            return
        if self.current_temp <= 80.4:
            self.fan_control("off")
            self.heater_control("on")
            print("current temp: ", self.current_temp, " | Fan: Off | Heater: On")
            return
        else:
            print("No action required")
            
    def get_temp(self):
        openapi = TuyaOpenAPI(self.API_ENDPOINT, self.ACCESS_ID, self.ACCESS_KEY)
        openapi_connection = openapi.connect()

        response = openapi.get("/v1.0/iot-03/devices/{}/status".format(self.DEVICE_ID))
        for stat in response['result']:
            if response['result'][0]['code'] == 'va_temperature':
                self.current_temperature = ((response['result'][0]['value']/10)*1.8+32)
                break

    def fan_check(self):
        if self.current_temp >= 81.5:
            self.kasa_controller.fan_control("on")
            self.kasa_controller.heater_control("off")
            print("current temp: ", self.current_temp, " | Fan: On | Heater: Off")
            return
        if self.current_temp <= 80.4:
            self.kasa_controller.fan_control("off")
            self.kasa_controller.heater_control("on")
            print("current temp: ", self.current_temp, " | Fan: Off | Heater: On")
            return
        else:
            print("No action required")