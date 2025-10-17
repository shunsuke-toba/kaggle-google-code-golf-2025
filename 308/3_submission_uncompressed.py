def p(s):
 p=~-len(s)//5;o=p+-~p;o=[[b:=max(s[0],key=s[0].count)]*o for j in[0]*o];t=[0]*20
 for x,h in enumerate(s):
  for j,h in enumerate(h):
   if h^b:t[h]+=x;t[~h]+=j
 for x,h in enumerate(s):
  for j,h in enumerate(h):
   if h^b:o[p+x-t[h]//4][p+j-t[~h]//4]=h
 return o