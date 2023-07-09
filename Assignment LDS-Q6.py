def is_operator(char):
    operators = {'+', '-', '*', '/'}
    return char in operators

def postfix_to_prefix(postfix):
    stack = []

    for char in postfix:
        if is_operator(char):
            operand2 = stack.pop()
            operand1 = stack.pop()
            prefix = char + operand1 + operand2
            stack.append(prefix)
        else:
            stack.append(char)

    return stack.pop()

postfix_expression = input("Enter the postfix expression: ")
prefix_expression = postfix_to_prefix(postfix_expression)
print("Prefix expression:", prefix_expression)