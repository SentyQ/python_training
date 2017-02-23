# -*- coding: utf-8 -*-

from model.group import Group
import random



def test_modify_first_group_name(app, db,check_ui, json_groups):
        group = json_groups
        if len(db.get_group_list()) == 0:
                app.group.create(group)
        old_groups = db.get_group_list()
        mod_group = random.choice(old_groups)
        app.group.modify_group_by_id(mod_group.id, group)
        new_groups = db.get_group_list()
        assert len(old_groups) == len(new_groups)
        for i in old_groups:
                if i.id == mod_group.id:
                        i.name = group.name
        assert old_groups == new_groups
        if check_ui:
                assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(),
                                                                         key=Group.id_or_max)




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