import logging
import datetime

def configure_logger():
    logfile = '/var/log/aquarium-temp-controller/' + datetime.datetime.now().strftime("%Y-%m-%d|%H:%M:%S") + '.log'
    logging.basicConfig(
        filename='/var/log/aquarium-temp-controller/' + datetime.datetime.now().strftime("%Y-%m-%d|%H:%M:%S") + '.log',
        level=logging.info,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='w'
    )
    file = open("logging.conf", "w")
    file.write(logfile)
