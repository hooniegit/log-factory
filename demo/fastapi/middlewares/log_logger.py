import os, sys

now_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(now_dir, "../libs")
log_dir = os.path.join(now_dir, "../logs")

sys.path.append(lib_dir)

from define_logs import *

from fastapi import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response


class DemoMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:

        endpoint_path = request.url.path
        logger_name = endpoint_path.replace("/", "_")[1:]

        log_file_dir = f"{log_dir}/{logger_name}"
        if not os.path.exists(log_file_dir):
            os.makedirs(log_file_dir)
        else:
            pass

        # can set - name, level, log_dir
        logger = setup_logger(name=logger_name, log_dir=log_file_dir)

        print(">>>>>>>>>>>>> START WORKING")
        logger.info(">>>>>>>>>>>>> START WORKING") 
        
        print(f"logger name: {logger_name}")
        logger.info(f"logger name: {logger_name}") 
           
        try:
            response = await call_next(request)
            for handler in logger.handlers[:]:
                logger.removeHandler(handler) # remove handlers
            for filter_ in logger.filters[:]:
                logger.removeFilter(filter_) # remove filters
            return response
        
        except Exception as e:
            logger.error(f"Internal Server Error: {str(e)}")
            for handler in logger.handlers[:]:
                logger.removeHandler(handler) # remove handlers
            for filter_ in logger.filters[:]:
                logger.removeFilter(filter_) # remove filters
            raise HTTPException(status_code=500, detail="Internal Server Error")
        