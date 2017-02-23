
from model.contact import Contact

import random
import string
import json
import os.path
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:],"n:f",["number of contacts", "file"])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)
n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix ,maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "* 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(FirstName="", MiddleName="", LastName="")] + [
    Contact(FirstName=random_string("FirstName", 10), MiddleName=random_string("MiddleName", 20),
            LastName=random_string("LastName", 20))
    for i in range(5)

    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))