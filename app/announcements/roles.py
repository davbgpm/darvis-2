from flask_principal import Permission, RoleNeed

list_announcements = Permission(RoleNeed('announcements:list'))
add_announcements = Permission(RoleNeed('announcements:add'))
edit_announcements = Permission(RoleNeed('announcements:edit'))
delete_announcements = Permission(RoleNeed('announcements:delete'))