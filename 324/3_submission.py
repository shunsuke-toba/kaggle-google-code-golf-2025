def p(g):
 f=sum(g,[]);c=f.count;a=f[c(f[0])<3];*h,=zip(*g);s=[];m={};e=enumerate
 for i,r in e(g):
  for j,d in e(r):
   if c(d)<3:s+=i+j,i-j-20;m[a in r and a in h[j]]=d
 return [[(d,m[a in r and a in h[j]])[i+j in s or i-j-20 in s]for j,d in e(r)]for i,r in e(g)]