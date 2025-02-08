from Database.Models.StudyProgram import StudyProgram
from Utils.Parser import Parser
from Repositories.Repository import Repository
from Seeders.BaseSeeder import BaseSeeder
import pandas as pd

class StudyProgramSeeder(BaseSeeder) :

    def __init__(self, session):
        super().__init__(session)
        self.repository : Repository = Repository(session, StudyProgram)
    
    def seed(self, file_path : str) -> None :
        df : pd.DataFrame = Parser.read_file(file_path)

        if df is None :
            print("No file!")
            return
        
        for _, row in df.iterrows() :
            studyProgram = StudyProgram(
                id = row['id'],
                name = row['name'],
                level = row['level']
            )
            self.repository.add(studyProgram)