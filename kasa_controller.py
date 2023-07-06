import logging
import subprocess
import time

def heater_control(toggle):
    command = "kasa --host 192.168.1.80 " + toggle +" --name \"40g heater\""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(10)
    stdout, stderr = process.communicate()
    # Print the output
    logging.info("Heater Status: ")
    logging.info(stdout.decode())

def fan_control(toggle):
    command = "kasa --host 192.168.1.80 " + toggle +" --name \"40g Cooling fans\""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(10)
    stdout, stderr = process.communicate()
    # Print the output
    logging.info("Fan Status: ")
    logging.info(stdout.decode())

# import asyncio
# import kasa
# import pprint
# async def get_plugs():
    # p = kasa.SmartPlug("192.168.1.80")
    # await p.update()    # Request the update
    # plugs = p.sys_info  # all info on strip
    # plugs = p.children
    # pprint.plogging.info(plugs)
    # for plug in plugs['children']:
    #     if plug['alias'] == "40g Cooling fans":
    #         plug.turn_on()
