calculation_to_unit = 24 * 60
name_of_unit = 'minutes'

def days_to_unit(num_of_daís):
    return f'{num_of_daís} days are {num_of_daís * calculation_to_unit} {name_of_unit}'


def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print('You entered a 0, please enter a valid positive number')
        else:
            print('You entered a negative number. Don\'t do this')
    except ValueError:
        print('Your input is not a valid.')

user_input = ''
while user_input != 'e':
    user_input = input(' "nap" mennyi perc vagy (e) for exit: ')
    validate_and_execute()

#days_to_unit = user_input * 24 * 60
