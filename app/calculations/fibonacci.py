def fibonacci(n: int) -> int:
    """
    Calculates the nth Fibonacci number.

    Args:
        n (int): A non negative integer.
    
    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Returns:
        int: The nth Fibonacci number.
        
    Time complexity: 
        O(n)
        
    Space complexity: 
        O(1)
    """
    
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be a non-negative integer")
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b

    return a

