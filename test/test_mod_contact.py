# -*- coding: utf-8 -*-

from model.contact import Contact
from random import randrange

def test_modify_some_contact(app):
        if app.contact.count() == 0:
                app.contact.create(Contact(FirstName="test"))
        old_contacts = app.contact.get_contact_list()
        index = randrange(len(old_contacts))
        contact = Contact(FirstName="OtherOne", MiddleName="JK", LastName="FSbnfs", SecondaryPhone='2463467',
                          Year="1999")
        contact.id = old_contacts[index].id
        contact.HomePhone = old_contacts[index].HomePhone
        contact.WorkPhone = old_contacts[index].WorkPhone
        contact.MobilePhone = old_contacts[index].MobilePhone
        app.contact.modify_contact_by_index(index, contact)
        assert len(old_contacts) == app.contact.count()
        new_contacts = app.contact.get_contact_list()
        old_contacts[index] = contact
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


