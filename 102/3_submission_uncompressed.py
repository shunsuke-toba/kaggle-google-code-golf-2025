def p(b):
 for q in range(11):
  for o in range(11):
   for p in range(11):
    if sum(sum(s[p:p+q+2])for s in b[o:o+q+2])-20*q-20==sum(sum(s[p+1:p+q+1])for s in b[o+1:o+q+1])==0:
     for s in b[o+1:o+q+1]:s[p+1:p+q+1]=[2]*q
 return b