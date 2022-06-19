class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def evaluate_post_fix(input_list):
    """
    Evaluate the postfix expression to find the answer

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
    """
    # TODO: Iterate over elements

    # TODO: Use stacks to control the element positions

    # pass

    stack = Stack()
    for i in input_list:
        if i == '*':
            second_element = stack.pop()
            first_element = stack.pop()
            result = first_element * second_element
            stack.push(result)
        elif i == '/':
            second_element = stack.pop()
            first_element = stack.pop()
            result = int(first_element / second_element)
            stack.push(result)
        elif i == '+':
            second_element = stack.pop()
            first_element = stack.pop()
            result = first_element + second_element
            stack.push(result)
        elif i == '-':
            second_element = stack.pop()
            first_element = stack.pop()
            result = first_element - second_element
            stack.push(result)
        else:
            stack.push(int(i))
    return stack.pop()


# def evaluate_post_fix(input_list):
#     stack = Stack()
#     for element in input_list:
#         if element == '*':
#             second = stack.pop()
#             first = stack.pop()
#             output = first * second
#             stack.push(output)
#         elif element == '/':
#             second = stack.pop()
#             first = stack.pop()
#             output = int(first / second)
#             stack.push(output)
#         elif element == '+':
#             second = stack.pop()
#             first = stack.pop()
#             output = first + second
#             stack.push(output)
#         elif element == '-':
#             second = stack.pop()
#             first = stack.pop()
#             output = first - second
#             stack.push(output)
#         else:
#             stack.push(int(element))
#     return stack.pop()


def test_function(test_case):
    output = evaluate_post_fix(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [["3", "1", "+", "4", "*"], 16]

test_function(test_case_1)
test_case_2 = [["4", "13", "5", "/", "+"], 6]
test_function(test_case_2)
test_case_3 = [["10", "6", "9", "3", "+", "-11",
                "*", "/", "*", "17", "+", "5", "+"], 22]
test_function(test_case_3)
