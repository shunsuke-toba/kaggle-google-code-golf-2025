def p(g):
 i=sum(g,[]).index(2)
 s=[divmod(i,len(g[0]))]
 o=0
 while s:
  y,x=s.pop()
  if y|x<0:continue
  try:v=g[y][x];g[y][x]=0;v and(s.extend(((y-1,x),(y+1,x),(y,x-1),(y,x+1))),v<3 and(o:=o+1))
  except:0
 return[[[0]],[[8]]][o>4]
