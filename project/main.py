from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from routers.item import router as item_router
from routers.socket import socket_app
# init_sentry()

app = FastAPI()
# app.celery_app = celery_application
# celery = app.celery_app

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


base_router = APIRouter(prefix="/api/v1")
base_router.include_router(item_router)
app.include_router(base_router)
# app.mount("/static", StaticFiles(directory="static"), name="static")
# app.mount("/media", StaticFiles(directory="media"), name="media")
app.mount("/ws/", socket_app)

@app.get("/")
async def root():
    return {"message": "Fast API Test Project API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
