import  re
from sys import maxsize

class Contact:

    def __init__(self, FirstName=None, MiddleName=None, LastName=None, HomePhone=None, MobilePhone=None,
                 WorkPhone=None, SecondaryPhone=None, Year=None, id = None, Address=None, email_from_home_page=None,
                 email1=None, email2=None, email3=None,
                 all_phones_from_home_page=None):
        self.FirstName = FirstName
        self.MiddleName = MiddleName
        self.LastName = LastName
        self.HomePhone = HomePhone
        self.MobilePhone = MobilePhone
        self.WorkPhone = WorkPhone
        self.SecondaryPhone = SecondaryPhone
        self.Year = Year
        self.id = id
        self.Address = Address
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.email_from_home_page = email_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page



    def __repr__(self):
        return "%s:%s %s" % (self.id, self.LastName, self.FirstName)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               self.LastName == other.LastName and self.FirstName == other.FirstName



    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize



