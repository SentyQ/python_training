# -*- coding: utf-8 -*-

from model.group import Group


def test_modify_first_group(app):
        app.session.login(username="admin", password="secret")
        app.group.modify_first_group(Group(name="New222", header="sghjddgsnhssa", footer="ыпыварфыв"))
        app.session.logout()
