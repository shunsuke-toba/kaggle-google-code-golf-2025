def p(g):
 while(b:=g[:3])==[*map(list,zip(*b))]:g=g[3:]
 return b
