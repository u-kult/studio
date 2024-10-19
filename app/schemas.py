from datetime import date as pydate

from pydantic import BaseModel


class Reservation(BaseModel):

    date: pydate
    band: str
    id: int | None = None
