def p(g):
 while 2in(f:=sum(g,[])):
  a=f.index(2);d,e=(f[a+9]<1)*18-9,f[a+1]<1or-1
  for s in a,a+d,a+e:
   while 81>s>=s%9!=e&8:g[s//9][s%9]=sum({*f})-2;s+=d+e
 return g