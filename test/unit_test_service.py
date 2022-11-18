from unittest import TestCase
from unittest.mock import Mock, MagicMock

from src.service.service import Service


class UnitTestService(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.repository = Mock()
        cls.repository.find_all_names = MagicMock(
            return_value=[['Camila Jones'], ['Vivian Banks'], ['Rory Simon']])
        cls.repository.find_all_ratings = MagicMock(
            return_value=[['Alaina Harvey', '7.53099034145014', 'give a bonus'],
                          ['Warren Bowen', '7.754997992271279', 'promote'],
                          ['Alaina Harvey', '4.1225488957725345', 'keep'],
                          ['Maria Moon', '4.792035680570405', 'demote'],
                          ['Maria Moon', '1.715895029072324', 'lay off']])

        cls.service = Service(cls.repository)

    def test_find_all_names(self):
        expected_result = ['Camila Jones', 'Vivian Banks', 'Rory Simon']
        self.assertEqual(expected_result, self.service.find_all_names())
        self.repository.find_all_names.assert_called_with()

    def test_save_rating(self):
        self.service.save_rating('Camila Jones', ["very productive", "outgoing", "about average"])
        self.repository.save_rating.assert_called_with('Camila Jones', 7.999396446135152, 'promote')

    def test_find_all_ratings(self):
        expected_result = [['Warren Bowen', '7.754997992271279', 'promote'],
                           ['Alaina Harvey', '7.53099034145014', 'give a bonus'],
                           ['Maria Moon', '4.792035680570405', 'demote'],
                           ['Alaina Harvey', '4.1225488957725345', 'keep'],
                           ['Maria Moon', '1.715895029072324', 'lay off']]
        self.assertEqual(expected_result, self.service.find_all_ratings())
        self.repository.find_all_ratings.assert_called_with()
