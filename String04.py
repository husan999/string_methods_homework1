def main(s):
    """
    A variable of type str is given. make sure all letters are lowercase.
    Args:
        s: str
    Returns:
        bool: answer
    """
    a=0
    if s==s.lower():
        a+=1
        return True
    else:
        return False
print(main("codeschool"))