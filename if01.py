def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    largest=a
    if largest<b:
        largest=b
    if largest<c:
        largest=c
    return largest
print(main(1,4,2))