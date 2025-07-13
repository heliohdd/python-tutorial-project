calculation_to_hours = 24
name_of_unit = "hours"


def days_to_unit(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}")
    print(custom_message)


days_to_unit(20, "Awesome!!!")
days_to_unit(35, "Looks good!!!")