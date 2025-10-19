def p(g):
 s=sum(g,Z:=[]);w=len(g[k:=0])
 for v in s:Z+=[k][v:];0<v!=s[0]and(p:=k);k+=1
 q=max(Z,key=lambda z:abs(p-z)+abs(p%w-z%w)*3)
 for z in Z:
  while w>z%w+p%w-q%w>-1<(z:=z+p-q)<k:g[z//w][z%w]=s[p]
 return g