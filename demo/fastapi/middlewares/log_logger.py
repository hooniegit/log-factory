import os, sys

now_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(now_dir, "../libs")
log_dir = os.path.join(now_dir, "../logs")

sys.path.append(lib_dir)

from log_libs import *
from os_libs import *

from fastapi import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response


class DemoMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:

        endpoint_path = request.url.path
        logger_name = endpoint_path.replace("/", "_")[1:]

        log_file_dir = f"{log_dir}/{logger_name}"
        check_mkdirs(log_file_dir) # module

        logger = setup_logger(name=logger_name, log_dir=log_file_dir) # module - can set: name, level, log_dir
        
        print(f"logger name: {logger_name}")
        logger.info(f"logger name: {logger_name}") 
           
        try:
            response = await call_next(request)
            remove_logger(logger) # module
            return response
        
        except Exception as e:
            message = f"Internal Server Error - {endpoint_path} - {str(e)}"
            logger.error(message)
            send_line_notification_thread(message=message) # module
            remove_logger(logger) # module
            raise HTTPException(status_code=500, detail="Internal Server Error")
        