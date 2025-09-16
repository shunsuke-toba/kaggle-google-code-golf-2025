def p(g):
 while 2in(f:=sum(g,[])):
  a=f.index(2);d,e=f[a+9]<1or-1,f[a+1]<1or-1
  for s in a,a+d*9,a+e:
   while 81>s>-1<s%9-e<9:g[s//9][s%9]=sum({*f})-2;s+=d*9+e
 return g