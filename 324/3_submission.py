def p(g,R=range):
 h,w=len(g),len(g[0]);C=[0]*10
 for r in g:
  for t in r:C[t]+=1
 a,b=sorted(R(10),key=C.__getitem__)[-2:]
 D=[0]*10;F=set();S=set();T=set()
 for i in R(h):
  for j in R(w):
   if(q:=g[i][j])in(a,b):continue
   F.add(q);S.add(i+j);T.add(i-j)
   for x in R(i-1,i+2):
    for y in R(j-1,j+2):
     if(0<=x<h)*(0<=y<w)*(x+y-i-j):D[q]+=(g[x][y]==a)-(g[x][y]==b)
 p,q=F
 if D[q]>D[p]:a,b=b,a
 return [[(lambda d=g[i][j]:[p,q][d==b]if(d in(a,b))*((i+j in S)|(i-j in T))else d)()for j in R(w)]for i in R(h)]