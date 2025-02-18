from sqlalchemy import (
    Column,
    Integer,
    Boolean,
    VARCHAR,
    CHAR,
    DATETIME,
    Enum,
    func,
    ForeignKey,
)
from db.connection import Base


class Schedules(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(VARCHAR(60), nullable=False)
    uploaded_at = Column(DATETIME, nullable=False, default=func.now())
    title = Column(VARCHAR(900), nullable=False)
    starts_at = Column(DATETIME, nullable=False, default=func.now())
    ends_at = Column(DATETIME, nullable=False, default=func.now())
    content = Column(VARCHAR(9000), nullable=False)
