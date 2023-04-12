def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=open("txt_file/data08.txt",mode="r").read()

    d=0
 

    for t in a:
        if t.isdigit():

            if d<int(t):
                d=int(t)
    return d
print(main("salom"))

# Read data from file