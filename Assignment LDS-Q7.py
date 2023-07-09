def is_operator(char):
    operators = {'+', '-', '*', '/'}
    return char in operators

def prefix_to_infix(prefix):
    stack = []

    for char in reversed(prefix):
        if is_operator(char):
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix = f"({operand1}{char}{operand2})"
            stack.append(infix)
        else:
            stack.append(char)

    return stack.pop()

prefix_expression = input("Enter the prefix expression: ")
infix_expression = prefix_to_infix(prefix_expression)
print("Infix expression:", infix_expression)