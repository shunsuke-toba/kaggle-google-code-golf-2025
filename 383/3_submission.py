def p(g):
 R=range;h=len(g);w=len(g[0]);a=h;c=w;b=d=0
 for k in R(h*w):
  if g[y:=k//w][x:=k%w]:a=min(a,y);b=max(b,y);c=min(c,x);d=max(d,x)
 t=g[a][c]
 for y in R(a,b+1):
  for x in R(c,d+1):
   if(v:=g[y][x])-t:
    for i in R((y<a+2or y>b-2)*h):g[i][x]=[v,t][a<=i<=b]
    for j in R((x<c+2or x>d-2)*w):g[y][j]=[v,t][c<=j<=d]
 return g
