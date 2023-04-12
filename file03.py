def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=open("txt_file/data03.txt", mode="r")
    b=a.read()
    d=[]
    for c in b:
        if c.isdigit():
            d+=list(c)
    return d
print(main("a"))
# Read data from file
