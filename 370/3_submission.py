def p(g):
 w=len(g[k:=0])
 for v in sum(g,Z:=[]):Z+=[k][v:];v*(v-g[0][0])and(p:=k,d:=v);k+=1
 q=max(Z,key=lambda z:abs(p-z)//w+abs(p%w-z%w))
 for z in Z:
  while w>(z%w+p%w-q%w)>-1<(z:=z+p-q)<k:g[z//w][z%w]=d
 return g