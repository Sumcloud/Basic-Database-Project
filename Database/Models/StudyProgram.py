from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped
from Database.Models.Base import Base

class StudyProgram(Base) :
    __tablename__ = 'studyprogram'

    id : Mapped[int] = mapped_column(Integer(),primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(),nullable=False)

    # Relationships
    level : Mapped[str] = mapped_column(ForeignKey('studyprogramtype.code'))