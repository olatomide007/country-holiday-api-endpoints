from fastapi import APIRouter,Depends
from database import get_db
from sqlalchemy.orm import Session
import models

router = APIRouter(tags=["Holidays"])


@router.get("/{country}")
async def Country(country:str,db:Session = Depends(get_db)):
    """returns the holiday of a country, if the country does not exist, it returns not found"""
    #relationship method
    # letter = user.letter
    country = db.query(models.Country).get(models.country.name==country ).all()

    holiday= db.query(models.Holiday).filter(models.Holiday.country_id == country.id).all()
    return [{"country":country,"holiday":holiday}]


