def p(g):
 s=b'\0\2\0\4\6\3\0\1\0';k=0
 for r in g:
  k+=r[0]>7;l=0
  for j,x in enumerate(r):r[j]=x or s[k*3+l];l+=x>7
 return g