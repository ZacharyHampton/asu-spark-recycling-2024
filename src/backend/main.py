from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.backend.api.v1 import router as api_v1_router
from src.backend.api.db import connect_to_mongo, close_mongo_connection

app = FastAPI()
app.include_router(api_v1_router)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("shutdown", close_mongo_connection)
app.add_event_handler("startup", connect_to_mongo)
