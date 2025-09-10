def p(g):
 f=sum(g,[]);c=f.count;a=f[c(f[0])<3];*s,=zip(*g);m={};e=enumerate
 for i,r in e(g):
  for j,d in e(r):
   if c(d)<3:s+=i+j,(i-j,);m[a in r and a in s[j]]=d
 return [[(d,m[a in r and a in s[j]])[i+j in s or(i-j,)in s]for j,d in e(r)]for i,r in e(g)]