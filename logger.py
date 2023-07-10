import logging
import datetime

def configure_logger():
    logfile = '/var/log/aquarium-temp-controller/' + datetime.datetime.now().strftime("%Y-%m-%d|%H:%M:%S") + '.log'
    logging.basicConfig(
        filename=logfile,
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    file = open("logging.conf", "w")
    file.write(logfile)
