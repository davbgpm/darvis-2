# This file is part of MyPHP.

# MyPHP is free software: you can redistribute it and/or modify it under 
# the terms of the GNU General Public License as published by the Free 
# Software Foundation, either version 3 of the License, or (at your 
# option) any later version.

# MyPHP is distributed in the hope that it will be useful, but WITHOUT 
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License 
# for more details.

# You should have received a copy of the GNU General Public License along
# with MyPHP. If not, see <https://www.gnu.org/licenses/>. 

from flask_principal import Permission, RoleNeed

add_flights = Permission(RoleNeed('fids:add_flights'))
edit_flights = Permission(RoleNeed('fids:edit_flights'))
delete_flights = Permission(RoleNeed('fids:delete_flights'))
list_flights = Permission(RoleNeed('fids:list_flights'))