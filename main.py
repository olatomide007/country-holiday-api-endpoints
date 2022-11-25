from fastapi import FastAPI
import schemas 
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Country names"}

  ##### IMPORTING#####
import pandas as pd
import json


csv_path = r"C:\Users\HP\Desktop\my-files\python\hng\hng-freelancer\country-holiday-api-endpoints\holiday_calendar.csv"
csv_data = pd.read_csv(csv_path, sep= ',')

# Converting to json
json_path = r"C:\Users\HP\Desktop\my-files\python\hng\hng-freelancer\country-holiday-api-endpoints\holiday_calendar.json"
json_data = csv_data.to_json(json_path, indent = 1, orient='records')
with open(json_path, 'r') as jfile:
    data = json.loads(jfile.read())

@app.get("/countries")
async def countries():
    country = []
    for step_data in data:
        if step_data["Country"] in country:
            step_data["Country"] = 0
        else:
            country.append(step_data["Country"])
    return country


@app.get("/{country}")
async def country():
    country_holiday = []
    for step_data in data:
        if step_data["Country"] and step_data["Holiday Name"] in country_holiday:
            step_data["Country"]= 0
            step_data["Holiday Name"] = 0
        else:
            country_holiday.append(step_data["Country"] + " : " + step_data["Holiday Name"])
    return country_holiday
