# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string

def random_string(prefix,maxlen):
        symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
        return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


testdata = [Contact(FirstName="", MiddleName="", LastName="")] + [
        Contact(FirstName=random_string("name",10), MiddleName=random_string("header",20),
                LastName=random_string("footer",20))
        for i in range (5)

]


@pytest.mark.parametrize("contact",testdata, ids=[repr(x) for x in testdata])
def test_modify_some_contact(app, contact):
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


