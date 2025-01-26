from fastapi import APIRouter
from app.RestService import RestService
import logging


router = APIRouter()
rest_service = RestService()


@router.get("/all")
async def get_all() -> dict[str, float]:
    logging.info("get_all called")
    return {**rest_service.get_moneys(), **rest_service.get_crypto()}

@router.get("/moneys")
async def get_moneys() -> dict[str, float]:
    logging.info("get_moneys called")
    return rest_service.get_moneys()

@router.get("/crypto")
async def get_crypto() -> dict[str, float]:
    logging.info("get_crypto called")
    return rest_service.get_crypto()