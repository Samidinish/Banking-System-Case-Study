from sqlalchemy import Column, Integer, Float
from db.base import Base


class CreditCard(Base):
    __tablename__ = "credit_cards"

    id = Column(Integer, primary_key=True)
    limit = Column(Float, nullable=False)
    balance = Column(Float, default=0.0)


    def charge(self, amount):
        if amount <= 0:
            raise ValueError("Charge amount must be positive")

        current_balance = self.balance or 0
        if current_balance + amount > self.limit:
            raise ValueError("Credit limit exceeded")

        self.balance = current_balance + amount

    def pay(self, amount):
        if amount <= 0:
            raise ValueError("Payment must be positive")

        self.balance = (self.balance or 0) - amount
