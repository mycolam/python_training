# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="First group", header="My first group", footer="Footer for my first group"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

