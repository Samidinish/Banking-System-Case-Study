from sqlalchemy import Column, Integer, String
from db.base import Base


class Employee(Base):
  

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    department = Column(String, nullable=False)

    def __repr__(self):
        return (
            f"Employee(id={self.id}, "
            f"name={self.first_name} {self.last_name}, "
            f"role={self.role}, department={self.department})"
        )
