from db import setup_database, store_calculation
from helpers import evaluate_expression, tokenize, validate_expression


def expression_calculator(conn, expression, base_2=False):
    if not validate_expression(expression):
        print("Invalid expression. Please use only allowed characters.")
        return None

    tokens = tokenize(expression)
    result = evaluate_expression(conn, tokens, base_2)
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
    base_2 = False
    while True:
        expression = input("Enter an expression to calculate, 's' for statistics, 'q' to quit, or 'b' for base: ")
        if expression.lower() == "q":
            break
        elif expression.lower() == "s":
            display_statistics(conn)
        elif expression.lower() == "b":
            base = input("Enter the desired base (2 or 10): ")
            base_2 = base == "2"
        else:
            result = expression_calculator(conn, expression, base_2)
            if result is not None:
                print(f"Result: {result}")
