def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    n1=n%10
    n2=n//10%10
    n3=n//100%10
    n4=n//1000%10
    n5=n//10000
    large=n1
    index=1
    if large<n2:
        index=2
        large=n2
    if large<n3:
        index=3
        large=n3
    if large<n4:
        index=4
        large=n4
    if large<n5:
        index=5
        large=n5
    return  large,index
print(main(76514))
print(main(54694))