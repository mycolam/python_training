# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


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
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
