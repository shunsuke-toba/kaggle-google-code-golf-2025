def p(g):
 h,w=len(g),len(g[0]);C=set(sum(g,[]))-{0};P=B=0
 for c in C:
  L=[(i,j)for i in range(h)for j in range(w)if g[i][j]==c]
  if L:
   a,b,d,e=min(x[0]for x in L),min(x[1]for x in L),max(x[0]for x in L),max(x[1]for x in L)
   if all(g[r][x]==c for r in range(a,-~d)for x in range(b,-~e)):B=(a,b,d,e)
   else:P=c
 if not P:return g
 O=[[P*(g[i][j]==P)for j in range(w)]for i in range(h)]
 if B:
  a,b,d,e=B
  for i in range(h):
   if i<a or i>d:
    L=[j for j in range(w)if g[i][j]==P]
    if L:
     m=(min(L)+max(L))/2
     for k in range(h*w):r,c=k//w,k%w;O[r][c]==P and 0<=int(2*m-c)<w and exec("O[r][int(2*m-c)]=P")
     return O
 L=[j for k in range(h*w)if g[k//w][k%w]==P for j in[k%w]]
 if L:
  m=(min(L)+max(L))/2
  for k in range(h*w):i,j=k//w,k%w;O[i][j]==P and 0<=int(2*m-j)<w and exec("O[i][int(2*m-j)]=P")
 return O
