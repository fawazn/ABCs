__author__ = 'fahmed'
import itertools
from collections import namedtuple

def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

#knapsack problem
weight = [0, 5, 4, 6, 3]; profit = [0, 10, 40, 30, 50]

def b(i,W):
    if i is 0 or W is 0: return 0
    return b(i-1, W) if weight[i] > W else max(b(i-1, W), b(i-1, W-weight[i]) + profit[i])

#coinchange problem
v = [1,3,10,21]
@memo
def c(p):
    return 0 if p <= 0 else min([c(p-vv) for vv in v]) + 1

#shortest path in a DAG
dag = {'a': {'f': 9, 'b': 2}, 'b': {'d': 2, 'c': 1, 'f': 6}, 'c': {'d': 7}, 'd': {'f': 3, 'e': 2}, 'e': {'f': 4}}
def minDAG(G,s,t):
    return 0 if s == t else min([G[s][v] + minDAG(G,v,t) for v in G[s]])

#insert
def insert(a,L):
    return L.insert(0,a) if a>L[0] else [L[0]] + insert(a,L[0:])
def insertion_sort(L):
    pass
    # reduce(insert(L),[])

#dijkstra minimum distance a -> f
wtList = {v:float('inf') for v in dag}
wtList.update({'f': float('inf')})
wtList['a'] = 0
def dij(i,end):
    if i is end: return wtList['f']
    for vrtx in dag[i]:
        if wtList[vrtx] > dag[i][vrtx] + wtList[i]:
            wtList[vrtx] = dag[i][vrtx] + wtList[i]
    d = {k:wtList[k] for k in dag[i].keys()}
    return dij(min(d, key=d.get), end)

def breadth_first(tree, children=iter): #Corecursive generator
    yield tree
    # last = tree
    for node in breadth_first(tree, children):
        for child in children(node):
            yield child
            # last = child
        # if last == node:
        #     return

def bfs(root,visitable,children=iter):
    queue = []
    # makes a shallow copy, makes it a collection, removes duplicates
    unvisited = list(set(visitable))

    if root in unvisited:
        unvisited.remove(root)
        queue.append(root)

    while len(queue) > 0:
        node = queue.pop(0)
        yield node

        for child in children(node):
            if child in unvisited:
                unvisited.remove(child)
                queue.append(child)
    return



#String ---------------------------------

def string_matching_rabin_karp(text='', pattern='', hash_base=256):
    """
Returns positions where pattern is found in text

We calculate the hash value of the pattern and we compare it to the hash
value of text[i:i+m] for i = 0..n-m
The nice thing is that we don't need to calculate the hash value of
text[i:i+m] each time from scratch, we know that:
h(text[i+1:i+m+1]) = (base * (h(text[i:i+m]) - (text[i] * (base ^ (m-1))))) + text[i+m]
We can get h('bcd') from h('abc').
h('bcd') = (base * (h('abc') - ('a' * (base ^ 2)))) + 'd'
worst case: O(nm)
we can expect O(n+m) if the number of valid matches is small and the pattern
large
Performance: ord() is slow so we shouldn't use it here

Example: text = 'ababbababa', pattern = 'aba'
string_matching_rabin_karp(text, pattern) returns [0, 5, 7]
@param text text to search inside
@param pattern string to search for
@param hash_base base to calculate the hash value
@return list containing offsets (shifts) where pattern is found inside text
"""

    n = len(text)
    m = len(pattern)
    offsets = []
    htext = hash_value(text[:m], hash_base)
    hpattern = hash_value(pattern, hash_base)
    for i in range(n-m+1):
        if htext == hpattern:
            if text[i:i+m] == pattern:
                offsets.append(i)
        if i < n-m:
            htext = (hash_base * (htext - (ord(text[i]) * (hash_base ** (m-1))))) + ord(text[i+m])

    return offsets


def hash_value(s, base):
    """
Calculate the hash value of a string using base

Example: 'abc' = 97 x base^2 + 98 x base^1 + 99 x base^0
@param s string to compute hash value for
@param base base to use to compute hash value
@return hash value
"""
    v = 0
    p = len(s)-1
    for i in range(p+1):
        v += ord(s[i]) * (base ** p)
        p -= 1

    return v

#Buildings with view of sunset
def sunsetView():
    b = [0]
    while True:
        newBldg = yield
        yield b
        if b[-1]<newBldg:
            b.append(newBldg)

sunset_eg = [12,3,25,32,14,1,23]
g = sunsetView()
g.send(None)
for i in sunset_eg:
    r = g.send(i)

graph_eg = ['a','b','c']


#Hanoi
def hanoi(n, source, helper, target):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        if source:
            target.append(source.pop())
            # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target)

Source, Target, Helper = [4,3,2,1], [], []
hanoi(len(Source), Source, Helper, Target)

#Tree traversal algorithms ---------------------------------------------------------------------------

Node = namedtuple('Node', 'data, left, right')
tree = Node(1,
            Node(2,
                 Node(4,
                      Node(7, None, None),
                      None),
                 Node(5, None, None)),
            Node(3,
                 Node(6,
                      Node(8, None, None),
                      Node(9, None, None)),
                 None))
#DFS
def preorder(node, visitor = print):
    if node is not None:
        visitor(node.data)
        preorder(node.left, visitor)
        preorder(node.right, visitor)

def inorder(node, visitor = print):
    if node is not None:
        inorder(node.left, visitor)
        visitor(node.data)
        inorder(node.right, visitor)

def postorder(node, visitor = print):
    if node is not None:
        postorder(node.left, visitor)
        postorder(node.right, visitor)
        visitor(node.data)

#BFS
def levelorder(node, more=None, visitor = print):
    if node is not None:
        if more is None:
            more = []
        more += [node.left, node.right]
        visitor(node.data)
    if more:
        levelorder(more[0], more[1:], visitor)

print('Level Traversal:')
levelorder (tree)
#Breadth First Traversal
# print('BFT: ',[v for v in bfs('a',graph_eg, lambda x: filter(lambda y: y != x,graph_eg))])
# print('SUNSET: ',r)
# print('Coinchange:', c(45))
# print('Knapsack:',b(4,10))
# print('HANOI: ',Source, Helper, Target)
# print('minDAG: ' + str(minDAG(dag,'a','f')))
# print('minDij: ' + str(dij('a','f')))
print('BFT: ' + str([a for a in itertools.islice(breadth_first(1,lambda x:  [x*2,x+2]),15)]))
print('RabinKarp' + str(string_matching_rabin_karp('absolution','ion')))
print('end')
