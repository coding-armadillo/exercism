def is_armstrong_number(number):
    numbers=str(number)
    return number == sum(int(n)**len(numbers) for n in numbers)
    
