
def log_resource_usage(logger):
    import psutil
    import time
    
    try:
        cpu_percent = psutil.cpu_percent(interval=1) # Consider MacOS (ARM)
        memory_percent = psutil.virtual_memory().percent

        logger.error(f"CPU_Usage: {cpu_percent}% | RAM_Usage: {memory_percent}%")

    except Exception as e:
        logger.error(f"Error while logging resource usage: {e}", exc_info=True)



if __name__ == "__main__":
    import os, sys
    
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    from logging_module import setup_logger
    import logging
    
    test_logger = setup_logger(name="test", level=logging.INFO, log_dir="/Users/kimdohoon/git/study/log-factory/log")
    log_resource_usage(test_logger)