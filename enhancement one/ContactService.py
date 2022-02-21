from Contact import Contact


class ContactService(list):
    # creates a list to hold contacts
    contactlist = []

    # Constructor that creates a list with a contact
    def __init__(self, contact):
        self.Contact = contact
        self._list = list(self.Contact)

    # Retrieves contact from list using id
    def get_contact(self, contact_id):
        for x in self:
            if Contact.get_contact_id(contact_id) is contact_id:
                print(x)

    # Adds contact into the list
    def add_contact(self, contact):
        if Contact.get_contact_id(contact) is not None:
            return False
        else:
            self.append(contact)

    # removes a contact from the list using an id
    def remove_contact(self, contact):
        # If the id isn't null then removes contact from list
        if Contact.get_contact_id(contact) is not None:
            x = self.index(contact)
            self.pop(x)

    # Updates the first name of a contact in the list using its id
    def update_first_name(self, contact_id, first_name):
        if Contact.get_contact_id(contact_id) is not None:
            self.Contact.get_contact_id(contact_id).Contact.update_first_name(first_name)

    # Updates the last name of a contact in the list using its id
    def update_last_name(self, contact_id, last_name):
        if self.Contact.get_contact_id(contact_id) is not None:
            self.Contact.get_contact_id(contact_id).Contact.update_last_name(last_name)

    # Updates the phone number of a contact in the list using its id
    def update_phone_number(self, contact_id, phone):
        if self.Contact.get_contact_id(contact_id) is not None:
            self.Contact.get_contact_id(contact_id).Contact.update_phone(phone)

    # Updates the address of a contact in the list using its id
    def update_address(self, contact_id, address):
        if self.Contact.get_contact_id(contact_id) is not None:
            self.Contact.get_contact_id(contact_id).Contact.update_address(address)