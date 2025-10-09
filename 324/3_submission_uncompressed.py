def p(g):
 e=sum(g,[]);c=e.count;a=e[c(e[0])<3];*s,=zip(*g);t={}
 for i,r in enumerate(g):
  for j,d in enumerate(r):
   if c(d)<3:s+=i+j,i-j-60;t[a in r and a in s[j]]=d
 for i,r in enumerate(g):
  for j,d in enumerate(r):
   if i+j in s or i-j-60 in s:r[j]=t[a in r and a in s[j]]
 return g