def p(s,l=range,n=0):
 while 0in s[n]:n+=1
 g=n+1;m=len(s)//g+1;i=max(([s[g*(f+u//3-1)][g*(x+u%3-1)]for u in l(9)]for f in l(1,m-1)for x in l(1,m-1)),key=sum)
 for f in l(m):
  for x in l(m):
   for u in l(9):
    for r in l(n*n*(m>=f+u//3>0)*(m>=x+u%3>0)*(i[4]==s[g*f][g*x])):s[g*(f+u//3-1)+r//n][g*(x+u%3-1)+r%n]=i[u]
 return s