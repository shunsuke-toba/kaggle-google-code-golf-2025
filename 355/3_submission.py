def p(g):
 c,h,w=min(f:=sum(g,[]),key=f.count),len(g),len(g[0]);r=[0]*h
 for k in range(h*w*9):
  if g[i:=k//w%h][j:=k%w]==c and (n:=[g[x][y]for x,y in((i-1,j),(i+1,j),(i,j-1),(i,j+1))if h>x>-1<y<w]).count(s:=max(n,key=n.count))>1:g[i][j]=s;r[s]+=1
 return[[r.index(max(r))]]
