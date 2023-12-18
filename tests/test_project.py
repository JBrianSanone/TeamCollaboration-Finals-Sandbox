import unittest
import io
from unittest.mock import patch, mock_open
from DataHRS import DataHRS

class TestDataHRS(unittest.TestCase):

    def setUp(self):
        # Create an instance of DataHRS for testing
        self.data_hrs = DataHRS()

        # Mock the file content for testing
        self.mock_file_content = """<?xml version='1.0' encoding='UTF-8'?>
                                    <root>
                                      <Patient id="1">
                                        <firstname>Brian</firstname>
                                        <lastname>James</lastname>
                                        <Age>12</Age>
                                        <Gender>Male</Gender>
                                      </Patient>
                                    </root>"""

        # Patch the open function to mock file writing
        self.mock_open_patch = patch('builtins.open', mock_open(read_data=self.mock_file_content))
        self.mock_open_patch.start()

    def tearDown(self):
        # Clean up any changes made during testing
        self.mock_open_patch.stop()

    def test_add_user(self):
        input_data = ['John', 'Doe', '25', 'Male']
        with unittest.mock.patch('builtins.input', side_effect=input_data):
            self.data_hrs.add_user()

        # Verify that the mock file content has been updated
        expected_content = f"{self.mock_file_content}\n  <Patient id=\"2\">\n    <firstname>John</firstname>\n    <lastname>Doe</lastname>\n    <Age>25</Age>\n    <Gender>Male</Gender>\n  </Patient>\n</root>"
        with open("xml/output.xml", "r") as f:
            actual_content = f.read()
        self.assertEqual(actual_content, expected_content)

    def test_search_user(self):
        input_data = ['1', 'stop']
        with unittest.mock.patch('builtins.input', side_effect=input_data):
            with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                self.data_hrs.search_user()

        # Verify the output printed to the console
        expected_output = "\nPatient ID: 1\nfirstname : Brian\nlastname : James\nAge : 12\nGender : Male\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update_patient_first(self):
        # Test updating the first name of a patient
        # Simulate user input for testing
        with patch('builtins.input', side_effect=['1', 'John', 'stop']):
            self.data_hrs.update_patient_first()

        # Verify that the mock file content has been updated
        expected_content = """<?xml version='1.0' encoding='UTF-8'?>
                            <root>
                              <Patient id="1">
                                <firstname>John</firstname>
                                <lastname>James</lastname>
                                <Age>12</Age>
                                <Gender>Male</Gender>
                              </Patient>
                            </root>"""
        with open("xml/output.xml", "r") as f:
            actual_content = f.read()
        self.assertEqual(actual_content, expected_content)

    def test_update_patient_last(self):
        # Test updating the last name of a patient
        # Simulate user input for testing
        with patch('builtins.input', side_effect=['1', 'Doe', 'stop']):
            self.data_hrs.update_patient_last()

        # Verify that the mock file content has been updated
        expected_content = """<?xml version='1.0' encoding='UTF-8'?>
                            <root>
                              <Patient id="1">
                                <firstname>Brian</firstname>
                                <lastname>Doe</lastname>
                                <Age>12</Age>
                                <Gender>Male</Gender>
                              </Patient>
                            </root>"""
        with open("xml/output.xml", "r") as f:
            actual_content = f.read()
        self.assertEqual(actual_content, expected_content)

if __name__ == '__main__':
    unittest.main()
