def p(g):
    h,w=len(g),len(g[0])
    # collect the two rectangles: {color:[top,bottom,left,right]}
    box={}
    for i,row in enumerate(g):
        for j,v in enumerate(row):
            if v and v!=8:
                a=box.setdefault(v,[i,i,j,j])
                if i<a[0]: a[0]=i
                if i>a[1]: a[1]=i
                if j<a[2]: a[2]=j
                if j>a[3]: a[3]=j
    (A,B)=[v for v in box.values()]
    ia,ja,ib,jb=A[0:2],A[2:4],B[0:2],B[2:4]
    def vline(inner,other):
        # vertical strip: columns = inner inner-columns, rows between the two rects
        if inner[1]<other[0]: ra,rb=inner[1]+1,other[0]-1
        else: ra,rb=other[1]+1,inner[0]-1
        for i in range(ra,rb+1):
            for j in range(inner[2]+1,inner[3]):
                g[i][j]=8
    def hline(inner,other):
        # horizontal strip: rows = inner inner-rows, cols between the two rects
        if inner[3]<other[2]: ca,cb=inner[3]+1,other[2]-1
        else: ca,cb=other[3]+1,inner[2]-1
        for j in range(ca,cb+1):
            for i in range(inner[0]+1,inner[1]):
                g[i][j]=8
    # decide direction by inclusion on one axis
    if ja[0]>=jb[0] and ja[1]<=jb[1]: vline(A,B)
    elif jb[0]>=ja[0] and jb[1]<=ja[1]: vline(B,A)
    elif ia[0]>=ib[0] and ia[1]<=ib[1]: hline(A,B)
    else: hline(B,A)
    return g