# 1. Check whether a number is even or odd
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_odd(10))
print(even_odd(7))


# 2. Find the largest of two numbers
def largest(a, b):
    if a > b:
        return a
    else:
        return b

print(largest(25, 18))


# 3. Calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

print(rectangle_area(10, 5))


# 4. Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(30))


# 5. Check whether a number is positive, negative or zero
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(-5))


# 6. Find the factorial of a number
def factorial(num):
    result = 1

    for i in range(1, num + 1):
        result *= i

    return result

print(factorial(5))


# 7. Count the number of digits in a number
def count_digits(num):
    return len(str(abs(num)))

print(count_digits(12345))


# 8. Reverse a string
def reverse_string(text):
    return text[::-1]

print(reverse_string("Kashish"))


# 9. Check whether a string is palindrome
def is_palindrome(text):
    text = text.lower()

    if text == text[::-1]:
        return True
    else:
        return False

print(is_palindrome("madam"))
print(is_palindrome("hello"))


# 10. Find the sum of numbers from 1 to n
def sum_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

print(sum_numbers(10))