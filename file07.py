def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=open("txt_file/data07.txt",mode="r")
    b=a.read()
    d=0
    for t in b:
        if t.isdigit():
            d+=int(t)
    return d
print(main("salom"))
    
# Read data from file