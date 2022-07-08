# The program asks for a sequence of non-negative integers until 0 is entered.
# As soon as 0 (zero) is entered, the program should calculate and display:
# - number of entered numbers (terminal 0 is not considered);
# - their sum;
# - product of numbers;
# - arithmetic mean (excluding the final number 0);
# - determine the value and ordinal number of the largest element of the
#   sequence. If there are several largest elements, output the ordinal number
#   of the first of them;
# - determine the number of even and odd elements in the sequence;
# - determine the value of the second-largest element in this sequence;
# - determine how many elements of this sequence are equal to its largest
#   element.


user_numbers_list = []
while (num := int(input("Enter number: "))) != 0:
    user_numbers_list.append(num)


def amount_of_entered_numbers(numbers_list: list) -> int:
    """This function will calculate amount of all numbers entered by user"""
    amount_of_en = len(numbers_list)
    return amount_of_en


def sum_of_entered_numbers(numbers_list: list) -> int:
    """This function will calculate sum of all numbers"""
    sum_of_en = sum(numbers_list)
    return sum_of_en


def multiply_of_entered_numbers(numbers_list: list) -> int:
    """This function will calculate multiply of all numbers"""
    mult = 1
    for number in numbers_list:
        mult *= number
    return mult


def arithmetical_mean_of_entered_number(numbers_list: list) -> float:
    """This function will calculate arithmetical mean of all numbers"""
    arithmetical_mean_of_numbers = sum(numbers_list) / len(numbers_list)
    return arithmetical_mean_of_numbers


def ordinal_number_largest_entered_number(numbers_list: list) -> tuple:
    """This function will search the largest number, and its ordinal number in
    the list"""
    largest_element = max(numbers_list)
    ordinal_number_of_largest_element = \
        numbers_list.index(largest_element) + 1
    return largest_element, ordinal_number_of_largest_element


def even_and_odd_numbers(numbers_list: list) -> tuple:
    """This function will calculate amount of odd and even numbers
    in the list"""
    even_numbers_amount = len([number for number in numbers_list
                               if number % 2 == 0])
    odd_numbers_amount = len([number for number in numbers_list
                              if number % 2 != 0])
    return even_numbers_amount, odd_numbers_amount


def second_by_value(numbers_list: list) -> int:
    """This function will search the second-largest number"""
    set_list = list(set(numbers_list))
    return set_list[-2]


def amount_of_largest_numbers(numbers_list: list) -> int:
    """This function will calculate amount of the largest numbers in the
    list"""
    amount = numbers_list.count(max(numbers_list))
    return amount


print(f'Amount of entered numbers is: '
      f'{amount_of_entered_numbers(user_numbers_list)}')
print(f'Sum of entered numbers is: '
      f'{sum_of_entered_numbers(user_numbers_list)}')
print(f'Multiply of entered numbers is: '
      f'{multiply_of_entered_numbers(user_numbers_list)}')
print(f'Arithmetical mean of entered numbers is: '
      f'{arithmetical_mean_of_entered_number(user_numbers_list)}')
print(f'Largest entered number is: '
      f'{ordinal_number_largest_entered_number(user_numbers_list)[0]}')
print(f'Ordinal number of largest entered number is: '
      f'{ordinal_number_largest_entered_number(user_numbers_list)[1]}')
print(f'Even numbers amount is: {even_and_odd_numbers(user_numbers_list)[0]}')
print(f'Odd numbers amount is: {even_and_odd_numbers(user_numbers_list)[1]}')
print(f'Second by value number is: {second_by_value(user_numbers_list)}')
print(f'Amount of largest numbers is: '
      f'{amount_of_largest_numbers(user_numbers_list)}')
