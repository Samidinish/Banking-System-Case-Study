from db.database import get_session
from models.customer import Customer
from models.account import Account
from models.loan import Loan
from models.credit_card import CreditCard
from models.employee import Employee


def seed_data():
    session = get_session()

    try:
        # -------------------------
        # Customers
        # -------------------------
        customer1 = Customer(
            first_name="John",
            last_name="Doe",
            address="123 Main St, NY"
        )

        customer2 = Customer(
            first_name="Jane",
            last_name="Smith",
            address="456 Oak Ave, CA"
        )

        customer3 = Customer(
            first_name="Alice",
            last_name="Brown",
            address="789 Pine Rd, TX"
        )

        # -------------------------
        # Accounts
        # -------------------------
        account1 = Account(account_type="Checking", balance=1500, customer=customer1)
        account2 = Account(account_type="Savings", balance=5000, customer=customer1)

        account3 = Account(account_type="Checking", balance=2200, customer=customer2)
        account4 = Account(account_type="Savings", balance=8000, customer=customer3)

        # -------------------------
        # Loans
        # -------------------------
        loan1 = Loan(amount=10000, interest_rate=0.05)
        loan2 = Loan(amount=20000, interest_rate=0.07)

        # -------------------------
        # Credit Cards
        # -------------------------
        card1 = CreditCard(limit=5000)
        card2 = CreditCard(limit=10000)

        # -------------------------
        # Employees
        # -------------------------
        employee1 = Employee(
            first_name="Michael",
            last_name="Scott",
            role="Branch Manager",
            department="Management"
        )

        employee2 = Employee(
            first_name="Pam",
            last_name="Beesly",
            role="Teller",
            department="Customer Service"
        )

        # -------------------------
        # Persist everything
        # -------------------------
        session.add_all([
            customer1, customer2, customer3,
            account1, account2, account3, account4,
            loan1, loan2,
            card1, card2,
            employee1, employee2
        ])

        session.commit()
        print("Sample data inserted successfully")

    except Exception as e:
        session.rollback()
        print("Error inserting sample data:", e)

    finally:
        session.close()


if __name__ == "__main__":
    seed_data()
