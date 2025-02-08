from sqlalchemy.orm import Session
from typing import Optional
from Database.Models.Course import Course
from Repositories import Repository

class CourseRepository(Repository[Course]) :

    def __init__(self, session : Session) :
        super.__init__(session, Course)

    def get_by_identifier(self, code  :str ) -> Optional[Course] :
        return self.session.query(self.model).filter_by(code = code).first()