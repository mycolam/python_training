# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify_first_contact(Contact(firstname="Cola"))


def test_modify_contact_last_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="test"))
    app.contact.modify_first_contact(Contact(lastname="Coca"))

