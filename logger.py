import logging
import datetime

def configure_logger():
    logging.basicConfig(
        filename='/var/log/aquarium-temp-controller/' + datetime.datetime.now().strftime("%Y-%m-%d|%H:%M:%S") + '.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )