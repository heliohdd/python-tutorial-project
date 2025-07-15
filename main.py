def days_to_unit(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} minutes are {num_of_days * 24 * 60} minutes"
    elif conversion_unit == "seconds":
        return f"{num_of_days} seconds are {num_of_days * 24 * 60 * 60} seconds"
    else:
        return "unsupported unit"


def validate_and_execute(dictionary):
    try:
        user_input_number = int(dictionary["days"])

        # We want to do conversion only for positive integers
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number, dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
        else:
            print("You entered a negative number, please enter a valid positive number")
    except ValueError:
        print('Your input is not a valid number. Don\'t ruim my program.')

"""user_input = ''
while user_input != "exit":
    user_input = input("Hey user, enter number of days and conversion unit! \n")
    days_and_unit = user_input.split(":")
    print(f"You entered: {days_and_unit}")

    days_and_unit_dictionary = {"days": int(days_and_unit[0]), "unit": days_and_unit[1]}
    print(f"You entered: {days_and_unit_dictionary}")
    print(f"The type of this input is {type(days_and_unit_dictionary)}")

    validate_and_execute(days_and_unit_dictionary)"""


message = "enter some value"
days = 20
price = 9.99
valid_number = True
exit_input = False
list_of_days = [20, 40, 20, 100]
list_of_months = ["January", "February", "March"]
set_of_days = {20, 45, 100}
days_and_unit = {"days": 10, "unit": "hours"}

print(f"Size of message variable: {sys.getsizeof(message)}")
print(f"Size of days variable: {sys.getsizeof(days)}")
print(f"Size of price variable: {sys.getsizeof(price)}")
print(f"Size of valid number variable: {sys.getsizeof(valid_number)}")