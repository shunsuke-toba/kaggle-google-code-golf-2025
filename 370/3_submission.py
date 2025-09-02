def p(g):
 w=len(g[k:=0]);Z=[]
 for v in sum(g,[]):
  if v<1:Z+=k,
  elif v-g[0][0]:p=k;d=v
  k+=1
 q=max(Z,key=lambda z:(p//w-z//w)**2*w+(p%w-z%w)**2)
 t=p-q;x=p%w-q%w
 for z in Z:
  c=z%w
  while len(g)>(z:=z+t)//w>=0<=(c:=c+x)<w:g[z//w][c]=d
 return g