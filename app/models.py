from datetime import date as pydate

from pydantic import BaseModel


class ReservationModel(BaseModel):

    date: pydate
    band: str
    id: int | None = None
