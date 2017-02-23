# -*- coding: utf-8 -*-

from model.contact import Contact

import random

def test_modify_some_contact(app, json_contacts):
        contact = json_contacts
        if app.contact.count() == 0:
                app.contact.create(Contact(FirstName="test"))
        old_contacts = app.contact.get_contact_list()
        index = random.randrange(len(old_contacts))
        contact.id = old_contacts[index].id
        contact.HomePhone = old_contacts[index].HomePhone
        contact.WorkPhone = old_contacts[index].WorkPhone
        contact.MobilePhone = old_contacts[index].MobilePhone
        app.contact.modify_contact_by_index(index, contact)
        assert len(old_contacts) == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts[index] = contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


