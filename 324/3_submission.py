def p(g):
 f=sum(g,[]);a=max(g[0][:2]+g[1][:2],key=f.count);b=max({*f}-{a},key=f.count);s=[];m={};e=enumerate
 for i,r in e(g):
  for j,d in e(r):
   if(d^a)*(d^b):s+=i+j,60+i-j;m[(b,a)[a in r and a in[t[j]for t in g]]]=d
 return [[(d,m.get(d,d))[i+j in s or 60+i-j in s]for j,d in e(r)]for i,r in e(g)]
