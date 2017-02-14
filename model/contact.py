from sys import maxsize

class Contact:

    def __init__(self, FirstName=None, MiddleName=None, LastName=None,  name=None, Year=None, id = None):
        self.FirstName = FirstName
        self. MiddleName = MiddleName
        self.LastName = LastName
        self.Year = Year
        if name == None:
            self.name = self.get_name()
        else:
            self.name = name
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
    def get_name(self):
        return  str(self.LastName) + " "+ str(self.FirstName)
