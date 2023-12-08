from fastapi import Request

async def demo_middleware(request: Request, call_next):
    import logging
    from fastapi.exceptions import HTTPException
    
    print(">>>>>>>> HELLO, WORLD!")
    
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        logging.error(f"Internal Server Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")