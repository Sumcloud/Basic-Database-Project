from Database.Models.Enrollment import Enrollment
from Utils.Parser import Parser
from Repositories.Repository import Repository
from Seeders.BaseSeeder import BaseSeeder
import pandas as pd

class EnrollmentSeeder(BaseSeeder) :

    def __init__(self, session):
        super().__init__(session)
        self.repository : Repository = Repository(session, Enrollment)
    
    def seed(self, file_path : str) -> None :
        df : pd.DataFrame = Parser.read_file(file_path)

        if df is None :
            print("No file!")
            return
        
        for _, row in df.iterrows() :
            enrollment = Enrollment(
                # Cast to int here as this seems to go wrong for association tables, I am not sure why, I think it has something to do with casting being laxer for this table IDK?
                student = int(row['student']),
                program = int(row['program']),
            )
            self.repository.add(enrollment)