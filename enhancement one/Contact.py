class Contact:
    #  Initialize the variables needed to hold the data
    contact_id = None
    first_name = None
    last_name = None
    phone = None
    address = None
    #  Set maximum length of first name, id, and last name
    max_length = 10
    #  Set maximum length of address
    address_length = 30
    #  Set maximum number of digits for phone
    phone_length = 10

    # Constructor that checks if inputs match the requirements
    def __init__(self, contact_id, f_name, l_name, phone_num, new_address):
        #  Check if id is null or larger than 10
        if contact_id is not None and len(contact_id) <= Contact.max_length:
            self.update_contact_id(contact_id)
        else:
            raise ValueError("Contact ID can not be null or larger than 10 characters.")
        #  Check if first name is null or larger than 10 characters
        if f_name is not None and len(f_name) <= Contact.max_length:
            self.first_name = f_name
        else:
            raise ValueError("First Name can not be null or larger than 10 characters.")
        #  Check if first name is null or larger than 10 characters
        if l_name is not None and len(l_name) <= Contact.max_length:
            self.last_name = l_name
        else:
            raise ValueError("Last Name can not be null or larger than 10 characters.")
        #  Make sure phone number is 10 digits and not null
        if len(phone_num) is not Contact.phone_length or Contact.is_numeric(self.phone) is True or phone_num is None:
            raise ValueError("Phone Number must be exactly 10 digits.")
        else:
            self.phone = phone_num
        #  Check if address is null or larger than 10 characters
        if new_address is not None and len(new_address) <= Contact.address_length:
            self.address = new_address
        else:
            raise ValueError("The address can not be larger than 30 characters long.")

    #  multiple get methods to return the variables
    def get_contact_id(self):
        return self.contact_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_phone(self):
        return self.phone

    def get_address(self):
        return self.address

    #  Update methods for client to update the contact information
    def update_contact_id(self, contact_id):
        #  Check if id is null or larger than 10
        if contact_id is not None and len(contact_id) <= Contact.max_length:
            self.contact_id = contact_id
        else:
            raise ValueError("Contact ID can not be null or larger than 10 characters.")

    def update_first_name(self, first_name):
        #  Check if first name is null or larger than 10 characters
        if first_name is not None and len(first_name) <= Contact.max_length:
            self.first_name = first_name
        else:
            raise ValueError("First Name can not be null or larger than 10 characters.")

    def update_last_name(self, last_name):
        #  Check if first name is null or larger than 10 characters
        if last_name is not None and len(last_name) <= Contact.max_length:
            self.last_name = last_name
        else:
            raise ValueError("Last Name can not be null or larger than 10 characters.")

    def update_phone(self, phone):
        #  Make sure phone number is 10 digits and not null
        if len(phone) is not Contact.phone_length or phone is None or Contact.is_numeric(phone) is False:
            raise ValueError("Phone Number must be 10 digits.")
        else:
            self.phone = phone

    def update_address(self, address):
        #  Checks if updated address is not null or longer than 30 characters
        if address is not None and len(address) <= Contact.address_length:
            self.address = address
        else:
            raise ValueError("The address can not be larger than 30 characters long.")

    #  Boolean method for making sure a string is all digits
    @staticmethod
    def is_numeric(string):
        return string is not None and string.matches("[-+]?\\d*\\.?\\d+")
