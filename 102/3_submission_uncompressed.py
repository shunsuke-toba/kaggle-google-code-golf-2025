def p(r):
 for o in range(11):
  for d in range(11):
   for u in range(11):
    if sum(sum(s[u:u+o+2])for s in r[d:d+o+2])-20*o-20==sum(sum(s[u+1:u+o+1])for s in r[d+1:d+o+1])==0:
     for s in r[d+1:d+o+1]:s[u+1:u+o+1]=[2]*o
 return r