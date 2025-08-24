def p(g):s=sum(g,[]);s=[max(s[k::3])for k in(0,1,2)]*5;return[s[i:i+7]for i in range(7)]
