def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=open("txt_file/data06.txt",mode="r")
    b=a.read()
    c=b.split()
    d=0
    e=0
    f=0
    g=0
    h=0
    j=0
    k=0
    p=[]

   
    
        
        
    for t in c[d]:
        if t.isalpha():
            e+=1


    d+=1
    for t in c[d]:
        if t.isalpha():
            f+=1


    d+=1
    for t in c[d]:
        if t.isalpha():
            g+=1


    d+=1
    for t in c[d]:
        if t.isalpha():
            h+=1


    d+=1
    for t in c[d]:
        if t.isalpha():
            j+=1


    d+=1
    for t in c[d]:
        if t.isalpha():
            k+=1

    
    
    p.append(e)
    p.append(f)
    p.append(g)
    p.append(h)
    p.append(j)
    p.append(k)
    
    return p
print(main("salom"))

# Read data from file