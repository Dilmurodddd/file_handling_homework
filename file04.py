def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=open("txt_file/data04.txt",mode="r")
    b=a.read()
    d=[]
    for c in b:
        if c.isalpha():
            d+=list(c)
    return d
print(main("salom"))
# Read data from file