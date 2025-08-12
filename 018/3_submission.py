def p(g):
 h=len(g);w=len(g[0])
 v=set();S=[]
 for r in range(h):
  for c in range(w):
   if g[r][c]and(r,c)not in v:
    q=[(r,c)];v.add((r,c));i=0;C=[];d={};m={}
    while i<len(q):
     y,x=q[i];i+=1;t=g[y][x];C+=[(y,x,t)];d[t]=d.get(t,0)+1;m.setdefault(t,[]).append((y,x))
     for Y,X in((y+1,x),(y-1,x),(y,x+1),(y,x-1)):
      if 0<=Y<h and 0<=X<w and g[Y][X]and(Y,X)not in v:v.add((Y,X));q.append((Y,X))
    if len(d)>=4:
     L=[k for k in d if d[k]==1]
     if len(L)==3:
      W=max(d,key=d.get);A={k:m[k][0]for k in L};Z=[(y,x)for y,x,t in C if t==W];S+=[(W,L,A,Z,C)]
 o=[r[:]for r in g]
 if not S:return o
 T=lambda x,y:[(x,y),(-y,x),(-x,-y),(y,-x),(x,-y),(y,x),(-x,y),(-y,-x)]
 sc=set()
 for W,L,A,Z,C in S:
  for y,x,t in C:sc.add((y,x));o[y][x]=0
 for W,L,A,Z,C in S:
  a,b,e=L;ar,ac=A[a];br,bc=A[b];cr,cc=A[e]
  vab=(br-ar,bc-ac);vac=(cr-ar,cc-ac)
  PA=[(r,c)for r in range(h)for c in range(w)if g[r][c]==a and(r,c)not in sc]
  PB=[(r,c)for r in range(h)for c in range(w)if g[r][c]==b and(r,c)not in sc]
  PC=[(r,c)for r in range(h)for c in range(w)if g[r][c]==e and(r,c)not in sc]
  for ta in PA:
   for tb in PB:
    for tc in PC:
     if ta==tb or ta==tc or tb==tc:continue
     dab=(tb[0]-ta[0],tb[1]-ta[1]);dac=(tc[0]-ta[0],tc[1]-ta[1])
     tv=T(*vab);tu=T(*vac);k=-1
     for i in range(8):
      if tv[i]==dab and tu[i]==dac:k=i;break
     if k<0:continue
     for yr,xc in Z:
      dr,dc=T(yr-ar,xc-ac)[k];R=ta[0]+dr;C=ta[1]+dc
      if 0<=R<h and 0<=C<w and(o[R][C]==0)and(R,C)!=ta and(R,C)!=tb and(R,C)!=tc:o[R][C]=W
 return o
