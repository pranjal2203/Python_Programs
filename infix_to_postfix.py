#infix to postfix conversion 


#declaring operators(as a set) along with priorities(as a dictionary)
OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])  
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3}  

 
#function that converts infix to postfix
def infix_to_postfix(expression): 
    stack = []         #initializing an empty stack
    output = ''        #initializing output as currently empty

    for ch in expression:
        if ch not in OPERATORS:         #checking for an operand if yes,put it directly in postfix expression
            output+= ch
        elif ch=='(':                   #else operators should be put in stack
            stack.append('(')
        elif ch==')':
            while stack and stack[-1]!= '(':
                output+=stack.pop()
            stack.pop()
        else:
            # lesser priority can't be on top so pop and put it in output   
            while stack and stack[-1]!='(' and PRIORITY[ch]<=PRIORITY[stack[-1]]:
                output+=stack.pop()
            stack.append(ch)

    while stack:
        output+=stack.pop()
    return output

#inputting infix expression fro user and printing its postfix form 
expression = input('Enter infix expression: ')
print('infix expression: ',expression)
print('postfix expression: ',infix_to_postfix(expression))
print("infix to postfix conversion is done ")
