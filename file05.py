def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=open("txt_file/data05.txt",mode="r")
    b=a.read()
    d=[]
    f=0
    k=0
    p=[]
    for c in b:
        if c.isdigit():
            # d+=list(c)
            k+=1
            l=int(c)
            if f<l:
                f=l
    
    g=f+k
    p.append(k)
    p.append(g)
    return p
print(main("salom"))
# Read data from filei