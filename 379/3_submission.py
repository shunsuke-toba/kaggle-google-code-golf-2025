def p(g):
 for _ in g*4:
  for i,b in enumerate(g):
   try:1/(b[j:=len(b)-b[::-1].index(2)]<1);k=b.index(8,j);b[j-1:k+2]=[2]*(k-j)+[8,2,8];g[i-1][k-1:k+2]=g[i+1][k-1:k+2]=[8]*3
   except:0
  g=[*map(list,zip(*g[::-1]))]
 return g