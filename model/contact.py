from sys import maxsize

class Contact:

    def __init__(self, FirstName=None, MiddleName=None, LastName=None,  Year=None, id = None):
        self.FirstName = FirstName
        self. MiddleName = MiddleName
        self.LastName = LastName
        self.Year = Year
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.LastName)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.LastName == other.LastName and self.FirstName == other.FirstName

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

