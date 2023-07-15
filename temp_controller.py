

    # response = openapi.get("/v1.0/iot-03/devices/{}/status".format(DEVICE_ID))
    # for stat in response['result']:
    #     if response['result'][0]['code'] == 'va_temperature':
    #         new_temp = (response['result'][0]['value']/10)*1.8+32
    #         if new_temp != current_temp:
    #             beep(4)
    #             print((response['result'][0]['value']/10)*1.8+32)
    #             current_temp = (response['result'][0]['value']/10)*1.8+32
    #         break

