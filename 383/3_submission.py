def p(g,R=range):
 h=len(g);w=len(g[0]);b=d=0
 for k in R(h*w):
  if (v:=g[y:=k//w][x:=k%w]):b or(a:=y,c:=x,t:=v);b=y;d=x
 for y in R(a,b+1):
  for x in R(c,d+1):
   if(v:=g[y][x])-t:
    for i in R((y-1in(a,b-2))*h):g[i][x]=[v,t][a<=i<=b]
    for j in R((x-1in(c,d-2))*w):g[y][j]=[v,t][c<=j<=d]
 return g
