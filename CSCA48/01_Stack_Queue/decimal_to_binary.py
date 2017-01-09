from stacks import StackA


def convert_to_binary(decimal_number):
    '''(int) -> str
    Return a string representing demical_number in binary
    '''
    # This stack will hold the remainders of the divisions,
    # which will eventually become the binary string
    remainder_stack = StackA()

    # if decimal number is 0, then directly push to stack
    if decimal_number == 0:
        remainder_stack.push(decimal_number)

    # while decimal_number is greater than zero, keep dividing it by 2 (using
    # integer division) and pushing the remainder onto the stack. This will
    # result in the stack becoming a binary representation (read top to bottom)
    # of the original decimal_number
    while(decimal_number > 0):
        remainder = decimal_number % 2
        remainder_stack.push(remainder)
        decimal_number = decimal_number // 2

    # the stack, read from top to bottom is now the binary number we want to
    # return. So we simply pop each item and add it (as a string) to the
    # return value
    binary_string = ""

    while(not (remainder_stack.is_empty())):
        binary_string += str(remainder_stack.pop())

    return binary_string

if (__name__ == "__main__"):
    print(convert_to_binary(0))
    print(convert_to_binary(1))
    print(convert_to_binary(10))
    print(convert_to_binary(42))
    print(convert_to_binary(13452))
