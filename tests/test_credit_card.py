import unittest
from models.credit_card import CreditCard


class TestCreditCard(unittest.TestCase):

    def setUp(self):
        self.card = CreditCard(limit=1000)

    def test_charge(self):
        self.card.charge(400)
        self.assertEqual(self.card.balance, 400)

    def test_charge_over_limit(self):
        with self.assertRaises(ValueError):
            self.card.charge(1500)

    def test_pay(self):
        self.card.charge(300)
        self.card.pay(100)
        self.assertEqual(self.card.balance, 200)


if __name__ == "__main__":
    unittest.main()
