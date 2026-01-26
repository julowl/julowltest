def is_palindrome(pol :str) -> bool:
    for left in range(len(pol)):
        right = len(pol) - ( left + 1)
        if pol[left] != pol[right]:
            return False
    return True
