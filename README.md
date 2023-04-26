# Expression Calculator
This is a simple calculator that evaluates mathematical expressions in base 10 and base 2 up to 128 characters in length.

# Usage
To use the calculator, run the main.py file and enter 'b' to choose a base and evaluate your desired expression, 's' to see the statistics or 'q' to terminate the program.


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
Each operation performed by the calculator is stored in a SQLite database calculator.db. The database contains a single table calculations.


# Descriptive Statistics
The calculator provides descriptive statistics for the operations performed. The following statistics are provided:

Total number of times the calculator performed each operation (+, -, *, /, ^, !, %)
Average number of operations performed per expression

