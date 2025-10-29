def p(t):
 for f in range(19):
  for n in range(19):
   if all(sum(t[f+c][n+j]for j in range(3))for c in range(3))and all(sum(t[f+c][n+j]for c in range(3))for j in range(3)):
    for r in range(3):
     for l in range(3):
      a,s=f,n
      for c in range(3):
       for j in range(3):
        a+=r*4-4;s+=l*4-4
        for c in range(3):
         for j in range(3):
          if t[f+c][n+j]and-1<a+c<21and-1<s+j<21:t[a+c][s+j]=max(t[f+r*4-4+c][n+l*4-4+j]for c in range(3)for j in range(3))
    return t