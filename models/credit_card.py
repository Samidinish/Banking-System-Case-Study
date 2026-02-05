from sqlalchemy import Column, Integer, Float
from db.base import Base


class CreditCard(Base):
    """
    Represents a credit card.
    """

    __tablename__ = "credit_cards"

    id = Column(Integer, primary_key=True)
    limit = Column(Float, nullable=False)
    balance = Column(Float, default=0.0)

    def charge(self, amount):
        if self.balance + amount > self.limit:
            raise ValueError("Credit limit exceeded")
        self.balance += amount

    def pay(self, amount):
        self.balance -= amount
