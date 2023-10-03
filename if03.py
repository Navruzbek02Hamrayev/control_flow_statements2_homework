def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    large=a
    small=a
    if large<b:
        large=b
    if large<c:
        large=c
    if small>b:
        small=b
    if small>c:
        small=c
    return a+b+c-large-small
print(main(3,7,1))
print(main(5,5,-1))