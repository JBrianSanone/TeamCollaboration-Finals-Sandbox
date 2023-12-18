from lxml import etree

class DataHRS:
  global tree
  tree = etree.parse("xml/output.xml")

  def add_user(self):
    root = tree.getroot()

    if len(root) > 0:
      last_patient = root[-1]
      last_patient_id = int(last_patient.get('id'))
      new_patient_id = last_patient_id + 1
    else:
      new_patient_id = 1

    child = etree.SubElement(root, "Patient", id=str(new_patient_id))
    print()
    name = etree.SubElement(child, "firstname")
    name.text = input('Enter First Name: ')
    lName = etree.SubElement(child, "lastname")
    lName.text = input('Enter Last Name: ')
    age = etree.SubElement(child, "Age")
    age.text = input('Enter Age: ')
    gender = etree.SubElement(child, "Gender")
    gender.text = input('Enter Gender: ')
    print()
    input("Press Enter to continue...")

    tree.write('xml/output.xml', encoding="utf-8", pretty_print=True, xml_declaration=True)

  def search_user(self):
    while True:
      id_no = input('Enter ID Number of Patient (Enter stop to exit): ')
      id_no = "ID " + id_no
      if id_no.lower() == 'stop':
        break

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

  def update_patient_first(self):
    while True:
      patient_id = str(input("Enter the patient ID (Enter stop to exit): "))

      if patient_id.lower() == 'stop':
        break

      elements = tree.xpath(f'/root/Patient[@id="{patient_id}"]')

      if elements:
        element = elements[0]
        subelement = element.find('firstname')

        new_firstname = str(input("Enter the new first name: "))
        subelement.text = new_firstname

        tree.write('xml/output.xml', encoding="utf-8", pretty_print=True, xml_declaration=True)
        print("First name updated successfully.")
      else:
        print("No matching patient found.")

  def update_patient_last(self):
    while True:
      patient_id = str(input("Enter the patient ID (Enter stop to exit): ")

      if patient_id.lower() == 'stop':
        break

      elements = tree.xpath(f'/root/Patient[@id="{patient_id}"]')

      if elements:
        element = elements[0]
        subelement = element.find('lastname')

        new_lastname = str(input("Enter the new last name: "))
        subelement.text = new_lastname

        tree.write('xml/output.xml', encoding="utf-8", pretty_print=True, xml_declaration=True)
        print("Last name updated successfully.")
      else:
        print("No matching patient found.")
