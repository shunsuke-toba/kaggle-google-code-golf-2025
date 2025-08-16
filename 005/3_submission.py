def p(g):
 h=len(g);w=len(g[0]);R=range(3);r=c=0
 while not all(map(any,(P:=[g[r+i][c:c+3]for i in R])+list(zip(*P)))):
  c+=1
  if c>w-3:c=0;r+=1
 for Y in-1,0,1:
  for X in-1,0,1:
   if X|Y and-1<(y:=r+4*Y)<h-2and-1<(x:=c+4*X)<w-2:
    t=max(g[y+i][x+j]for i in R for j in R);s=0
    while t:
     s+=1;yy=r+4*Y*s;xx=c+4*X*s
     for i in R:
      for j in R:
       if 0<=yy+i<h and 0<=xx+j<w and P[i][j]:g[yy+i][xx+j]=t
     if not(-1<yy<h-2and-1<xx<w-2):break
 return g
