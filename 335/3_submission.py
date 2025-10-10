def p(g):
 s,e=map(sum(g,[]).index,(8,2));w=len(g[0])
 while(s:=s+(-1,1)[e>s]*(w,1)[not e//w-s//w])-e:g[s//w][s%w]=4
 return g