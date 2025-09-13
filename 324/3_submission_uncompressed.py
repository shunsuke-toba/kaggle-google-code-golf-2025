def p(g):
 f=sum(g,[]);c=f.count;a=f[c(f[0])<3];*s,=zip(*g);m={};e=enumerate
 for i,r in e(g):
  for j,d in e(r):
   if c(d)<3:s+=i+j,i-j<<6;m[a in r and a in s[j]]=d
 for i,r in e(g):
  for j,d in e(r):
   if i+j in s or i-j<<6 in s:r[j]=m[a in r and a in s[j]]
 return g