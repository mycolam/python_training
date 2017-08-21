# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact("aaaa", "bbbb", "cccc", "dddd", "eeee", "ffff", "gggg", "1111111", "2222222", "3333333",
                      "4444444", "email1@abc.com", "email2@abc.com", "email3@abc.com", "abrvalh.abc.com", "1",
                      "January", "1999", "2", "February", "2000", "sec address", "home", "notes")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

