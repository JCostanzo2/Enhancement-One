import unittest
from Contact import Contact

# working inputs for contact class
good_id = "01"
good_first_name = "John"
good_last_name = "Smith"
good_phone_number = "0123456789"
good_address = "01 Washington Court"

# a string that is null
string_null = ""

# inputs that are too long
bad_id = "01234567890"
bad_first_name = "John Jacob Jingleheimer"
bad_last_name = " a pretty long last name"
bad_phone_number = "55196541684166849191984651984"
bad_address = "An extremely long address that in no way should be considered to work drive"


class ContactTestCase(unittest.TestCase):
    # Set's  up the different contacts used to test.
    def setUp(self):
        self.good_contact = Contact(good_id, good_first_name, good_last_name, good_phone_number, good_address)

    # Tests if the good contact has working variables
    def test_good_contact(self):
        self.assertEqual(self.good_contact.get_contact_id(), good_id, 'wrong id')
        self.assertEqual(self.good_contact.get_first_name(), good_first_name, 'wrong first name')
        self.assertEqual(self.good_contact.get_last_name(), good_last_name, 'wrong last name')
        self.assertEqual(self.good_contact.get_address(), good_address, 'wrong address')
        self.assertEqual(self.good_contact.get_phone(), good_phone_number, 'wrong phone number')

    # Tests update methods raise errors with bad ids
    def test_update_bad_contact(self):
        with self.assertRaises(ValueError):
            self.good_contact.update_contact_id(bad_id)
            self.good_contact.update_phone(bad_phone_number)
            self.good_contact.update_address(bad_address)
            self.good_contact.update_first_name(bad_first_name)
            self.good_contact.update_last_name(bad_first_name)

    # Tests if constructor raises errors with bad ids
    def test_constructor_bad_contact(self):
        with self.assertRaises(ValueError):
            self.bad_contact = Contact(bad_id, good_first_name, good_last_name, good_phone_number, good_address)
            self.bad_contact = Contact(good_id, bad_first_name, good_last_name, good_phone_number, good_address)
            self.bad_contact = Contact(good_id, good_first_name, bad_last_name, good_phone_number, good_address)
            self.bad_contact = Contact(good_id, good_first_name, good_last_name, bad_phone_number, good_address)
            self.bad_contact = Contact(good_id, good_first_name, good_last_name, good_phone_number, bad_address)


if __name__ == '__main__':
    unittest.main()
