# Queue must be formed by two stacks.

class MyQueue(object):
    def __init__(self):
        self.stack_a = []
        self.stack_b = []

    def peek(self):
        if not self.stack_b:
            self.stack_b = [self.stack_a.pop() for i in range(len(self.stack_a))]
            # print("Transit values from stack_a to stack_b")
            if not self.stack_b:
                # print("Stack is empty...")
                return None

        x = self.stack_b[-1]
        # print("View top of stack_b", x)
        return x

    def pop(self):
        if not self.stack_b:
            self.stack_b = [self.stack_a.pop() for i in range(len(self.stack_a))]
            # print("Transit values from stack_a to stack_b")
            if not self.stack_b:
                # print("Nothing to pop...")
                return None

        x = self.stack_b.pop()
        # print("Pop {} from stack_b. stack_b {}".format(x, self.stack_b))

    def put(self, value):
        # Note: no need to move stack_b to stack_a.
        #       stack_a always in NORMAL stack, stack_b always in REVERSE stack
        # if self.stack_b:
        #     self.stack_a = [self.stack_b.pop() for i in range(len(self.stack_b))]
            # print("Transit values from stack_b to stack_a")
        self.stack_a.append(value)
        # print("Push {}. stack_a {}".format(value, self.stack_a))


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    # print("")
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
