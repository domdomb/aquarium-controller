import kasa_controller

def fan_check(current_temp):
    if current_temp >= 81.5:
        kasa_controller.fan_control("on")
        kasa_controller.heater_control("off")
        print("current temp: ", current_temp, " | Fan: On | Heater: Off")
        return
    if current_temp <= 80.4:
        kasa_controller.fan_control("off")
        kasa_controller.heater_control("on")
        print("current temp: ", current_temp, " | Fan: Off | Heater: On")
        return
    else:
        print("No action required")
