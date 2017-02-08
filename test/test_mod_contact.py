# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_first_contact(app):
        app.contact.modify_first_contact(Contact(FirstName="OtherOne", MiddleName="JK", LastName="2Person", Year="1999"))
