class ContactHelper:
    def __init__(self, app):
        self.app = app



    def create(self, contact):
        wd = self.app.wd
        self.open_contact_add_page()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.FirstName)
        self.change_field_value("middlename", contact.MiddleName)
        self.change_field_value("lastname", contact.LastName)
        self.change_field_value("byear", contact.Year)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name("firstname").send_keys(text)

    def modify_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_first_contact()
        wd.find_element_by_link_text("Edit").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        self.select_first_contact()
        wd.find_element_by_name("delete").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def open_contact_add_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()