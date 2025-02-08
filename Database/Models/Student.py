from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped
from Database.Models.Base import Base

class Student(Base) :
    __tablename__ = 'student'

    id : Mapped[int] = mapped_column(primary_key=True, unique=True, nullable=False,autoincrement=True)
    first_name : Mapped[str] = mapped_column(String(),nullable=False)
    last_name : Mapped[str] = mapped_column(String(), nullable=False)