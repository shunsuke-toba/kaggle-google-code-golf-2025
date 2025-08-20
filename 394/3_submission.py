def p(g):
 w=len(g[0]);r=range;p=[divmod(i,w)for i in r(len(g)*w)];z=[(i,j)for i,j in p if g[i][j]<1];a,b,c,d=z[0]+z[-1];R=C=1
 while any((g[i][j]-g[i%R][j])*g[i][j]*g[i%R][j]for i,j in p):R+=1
 while any((g[i][j]-g[i][j%C])*g[i][j]*g[i][j%C]for i,j in p):C+=1
 t={(i%R,j%C):k for i,j in p if(k:=g[i][j])}
 return[[t[i%R,j%C]for j in r(b,d+1)]for i in r(a,c+1)]
