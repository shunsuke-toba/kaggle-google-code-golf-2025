def p(j,A=range(18)):
 for c in A:
  E,k,W=j[c:c+3]
  for l in A:
   s=l+3
   if sum(E[l:s]+k[l:s]+W[l:s])<1:E[l:s]=k[l:s]=W[l:s]=3*[1]
 return j