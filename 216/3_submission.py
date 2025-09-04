def p(g,b=0):
 for n in range(400):
  a=[]
  while(s:=(g+[[]])[n//20][n%20:]+[0])[0]:a+=s[:s.index(0)],;n+=20
  if(r:=str(a).count('2'))>b:o=a;b=r
 return o