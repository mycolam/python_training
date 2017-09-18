from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]).strip()


testdata = [
    Contact(firstname=random_string("firstname", 10), middlename="bbbb", lastname=random_string("lastname", 10),
            nickname="dddd", title="eeee", company="ffff", address=random_string("address", 20), homephone="1111111",
            mobilephone="2222222", workphone="3333333", fax="4444444", email1="email1@abc.com", email2="email2@abc.com",
            email3="email3@abc.com", homepage="abrvalh.abc.com", birthday="1", birthmonth="January", birthyear="1999",
            annivday="2", annivmonth="February", annivyear="2000", sec_address="sec address", sec_home="home",
            sec_notes="notes")
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

