p=lambda g,e=enumerate:[[v<2 and any(2in s[j-1+(j<1):j+2]for s in g[i-1+(i<1):i+2]) or v for j,v in e(r)]for i,r in e(g)]
