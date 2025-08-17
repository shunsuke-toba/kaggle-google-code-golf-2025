def p(g,R=range,E=enumerate):
 m={}
 for y,r in E(g):
  for x,v in E(r):
   if v:b=m.setdefault(v,[x,y,x,y]);b[:]=min(b[0],x),min(b[1],y),max(b[2],x),max(b[3],y)
 s,o=sorted(m,key=lambda k:((b:=m[k])[2]-b[0]!=b[3]-b[1],(b[2]-b[0])*(b[3]-b[1])))
 a,b,c,d=m[s];x=-~(c-a)//3
 return[[o*all(g[b+i*x+Y][a+j*x+X]==s for Y in R(x)for X in R(x))for j in R(3)]for i in R(3)]
