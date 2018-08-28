# Other Cool Parts of Python
# Note: This is a conglomerate lesson.

# You can import your own Python functions into another script.
# Just make sure there's an __init__.py file in that particular
# folder and that folder will become a Python module.
#
# This line imports the print_many_times() function from part 2.
from part2.part2 import print_many_times

# You can also import other modules for certain functions. This one
# will allow us to get pause functions with time.
import time


def print_list_slowly(your_list):
    for item in your_list:
        print item

        # This line is brought from the Time module. The parameter indicates
        # seconds to pause for,
        time.sleep(1.00)


def write_a_message(filename, message):
    # Python also allows for reading and writing files. The parameters for the
    # open function include the file path and which mode to read it in. 'r' is read,
    # 'w' is write, and 'a' is append (basically edit or add). A plus sign (+)
    # indicates a new file if it doesn't already exist, and a b indicates binary
    # data.
    with open(filename, 'w+') as message_file:
        message_file.writelines(message)


def read_a_message(filename):
    with open(filename, 'r') as message_file:
        return message_file.readlines()


if __name__ == "__main__":
    print_many_times(2, "Hello")

    test_list = [0, 1, 3, 5, 7, 9]
    print_list_slowly(test_list)

    write_a_message('messagefile.txt', 'I enjoyed this. Did you?')
    print(read_a_message('messagefile.txt'))
