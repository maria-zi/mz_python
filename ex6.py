#!/usr/bin/python3

types_of_people = 10 #присвоение переменной значения
x = f"There are {types_of_people} types of people."
# присвоение переменной х значения с встроенной переменной
# через форматирование в ввиде fстроки
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))
# выведение на экран предыдущей переменной форматированной с помощью
# .format()
w = "This is the left side of..."
e = "a string with a right side."
 #в предыдущей строке сложение 2 переменных с присвоенными им значениями
print(w + e)
