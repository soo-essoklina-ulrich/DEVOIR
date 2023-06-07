from fastapi import FastAPI
from models import Vehicule, Proprio, vehicules, Categories
from typing import List


app = FastAPI()

 
@app.get("/category/{category}")
async def category(category: str) -> List[Vehicule]:
    return [category for category in Categories if category.category == category ]

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
