p=lambda g:(t:=[a+[*b]for a,b in zip(g,zip(*g[::-1]))],t+[r[::-1]for r in t[::-1]])[1]
