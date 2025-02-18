from fastapi import Request
from db.model import DBJoin, User

from sqlalchemy.orm import Session


def getUserBySession(req: Request, mariadb: Session):
    return (
        mariadb.query(User)
        .filter(
            User.idx == req.cookies.get("useridx"),
            User.session == req.cookies.get("session_id"),
        )
        .all()
    )


def DBJoinByUseridx(did: int, useridx: int, mariadb: Session):
    return mariadb.query(DBJoin).filter(DBJoin.db == did, DBJoin.user == useridx).all()
