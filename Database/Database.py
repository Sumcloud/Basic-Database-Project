from sqlalchemy import create_engine, Engine

class Database :

    def __init__(self):
        self.engine : Engine = create_engine("sqlite:///university.db")