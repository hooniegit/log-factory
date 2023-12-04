from time import time
import os, sys
now_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(now_dir, "../log")
lib_dir = os.path.join(now_dir, "../lib")
sys.path.append(lib_dir)

from file_handler import set_handler_timed_rotating
import logging

# set handler
tr_handler = set_handler_timed_rotating(log_dir = log_dir)

# record time
start_time = time()
print("Hello, World!" for I in range(1, 10))
end_time = time()

# write sample logs
logging.info(f"Time Spent(second): {end_time - start_time}")

# remove file handler
logging.getLogger().removeHandler(tr_handler)