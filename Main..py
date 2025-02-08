from sqlalchemy.orm import Session
from Database.ConnectionManager import ConnectionManager
from Seeders.SeederManager import SeederManager
from Database.Database import Database

class Main :

    @staticmethod
    def main() -> None :
        connection : ConnectionManager = ConnectionManager()
        connection.create_tables()

        session : Session = connection.get_session()

        seeder_manager : SeederManager = SeederManager(session)
        seeder_manager.run_all()

        session.close()

if __name__ == '__main__' :
    Main.main()