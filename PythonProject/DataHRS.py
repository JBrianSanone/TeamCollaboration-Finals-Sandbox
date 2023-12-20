from lxml import etree


class DataHRS:

    global tree
    tree = etree.parse("xml/output.xml") # bandit: ignore this line

    def add_user(self):
        root = tree.getroot()  # Access the root

        if len(root) > 0:
            last_patient = root[-1]
            last_patient_id = int(last_patient.get('id'))
            new_patient_id = last_patient_id + 2
        else:
            new_patient_id = 1

        child = etree.SubElement(root, "Patient", id=str(new_patient_id))
        print()

        # Validation for first name (non-empty string)
        while True:
            first_name_input = input('Enter First Name: ')
            if first_name_input.strip():
                name = etree.SubElement(child, "firstname")
                name.text = first_name_input
                break
            else:
                print("Invalid first name. Please enter a non-empty string.")

        # Validation for last name (non-empty string)
        while True:
            last_name_input = input('Enter Last Name: ')
            if last_name_input.strip():
                lName = etree.SubElement(child, "lastname")
                lName.text = last_name_input
                break
            else:
                print("Invalid last name. Please enter a non-empty string.")

        # Validation for age (positive integer)
        while True:
            age_input = input('Enter Age: ')
            if age_input.isdigit() and int(age_input) > 0:
                age = etree.SubElement(child, "Age")
                age.text = age_input
                break
            else:
                print("Invalid age. Please enter a positive integer for age.")

        # Validation for gender ('male' or 'female')
        while True:
            gender_input = input('Enter Gender: ')
            if gender_input.lower() in ['male', 'female']:
                gender = etree.SubElement(child, "Gender")
                gender.text = gender_input.lower()
                break
            else:
                print("Invalid gender. Please enter 'male' or 'female'.")

        print()
        input("Press Enter to continue...")


        tree.write('xml/output.xml', encoding="utf-8", pretty_print=True, xml_declaration=True)


    def search_user(self):  # Search function
        while True:
            id_no = input('Enter ID Number of Patient (Enter stop to exit): ')


            if id_no.lower() == 'stop': break  # exits the loop if you enter stop

            # Search for the patient with the specified ID
            patient_elements = tree.findall(".//Patient[@id='" + id_no + "']")

            if patient_elements:
                for patient in patient_elements:
                    print()
                    print("Patient ID:", id_no)
                    for subelement in patient:
                        print(subelement.tag, ":", subelement.text)
                    print()
            else:
                print(f"Patient with ID '{id_no}' not found.")

    def update_patient_first(self):  # Update patient last name function
        while True:
            patient_id = str(input("Enter the patient ID (Enter stop to exit): "))

            if patient_id.lower() == 'stop': break  # exits the loop if you enter stop

            elements = tree.xpath(f'/root/Patient[@id="{patient_id}"]')  # Elements with the specified patient ID

            if elements:  # Check if the list is not empty
                element = elements[0]  # Select the first matching element
                subelement = element.find('firstname')  # Subelement, can be another subelement of <Patient>

                new_firstname = str(input("Enter the new first name: "))
                subelement.text = new_firstname  # Change value

                tree.write('xml/output.xml', encoding="utf-8", pretty_print=True, xml_declaration=True)
                print("First name updated successfully.")
            else:
                print("No matching patient found.")

    def update_patient_last(self):  # Update patient first name function
        while True:
            patient_id = str(input("Enter the patient ID (Enter stop to exit): "))

            if patient_id.lower() == 'stop': break  # exits the loop if you enter stop

            elements = tree.xpath(f'/root/Patient[@id="{patient_id}"]')  # Elements with the specified patient ID

            if elements:  # Check if the list is not empty
                element = elements[0]  # Select the first matching element
                subelement = element.find('lastname')  # Subelement, can be another subelement of <Patient>

                new_lastname = str(input("Enter the new last name: "))
                subelement.text = new_lastname  # Change value

                tree.write('xml/output.xml', encoding="utf-8", pretty_print=True, xml_declaration=True)
                print("First name updated successfully.")
            else:
                print("No matching patient found.")
