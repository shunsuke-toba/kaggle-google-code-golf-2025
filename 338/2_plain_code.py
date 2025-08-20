from collections import deque

def p(g):
 # fill all 0-regions reachable from the outer border (without crossing 2)
 h,w=len(g),len(g[0])
 vis=[[False]*w for _ in range(h)]
 q=deque()
 for i in range(h):
  for j in (0,w-1):
   if g[i][j]!=2 and not vis[i][j]: vis[i][j]=1; q.append((i,j))
 for j in range(w):
  for i in (0,h-1):
   if g[i][j]!=2 and not vis[i][j]: vis[i][j]=1; q.append((i,j))
 while q:
  i,j=q.popleft()
  for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
   ni,nj=i+di,j+dj
   if 0<=ni<h and 0<=nj<w and not vis[ni][nj] and g[ni][nj]!=2:
    vis[ni][nj]=1; q.append((ni,nj))
 # interior (unvisited) zeros -> 3, borders (2) -> 0
 out=[]
 for i in range(h):
  r=[]
  for j in range(w):
   v=g[i][j]
   r.append(0 if v==2 else 3 if v==0 and not vis[i][j] else v)
  out.append(r)
 return out