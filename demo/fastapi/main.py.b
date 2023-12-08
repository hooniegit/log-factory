from fastapi import FastAPI

from routers import demo as demo_router
from middlewares.demo import demo_middleware

app = FastAPI()

# add handlers & routers
app.add_middleware(demo_middleware)
app.include_router(demo_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
