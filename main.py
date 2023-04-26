from db import setup_database, store_calculation
from helpers import evaluate_expression, tokenize, validate_expression


def expression_calculator(conn, expression):
    if not validate_expression(expression):
        print("Invalid expression. Please use only allowed characters.")
        return None

    tokens = tokenize(expression)
    result = evaluate_expression(conn, tokens)
    return result


def display_statistics(conn):
    cur = conn.cursor()
    operations = ['+', '-', '*', '/', '^', '!', '%']

    print("Descriptive statistics:")
    for operation in operations:
        cur.execute("""
        SELECT COUNT(*) FROM calculations WHERE operation=?
        """, (operation,))
        count = cur.fetchone()[0]
        print(f"Total number of times the calculator performed the '{operation}' operation: {count}")

    cur.execute("""
    SELECT COUNT(*) FROM calculations
    """)
    total = cur.fetchone()[0]
    average = total / len(operations)
    print(f"Average number of times the calculator performed elementary operations: {average:.2f}")


if __name__ == "__main__":
    conn = setup_database()
    while True:
        expression = input("Enter an expression to calculate, 's' for statistics or 'q' to quit: ")
        if expression.lower() == "q":
            break
        elif expression.lower() == "s":
            display_statistics(conn)
        else:
            result = expression_calculator(conn, expression)
            if result is not None:
                print(f"Result: {result}")

