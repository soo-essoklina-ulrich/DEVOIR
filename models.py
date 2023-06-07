from pydantic import BaseModel



# classe des vehicules
class Vehicule(BaseModel):
    immatricule: str
    owner: str
    category: str
    cotation: float
    facture: float



#class du proprietaire
class Proprio(BaseModel):
    immatricule: str
    owner: str
    cotation: float
    facture: float
    total: float


Categories = [
    Vehicule(immatricule="", owner="", category="", cotation=0.0, facture=0.0),
    Vehicule(immatricule="", owner="", category="", cotation=0.0, facture=0.0),
    
]
vehicules = [
    Vehicule(immatricule="1-ABC-123", owner="Jean ", category="Voiture", cotation=100.0, facture=1000.0),
    Vehicule(immatricule="1-DEF-456", owner="Jean2", category="Moto", cotation=20.0, facture=1000.0),
    Vehicule(immatricule="1-GHI-789", owner="Jean3", category="Voiture", cotation=500.0, facture=1000.0),
    Vehicule(immatricule="1-JKL-012", owner="Jean4", category="Moto", cotation=50.0, facture=1000.0),
]
