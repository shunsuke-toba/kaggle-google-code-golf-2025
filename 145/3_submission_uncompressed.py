def p(i):
 n=[]
 def p(r,d):
  if len(i)>r>~0<d<len(i[0])>i[r][d]==0:i[r][d]=~len(n);n[-1]+=1;p(r+1,d);p(r-1,d);p(r,d+1);p(r,d-1)
 for d in range(len(i[0])):
  for r in range(len(i)):
   if len(i)>r>~0<d<len(i[0])>i[r][d]==0:n+=0,;p(r,d)
 for d in range(len(i[0])):
  for r in range(len(i)):
   if len(i)>r>~0<d<len(i[0])>i[r][d]<1:i[r][d]=(n[-i[r][d]-2]==max(n))+((n[-i[r][d]-2]==min(n))<<3)
 return i