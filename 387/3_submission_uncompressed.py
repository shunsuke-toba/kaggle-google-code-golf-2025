def p(g):
 (a,c,e),(a,d,f),(b,c,_),(b,d,_)=p=[(i,j,v)for i,r in enumerate(g)for j,v in enumerate(r)if v]
 for i in range(a,b+1):g[i][c]=g[i][d]=min(i-a,b-i)%2*-5+5
 for i in range(c,d+1):g[a][i]=g[b][i]=min(i-c,d-i)%2*-5+5
 for i,j,v in p:g[i][j-1:j+2]=g[i-1][j-1:j+2]=g[i+1][j-1:j+2]=[e^f^v]*3;g[i][j]=v
 return g