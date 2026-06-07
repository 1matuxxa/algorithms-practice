'''SimpleGen1. Написать функцию-генератор, которая принимает на вход список целых чисел и
порождает последовательность текущих минимумов.'''

def running_minimum(numbers):
    if not numbers:
        return
    current_min = numbers[0]
    for num in numbers:
        if num < current_min:
            current_min = num
        yield current_min
        print(current_min)

print(list(running_minimum([6,6,7,4,3,7,9,3,2,1,6,526,5,235])))