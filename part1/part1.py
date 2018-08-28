# Variable Types and Functions (Basic)

# Bool can be True or False
boolean_value = False


def play_integers():
    # Variable Types
    integer = 1
    float_number = 1.00

    # Note that integer is now a different value.
    integer = integer + 3
    print(integer)

    # To increment by one, do the following:
    integer += 1
    print(integer)

    # Note that you cannot add integers and floats in other languages.
    try:
        print(float_number + integer)
    except Exception as e:
        print(e)


def concat_string():
    # Note that the string also has an '\n', meaning a new line.
    string = "This is a string.\nStrings can have new lines, making paragraphs."
    number = 16
    try:
        print(string + number)
        # Why does this not work?
    except Exception as e:
        print(e)

    # This works though!
    print(string + str(number))


# This function takes parameters. Params work the same way as variables.
# This function in particular will produce something that can be stored
# in a variable.
def multiply(x, y):
    """
    Multiplies two numbers together and returns the product.
    :param x: The first number
    :param y: The second number
    :returns: The product of x and y
    """
    return x * y


if __name__ == "__main__":
    play_integers()
    concat_string()
    product = multiply(2, 3)
    print(product)