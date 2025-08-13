def p(g):
 R,C=len(g),len(g[0]);c=[]
 for r in range(R):
  for j in range(C):
   if g[r][j]==4:c+=[(r,j)]
 mr,xr,mc,xc=min(r for r,j in c),max(r for r,j in c),min(j for r,j in c),max(j for r,j in c)
 pr,xpr,pc,xpc=R,-1,C,-1
 for r in range(R):
  for j in range(C):
   if g[r][j]!=0and not(mr<=r<=xr and mc<=j<=xc):pr,xpr,pc,xpc=min(pr,r),max(xpr,r),min(pc,j),max(xpc,j)
 A,S,P=0,1,None;s=[None]*5
 for k in[2,3,4]:
  s[k]=[[0]*((xpc-pc+1)*k)for _ in range((xpr-pr+1)*k)]
  for r in range(len(s[k])):
   for j in range(len(s[k][0])):s[k][r][j]=g[pr+r//k][pc+j//k]
  for r in range(mr,xr-len(s[k])+2):
   for j in range(mc,xc-len(s[k][0])+2):
    M,a=1,0
    for i in range(len(s[k])):
     for o in range(len(s[k][0])):
      if g[r+i][j+o]!=0:
       if g[r+i][j+o]!=s[k][i][o]:M=0
       a+=1
    if M and a>A:A,S,P=a,k,(r,j)
 r,j=P
 for i in range(len(s[S])):
  for o in range(len(s[S][0])):g[r+i][j+o]=s[S][i][o]
 return[[g[r][j]for j in range(mc,xc+1)]for r in range(mr,xr+1)]