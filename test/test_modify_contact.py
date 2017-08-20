# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact_first_name(app):
    app.contact.modify_first_contact(Contact(firstname="Cola"))


def test_modify_contact_last_name(app):
    app.contact.modify_first_contact(Contact(lastname="Coca"))

