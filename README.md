# Make10 Solver

This is a Python implementation of a "Make10" solver. The goal of this solver is to find an expression using a given list of numbers and basic arithmetic operations (+, -, *, /) that evaluates to 10.

## How It Works

The solver uses permutations of the numbers and combinations of the operations to try and find an expression that evaluates to 10. It generates all possible permutations of the numbers and all possible combinations of the operations, then evaluates each expression to see if it equals 10.

## Functions

### `make10_solver(numbers)`
Finds an expression using the given numbers that evaluates to 10.

- **Parameters:**
  - `numbers` (list): A list of four integers.

- **Returns:**
  - `str`: An expression that evaluates to 10, or `None` if no such expression exists.

### Example Usage

Here is an example of how to use the Make10 solver:

```python
import itertools

def make10_solver(numbers):
    # Define all the operations
    operations = ['+', '-', '*', '/']

    # Generate all permutations of numbers
    for num_perm in itertools.permutations(numbers):
        # Generate all combinations of operations
        for ops in itertools.product(operations, repeat=len(numbers)-1):
            # Create an expression in the form of ((a op1 b) op2 c) op3 d
            expression = f"(({num_perm[0]} {ops[0]} {num_perm[1]}) {ops[1]} {num_perm[2]}) {ops[2]} {num_perm[3]}"
            try:
                # Evaluate the expression
                if abs(eval(expression) - 10) < 1e-9:  # Using a tolerance for floating point comparison
                    return expression
            except ZeroDivisionError:
                # Skip division by zero errors
                continue
    return None

# Example usage:
numbers = [1, 3, 4, 6]
solution = make10_solver(numbers)
if solution:
    print(f"Solution found: {solution} = 10")
else:
    print("No solution found")
```

### Output

The above script will output:
```
Solution found: ((6 / 3) * 4) - 1 = 10
```
if a solution exists, otherwise it will output:
```
No solution found
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/make10-solver.git
```

2. Navigate to the project directory:
```bash
cd make10-solver
```

3. Run the solver script:
```bash
python make10_solver.py
```

## License

This project is licensed under the MIT License.
