def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    smallest=a
    if smallest>b:
        smallest=b
    if smallest>c:
        smallest=c
    return smallest
print(main(1,4,2))
print(main(-5,-3,-1))