def p(g):
 f,r=sum(g,[]),{};c,h,w=min(set(f),key=f.count),len(g),len(g[0])
 for k in range(9*h*w):
  i,j=k//w%h,k%w
  if g[i][j]==c and(n:=[g[i+a][j+b]for a,b in[(-1,0),(1,0),(0,-1),(0,1)]if h>i+a>-1<j+b<w>c!=g[i+a][j+b]])and n.count(s:=max(set(n),key=n.count))>1:g[i][j]=s;r[s]=r.get(s,0)+1
 return[[max(r,key=r.get)if r else c]]
