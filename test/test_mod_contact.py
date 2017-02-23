# -*- coding: utf-8 -*-

from model.contact import Contact

import random

def test_modify_some_contact(app, db, check_ui, json_contacts):
        contact = json_contacts
        if len(db.get_contact_list()) == 0:
                app.contact.create(Contact(FirstName="test"))
        old_contacts = db.get_contact_list()
        mod_contact = random.choice(old_contacts)
        app.contact.modify_contact_by_id(mod_contact.id, contact)
        new_contacts = db.get_contact_list()
        assert len(old_contacts) == len(new_contacts)
        for i in old_contacts:
                if i.id == mod_contact.id:
                        i.FirstName = contact.FirstName
                        i.LastName = contact.LastName
        assert old_contacts == new_contacts
        if check_ui:
                assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


