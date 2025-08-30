def p(g):
 s,e=map(sum(g,[]).index,(2,3));w=len(g[0])
 while(s:=s+((e%w>s%w)-(e%w<s%w)or(w,-w)[e<s]))-e:g[s//w][s%w]=8
 return g