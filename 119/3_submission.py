def p(g,c=0):
 while g[6][0]!=2:g=[*map(list,zip(*g[::-1]))];c+=1
 f=8 in g[-1]
 if f:g=g[::-1]
 w,s=g[0].count(2),g[0].index(8)
 for i in range(12):j=abs(s-i-w)+w;g[i][j]=g[i][j]or 3
 if f:g=g[::-1]
 while c%4:g=[*map(list,zip(*g[::-1]))];c+=1
 return g
