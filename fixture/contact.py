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
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.open_home_page()

    def open_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook/") :
            wd.find_element_by_link_text("home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def open_contact_add_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit"))> 0) :
            wd.find_element_by_link_text("add new").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))