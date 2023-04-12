def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=open("txt_file/data09.txt",mode="r").read()
    b=0
    for t in a:
        if t.isdigit():
            if b>int(t):
                b=int(t)
    return b
print(main("salom"))
# Read data from file