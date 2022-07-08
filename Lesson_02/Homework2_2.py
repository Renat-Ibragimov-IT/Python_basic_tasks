# 2. Напишите программу, которая считывает целое число и выводит текст,
# аналогичный  приведенному в примере (пробелы важны!). Первая строка содержит
# следующее значение, а вторая строка содержит предыдущее значение введёного
# числа:
# Please enter an integer number: 1234
# The next number for the number 1234 is 1235.
# The previous number for the number 1234 is 1233.
#     or
# Please enter an integer number: 0
# The next number for the number 0 is 1.
# The previous number for the number 0 is -1.

initial_int = int(input('Please enter an integer number: '))
print('The next number for the number ', initial_int, ' is ', initial_int+1)
print('The previous number for the number ', initial_int, ' is ',
      initial_int-1)
