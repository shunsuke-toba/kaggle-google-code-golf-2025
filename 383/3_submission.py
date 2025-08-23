def p(g,R=range):
 h=len(g);w=len(g[0]);b=0;L=[]
 for k in R(h*w):
  if (v:=g[y:=k//w][x:=k%w]):L+=[(y,x,v)];b or(a:=y,c:=x,t:=v);b=y;d=x
 for y,x,v in L:
  if v-t:
   for i in R((y-1in(a,b-2))*h):g[i][x]=[v,t][a<=i<=b]
   for j in R((x-1in(c,d-2))*w):g[y][j]=[v,t][c<=j<=d]
 return g
