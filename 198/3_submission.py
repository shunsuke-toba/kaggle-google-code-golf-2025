def p(g):
 R=range(h:=len(g));q=[(y,x)for y in R for x in R if sum(g[y]+[r[x]for r in g])*2>h*max(sum(g,[]))]
 for y,x in q:
  if 0<=y<h>x>=0==g[y][x]:g[y][x]=4;q+=(y+1,x),(y-1,x),(y,x+1),(y,x-1)
 return eval(str(g).replace("0","3"))