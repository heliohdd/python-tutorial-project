my_list = ["January", "February", "March", "April", "May", "January"]
print(my_list[0])

my_list.append("June")
print(my_list)

my_list.remove("February")
print(f"List with remove February: {my_list}")

my_list.remove("January")
print(f"List with remove January: {my_list}")