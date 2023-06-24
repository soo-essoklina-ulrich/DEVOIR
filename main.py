from fastapi import FastAPI, Depends
from models import Vehicule, Proprio, vehicules as Pyvehicules, Categories
from typing import List
from db import Session


app = FastAPI()


@app.get("/category/{category}")
async def category(category: str) -> List[Vehicule]:
    return []


@app.get("/owner/{owner}")
async def owner(owner: str) -> List[Vehicule]:
    return [vehicle for vehicle in Pyvehicules if vehicle.owner == owner]


@app.get("/bills/{owner}")
async def bills(owner: str) -> List[Proprio]:
    bills = []
    for vehicle in Pyvehicules:
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


@app.post("/add-new", response_model=Vehicule)
async def add_new(vh: Vehicule, db: Session = Depends(get_db)):
    vhs = Pyvehicules(id=vh.id, immatricule=vh.immatricule, owner=vh.owner, cotation=vh.cotation, facture=vh.facture)
    db.add(vhs)
    db.commit()
    db.refresh(vhs)

    return Pyvehicules(**vh.dict())
