from fastapi import FastAPI
from database import engine
from fastapi.middleware.cors import CORSMiddleware
from models import *
from routers import authentication,countries,holidays


tags_metadata = [
    {
        "name": "auth",
        "description": "authenticating admin",
    },
    {
        "name": "countries",
        "description": "List of all countries",
    },
    {
        "name": "holidays",
        "description": "All Holidays for a particular country",
    },
]

app = FastAPI(
    title="Country Holidays",
    description="Know the days of rest of your country.",
    openapi_tags=tags_metadata
)
Base.metadata.create_all(engine)
app.add_middleware(CORSMiddleware,
allow_origins=['*'],
allow_credentials=True,
allow_methods=['*'],
allow_headers=['*'])


app.include_router(authentication.router)
app.include_router(countries.router)
app.include_router(holidays.router)
@app.get("/")
def get():
    return {"msg": "Your country's day of rest!"}

