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

