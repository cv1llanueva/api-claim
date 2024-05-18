from pydantic import BaseModel
#from datetime import date

class Claim(BaseModel):
    poliza_id: int
    fecha: str
    descripcion: str
    monto: float