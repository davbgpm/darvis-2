from flask_principal import Permission, RoleNeed

list_achievements = Permission(RoleNeed('achievements:list'))
add_achievements = Permission(RoleNeed('achievements:add'))
edit_achievements = Permission(RoleNeed('achievements:edit'))
delete_achievements = Permission(RoleNeed('achievements:delete'))