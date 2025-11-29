# import unittest
# from func import cars

# class TestCarsFunction(unittest.TestCase):

#     def test_single_brand(self):
#         brands = ("Ford",)
#         expected = ["Ford is a good car"]
#         result = list(map(cars, brands))
#         self.assertEqual(result, expected)

#     def test_no_brand(self):
#         brands = ()
#         expected = []
#         result = list(map(cars, brands))
#         self.assertEqual(result, expected)

#     def test_all_brands(self):
#         brands = ("Ford", "Chevrolet", "Dodge")
#         expected = [
#             "Ford is a good car",
#             "Chevrolet is a good car",
#             "Dodge is a good car"
#         ]
#         result = list(map(cars, brands))
#         self.assertEqual(result, expected)

#     def test_two_brand_combinations(self):
#         brand_sets = [
#             ("Ford", "Chevrolet"),
#             ("Ford", "Dodge"),
#             ("Chevrolet", "Dodge")
#         ]

#         expected_sets = [
#             ["Ford is a good car", "Chevrolet is a good car"],
#             ["Ford is a good car", "Dodge is a good car"],
#             ["Chevrolet is a good car", "Dodge is a good car"]
#         ]

#         for i in range(len(brand_sets)):
#             with self.subTest(brands=brand_sets[i]):
#                 result = list(map(cars, brand_sets[i]))
#                 self.assertEqual(result, expected_sets[i])

# if __name__ == "__main__":
#     unittest.main()


# import unittest
# from func import square

# class TestAddFunction(unittest.TestCase):

#     def test_sq_positive_numbers(self):
#         self.assertEqual(square(10), 100)
#         self.assertEqual(square(0), 0)
#         self.assertEqual(square(9), 81)
    
#     def test_sq_negative_numbers(self):
#         self.assertEqual(square(-10), 100)
#         self.assertEqual(square(-5), 25)

#     def test_sq_floats(self):
#         self.assertAlmostEqual(square(2.5), 6.25)
#         self.assertAlmostEqual(square(-3.5), 12.25) 
      

# if __name__ == "__main__":
#     unittest.main()


import unittest
from func import is_board_full, check_winner

class TestTicTacToeFunctions(unittest.TestCase):

     def test_is_boardFull(self):
        self.assertTrue(is_board_full(['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']))
        self.assertFalse(is_board_full(['X', 'O', 'X', 4, 'X', 'O', 'X', 'O', 'X']))

     def test_check_winner(self):
         self.assertTrue(check_winner(['X', 'X', 'X', 'O', 'O', 6, 7, 8, 9]))
         self.assertFalse(check_winner(['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'])) 

     def test_no_winner_yet(self):
        self.assertFalse(check_winner(['X', 'O', 'X', 4, 'O', 6, 7, 8, 9]))

     def test_row_winner(self):
        self.assertTrue(check_winner([1, 2, 3, 'O', 'O', 6, 'X', 'X', 'X']))

     def test_column_winner(self):
        self.assertTrue(check_winner(['O', 2, 'X', 'O', 5, 'X', 'O', 8, 9])) 

     def test_diagonal_winner(self):
        self.assertTrue(check_winner(['X', 2, 3, 4, 'X', 6, 7, 8, 'X']))

if __name__ == "__main__":
    unittest.main()