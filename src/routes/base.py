from fastapi import APIRouter, FastAPI, Depends
from dotenv import load_dotenv
import os
from src.helpers.config import get_settings, Settings


base_router = APIRouter(
    prefix = "/api/v1",
    tags =["api_v1"]   
)
@base_router.get("/")
def welcome(app_setting: Settings=Depends(get_settings)):
    app_settings = get_settings()
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    
    app_version = os.getenv('APP_VERSION')
    return {
            "app_name": app_name,
            "app_version": app_version
            }