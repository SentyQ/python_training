class ContactHelper:
    def __init__(self, app):
        self.app = app



    def create(self, contact):
        wd = self.wd
        self.open_contact_add_page()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.FirstName)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.MiddleName)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.LastName)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.Year)
        wd.find_element_by_name("submit").click()


    def modify_first_contact(self, contact):
        wd = self.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_link_text("Edit").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.FirstName)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.MiddleName)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.LastName)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.Year)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()



    def open_contact_add_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()