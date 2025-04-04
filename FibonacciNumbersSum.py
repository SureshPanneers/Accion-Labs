def sum_even_fibonacci(limit=100):
    """Calculate the sum of the first `limit` even Fibonacci numbers efficiently."""
    even_fib_1, even_fib_2 = 2, 8  # First two even Fibonacci numbers
    total_sum = even_fib_1 + even_fib_2
    
    for _ in range(limit - 2):  # We already have 2 values, so iterate (limit - 2) times
        next_even_fib = 4 * even_fib_2 + even_fib_1
        total_sum += next_even_fib
        even_fib_1, even_fib_2 = even_fib_2, next_even_fib  # Move to the next numbers
    
    return total_sum

# Compute and print the sum of the first 100 even Fibonacci numbers
result = sum_even_fibonacci(100)
print("Sum of the first 100 even Fibonacci numbers:", result)
