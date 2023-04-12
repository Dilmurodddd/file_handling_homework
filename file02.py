def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=open("txt_file/data02.txt", mode="r")
    b=a.read()
    c=len(b)
    return c
print(main('salom'))
# Read data from file