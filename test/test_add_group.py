# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
        app.group.create(Group(name="New", header="sgsdaga", footer="sdfgfgh"))
