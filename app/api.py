from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import get_db
from .models import ReservationModel
from .orm import Base
from .orm import ReservationOrm

router = APIRouter()


@router.post('/create')
def create_all():
    return Base.metadata.create_all()


@router.get('/reservations', response_model=list[ReservationModel])
def get_reservations(db: Annotated[Session, Depends(get_db)]):
    return db.scalars(select(ReservationOrm))
