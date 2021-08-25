import re


def task_6_1(coin, code):
    split_paramps = coin.split(), code.split()
    new_dict = dict(zip(split_paramps[0], split_paramps[1]))
    return new_dict


def task_7_2(u_input: float, temperature_type: str):
    if temperature_type == 'C':
        celsius = u_input
        kelvin = u_input + 273.15
        fahrenheit = u_input * 1.8 + 32
        return celsius, kelvin, fahrenheit
    elif temperature_type == 'F':
        celsius = (u_input - 32) / 1.8
        kelvin = (u_input + 459.67) * 5 / 9
        fahrenheit = u_input
        return celsius, kelvin, fahrenheit
    elif temperature_type == 'K':
        celsius = u_input - 273.15
        kelvin = u_input
        fahrenheit = u_input * 1.8 - 459.67
        return celsius, kelvin, fahrenheit
    else:
        return False


def task_11_2(us_input):
    us_input = str(us_input)
    palindrome = us_input[::-1]
    if palindrome == us_input:
        return True
    else:
        return False


def task_15_2(u_input):
    match = re.sub(r'.*(\d{3}).*(\d{3}).*(\d{2}).*(\d{2}).*',
                   r'(+38) \1 \2-\3-\4', u_input)
    if len(match) > 9:
        return match
    else:
        return 'Failed to recognize number'
