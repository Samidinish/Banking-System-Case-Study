from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.base import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    address = Column(String, nullable=False)

    accounts = relationship("Account", back_populates="customer")

    def add_account(self, account):
        self.accounts.append(account)

    def get_accounts(self):
        return self.accounts
