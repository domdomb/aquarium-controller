import datetime
import time


start_time = datetime.datetime.now()

time.sleep(10)

current_time = datetime.datetime.now()

logging.info((current_time - start_time).total_seconds())


