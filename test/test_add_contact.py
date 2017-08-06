# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact("aaaa", "bbbb", "cccc", "dddd", "eeee", "ffff", "gggg", "1111111", "2222222", "3333333",
                               "4444444", "email1@abc.com", "email2@abc.com", "email3@abc.com", "abrvalh.abc.com", "1",
                               "January", "1999", "2", "February", "2000", "sec address", "home", "notes"))
    app.session.logout()

