def return_10():
    return 10

def add(param_1, param_2):
    return param_1 + param_2

def subtract(param_1, param_2):
    return param_1 - param_2

def multiply(param_1, param_2):
    return param_1 * param_2

def divide(param_1, param_2):
    return param_1 / param_2

def length_of_string(param_1):
    return len(param_1)

def join_string(word_1, word_2):
    return word_1 + word_2

def add_string_as_number(num_1, num_2):
    return int(num_1) + int(num_2)

# months = [
#         "January",
#         "February",
#         "March",
#         "April",
#         "May",
#         "June",
#         "July",
#         "August",
#         "September",
#         "October",
#         "November",
#         "December"
#     ]

def number_to_full_month_name(month_number):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    return months[month_number - 1]


def number_to_short_month_name(long_month_name):
    return number_to_full_month_name(long_month_name)[0:3]


def cube_volume(side_length):
    return side_length ** 3


def reverse_string(string_to_reverse):
    return string_to_reverse[::-1]


def temp_convert(fahrenheit_to_celsius):
    return ((fahrenheit_to_celsius - 32) * 5) / 9