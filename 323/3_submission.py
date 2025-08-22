def p(g):
 i=sum(g,[]).index(8)
 for s in-1,1:
  x,y=i//13,i%13
  for t in range(24):
   x-=s*(t&2<1);y+=s*(t&2>0)
   if 13>x>-1<y<13:g[x][y]=5
   else:break
 return g