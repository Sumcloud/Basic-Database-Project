from sqlalchemy import Integer, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.sql import func
from datetime import datetime
from Database.Models.Base import Base

class Enrollment(Base) :
    __tablename__ = 'enrollment'

    enrollmentDate : Mapped[datetime] = mapped_column(DateTime(), server_default=func.now(), primary_key=True)
    student : Mapped[int] = mapped_column(Integer(), ForeignKey('student.id'), primary_key=True)
    program : Mapped[int] = mapped_column(Integer(), ForeignKey('studyprogram.id'), primary_key=True)