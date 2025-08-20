def p(g):
 d={}
 for i in range(10):
  for j in range(10):
   if(v:=g[i][j]):d.setdefault(v,[]).append((i,j))
 a=[]
 for k,v in d.items():
  I,J=zip(*v);i=min(I);j=min(J);h=max(I)-i+1;w=max(J)-j+1;m=sum(1<<(I-i)*3+J-j for I,J in v)
  a.append((k,[m<<(3*y+x)for y in range(4-h)for x in range(4-w)]))
 (c1,p1),(c2,p2)=a
 t=max(((A,B)for A in p1 for B in p2 if A&B<1),key=lambda x:(x[0]|x[1]).bit_count())
 return [[(t[0]>>3*y+x&1)*c1+(t[1]>>3*y+x&1)*c2 for x in range(3)]for y in range(3)]
