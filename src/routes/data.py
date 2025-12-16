from fastapi import APIRouter, FastAPI, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os
from src.helpers.config import get_settings, Settings
from src.controllers import DataController

data_router = APIRouter(
    prefix = "/api/v1/data",
    tags =["api_v1","data"]   
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str,file : UploadFile,
                      app_settings: Settings = Depends(get_settings)):
    # validate the file properties
    is_valid, result_signal = DataController().validate_uploaded_file(file=file)
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal
            }
        )
   # Add success response
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "signal": result_signal,
        }
    )
