def p(g):
    h,w=len(g),len(g[0])
    for i in range(h):
        for j in range(w):
            if g[i][j]==5:
                st=[(i,j)]; g[i][j]=0; comp=[]
                while st:
                    x,y=st.pop(); comp.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and g[nx][ny]==5:
                            g[nx][ny]=0; st.append((nx,ny))
                c=2 if len(comp)==6 else 1
                for x,y in comp: g[x][y]=c
    return g