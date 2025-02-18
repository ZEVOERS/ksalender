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

# example:
# class Cafe(Base):
#     __tablename__ = "db"

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(VARCHAR(120), nullable=False)
#     is_mkofficial = Column(Boolean, nullable=False, default=False)
#     created_at = Column(DATETIME, nullable=False, default=func.now())
#     is_deleted = Column(Boolean, nullable=False, default=False)
