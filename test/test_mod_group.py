# -*- coding: utf-8 -*-

from model.group import Group

import random



def test_modify_first_group_name(app, json_groups):
        group = json_groups
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