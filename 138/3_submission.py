def p(g):
 f=lambda x:[i for i,s in enumerate(x)if min(s)];x,y=f(zip(*g));u,v=f(g);g=[r[x:y+1]for r in g[u:v+1]];h=len(g)-1;w=len(g[0])-1
 for i in range(1,h):
  for j in range(1,w):
   c=g[i][j];d=(c==g[-1][1])-(c==g[0][1]);e=(c==g[1][-1])-(c==g[1][0]);I,J=i,j
   while(d|e)&(0<I+d<h)&(0<J+e<w):g[I:=I+d][J:=J+e]=c
 return g
