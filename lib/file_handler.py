
def set_handler_timed_rotating(log_dir:str):
    import logging
    from logging.handlers import TimedRotatingFileHandler
    from datetime import datetime
    
    # set level & fromat
    level = logging.INFO
    format = "%(asctime)s - %(levelname)s - %(message)s"

    # set basic config
    logging.basicConfig(level=level, format=format)

    # set file handler
    file_handler = TimedRotatingFileHandler(
        f"{log_dir}/{datetime.now().strftime('%Y-%m-%d')}.log", 
        when="midnight", 
        interval=1, 
        backupCount=5, 
        encoding="utf-8")
    file_handler.setFormatter(logging.Formatter(format))

    # add file handler
    logging.getLogger().addHandler(file_handler)
    
    return file_handler