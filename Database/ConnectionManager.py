from sqlalchemy.orm import Session, sessionmaker
from Database.Database import Database
from Database.Models.Base import Base

# Models
from Database.Models.Course import Course
from Database.Models.Electives import Electives
from Database.Models.Enrollment import Enrollment
from Database.Models.Student import Student
from Database.Models.StudyProgram import StudyProgram
from Database.Models.StudyProgramType import StudyProgramType

class ConnectionManager :

    def __init__(self):
        self.database : Database = Database()
        self.SessionLocal = sessionmaker(bind = self.database.engine)
    
    def create_tables(self) :
        Base.metadata.create_all(self.database.engine)

    def get_session(self) -> Session :
        return self.SessionLocal()