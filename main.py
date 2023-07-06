import temp_controller
import kasa_controller
import time

print(temp_controller.get_temp())

def main():
    current_temp = 0
    while True:
        new_temp = temp_controller.get_temp()
        print("Temp: ", new_temp, "F")
        if new_temp != current_temp:
            current_temp = new_temp
            print(current_temp)
            fan_check(current_temp)
        time.sleep(10)


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


main()
# beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
# beep(4)
