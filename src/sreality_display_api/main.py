
from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from data.database import database, table

app = FastAPI()
templates = Jinja2Templates(directory="templates")
#import json
#with open("../../data/sreality_flats.json") as f:
#    data = json.load(f)
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    query = table.select()
    data = await database.fetch_all(query)
    return templates.TemplateResponse("scrapped_items.html", {"request": request, "items": data})
