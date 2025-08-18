def p(g):
 s=sum(g,[]);r,c=divmod(s.index(8),10);a=[-8]*4;C=8-c
 for q in range(100):a[(q//10>r)*2+(q%10>c)]+=s[q]
 z=[[0]*10];return z*r+[[0]*c+a[:2]+[0]*C,[0]*c+a[2:]+[0]*C]+z*(8-r)