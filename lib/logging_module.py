
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


def setup_logging():
    import logging

    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(format=log_format, level=logging.DEBUG)

    git_branch = get_git_branch()

    if git_branch and ('rel' in git_branch or 'main' in git_branch):
        logging.getLogger().setLevel(logging.INFO)


def timed_rotating_handler(log_dir:str):
    import logging
    from logging.handlers import TimedRotatingFileHandler
    from datetime import datetime
    
    # set log format
    log_format = "%(asctime)s - %(levelname)s - %(message)s"

    # set file handler
    file_handler = TimedRotatingFileHandler(
        f"{log_dir}/{datetime.now().strftime('%Y-%m-%d')}.log", 
        when="midnight", 
        interval=1, 
        backupCount=5, 
        encoding="utf-8")
    file_handler.setFormatter(logging.Formatter(log_format))

    # add file handler
    logging.getLogger().addHandler(file_handler)
    
    return file_handler


if __name__ == "__main__":
    import logging

    setup_logging()
    handler = timed_rotating_handler("/Users/kimdohoon/git/study/log-factory/log/sample")

    # 예제 DEBUG 로그
    logging.debug("This is a debug message.")
    logging.info("This is an informational message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")