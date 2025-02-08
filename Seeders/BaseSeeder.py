from Repositories.Repository import Repository
from sqlalchemy.orm import Session
from abc import ABC, abstractmethod
import pandas as pd

class BaseSeeder(ABC) :

    def __init__(self, session : Session):
        self.session : Session = session

    @abstractmethod
    def seed(self, file_path : str) -> None : 
        pass