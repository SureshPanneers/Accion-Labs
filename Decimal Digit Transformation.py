def calculate_pattern_sum(x):
    """Calculate the sum of X + XX + XXX + XXXX for a given single digit X."""
    if not isinstance(x, int) or x < 0 or x > 9:
        raise ValueError("Input must be a single decimal digit (0-9).")
    
    # Construct the numbers using string manipulation
    term1 = x
    term2 = int(f"{x}{x}")       # XX
    term3 = int(f"{x}{x}{x}")    # XXX
    term4 = int(f"{x}{x}{x}{x}") # XXXX
    
    return term1 + term2 + term3 + term4


try:
    result = calculate_pattern_sum(3)
    print("Result:", result)  # Output: 3702
except ValueError as e:
    print("Error:", e)

  
