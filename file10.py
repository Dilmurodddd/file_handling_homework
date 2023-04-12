def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=open("txt_file/data10.txt",mode="r").read().split("\n")
    b=0
    c=0
    for t in a:
        if c<len(a[b]):
            c=len(a[b])
        b+=1
    return c
print(main("salom"))
# Read data from file