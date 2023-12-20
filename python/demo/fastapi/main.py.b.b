from fastapi import FastAPI, HTTPException
import logging
from routers import demo as demo_router

app = FastAPI()

logging.basicConfig(filename='/Users/kimdohoon/git/study/log-factory/demo/fastapi/logs/error.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.middleware("http")
async def catch_exceptions(request, call_next):
    print(">>>>>>>>>>>>> START WORKING")
    logging.info(">>>>>>>>>>>>> START WORKING")
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        logging.error(f"Internal Server Error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

app.include_router(demo_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)

