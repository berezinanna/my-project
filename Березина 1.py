numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = 0
odd_count = 0
for number in numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Количество четных чисел:", even_count)
print("Количество нечетных чисел:", odd_count)
total_sum = 0
for number in numbers:
    total_sum += number
average = total_sum / len(numbers)
print("Среднее арифметическое значение чисел в списке:", average)
user_number = int(input("Введите число: "))
number_found = False
for number in numbers:
    if number == user_number:
        number_found = True
        break
if number_found:
    print("Число есть в списке")
else:
    print("Числа нет в списке")
    