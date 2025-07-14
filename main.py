calculation_to_units = 24
name_of_unit = "hours"


def days_to_unit(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

user_input = input("Please enter hours: ")
user_input_number = int(user_input)
calculated_value = days_to_unit(user_input_number)

print(calculated_value)