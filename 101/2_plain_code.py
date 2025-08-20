def p(grid):
    n,m=len(grid),len(grid[0])
    x1,y1,x2,y2=99,99,0,0
    d=1,0,-1,0
    used=set()
    for b in range(9**5):
        i,j,k=b%97%n,b%89%m,b%4
        if grid[i][j]==1 or (grid[i][j]==2 and (0<=i+d[k]<n and 0<=j+d[k-3]<m and grid[i+d[k]][j+d[k-3]]==1 or (i+d[k],j+d[k-3]) in used)):
            x1=min(x1,i)
            y1=min(y1,j)
            x2=max(x2,i)
            y2=max(y2,j)
            if grid[i][j]==2:used.add((i,j))
    P=[r[y1:y2+1]for r in grid[x1:x2+1]]
    N=len(used)
    for s in [3,2,1]:
        P2=[[P[i//s][j//s] for j in range(len(P[0])*s)] for i in range(len(P)*s)]
        s1,s2=len(P2),len(P2[0])
        for b in range(n*m*9):
            i,j=b//(3*m)-n,b%(3*m)-m
            ok=True
            cnt2_cur=0
            for x in range(s1):
                for y in range(s2):
                    if 0<=i+x<n and 0<=j+y<m and not (i+x,j+y) in used:
                        if grid[i+x][j+y]!=P2[x][y]//2*2:
                            ok=False
                        elif P2[x][y]==2:
                            cnt2_cur+=1
            if ok and cnt2_cur==N*s*s:
                for x in range(s1):
                    for y in range(s2):
                        if 0<=i+x<n and 0<=j+y<m:
                            grid[i+x][j+y]=P2[x][y]
                            used.add((i+x,j+y))
    return grid