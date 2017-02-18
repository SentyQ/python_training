# -*- coding: utf-8 -*-

from model.group import Group
import pytest
import random
import string

def random_string(prefix,maxlen):
        symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
        return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
        Group(name=random_string("name",10), header=random_string("header",20), footer=random_string("footer",20))
        for i in range (5)

]

@pytest.mark.parametrize("group",testdata, ids=[repr(x) for x in testdata])
def test_modify_first_group_name(app, group):
        if app.group.count() == 0:
                app.group.create(group)
        old_groups = app.group.get_group_list()
        index = random.randrange(len(old_groups))
        group.id = old_groups[index].id
        app.group.modify_group_by_index(index, group)
        assert len(old_groups) == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups[index] = group
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




#def test_modify_first_group_header(app):
 #               app.group.create(Group(name="test"))
 #      old_groups = app.group.get_group_list()
 #      group = Group(header="dbadfbazaaa")
  #      group.id = old_groups[0].id
  #      app.group.modify_first_group(group)
   #     new_groups = app.group.get_group_list()
   #     assert len(old_groups) == len(new_groups)
    #    old_groups[0] = group
    #    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)