from random import sample
from queue import deque

#Traversal -- i'm not sure why dict instead of set for P
def walk (G, s):
    P, Q = dict(), set()
    P[s] = None
    Q.add(s)
    while Q:
        u = Q.pop()
        for v in G[u].difference(P):
            Q.add(v)
            P[v] = u
    return P

#Depth first search
def dfs(G,s, S=None,target = None):
    if S is None: S = set()
    S.add(s)
    for u in G[s]:
        if u in S: continue
        dfs(G,u,S,s)
    return S

#BFS traversal, pretty much same as before
def bfs(G,s):
    P, Q = set(), deque(s)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v in P: continue
            Q.append(v)
            P.add(v)
    return P

#Quicksort using list comprehensions
def qsort(list):
    if list == []: return []
    else:
        pivot = list[0]
        lesser = qsort([x for x in list[1:] if x < pivot])
        greater = qsort([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater

def iddfs(G, s):
    yielded = set() # Visited for the first time
    def recurse(G, s, d, S=None): # Depth-limited DFS
        if s not in yielded:
            yield s
            yielded.add(s)
        if d == 0: return # Max depth zero: Backtrack
        if S is None:
            S = set()
            S.add(s)
            for u in G[s]:
                if u in S: continue
                for v in recurse(G, u, d-1, S): # Recurse with depth-1
                    yield v
    n = len(G)
    for d in range(n): # Try all depths 0..V-1
        if len(yielded) == n: break # All nodes seen?
        for u in recurse(G, s, d):
            yield u

bratislav = {'a' :  {'b','c','d' }, 'b' : {'a', 'c','x' }, 'c' : {'a', 'b'} ,'d' : {'a'}, 'x' : {'b', 'y'}, 'y' : {'x', 'z'}, 'z': {'x'} }
vr = bfs (bratislav,'a')
print(vr)
unsrtd = sample(range(100),12)
sorted = qsort(unsrtd)
var = walk(bratislav,'a')
var2 = dfs (bratislav,'z')
print (var)
