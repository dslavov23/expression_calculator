# Expression Calculator
This is a simple calculator that evaluates mathematical expressions up to 128 characters in length.

# Usage
To use the calculator, run the main.py file and enter the expression you would like to evaluate when prompted. The calculator will then output the result of the expression.

The calculator supports the following operations:

+ Addition
- Subtraction
* Multiplication
/ Division
^ Exponential power (a to the power of b)
! Factorial
% Percent (a percent of b)
(, [ and ], ) Parentheses to specify order of operations
Operands must be base 10 and the following characters are allowed:

(, [ and ], )
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
*, /, +, -, ^, !, %

# Database
Each operation performed by the calculator is stored in a SQLite database calculations.db. The database contains a single table calculations with the following columns:

id Primary key auto-incrementing integer value
operation The mathematical operation performed
operand1 The first operand in the operation
operand2 The second operand in the operation (if applicable)
result The result of the operation
timestamp The date and time the operation was performed

# Descriptive Statistics
The calculator provides descriptive statistics for the operations performed. The following statistics are provided:

Total number of times the calculator performed each operation (+, -, *, /, ^, !, %)
Average number of operations performed per expression
