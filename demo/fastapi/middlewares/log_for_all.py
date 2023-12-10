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
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class DemoMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:

        handler = file_handler(log_dir=log_dir)
        logging.getLogger().addHandler(handler)

        print(">>>>>>>>>>>>> START WORKING")
        logging.info(">>>>>>>>>>>>> START WORKING") 
        
        endpoint_path = request.url.path
        print(f"endpoint path: {endpoint_path}")
        logging.info(f"endpoint path: {endpoint_path}") 
           
        try:
            response = await call_next(request)
            logging.getLogger().removeHandler(handler)
            return response
        except Exception as e:
            logging.error(f"Internal Server Error: {str(e)}")
            logging.getLogger().removeHandler(handler)
            raise HTTPException(status_code=500, detail="Internal Server Error")
        