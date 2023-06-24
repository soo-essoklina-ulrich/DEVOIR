from fastapi import FastAPI
from models import Vehicule, Proprio, vehicules, Categories
from typing import List
from db import Session


app = FastAPI()

 
@app.get("/category/{category}")
async def category(category: str) -> List[Vehicule]:
    return []

@app.get("/owner/{owner}")
async def owner(owner: str) -> List[Vehicule]:
    return [vehicle for vehicle in vehicules if vehicle.owner == owner]

@app.get("/bills/{owner}")
async def bills(owner: str) -> List[Proprio]:
    bills = []
    for vehicle in vehicules:
        if vehicle.owner == owner:
            total = vehicle.cotation + vehicle.facture
            bill = Proprio(
                registration=vehicle.immatricule,
                owner=vehicle.owner,
                cotation=vehicle.cotation,
                facture=vehicle.facture,
                total_amount=total
            )
            bills.append(bill)
    return bills

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()