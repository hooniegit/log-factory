from fastapi import Request #
from fastapi.responses import JSONResponse 
import logging

async def custom_exception_handler(request: Request, exc: Exception):
    logging.error(f"Internal Server Error: {exc}")

    print("TEST SUCCEED")
    
    return JSONResponse(
        status_code=500,
        content={"message": "INTERNAL SERVER ERROR"},
    )