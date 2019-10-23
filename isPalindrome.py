def isPalindrome(x):
    reverse = 0
    if x < 0:
        return False
    if x < 10:
        return True
    while(x > reverse):
        reverse = (reverse * 10) + (x % 10)
        if reverse == 0:
            return False
        if x == reverse:
            return True
        x /= 10
        if x == reverse:
            return True
    return False