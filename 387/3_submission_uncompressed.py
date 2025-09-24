def p(g):
 (y,x,a),(y,X,b),(Y,x,_),(Y,X,_)=p=[(i,j,v)for i,r in enumerate(g)for j,v in enumerate(r)if v]
 for i in range(x,X+1):g[y][i]=g[Y][i]=(min(i-x,X-i)&1^1)*5
 for i in range(y,Y+1):g[i][x]=g[i][X]=(min(i-y,Y-i)&1^1)*5
 for i,j,v in p:g[i-1][j-1:j+2]=g[i][j-1:j+2]=g[i+1][j-1:j+2]=[a^b^v]*3
 for i,j,v in p:g[i][j]=v
 return g
