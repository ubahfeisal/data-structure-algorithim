def is_balanced (expression):
    stack = []
    
    opening_brackets = "[,{,("
    closing_brackets = "],},)"
    
    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            top_element = stack.pop()
            if opening_brackets.index(top_element) != closing_brackets.index(char):
                return False
            
    return len(stack) == 0 
# test1 
expression1 = "{(})"
print(is_balanced(expression1))

#test 2
expression2 = "{()}"
print(is_balanced(expression2))