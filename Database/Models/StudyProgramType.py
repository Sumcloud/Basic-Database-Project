from sqlalchemy import String
from sqlalchemy.orm import relationship, mapped_column, Mapped
from typing import List
from Database.Models.StudyProgram import StudyProgram
from Database.Models.Base import Base

class StudyProgramType(Base) :
    __tablename__ = 'studyprogramtype'

    code : Mapped[str] = mapped_column(String(),primary_key=True)
    description : Mapped[str] = mapped_column(String(),unique=True, nullable=False)

    programs : Mapped[List['StudyProgram']] = relationship()