import os
now_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(now_dir, "../log")

import logging
from logging.handlers import TimedRotatingFileHandler
from time import time

# set level & fromat
level = logging.INFO
format = "%(asctime)s - %(levelname)s - %(message)s"

# set basic config
logging.basicConfig(level=level, format=format)

# set file handler
file_handler = TimedRotatingFileHandler(
    f"{log_dir}/sample/TimedRotatingFileHandler.sample", 
    when="midnight", 
    interval=1, 
    backupCount=5, 
    encoding="utf-8")
file_handler.setFormatter(logging.Formatter(format))

# add file handler
logging.getLogger().addHandler(file_handler)

# record time
start_time = time()
print("Hello, World!" for I in range(1, 10))
end_time = time()

# write sample logs
logging.info(f"Time Spent(second): {end_time - start_time}")

# remove file handler
logging.getLogger().removeHandler(file_handler)