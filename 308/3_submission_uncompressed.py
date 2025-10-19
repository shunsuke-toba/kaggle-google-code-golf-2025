def p(n):
 m=~-len(n)//5;o=m+-~m;o=[[g:=max(n[0],key=n[0].count)]*o for j in[0]*o];e=[0]*20
 for w,f in enumerate(n):
  for j,f in enumerate(f):
   if f^g:e[f]+=w;e[~f]+=j
 for w,f in enumerate(n):
  for j,f in enumerate(f):
   if f^g:o[m+w-e[f]//4][m+j-e[~f]//4]=f
 return o