class Stack:

    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, data):
        if self.next_index == len(self.arr):
            print("Out of space! Increasing array capacity ...")
            self._handle_stack_capacity_full()

        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1

    # TODO: Add the pop method
    def pop(self):
        if self.is_empty():
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def _handle_stack_capacity_full(self):
        old_arr = self.arr

        self.arr = [0 for _ in range(2 * len(old_arr))]
        for index, value in enumerate(old_arr):
            self.arr[index] = value


foo = Stack()
# We first have to push an item so that we'll have something to pop
foo.push("Test")
print(foo.pop())  # Should return the popped item, which is "Test"
print(foo.pop())  # Should return None, since there's nothing left in the stack
