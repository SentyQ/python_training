import  re
from random import randrange

def test_phones_on_home_page(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    #assert first and last names
    assert contact_from_home_page == contact_from_edit_page
    assert contact_from_home_page.Address == addr_norm(contact_from_edit_page.Address)
    assert contact_from_home_page.email_from_home_page == merge_email(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


#def test_phones_on_contact_view_page(app):
#    contact_view_page = app.contact.get_contact_from_view_page(0)
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert contact_view_page.HomePhone == contact_from_edit_page.HomePhone
#    assert contact_view_page.MobilePhone == contact_from_edit_page.MobilePhone
#    assert contact_view_page.WorkPhone == contact_from_edit_page.WorkPhone
#    assert contact_view_page.SecondaryPhone == contact_from_edit_page.SecondaryPhone

def clear(s):
    return re.sub("[() -\/]","",s)

def addr_norm(s):
    return re.sub("\n"," ",s)

def merge_email(contact):
    return '\n'.join(filter(lambda x: x !="",filter(lambda x: x is not None,[contact.email1, contact.email2, contact.email3])))

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda  x: clear (x),
                         filter(lambda x: x is not None,
                         [contact.HomePhone, contact.MobilePhone, contact.WorkPhone, contact.SecondaryPhone]))))