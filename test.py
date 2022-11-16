# 

# l = [(6,'A','B'), (3,'A','C'), (2,'C','D'), (7,'C','F'), (2,'E','F'), (10,'D','F')]

pop 'A'
usedNodes = ['A']
[(3,'A','C'), (6,'A','B')]

pop 'C'
usedNodes = ['A', 'C']
[(2, 'C','D'), (7,'C','F'),(6,'A','B')]

pop 'D'
usedNodes = ['A', 'C', 'D']
[(2, 'D','E'), (7,'C','F'),(6,'A','B')]

pop 'E'
usedNodes = ['A', 'C', 'D', 'E']
[(2,'E','F'),(4,'E','G'),(6,'A','B'),(8,'E','H')]

pop 'F'
usedNodes = ['A', 'C', 'D', 'E', 'F']
[(4,'E','G'),(6,'A','B'),(8,'E','H')]

pop 'G'
usedNodes = ['A', 'C', 'D', 'E', 'F', 'G']
[(6,'A','B'),(6,'G','H')]

pop 'B'
usedNodes = ['A', 'C', 'D', 'E', 'F', 'G', 'B']
[(6,'G','H')]

pop 'H'
usedNodes = ['A', 'C', 'D', 'E', 'F', 'G', 'B', 'H']
[]


for tup in l:
    # if t[1] == tup[2] and t[2] == tup[1]:

    if t[2] == tup[2] and t[0] < tup[0]:
        l.remove(tup)
        l.append(t)



l.sort()
print(l)
