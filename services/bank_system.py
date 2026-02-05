import logging
from models.customer import Customer
from models.account import Account

logger = logging.getLogger(__name__)

class BankSystem:
    def __init__(self):
        self.customers = []

    def create_customer(self):
        fname = input("First name: ")
        lname = input("Last name: ")
        address = input("Address: ")
        customer = Customer(fname, lname, address)
        self.customers.append(customer)
        logger.info("Customer created")

    def run_cli(self):
        while True:
            print("\n1. Create Customer")
            print("2. Exit")
            choice = input("Choose option: ")

            try:
                if choice == "1":
                    self.create_customer()
                elif choice == "2":
                    break
                else:
                    print("Invalid choice")
            except Exception as e:
                logger.error("Error occurred", exc_info=True)
