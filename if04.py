def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    large=a
    if large<b:
        large=b
    if a==b:
        return 0
    if a!=b:
        return large
print(main(3,7))
print(main(5,5))