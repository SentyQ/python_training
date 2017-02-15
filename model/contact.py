from sys import maxsize

class Contact:

    def __init__(self, FirstName=None, MiddleName=None, LastName=None, HomePhone=None, MobilePhone=None,
                 WorkPhone=None, SecondaryPhone=None, Year=None, id = None):
        self.FirstName = FirstName
        self.MiddleName = MiddleName
        self.LastName = LastName
        self.HomePhone = HomePhone
        self.MobilePhone = MobilePhone
        self.WorkPhone = WorkPhone
        self.SecondaryPhone = SecondaryPhone
        self.Year = Year
        self.id = id

    def __repr__(self):
        return "%s:%s %s:%s:%s:%s:%s" % (self.id, self.LastName, self.FirstName,self.HomePhone,self.MobilePhone,
                                         self.WorkPhone,self.SecondaryPhone)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               self.LastName == other.LastName and self.FirstName == other.FirstName #and \
               #self.MobilePhone == other.MobilePhone and self.HomePhone == other.HomePhone \
               #and self.WorkPhone == other.WorkPhone and self.SecondaryPhone == other.SecondaryPhone


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

