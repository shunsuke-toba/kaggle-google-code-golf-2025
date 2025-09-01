def p(g):
 f=sum(g,[]);b=g[0][1]==g[1][0];a=g[0][b];*c,=zip(*g);s=[];m={};e=enumerate
 for i,r in e(g):
  for j,d in e(r):
   if f.count(d)<3:s+=i+j,i-j-20;m[a in r and a in c[j]]=d
 return [[(d,m[a in r and a in c[j]])[i+j in s or i-j-20 in s]for j,d in e(r)]for i,r in e(g)]