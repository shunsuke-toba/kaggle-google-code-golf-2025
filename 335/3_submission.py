def p(g):
 s,e=map(sum(g,[]).index,(2,8));w=len(g[0])
 while(s:=s+((e%w>s%w)-(e%w<s%w)or(w,-w)[e<s]))-e:g[s//w][s%w]=4
 return g