from fastapi import FastAPI

from routers import demo as demo_router
from middlewares.demo import DemoMiddleware

app = FastAPI()

app.add_middleware(DemoMiddleware)
app.include_router(demo_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)