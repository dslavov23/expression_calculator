import math
import re
from db import store_calculation

precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
    '%': 2,
    '!': 4
}


def dec_to_bin(dec):
    return bin(dec).replace("0b", "")


def bin_to_dec(binary):
    return int(str(binary), 2)


def apply_operation(conn, op, b, a=None, base_2=False):
    if a is not None:
        result = apply_operation_without_db(op, b, a, base_2)
        store_calculation(conn, op, a, b, result)
    else:
        result = apply_operation_without_db(op, b, None, base_2)
        store_calculation(conn, op, b, None, result)
    return result


def apply_operation_without_db(op, b, a=None, base_2=False):
    result = None  # Add this line to initialize the result variable

    if base_2:
        a = bin_to_dec(a) if a is not None else None
        b = bin_to_dec(b)

    if op == '+':
        result = a + b
    elif op == '-':  # Change this line to use 'elif' instead of 'if'
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        result = a / b
    elif op == '^':
        result = a ** b
    elif op == '%':
        result = (a * b) / 100
    elif op == '!':
        result = math.factorial(b)

    if base_2:
        result = dec_to_bin(result)

    return result



def greater_precedence(op1, op2):
    return precedence[op1] > precedence[op2]


def evaluate_expression(conn, tokens, base_2=False):
    values = []
    operators = []

    def handle_operator(op):
        while operators and operators[-1] != '(' and operators[-1] != '[' and greater_precedence(operators[-1], op):
            operation = operators.pop()
            b = values.pop()
            a = values.pop() if operation != '!' else None
            values.append(apply_operation(conn, operation, b, a, base_2))
        operators.append(op)

    for token in tokens:
        if token.isdigit() or token.replace(".", "", 1).isdigit():
            if base_2:
                values.append(int(token))
            else:
                values.append(float(token))
        elif token == '(' or token == '[':
            operators.append(token)
        elif token == ')' or token == ']':
            while operators[-1] != '(' and operators[-1] != '[':
                operation = operators.pop()
                b = values.pop()
                a = values.pop() if operation != '!' else None
                values.append(apply_operation(conn, operation, b, a, base_2))
            operators.pop()
        else:
            handle_operator(token)

    while operators:
        operation = operators.pop()
        b = values.pop()
        a = values.pop() if operation != '!' else None
        values.append(apply_operation(conn, operation, b, a, base_2))

    return values[0]


def tokenize(expression):
    tokens = re.findall(r"(\d+\.?\d*|\(|\[|\)|\]|\\|\^|\!|%|\*|/|\+|\-)", expression)
    return tokens


def validate_expression(expression):
    allowed_characters = re.compile(r"^[0-9\+\-\*/\^%!()\[\]\\.]+$")
    return allowed_characters.match(expression) is not None
