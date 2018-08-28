# Conditional Statements and Loops


def check_if_true(bool_value):
    # If statements by themselves can indicate whether a value is true.
    if bool_value:
        print("This is true!")

    # Else is the equivalent of "otherwise"
    else:
        print("This is false!")


def read_my_input(number):

    # Note that there are two equal signs (indicates a check for
    # equal rather than assignment)
    if number == 0:
        print("Value is 0")

    # If you have another condition to check, elif (else if) works.
    # Note that you can check for logical operations like inequalities,
    # combinations, or options.
    elif 0 < number <= 5:
        print("It's within that range, yeah...")
    elif number >= 6:
        print("You're going sky high!")

    # As is the case here, we're checking for an "or" operator.
    elif number >= 10 or number < -10:
        print("So, uh, you really like going out of bounds, eh?")
    else:
        print("WTF mate?")


def match_password(password):
    # You can also check for inverses of statements ("not something").
    if password != "kittens123":
        print("Password is incorrect!")

        # Conditionals in functions can also return values and stop
        # the function all together.
        return False
    else:
        print("You logged onto the server successfully.")
        return True


def print_many_times(n, message):
    # This is a loop. This will repeat an action for 'n' amount of times.
    # Alternatively, you can use a 'while' loop.
    for i in range(n):
        print(message)

    # Alternate
    # i = 0
    # while i <= n:
    #     print(message)
    #     i += 1


def print_list(your_list):
    # For loops can also work with lists/arrays for each item in that list.
    for item in your_list:
        print(item)


if __name__ == "__main__":
    cool_beans = False
    check_if_true(cool_beans)

    read_my_input(42)

    match_password("system124")

    print_many_times(42, "I like chocolate.")
    
    my_list = [0, 12, 34, 56, 78]
    print_list(my_list)
