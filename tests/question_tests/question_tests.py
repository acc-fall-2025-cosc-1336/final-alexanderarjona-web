#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())
    
    def test_question_b_config(self):
        self.assertEqual(True, test_config_b())

    def test_question_c_config(self):
        self.assertEqual(True, test_config_c())

    def test_question_d_config(self):
        self.assertEqual(True, test_config_d())

    def test_get_most_likely_ancestor_consensus(self):
        # Test required by the instructions for Question D
        # Parameters: "GATATATGCATATACTT", "ATAT" -> Returns: (2, 4, 10)
        expected_output = (2, 4, 10)
        self.assertEqual(expected_output, get_most_likely_ancestor_consensus("GATATATGCATATACTT", "ATAT"))


