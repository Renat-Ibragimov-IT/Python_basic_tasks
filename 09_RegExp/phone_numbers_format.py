# Write a program that will format the phone number to a single form.
# For input, the program accepts the string of the entered phone number.
# For example:
# 063-999-99-99, output: (+38) 063 999-99-99
# 063 999-99-99, output: (+38) 063 999-99-99
# 063-99999-99, output: (+38) 063 999-99-99
# +3806399-999-99, output: (+38) 063 999-99-99
# 380639999999, output: (+38) 063 999-99-99
# Если что-то не так с номером - пишет 'Failed to recognize number'.
import re
user_number = input("Please enter Your phone number: ")


def change_number_format(number: str):
    """This function will return ukrainian phone numbers in single format"""
    clear_num = re.sub(r'[\-\s+]', '', number)
    if re.fullmatch(r'(\+?\d+)?(0\d{2})(\d{3})(\d{2})(\d{2})', clear_num):
        return re.sub(r'(\+?\d+)?(0\d{2})(\d{3})(\d{2})(\d{2})',
                      r'(+38) \2 \3-\4-\5', clear_num)
    else:
        return f'Failed to recognize number'


print(change_number_format(user_number))
