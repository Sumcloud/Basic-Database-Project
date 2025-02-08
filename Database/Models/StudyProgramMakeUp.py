from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from Database.Models.Base import Base

class StudyProgramMakeUp(Base) :
    __tablename__ = 'studyprogrammakeup'

    course : Mapped[str] = mapped_column(String(), ForeignKey('course.code'), primary_key=True)
    studyProgram : Mapped[int] = mapped_column(Integer(), ForeignKey('studyprogram.id'), primary_key=True)