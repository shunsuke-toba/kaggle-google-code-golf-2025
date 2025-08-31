def p(g):
 g=[[*map(max,a,b[::-1],a[::-1],b)]for a,b in zip(g,g[::-1])]
 for i in 1,3,5:k=i;exec('g[i][k:=k+2]=g[~i][k]=g[k][i]=g[k][~i]=g[i][i+2];'*(8-i))
 return g