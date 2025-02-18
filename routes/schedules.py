from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.connection import get_db
from db.model import Schedules
from utils.responses import SCHEDULE_NOT_FOUND

router = APIRouter(prefix="/schedules", tags="/schedules")


@router.get("/{sid}")
def srfunc(sid: int, mariadb: Session = Depends(get_db)):
    schedule_res = mariadb.query(Schedules).filter(Schedules.id == sid).all()
    if not schedule_res:
        raise SCHEDULE_NOT_FOUND
    return schedule_res


@router.post("/{sid}")
def srfunc(sid: int, mariadb: Session = Depends(get_db)):
    # HaruAPI required
    new_schedule = Schedules()
