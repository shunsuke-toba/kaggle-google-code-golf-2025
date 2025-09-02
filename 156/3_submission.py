def p(g):
 T=[[],[]];A=[0,0];i=0
 for r in g:
  if s:=sum(r)>>2:T[i]+=r,;A[i]+=s
  elif A[i]:i=1
 for i in 0,1:
  for r in T[i][1:-1]:x=r.index(4);w=sum(r)>>2;r[x+1:x+w-1]=[1+(A[i]>A[~i])]*(w-2)
 return g