from sqlalchemy import Column, Integer, Float
from db.base import Base


class Loan(Base):
    """
    Represents a bank loan.
    """

    __tablename__ = "loans"

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    interest_rate = Column(Float, nullable=False)

    def calculate_due(self):
        return self.amount * (1 + self.interest_rate)
