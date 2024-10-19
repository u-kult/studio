from typing import Annotated

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from .database import engine
from .database import get_db
from .models import ReservationModel
from .orm import Base
from .orm import ReservationOrm

router = APIRouter()


@router.post('/create')
def create_all():
    return Base.metadata.create_all(engine)


@router.get('/reservations')
def get_reservations(
    db: Annotated[Session, Depends(get_db)],
) -> list[ReservationModel]:
    return db.scalars(select(ReservationOrm))


@router.post('/reservation')
def add_reservation(
    model: ReservationModel,
    db: Annotated[Session, Depends(get_db)],
) -> ReservationModel:
    reservation = ReservationOrm(
        **model.model_dump()
    )

    db.add(reservation)
    db.flush()
    db.refresh(reservation)

    return reservation
