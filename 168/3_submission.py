def p(g):
 h,w=len(g),len(g[0]);L=[]
 for y in range(h-1):
  for x in range(w-1):
   if 0 in(b:=g[y][x:x+2]+g[y+1][x:x+2])and sum(b)==3*(c:=max(b))>0:L+=c,y+(k:=b.index(0))//2*3-1,x+k%2*3-1,k//2*2-1,k%2*2-1
 while L:
  c,y,x,d,e,*L=L
  while-1<y<h>-1<x<w:g[y][x]=c;y+=d;x+=e
 return g
