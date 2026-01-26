from admin_privilege import Admin as ad

group_admin = ad("Aris", "Mang", 29, "Maryland", "Male")

group_admin.describe_user()
group_admin.privileges.list_of_privileges = ["Can mute users"]

group_admin.privileges.show_privileges()