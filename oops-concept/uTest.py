import unittest
from oops import John,Mike,Sarah

# class TestClassPerson(unittest.TestCase):
#     def test_person_verifyAge(self):
#         datas = Person("Alice", 30)
#         self.assertEqual(datas.age, 30)
        
#     def test_person_verifyName(self):
#         datas = Person("Bob", 25)
#         self.assertEqual(datas.name, "Bob")

class TestClassInheritance(unittest.TestCase):
    def test_john_who_am_i(self):
        john = John("John Wick")
        self.assertEqual(john.tester(), "John Wick is a tester")


if __name__ == "__main__":
    unittest.main()