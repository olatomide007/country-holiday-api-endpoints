from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Country names"}

@app.get("/countries")
async def countries():
    pass


@app.get("/{country}")
async def country():
    pass
