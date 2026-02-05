import unittest
from models.account import Account


class TestAccount(unittest.TestCase):


    def setUp(self):
        self.account = Account(account_type="Checking", balance=1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_withdraw(self):
        self.account.withdraw(300)
        self.assertEqual(self.account.balance, 700)

    def test_withdraw_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

    def test_get_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)


if __name__ == "__main__":
    unittest.main()
