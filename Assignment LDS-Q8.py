def are_brackets_closed(code):
    stack = []

    for char in code:
        if char in ['(', '[', '{']:
            stack.append(char)
        elif char in [')', ']', '}']:
            if not stack:
                return False

            top = stack.pop()
            if (char == ')' and top != '(') or \
               (char == ']' and top != '[') or \
               (char == '}' and top != '{'):
                return False

    return len(stack) == 0

# Test the code snippet
code_snippet = input("Enter the code snippet: ")

if are_brackets_closed(code_snippet):
    print("All brackets are closed.")
else:
    print("Not all brackets are closed.")