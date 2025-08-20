def p(g):c=__import__('collections').Counter(sum(g,[])).most_common();return[[k*(v>i)for k,v in c]for i in range(c[0][1])]
