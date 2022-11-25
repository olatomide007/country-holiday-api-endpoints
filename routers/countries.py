from fastapi import APIRouter,HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
from fastapi import Depends


router = APIRouter(tags=['countries'])


@router.get("/countries")
async def get_country(db:Session = Depends(get_db),):
    country_list = db.query(Countries).all()
    return country_list
