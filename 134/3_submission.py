def p(g,R=range,E=enumerate):
 m={}
 for y,r in E(g):
  for x,v in E(r):
   if v:
    b=m.setdefault(v,[x,y,x,y]);b[0]=min(b[0],x);b[1]=min(b[1],y);b[2]=max(b[2],x);b[3]=max(b[3],y)
 s=min((k for k in m if m[k][2]-m[k][0]==m[k][3]-m[k][1]),key=lambda k:(m[k][2]-m[k][0])*(m[k][3]-m[k][1]));o=(set(m)-{s}).pop();a,b,c,d=m[s];x=-~(c-a)//3;y=-~(d-b)//3
 return[[o*all(g[Y][X]==s for Y in R(b+i*y,b+(i+1)*y)for X in R(a+j*x,a+(j+1)*x))for j in R(3)]for i in R(3)]
