from tuya_connector import TuyaOpenAPI, TUYA_LOGGER
import logging
import os

ACCESS_ID = os.getenv('AQUARIUM_ACCESS_ID')
ACCESS_KEY = os.getenv('AQUARIUM_ACCESS_KEY')
API_ENDPOINT = "https://openapi.tuyaus.com"
DEVICE_ID = os.getenv('AQUARIUM_DEVICE_ID')

def get_temp():
    openapi = TuyaOpenAPI(API_ENDPOINT,ACCESS_ID,ACCESS_KEY)
    openapi_connection = openapi.connect()

    response = openapi.get("/v1.0/iot-03/devices/{}/status".format(DEVICE_ID))
    for stat in response['result']:
        if response['result'][0]['code'] == 'va_temperature':
            return((response['result'][0]['value']/10)*1.8+32)
            break

    # response = openapi.get("/v1.0/iot-03/devices/{}/status".format(DEVICE_ID))
    # for stat in response['result']:
    #     if response['result'][0]['code'] == 'va_temperature':
    #         new_temp = (response['result'][0]['value']/10)*1.8+32
    #         if new_temp != current_temp:
    #             beep(4)
    #             print((response['result'][0]['value']/10)*1.8+32)
    #             current_temp = (response['result'][0]['value']/10)*1.8+32
    #         break

