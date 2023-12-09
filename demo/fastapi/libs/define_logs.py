
def get_git_branch():
    import os, subprocess
    
    now_dir = os.path.dirname(os.path.abspath(__file__))
    
    try:
        # git -C [path] rev-parse --abbrev-ref HEAD
        command = ["git", "-C", now_dir, "rev-parse", "--abbrev-ref", "HEAD"]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    
    except subprocess.CalledProcessError as e:
        print(f"Error Appeared: {e}")
        return None


def file_handler(log_dir:str):
    import logging
    from datetime import datetime
    
    # set log format
    log_format = "%(asctime)s - %(levelname)s - %(message)s"

    # set file handler
    file_handler = logging.FileHandler(
        f"{log_dir}/{datetime.now().strftime('%Y-%m-%d')}.log", 
        encoding="utf-8")
    file_handler.setFormatter(logging.Formatter(log_format))
    
    return file_handler


def setup_logger(name:str, level=None, log_dir=None):
    import logging

    # create logger
    logger = logging.getLogger(name)
    
    # set logger level
    if level == None:
        logger.setLevel(logging.DEBUG)
        # check github branch & change log level
        git_branch = get_git_branch()
        if git_branch and ('rel' in git_branch or 'main' in git_branch):
            logger.setLevel(logging.INFO)
    else:
        try:
            logger.setLevel(level)
        except:
            # print error message
            print("CANNOT SET LOG LEVEL - WRONG 'level' PARAMS")
            return

    # add file handler
    if log_dir != None:
        handler = file_handler(log_dir)
        logger.addHandler(handler)

    return logger