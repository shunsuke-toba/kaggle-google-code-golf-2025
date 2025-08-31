def p(g):
 h=len(g);q=[n for n in range(h*h)if sum(g[n//h]+[r[n%h]for r in g])*2>h*max(g)[0]]
 for n in q:
  y=n//h;x=n%h
  if 0<=y<h>x>=0==g[y][x]:g[y][x]=4;q+=n+h,n-h,n+(x<h-1),n-(x>0)
 return eval(str(g).replace(*"03"))