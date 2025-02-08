from Database.Models.Electives import Electives
from Utils.Parser import Parser
from Repositories.Repository import Repository
from Seeders.BaseSeeder import BaseSeeder
import pandas as pd

class ElectivesSeeder(BaseSeeder) :

    def __init__(self, session):
        super().__init__(session)
        self.repository : Repository = Repository(session, Electives)
    
    def seed(self, file_path : str) -> None :
        df : pd.DataFrame = Parser.read_file(file_path)

        if df is None :
            print("No file!")
            return
        
        for _, row in df.iterrows() :
            elective = Electives(
                # Cast to int here as this seems to go wrong for association tables, I am not sure why, I think it has something to do with casting being laxer for this table IDK?
                course = int(row['course']),
                student = int(row['student']),
            )
            self.repository.add(elective)