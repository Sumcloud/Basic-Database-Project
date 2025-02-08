from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.sql import func
from datetime import datetime
from Database.Models.Base import Base

class Electives(Base) :
    __tablename__ = 'electives'

    enrollment_date : Mapped[datetime] = mapped_column(DateTime(), server_default=func.now(), primary_key=True)
    course : Mapped[str] = mapped_column(String(), ForeignKey('course.code'),primary_key=True)
    student : Mapped[int] = mapped_column(Integer(), ForeignKey('student.id'), primary_key=True)