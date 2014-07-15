__author__ = 'fahmed'

#DP Max sub array -- kadane's algorithm O(n)
def max_sub_kad(a):
    max_sofar = max_contig = a[0]
    for aa in a[1:]:
        max_contig = max(aa,max_contig+aa)
        max_sofar = max(max_contig,max_sofar)
    return max_sofar
#Max sub array -- recursive O(nLog(n))
def max_sub_recurse(A, start, stop):
    if stop == start:                         # zero elements
        return (0, 0, 0)
    elif stop == start + 1:                   # one element
        if A[start] > 0:
            return (A[start], start, stop)
        else:
            return (0, start, start)
    else:                                     # two or more elements
        mid = (start + stop) // 2

        # find maximum sum(A[i:mid]) for i < mid
        total = 0
        lmax = (0, mid)                       # (t,i) such that sum(A[i:mid]) = t
        for i in range(mid-1, start-1, -1):
            total += A[i]
            if total > lmax[0]:
                lmax = (total,i)

        # find maximum sum(A[mid:j]) for j > mid
        total = 0
        rmax = (0, mid)                       # (t, j) such that sum(A[mid:j]) = t
        for j in range(mid+1, stop+1):
            total += A[j-1]
            if total > rmax[0]:
                rmax = (total,j)

        overlay = (lmax[0]+rmax[0], lmax[1], rmax[1])

        return max(max_sub_recurse(A, start, mid),
                   max_sub_recurse(A, mid, stop),
                   overlay)

#Length of longest increasing subsequence ENDING AT A[-1], DP
def lomis(A):
    return 1 if len(A) == 1 or len(A) == 0 else (1 + max([lomis(A[:(j+1)]) for j in [k for k in range(len(A)) if A[-1]>A[k]]] or [0]))
                                                                # 1 + fn(1...j), j < i, A[j] < A[i]
def longest_increasing_subsequence(d):   # https://www.youtube.com/watch?v=4fQJGoeW5VE
    l = []
    for i in range(len(d)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]], key=len) + [d[i]])
    return max(l, key=len)

maxsubtestlist = [-2,23,2,5,1,-3,2,22,-1,-9,2,42]
print('max sub kadanes:',max_sub_kad(maxsubtestlist))
# print('max sub divide&conq:',max_sub_recurse(maxsubtestlist,0,len(maxsubtestlist)))
print('length of longest increasing subsequence:',lomis(maxsubtestlist))
print('maximum increasing subsequence:',longest_increasing_subsequence(maxsubtestlist))