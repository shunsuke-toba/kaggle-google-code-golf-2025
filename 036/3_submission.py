def p(g,E=enumerate):
 m={}
 for y,r in E(g):
  for x,v in E(r):
   t=m.setdefault(v,[99,0,99,0]);t[0]=min(t[0],x);t[1]=max(t[1],x+1);t[2]=min(t[2],y);t[3]=max(t[3],y+1)
 a,b,c,d=min(m.values(),key=lambda t:(t[1]-t[0])*(t[3]-t[2]));return[r[a:b]for r in g[c:d]]
