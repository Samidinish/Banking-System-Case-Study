import unittest
from models.customer import Customer
from models.account import Account


class TestCustomer(unittest.TestCase):
 
    def setUp(self):
        self.customer = Customer(
            first_name="John",
            last_name="Doe",
            address="123 Main St"
        )

    def test_add_account(self):
        account = Account(account_type="Savings", balance=500)
        self.customer.add_account(account)
        self.assertEqual(len(self.customer.get_accounts()), 1)


if __name__ == "__main__":
    unittest.main()
