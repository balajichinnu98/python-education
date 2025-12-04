import unittest
from oops import Person

class TestClassPerson(unittest.TestCase):
    def test_person_verifyAge(self):
        datas = Person("Alice", 30)
        self.assertEqual(datas.age, 30)
        
    def test_person_verifyName(self):
        datas = Person("Bob", 25)
        self.assertEqual(datas.name, "Bob")




if __name__ == "__main__":
    unittest.main()