def p(g):
 h=len(g);w=len(g[0]);R=range;I=int;C=complex.conjugate
 u=set();S=[];o=[r[:]for r in g];sc=set()
 for r in R(h):
  for c in R(w):
   z=r+c*1j
   if g[r][c]and z not in u:
    q=[z];u.add(z);D=[];d={};p={}
    for z in q:
     y,x=I(z.real),I(z.imag);t=g[y][x];D+=[(z,t)];d[t]=d.get(t,0)+1;p[t]=z
     for d4 in 1,-1,1j,-1j:
      n=z+d4;Y,X=I(n.real),I(n.imag)
      if 0<=Y<h and 0<=X<w and g[Y][X]and n not in u:u.add(n);q.append(n)
    if len(d)>=4:
     L=[k for k in d if d[k]==1]
     if len(L)==3:
      a,b,c=L;f=max(d,key=d.get);za=p[a];S+=[(a,b,c,f,p[b]-za,p[c]-za,[z-za for z,t in D if t==f])]
      for z,t in D:o[I(z.real)][I(z.imag)]=0;sc.add(z)
 for a,b,c,f,B,v,Z in S:
  P=[[r+c*1j for r in R(h)for c in R(w)if g[r][c]==x and r+c*1j not in sc]for x in(a,b,c)]
  for ta in P[0]:
   for tb in P[1]:
    for tc in P[2]:
     if len({ta,tb,tc})<3:continue
     dab=tb-ta;dac=tc-ta
     for s0 in 1,1j,-1,-1j:
      for m in 0,1:
       if dab==(C(B) if m else B)*s0 and dac==(C(v) if m else v)*s0:
        for dz in Z:
         dz=C(dz) if m else dz
         nz=ta+dz*s0;Y,X=I(nz.real),I(nz.imag)
         if 0<=Y<h and 0<=X<w and o[Y][X]==0 and nz not in(ta,tb,tc):o[Y][X]=f
 return o
