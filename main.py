import temp_controller
import temp_check
import kasa_controller
import time
import datetime
import logging

def main():
    current_temp = 0
    while True:
        new_temp = temp_controller.get_temp()
        print("Temp: ", new_temp, "F -- ", datetime.datetime.now())
        if new_temp != current_temp:
            print("New temp | checking if action needed...")
            current_temp = new_temp
            temp_check.fan_check(current_temp)
        time.sleep(10)

main()

