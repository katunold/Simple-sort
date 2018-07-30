from unittest import TestCase
from simple_sort import simple_sort


class Tests(TestCase):
    def test_simple_sort(self):
        self.assertEqual(simple_sort("Tom", 19, 80), [("Tom", 19, 80)])
        self.assertEqual(simple_sort("John", 20, 90), [("John", 20, 90), ("Tom", 19, 80)])
        self.assertEqual(simple_sort("Jony", 17, 91), [("John", 20, 90), ("Jony", 17, 91), ("Tom", 19, 80)])
        self.assertEqual(simple_sort("Jony", 17, 93), [("John", 20, 90), ("Jony", 17, 91), ("Jony", 17, 93), ("Tom", 19, 80)])
        self.assertEqual(simple_sort("Json", 21, 85),
                         [("John", 20, 90), ("Jony", 17, 91), ("Jony", 17, 93), ("Json", 21, 85), ("Tom", 19, 80)])
