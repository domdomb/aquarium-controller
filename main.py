import aquarium_manager
import datetime
import time

def __main__():
    my_tank = aquarium_manager.AquariumManager()
    while True:
        my_tank.new_temp = my_tank.get_temp()
        print("Temp: ", my_tank.new_temp, "F -- ", datetime.datetime.now())
        if my_tank.new_temp != my_tank.current_temp:
            print("New temp | checking if action needed...")
            my_tank.current_temp = my_tank.new_temp
            my_tank.fan_check(my_tank.current_temp)
        time.sleep(120)


