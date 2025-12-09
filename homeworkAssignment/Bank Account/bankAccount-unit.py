import unittest
from bankAccount import BankAccount

class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount("Bob", 1000)
        new_balance = account.deposit(500)
        self.assertEqual(new_balance, 1500)

    def test_withdraw(self):
        account = BankAccount("Bob", 1000)
        new_balance = account.withdraw(300)
        self.assertEqual(new_balance, 700)

    def test_withdraw_insufficient_funds(self):
        account = BankAccount("Bob", 1000)
        result = account.withdraw(1500)
        self.assertEqual(result, "Insufficient funds")


    
if __name__ == "__main__":
    unittest.main()



