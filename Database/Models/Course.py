from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped
from Database.Models.Base import Base

class Course(Base) :
    __tablename__ = 'course'

    code : Mapped[str] = mapped_column(String(10), primary_key=True)
    description : Mapped[str] = mapped_column(String(255), nullable= False)
    ecs : Mapped[int] = mapped_column(Integer(), nullable= False)