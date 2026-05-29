

def factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer.

    Args:
        n (int): A non-negative integer

    Raises:
        ValueError: If n is negative or greater than 1000.

    Returns:
        int: The factorial of n
        
    Time complexity: 
        O(n)
        
    Space complexity: 
        O(n), uses the call stack.
    """
    if n < 0:
        raise ValueError("Factorial for negative numbers is not defined.")
    if n > 1000:
        raise ValueError("Number too large. Please enter a smaller number.")
    if n <= 1: # covers 0 and 1
        return 1
    return n * factorial(n-1) # recursive

