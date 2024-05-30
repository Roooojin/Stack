class Stack:
    def __init__(self):
        self.items = []
        self.max_stack = []

    def push(self, item):
        self.items.append(item)
        if not self.max_stack or item >= self.max_stack[-1]:
            self.max_stack.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            popped_item = self.items.pop()
            if popped_item == self.max_stack[-1]:
                self.max_stack.pop()
            return popped_item

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def get_max(self):
        if self.isEmpty():
            return None
        else:
            return self.max_stack[-1]

# Example usage:
stack = Stack()
stack.push(5)
stack.push(3)
stack.push(7)
print("Max element in stack:", stack.get_max())  # Output: 7
print("Stack size:", stack.size())  # Output: 3
print("Popped item:", stack.pop())  # Output: 7
print("Top of stack:", stack.peek())  # Output: 3
print("Is stack empty?", stack.isEmpty())  # Output: False

def reverse_String(input_string):
    stack=Stack()
    reverse_String=""

    while not stack.isEmpty():
        reverse_String+=stack.pop()

    return reverse_String


def evaluate_postfix(expression):
    stack = Stack()
    operators = set(['+', '-', '*', '/'])

    for token in expression.split():
        if token not in operators:
            stack.push(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 // operand2

            stack.push(result)

    return stack.pop()

def is_balanced(expression):
    stack = Stack()
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')', ']', '}'}
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for char in expression:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.isEmpty():
                return False
            if bracket_pairs[stack.pop()] != char:
                return False
    return stack.isEmpty()

def is_operator(char):
    return char in ['+', '-', '*', '/']


def prefix_to_postfix(expression):
    stack = Stack()
    tokens = expression.split()


    for token in reversed(tokens):
        if is_operator(token):
            operand1 = stack.pop()
            operand2 = stack.pop()
            new_token = operand1 + ' ' + operand2 + ' ' + token
            stack.push(new_token)
        else:
            stack.push(token)


    return stack.pop()


def sort_stack(stack):
    sorted_stack = Stack()

    while not stack.isEmpty():
        temp = stack.pop()


        while not sorted_stack.isEmpty() and sorted_stack.peek() > temp:
            stack.push(sorted_stack.pop())


        sorted_stack.push(temp)

    return sorted_stack


def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = Stack()

    for token in expression.split():
        if token.isalnum():
            # Operand, add to output
            output.append(token)
        elif token == '(':
            # Left parenthesis, push onto stack
            stack.push(token)
        elif token == ')':
            # Right parenthesis, pop operators from stack and add to output until '(' is encountered
            while stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # Discard '('
        else:
            # Operator
            while (not stack.isEmpty()) and (stack.peek() != '(') and (precedence[token] <= precedence[stack.peek()]):
                output.append(stack.pop())
            stack.push(token)

    # Append remaining operators from stack to output
    while not stack.isEmpty():
        output.append(stack.pop())

    return ' '.join(output)


def daily_temperatures(temperatures):
    stack = Stack()
    result = [0] * len(temperatures)

    for i, temp in enumerate(temperatures):
        while not stack.isEmpty() and temp > temperatures[stack.peek()]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.push(i)

    return result



def longest_valid_parentheses(s):
    stack = Stack()
    max_length = 0

    # Initialize the stack with -1 as the base index
    stack.push(-1)

    for i in range(len(s)):
        if s[i] == '(':
            stack.push(i)
        else:
            stack.pop()
            if stack.isEmpty():
                # If stack is empty, no more '(' to match, so update the base index
                stack.push(i)
            else:
                # Calculate the length of the valid parentheses substring
                max_length = max(max_length, i - stack.peek())

    return max_length






