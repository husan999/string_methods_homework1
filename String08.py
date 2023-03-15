def main(s):
    """
    A variable of type str is given. Make sure it only consists of uppercase letters.
    Args:
        s: str
    Returns:
        bool: answer
    """
    a=0
    if s==s.upper():
        a+=1
        return True
    else:
        return False
print(main("CODESCHOOL"))
