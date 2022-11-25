from fastapi import APIRouter,Depends
from database import get_db
from sqlalchemy.orm import Session
import models

router = APIRouter(tags=["dashboard"])


@router.get("/{country}")
async def Country(db:Session = Depends(get_db)):
    """returns the holiday of a country, if the country does not exist, it returns not found"""
    #relationship method
    # letter = user.letter
    country = db.query(models.Country).get(models.country.name==country ).all()

    holiday= db.query(models.Holiday).filter(models.Holiday.country_id == country.id).all()
    return {country,holiday}


# @router.get("/api/v1/dashboard/scheduled/{id}")
# async def Letterdetails(id:int,user:dict=Depends(get_current_user), db:Session = Depends(get_db)):
    # details  = db.query(models.Schedule).filter(models.Schedule.id == id).first()
    # return details



# @router.get("/api/v1/dashboard/sent/{id}")
# async def Letterdetails(id:int,user:dict=Depends(get_current_user), db:Session = Depends(get_db)):
    # details  = db.query(models.Letter).filter(models.Letter.id == id).first()
#     return details
