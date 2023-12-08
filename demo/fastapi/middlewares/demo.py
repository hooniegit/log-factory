from fastapi import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response
import logging

logging.basicConfig(filename='/Users/kimdohoon/git/study/log-factory/demo/fastapi/logs/error.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DemoMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:

        print(">>>>>>>>>>>>> START WORKING")
        logging.info(">>>>>>>>>>>>> START WORKING")  
           
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            logging.error(f"Internal Server Error: {str(e)}")
            raise HTTPException(status_code=500, detail="Internal Server Error")