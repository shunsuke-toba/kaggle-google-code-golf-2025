def p(g):
 def f(n):s=(g+[[]])[n//20][n%20:]+[0];return s[0]and[s[:s.index(0)]]+f(n+20)or[]
 return max(map(f,range(400)),key=lambda a:str(a).count('2'))