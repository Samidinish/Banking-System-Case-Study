from db.database import get_session
from models.customer import Customer
from models.account import Account

session = get_session()

customer = Customer(
    first_name="John",
    last_name="Doe",
    address="123 Main St"
)

account = Account(
    account_type="Checking",
    balance=1000,
    customer=customer
)

session.add(customer)
session.add(account)
session.commit()
session.close()

print("Customer and account inserted successfully")
