# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact("Cola", "ACDC", "Coca", "edit", "eeee", "ffff", "gggg", "1111111", "2222222", "3333333",
                             "4444444", "email9@abc.com", "email8@abc.com", "email7@abc.com", "astalav.abc.com", "5",
                             "March", "2002", "6", "august", "2003", "sec address", "home", "notes"))
    app.session.logout()

