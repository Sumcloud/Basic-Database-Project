from Database.Models.StudyProgramMakeUp import StudyProgramMakeUp
from Utils.Parser import Parser
from Repositories.Repository import Repository
from Seeders.BaseSeeder import BaseSeeder
import pandas as pd

class StudyProgramMakeUpSeeder(BaseSeeder) :

    def __init__(self, session):
        super().__init__(session)
        self.repository : Repository = Repository(session, StudyProgramMakeUp)
    
    def seed(self, file_path : str) -> None :
        df : pd.DataFrame = Parser.read_file(file_path)

        if df is None :
            print("No file!")
            return
        
        for _, row in df.iterrows() :
            studyProgramMakeUp = StudyProgramMakeUp(
                course = row['course'],
                studyProgram = row['studyProgram'],
            )
            self.repository.add(studyProgramMakeUp)