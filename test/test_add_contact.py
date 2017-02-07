# -*- coding: utf-8 -*-
import unittest

import pytest

from model.contact import Contact

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(FirstName="NewOne", MiddleName="J", LastName="Person", Year="1899"))
    app.session.logout()




