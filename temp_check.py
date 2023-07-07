import kasa_controller
import logging

def fan_check(current_temp):
    if current_temp >= 81.3:
        print("current temp: ", current_temp, " | Fan: On | Heater: Off")
        kasa_controller.fan_control("on")
        kasa_controller.heater_control("off")
        return
    if current_temp <= 80.1:
        print("current temp: ", current_temp, " | Fan: Off | Heater: On")
        kasa_controller.fan_control("off")
        kasa_controller.heater_control("on")
        return
    else:
        print("No action required")
