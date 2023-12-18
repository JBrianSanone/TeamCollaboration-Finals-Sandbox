import unittest
import os
import io
from lxml import etree
from unittest.mock import patch
from DataHRS import DataHRS

class TestDataHRS(unittest.TestCase):

    def setUp(self):
        # Create an instance of DataHRS for testing
        self.data_hrs = DataHRS()

        with open("xml/output.xml", "w") as f:
            f.write("""<?xml version='1.0' encoding='UTF-8'?>
                        <root>
                          <Patient id="1">
                            <firstname>Brian</firstname>
                            <lastname>James</lastname>
                            <Age>12</Age>
                            <Gender>Male</Gender>
                          </Patient>
                        </root>""")

    def tearDown(self):
        # Clean up any changes made during testing
        if os.path.exists("xml/output.xml"):
            os.remove("xml/output.xml")

    def test_add_user(self):
        input_data = ['John', 'Doe', '25', 'Male']
        with unittest.mock.patch('builtins.input', side_effect=input_data):
            self.data_hrs.add_user()

        # Verify that the XML file has been updated
        tree = etree.parse("xml/output.xml")
        root = tree.getroot()
        self.assertEqual(len(root), 2)  # Assuming there were already 1 patient in the XML
        new_patient = root[-1]
        self.assertEqual(new_patient.get('id'), '2')
        self.assertEqual(new_patient.find('firstname').text, 'John')
        self.assertEqual(new_patient.find('lastname').text, 'Doe')
        self.assertEqual(new_patient.find('Age').text, '25')
        self.assertEqual(new_patient.find('Gender').text, 'Male')

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

        # Verify that the XML file has been updated
        tree = etree.parse("xml/output.xml")
        root = tree.getroot()
        updated_patient = root.find(".//Patient[@id='1']")
        self.assertEqual(updated_patient.find('firstname').text, 'John')

    def test_update_patient_last(self):
        # Test updating the last name of a patient
        # Simulate user input for testing
        with patch('builtins.input', side_effect=['1', 'Doe', 'stop']):
            self.data_hrs.update_patient_last()

        # Verify that the XML file has been updated
        tree = etree.parse("xml/output.xml")
        root = tree.getroot()
        updated_patient = root.find(".//Patient[@id='1']")
        self.assertEqual(updated_patient.find('lastname').text, 'Doe')

    if __name__ == '__main__':
        unittest.main()
