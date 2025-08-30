def p(g):
 f=sum(g,[]);q=f.count;a=max(f[:2]+g[1][:1],key=q);*c,=zip(*g);s=[];m={};e=enumerate
 for i,r in e(g):
  for j,d in e(r):
   if q(d)<3:s+=i+j,58+i-j;m[a in r and a in c[j]]=d
 return [[(d,m[a in r and a in c[j]])[i+j in s or 58+i-j in s]for j,d in e(r)]for i,r in e(g)]