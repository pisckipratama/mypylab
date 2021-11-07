def my_function():
    return "this is my basic function"


print(my_function())


# using arguments in function
def my_function_with_argument(str1, str2):
    return f"the parameter 1 is {str1} and parameter 2 is {str2}"


print(my_function_with_argument("Piscki", "Pratama"))


# using default argument
def my_function_with_default_argument(num1, num2=1):
    return num1 + num2


print(my_function_with_default_argument(4))

# using keyword argument
print(my_function_with_default_argument(num2=9, num1=11))


def my_infinite_arguments_function(*people):
    for person in people:
        print(f"This person is {person}")


my_infinite_arguments_function("Nick", "John", "Peter")
