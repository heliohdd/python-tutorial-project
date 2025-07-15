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

user_input_message = "Hey user, enter number of days and conversion unit! \n"