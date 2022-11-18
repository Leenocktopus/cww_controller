import os
import shutil
from unittest import TestCase

from src.main import get_absolute_path
from src.repository.repository import Repository


class UnitTestRepository(TestCase):
    employees = get_absolute_path('../test/resources/employees.csv')
    ratings = get_absolute_path("../test/resources/ratings.csv")

    employees_copy = get_absolute_path('../test/resources/employees_copy.csv')
    ratings_copy = get_absolute_path("../test/resources/ratings_copy.csv")

    def setUp(self):
        print("setting up")
        shutil.copyfile(self.employees, self.employees_copy)
        shutil.copyfile(self.ratings, self.ratings_copy)
        self.repository = Repository(self.employees_copy, self.ratings_copy)

    def tearDown(self):
        print("tearing down")
        os.remove(self.employees_copy)
        os.remove(self.ratings_copy)

    def test_employees(self):
        expected_result = [['Camila Jones'], ['Vivian Banks'], ['Rory Simon']]
        self.assertEqual(expected_result, self.repository.find_all_names())

    def test_ratings(self):
        expected_result = [['Alaina Harvey', '7.53099034145014', 'give a bonus'],
                           ['Warren Bowen', '7.754997992271279', 'promote'],
                           ['Alaina Harvey', '4.1225488957725345', 'keep'],
                           ['Maria Moon', '4.792035680570405', 'demote'],
                           ['Maria Moon', '1.715895029072324', 'lay off']]
        self.assertEqual(expected_result, self.repository.find_all_ratings())
        self.repository.save_rating('John Doe', '9.998', 'promote with a bonus')
        expected_result.append(['John Doe', '9.998', 'promote with a bonus'])
        self.assertEqual(expected_result, self.repository.find_all_ratings())
