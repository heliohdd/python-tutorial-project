from helper import validate_and_execute, user_input_message
import os
import logging


logging = logging.getLogger("MAIN")
logging.error("This is an error message")
logging.info("This is an info message")

print(f"The operating system name is: {os.name}")
print(f"The operating system version is: {logging.}")


"""user_input = ''
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    print(f"You entered: {days_and_unit}")

    days_and_unit_dictionary = {"days": int(days_and_unit[0]), "unit": days_and_unit[1]}
    print(f"You entered: {days_and_unit_dictionary}")
    print(f"The type of this input is {type(days_and_unit_dictionary)}")

    validate_and_execute(days_and_unit_dictionary)"""