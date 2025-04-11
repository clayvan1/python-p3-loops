# looping.py

def happy_new_year():
    """
    Counts down from 10 to 1 using a while loop and prints "Happy New Year!".
    """
    count = 10
    while count >= 1:
        print(count)
        count -= 1
    print("Happy New Year!")

def square_integers(numbers):
    """
    Takes a list of integers and returns a new list with each element squared.

    Args:
        numbers (list): A list of integers.

    Returns:
        list: A new list containing the squares of the input integers.
    """
    squared_numbers = []
    for number in numbers:
        squared_numbers.append(number ** 2)
    return squared_numbers

def fizzbuzz():
    """
    Prints numbers from 1 to 100, with "Fizz" for multiples of 3,
    "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

# Example usage (these won't be run by pytest directly)
if __name__ == "__main__":
    happy_new_year()
    print(square_integers([1, 2, 3, 4, 5]))
    fizzbuzz()