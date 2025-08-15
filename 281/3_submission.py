def p(j):
 R=range;h=len(j);w=len(j[0]);u=h;v=-1;x=w;y=-1;b=c=-1
 for i in R(h):
  for k in R(w):
   if(q:=j[i][k]):
    if i<u:u=i
    if i>v:v=i
    if k<x:x=k
    if k>y:y=k
    if q-8:
     if b<0:b=q
     elif q-b:c=q
 for i in R(u,v+1):
  for k in R(x,y+1):j[i][k]=[c,b][i in(u,v)or k in(x,y)]
 return j
