# 2. Программа запрашивает ввод последовательности целых неотрицательных чисел,
# пока не будет введён 0. Как только будет введён 0 (ноль), программа должна
# посчитать и вывести на экран:
# - количество введённых чисел (завершающий 0 не считается)
# - их сумму
# - произведение
# - среднее арифметическое (не считая завершающего числа 0)
# - определить значение и порядковый номер наибольшего элемента
#       последовательности. Если наибольших элементов несколько, выведите
#       порядковый номер первого из них.
# - определить количество чётных и не чётных элементов в последовательности
# - определить значение второго по величине элемента в этой последовательности
# - определите, сколько элементов этой последовательности равны ее наибольшему
#       элементу


user_numbers_list = []
while (num := int(input("Enter number: "))) != 0:
    user_numbers_list.append(num)


def amount_of_entered_numbers():
    amount_of_en = len(user_numbers_list)
    return amount_of_en


def sum_of_entered_numbers():
    sum_of_en = sum(user_numbers_list)
    return sum_of_en


def multiply_of_entered_numbers():
    mult = 1
    for number in user_numbers_list:
        mult *= number
    return mult


def arithmetical_mean_of_entered_number():
    arithmetical_mean_of_en = sum_of_entered_numbers() / \
                              amount_of_entered_numbers()
    return arithmetical_mean_of_en


def index_of_largest_entered_number():
    largest_en = max(user_numbers_list)
    index_of_largest_en = user_numbers_list.index(largest_en)
    return largest_en, index_of_largest_en


def even_and_odd_numbers():
    even_numbers_amount = len([number for number in user_numbers_list
                               if number % 2 == 0])
    odd_numbers_amount = len([number for number in user_numbers_list
                              if number % 2 != 0])
    return even_numbers_amount, odd_numbers_amount


def second_by_value():
    set_list = list(set(user_numbers_list))
    return set_list[-2]


def amount_of_largest_numbers():
    amount = user_numbers_list.count(index_of_largest_entered_number()[0])
    return amount


print("Amount of entered numbers is: ", amount_of_entered_numbers())
print("Sum of entered numbers is: ", sum_of_entered_numbers())
print("Multiply of entered numbers is: ", multiply_of_entered_numbers())
print("Arithmetical mean of entered numbers is: ",
      arithmetical_mean_of_entered_number())
print("Largest entered number is: ", index_of_largest_entered_number()[0])
print("Index of largest entered number is: ",
      index_of_largest_entered_number()[1])
print("Even numbers amount is: ", even_and_odd_numbers()[0])
print("Odd numbers amount is: ", even_and_odd_numbers()[1])
print("Second by value number is: ", second_by_value())
print("Amount of largest numbers is: ", amount_of_largest_numbers())

# Кучу принтов внизу добавил для простоты проверки. Понимаю, что можно без них.