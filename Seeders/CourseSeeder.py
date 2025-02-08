from Database.Models.Course import Course
from Utils.Parser import Parser
from Repositories.Repository import Repository
from Seeders.BaseSeeder import BaseSeeder
import pandas as pd

class CourseSeeder(BaseSeeder) :

    def __init__(self, session):
        super().__init__(session)
        self.repository : Repository = Repository(session, Course)
    
    def seed(self, file_path : str) -> None :
        df : pd.DataFrame = Parser.read_file(file_path)

        if df is None :
            print("No file!")
            return
        
        for _, row in df.iterrows() :
            course = Course(
                code = row['code'],
                description = row['description'],
                ecs = row['ecs']
            )
            self.repository.add(course)