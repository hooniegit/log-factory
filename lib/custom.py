
def log_resource_usage(logger):
    import psutil
    
    try:
        cpu_percent = psutil.cpu_percent(interval=1) # Consider MacOS (ARM)
        memory_percent = psutil.virtual_memory().percent

        logger.error(f"CPU_Usage: {cpu_percent}% | RAM_Usage: {memory_percent}%")

    except Exception as e:
        logger.error(f"Error while logging resource usage: {e}", exc_info=True)
        

def log_and_alert_cpu(logger, boundary:tuple):
    import psutil
    
    try:
        boundary_warning = boundary[0]
        boundary_error = boundary[1]
        
        cpu_percent = psutil.cpu_percent(interval=1) # Consider MacOS (ARM)
        
        if cpu_percent < boundary_warning:
            logger.info(f"CPU_Usage: {cpu_percent}% - STABLE")
        
        elif boundary_warning <= cpu_percent < boundary_error:
            logger.warning(f"CPU_Usage: {cpu_percent}% - SYSTEM IS IN DANGER, ACTION REQUIRED")
        
        elif cpu_percent >= boundary_error:
            logger.error(f"CPU_Usage: {cpu_percent}% - IMMEDIATE ACTION REQUIRED!!")
            
    except:
        print("boundary param is wrong")
        

# TEST
if __name__ == "__main__":
    import os, sys
    
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    
    from logging_module import setup_logger
    import logging
    
    test_logger = setup_logger(name="test", level=logging.INFO, log_dir="/Users/kimdohoon/git/study/log-factory/log")
    log_and_alert_cpu(test_logger, (70, 90))