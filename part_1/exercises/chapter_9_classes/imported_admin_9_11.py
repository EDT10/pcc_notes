"""
Start with your work from Exercise 9-8 (page 173). Store the classes User, Privileges 
and Admin in one module. Create a separate file, make an Admin instance, and call 
show_priveleges() to show that everything is working correctly.
"""

import admin_users as ad

admin = ad.Admin("Vye", "Sym", 27, "DC", "Female")


admin.describe_user()
admin.privileges.list_of_privileges = ["Can delete users",
                                       "Can moderate chats"]
admin.privileges.show_privileges()