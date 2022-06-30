# Code

def reverse_string(input):
    """
    Return reversed input string

    Examples:
       reverse_string("abc") returns "cba"

    Args:
      input(str): string to be reversed

    Returns:
      a string that is the reverse of input
    """

    # TODO: Write your recursive string reverser solution here

    # pass
    if len(input) == 0:
        return ""
    else:
        first_character = input[0]
        x = slice(1, None)
        sub_string = input[x]
        return reverse_string(sub_string) + first_character

# Test Cases


print("Pass" if ("" == reverse_string("")) else "Fail")
print("Pass" if ("cba" == reverse_string("abc")) else "Fail")
