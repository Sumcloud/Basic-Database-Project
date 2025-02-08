from typing import List

# Seeders
from Seeders.BaseSeeder import BaseSeeder
from Seeders.CourseSeeder import CourseSeeder
from Seeders.StudentSeeder import StudentSeeder
from Seeders.StudyProgramTypeSeeder import StudyProgramTypeSeeder
from Seeders.StudyProgramSeeder import StudyProgramSeeder
from Seeders.StudyProgramMakeUpSeeder import StudyProgramMakeUpSeeder
from Seeders.EnrollmentSeeder import EnrollmentSeeder
from Seeders.ElectivesSeeder import ElectivesSeeder

from sqlalchemy.orm import Session

class SeederManager :

    def __init__(self, session : Session):
        self.seeders : List[BaseSeeder] = [
            CourseSeeder(session),
            StudentSeeder(session),
            StudyProgramTypeSeeder(session),
            StudyProgramSeeder(session),
            StudyProgramMakeUpSeeder(session),
            EnrollmentSeeder(session),
            ElectivesSeeder(session)
        ]

    def run_all(self) : 
        for seeder in self.seeders :
            filepath : str = f"Data/{seeder.__class__.__name__.replace('Seeder','').lower()}.csv"
            seeder.seed(file_path=filepath)