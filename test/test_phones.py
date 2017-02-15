def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.HomePhone == contact_from_edit_page.HomePhone
    assert contact_from_home_page.MobilePhone == contact_from_edit_page.MobilePhone
    assert contact_from_home_page.WorkPhone == contact_from_edit_page.WorkPhone
    assert contact_from_home_page.SecondaryPhone == contact_from_edit_page.SecondaryPhone