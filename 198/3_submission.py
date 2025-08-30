def p(g):
 h=len(g);q=[(n//h,n%h)for n in range(h*h)if sum(g[n//h]+[r[n%h]for r in g])*2>h*max(g)[0]]
 for y,x in q:
  if 0<=y<h>x>=0==g[y][x]:g[y][x]=4;q+=(y+1,x),(y-1,x),(y,x+1),(y,x-1)
 return eval(str(g).replace(*"03"))