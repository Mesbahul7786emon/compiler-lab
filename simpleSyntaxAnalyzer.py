readMe = open('input.txt').read()
print(readMe.split(' '))

value = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
operator = ['+', '-', '*', '/']
identifiers = ['a', 'b', 'c', 'd', 'i']
keyword = ['if', 'else', 'for', 'switch', 'while', 'return', 'byte', 'int', 'float', 'double', 'string', 'char', 'for']
logicalOperator = ['<', '>', '&&', '=', '==', '!=', '||']
others = [',', ':', ';', '(', ')''{', '}', '[', ']']

print('\nvalue = ', end=' ')
for i in readMe:
    for val in value:
        if i == val:

            print(i, end=' ')
print('\noperator = ', end=' ')
for i in readMe:
    for val in operator:
        if i == val:

            print(i, end=' ')
print('\nIdentifiers = ', end=' ')
for i in readMe:
    for val in identifiers:
        if i == val:

            print(i, end=' ')
print('\nkeywords = ', end=' ')
for i in readMe:
    for val in keyword:
        if i == val:

            print(i, end=' ')

print('\nLogical Operators = ', end=' ')
for i in readMe:
    for val in logicalOperator:
        if i == val:

            print(i, end=' ')

print('\nothers = ', end=' ')
for i in readMe:
    for val in others:
        if i == val:

            print(i, end=' ')