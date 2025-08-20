def p(g):
 r=sum(map(any,c:=list(zip(*g))));n=1
 while(c[:n]*9)[:r]!=c[:r]:n+=1
 return[*map(list,zip(*(c[:n]*15)[:15]))]