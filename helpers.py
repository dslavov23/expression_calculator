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


def apply_operation(conn, op, b, a=None):
    if a is not None:
        result = apply_operation_without_db(op, b, a)
        store_calculation(conn, op, a, b, result)
    else:
        result = apply_operation_without_db(op, b)
        store_calculation(conn, op, b, None, result)
    return result


def apply_operation_without_db(op, b, a=None):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        return a / b
    if op == '^':
        return a ** b
    if op == '%':
        return (a * b) / 100
    if op == '!':
        return math.factorial(b)


def greater_precedence(op1, op2):
    return precedence[op1] > precedence[op2]


def evaluate_expression(conn, tokens):
    values = []
    operators = []

    def handle_operator(op):
        while operators and operators[-1] != '(' and operators[-1] != '[' and greater_precedence(operators[-1], op):
            operation = operators.pop()
            b = values.pop()
            a = values.pop() if operation != '!' else None
            values.append(apply_operation(conn, operation, b, a))
        operators.append(op)

    for token in tokens:
        if token.isdigit() or token.replace(".", "", 1).isdigit():
            values.append(float(token))
        elif token == '(' or token == '[':
            operators.append(token)
        elif token == ')' or token == ']':
            while operators[-1] != '(' and operators[-1] != '[':
                operation = operators.pop()
                b = values.pop()
                a = values.pop() if operation != '!' else None
                values.append(apply_operation(conn, operation, b, a))
            operators.pop()  # Discard the '(' or '['
        else:  # Operator
            handle_operator(token)

    while operators:
        operation = operators.pop()
        b = values.pop()
        a = values.pop() if operation != '!' else None
        values.append(apply_operation(conn, operation, b, a))

    return values[0]


def tokenize(expression):
    tokens = re.findall(r"(\d+\.?\d*|\(|\[|\)|\]|\\|\^|\!|%|\*|/|\+|\-)", expression)
    return tokens


def validate_expression(expression):
    allowed_characters = re.compile(r"^[0-9\+\-\*/\^%!()\[\]\\.]+$")
    return allowed_characters.match(expression) is not None
