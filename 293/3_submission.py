def p(E):
 k=lambda E:[A[0]and[A[0]]*len(A)or A for A in E]
 return k(E)==E and[*map(list,zip(*k(zip(*E))))] or k(E)