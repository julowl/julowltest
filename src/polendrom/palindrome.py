def is_palindrome(pol :str) -> bool:
    left = 0
    right = len(pol)-1
    while left < right:
        if pol[left] != pol[right]:
            return False
        else:
            left += 1
            right -= 1
    return True
